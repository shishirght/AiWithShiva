# ------------------------------------------
# IMPORT LIBRARIES
# ------------------------------------------
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File
import shutil
from rag import (
    read_pdf,
    chunk_text,
    create_embeddings,
    store_in_chromadb,
    search_query,
    generate_answer,
    collection
)

# ------------------------------------------
# CONFIGURE LOGGING
# ------------------------------------------
logging.basicConfig(
    level=logging.INFO,  # INFO level shows important events
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ------------------------------------------
# CREATE FASTAPI APP
# ------------------------------------------
app = FastAPI()

# ------------------------------------------
# ADD CORS MIDDLEWARE
# ------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # ["*"] means all domains are allowed (not secure for production) 
    allow_credentials=True, # Whether cookies, authorization headers, or TLS client certificates
    allow_methods=["*"],    # ["*"] means all methods are allowed GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],    # Which request headers are allowed
)

# ------------------------------------------
# HOME API
# ------------------------------------------
@app.get("/")
def home():
    logger.info("Home endpoint called")
    return {"message": "LLM RAG Project Running"}

# ------------------------------------------
# PDF UPLOAD API
# ------------------------------------------
@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    logger.info(f"Received file upload request: {file.filename}")
    pdf_path = f"../uploads/{file.filename}"

    # Save uploaded PDF
    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    logger.info(f"Saved PDF to {pdf_path}")

    # STEP 1 : READ PDF
    text = read_pdf(pdf_path)
    logger.info(f"Extracted text length: {len(text)} characters")

    # STEP 2 : CHUNK TEXT
    chunks = chunk_text(text)
    logger.info(f"Created {len(chunks)} chunks")

    # STEP 3 : CREATE EMBEDDINGS
    embeddings = create_embeddings(chunks)
    logger.info("Embeddings created")

    # STEP 4 : STORE IN CHROMADB
    store_in_chromadb(chunks, embeddings)
    logger.info("Stored chunks and embeddings in ChromaDB")

    return {
        "message": "PDF Uploaded Successfully",
        "total_chunks": len(chunks)
    }

# ------------------------------------------
# ASK QUESTION API
# ------------------------------------------
@app.get("/ask/")
def ask_question(question: str):
    logger.info(f"Question received: {question}")

    # SEARCH RELEVANT CHUNKS
    results = search_query(question)
    documents = results['documents'][0]
    logger.info(f"Found {len(documents)} relevant documents")

    # CREATE CONTEXT
    context = " ".join(documents)

    # GENERATE FINAL ANSWER
    answer = generate_answer(question, context)
    logger.info("Generated answer")

    return {
        "question": question,
        "answer": answer
    }

# ------------------------------------------
# VIEW CHROMADB DATA
# ------------------------------------------
@app.get("/view-data/")
def view_data():
    logger.info("Fetching data from ChromaDB collection")
    data = collection.get(include=["documents"])
    logger.info(f"Retrieved {len(data['documents'])} documents")

    return {
        "total_chunks": len(data["documents"]),
        "documents": data["documents"]
    }
