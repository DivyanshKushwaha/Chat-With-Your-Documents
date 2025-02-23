import os
from dotenv import load_dotenv
from utils.db import retrieve_documents
from utils.llm import generate_response

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

def rag_pipeline(query, namespace):
    """Retrieves relevant documents and generates a response using LLM."""
    retrieved_docs = retrieve_documents(query, namespace)
    
    if not retrieved_docs:
        print(f"⚠️ No relevant context found for query: {query}")
        return "No relevant information available."
    
    context = " ".join(retrieved_docs)
    
    return generate_response(query, context)
