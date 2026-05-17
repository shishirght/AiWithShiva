"""
    PdfReader is the predefined class
    PdfReader used to read data from pdf file
"""
from pypdf import PdfReader

"""
    SentenceTransformer is the predefined class
    SentenceTransformer used to implement the emdebbings
"""
from sentence_transformers import SentenceTransformer

# used to connect to vectordb
import chromadb

# OpenAI- used to generate LLM output 
from openai import OpenAI


#cd 11# load the model
model = SentenceTransformer("all-MiniLM-L6-v2")


# create the table (collection)
client = chromadb.Client()
collection = client.create_collection("pdf_data")

# read pdf file
def read_pdf(pdf_path): 
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        extracted_text = page.extract_text()
        if extracted_text:
            text += extracted_text
    
    return text

# chunk
def chunk_text(text):
    chunk_size = 500
    chunks = []

    for i in range(0,len(text),chunk_size):
        chunk = text[i:i+chunk_size]
        chunks.append(chunk)

    return chunks


# embeddings        
def create_embeddings(chunks):
    embeddings = model.encode(chunks)
    return embeddings

# store in db
def store_in_chromadb(chunks,embeddings):
    collection.add(documents = chunks, embeddings = embeddings.tolist(), ids=[str(i) for i in range(len(chunks))] )
    return "Data Stored Successfully !!!"


# search 
def search_query(question):
    query_embedding = model.encode([question])
    results = collection.query(query_embeddings=query_embedding.tolist(),n_results=2)
    return results

# generate output
def generate_answer(question,context):   
    # openai_client = provide key here
    prompt = f"""
    Answer the question using below context only
    Context: 
    {context}
    Question:
    {question}
    """
    response = openai_client.chat.completions.create(model="gpt-4.1-mini",messages=[{"role":"user","content":prompt}])
    final_answer = response.choices[0].message.content
    return final_answer


















