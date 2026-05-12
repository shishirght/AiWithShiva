from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb # for vector database import whole chromadb package like com.javax.*
from  openai import OpenAI

model = SentenceTransformer('all-MiniLM-L6-v2') # create embedding free
client = chromadb.Client()
collection = client.create_collection(name="pdf_data") # create collection for pdf embeddings 
# table name pdf data


#code to read pdf and create embeddings and store in vector database
def process_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        extracted_text = page.extract_text()
        if extracted_text: 
            text += extracted_text
    return text

def chunk_text(text):
    chunk_size = 500 # define chunk size
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

def create_embeddings(chunks):
    embeddings = model.encode(chunks) # tokeniztion , id creation and embedding for saving vector db 
    return embeddings

# Function to store text chunks and their embeddings into a vector database collection
def store_embeddings_in_db(chunks, embeddings):
    """
    chunks: list of text segments (strings) extracted from your PDF
    embeddings: numpy array of vectors generated for each chunk
    """

    # Prepare a list of unique IDs for each chunk
    # Example: ["0", "1", "2", ...] corresponding to each chunk
    ids = [str(i) for i in range(len(chunks))]

    # Convert the numpy array of embeddings into a Python list
    # This is required because many vector databases expect plain lists, not numpy arrays
    embeddings_list = embeddings.tolist()

    # Add the chunks, their embeddings, and IDs into the collection
    # - documents = the actual text chunks
    # - embeddings = the numerical vector representations
    # - ids = unique identifiers for each chunk
    collection.add(documents=chunks,embeddings=embeddings_list,ids=ids)
    return "Embeddings stored in database successfully."

#search function to query vector database and return relevant chunks based on query
def search_query(question):
    query_embedding = model.encode([question]) # create embedding for query 
    results = collection.query(query_embeddings=query_embedding.tolist(),n_results=2) #query vector database for relevant chunks
    return results
    