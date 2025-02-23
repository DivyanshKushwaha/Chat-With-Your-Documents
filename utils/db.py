import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from dotenv import load_dotenv

from utils.file_handler import extract_text

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API for embeddings
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", google_api_key=GEMINI_API_KEY
)

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
INDEX_NAME = "llama-chatbot"

def namespace_exists(namespace):
    """Check if the namespace exists in Pinecone."""
    vectorstore = PineconeVectorStore(
        index_name=INDEX_NAME,
        pinecone_api_key=PINECONE_API_KEY,
        embedding=embedding_model
    )
    try:
        existing_vectors = vectorstore.similarity_search("test", k=1, namespace=namespace)
        return bool(existing_vectors)
    except Exception:
        return False

def add_documents_to_vectorstore(file_path):
    """Extracts text, splits it into chunks, and adds embeddings to Pinecone if not already added."""
    namespace = os.path.splitext(os.path.basename(file_path))[0].lower().replace(" ", "")

    if namespace_exists(namespace):
        print(f"✅ Namespace '{namespace}' already exists. Skipping embedding.")
        return

    text_chunks = extract_text(file_path)
    
    if not text_chunks:
        print(f"⚠️ No valid text extracted from {file_path}. Skipping embedding.")
        return
    
    vectorstore = PineconeVectorStore(
        index_name=INDEX_NAME,
        pinecone_api_key=PINECONE_API_KEY,
        embedding=embedding_model,
        namespace=namespace
    )

    texts = [chunk.page_content for chunk in text_chunks]
    
    if not texts:
        print(f"⚠️ No text found for embedding in {file_path}.")
        return
    
    vectorstore.add_texts(
        texts=texts, 
        metadatas=[{"source": file_path} for _ in text_chunks]
    )
    print(f"✅ Successfully added {len(texts)} text chunks to Pinecone for {file_path}")

def retrieve_documents(query, namespace, top_k=3):
    """Retrieve relevant documents from Pinecone."""
    namespace = namespace.lower().replace(" ", "")  # Ensure consistency in namespace usage
    
    vectorstore = PineconeVectorStore(
        index_name=INDEX_NAME,
        pinecone_api_key=PINECONE_API_KEY,
        embedding=embedding_model,
        namespace=namespace
    )
    
    docs = vectorstore.similarity_search(query, k=top_k)
    
    if not docs:
        print(f"⚠️ No relevant documents found for query: {query}")
        return ["No relevant information found."]
    
    return [doc.page_content for doc in docs]
