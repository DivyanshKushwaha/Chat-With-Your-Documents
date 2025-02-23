import streamlit as st
import os
from utils.file_handler import save_uploaded_files
from utils.db import add_documents_to_vectorstore, namespace_exists
from utils.rag import rag_pipeline

st.set_page_config(page_title="RAG Chat", layout="wide")
st.title("📄 Chat with Your Documents")

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

uploaded_files = st.file_uploader("Upload documents", type=["pdf", "docx", "txt"], accept_multiple_files=True)

file_paths = []
if uploaded_files:
    file_paths = save_uploaded_files(uploaded_files)

    for file_path in file_paths:
        add_documents_to_vectorstore(file_path)  # Now skips if namespace exists
    st.success("Files uploaded and embedded successfully!")

query = st.text_input("Ask a question about your documents:", value="")

# Fix: Add a button to explicitly trigger the response
if st.button("Submit"):
    if not query.strip():
        st.warning("Please enter a question before submitting.")
    elif not file_paths:
        st.warning("Please upload a document first.")
    else:
        namespace = os.path.splitext(os.path.basename(file_path))[0].lower().replace(" ", "")  # Ensure lowercase & no spaces
        
        if not namespace_exists(namespace):
            st.warning("The document hasn't been processed yet. Please upload it first.")
        else:
            response = rag_pipeline(query, namespace)
            st.write("### Response:")
            st.info(response)

