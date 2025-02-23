# 📄 RAG Chatbot with Pinecone and Gemini AI

This project is a **Retrieval-Augmented Generation (RAG) chatbot** that allows users to upload documents (PDF, DOCX, TXT) and chat with them using **Google Gemini AI**. The documents are stored as vector embeddings in **Pinecone**, enabling efficient retrieval of relevant information when a query is made.

## 🚀 Features
- **Upload & Process Documents**: Supports PDF, TXT, and DOCX files.
- **Embeddings & Storage**: Uses **Google Gemini** for embeddings and **Pinecone** as a vector database.
- **Efficient Retrieval**: Fetches the most relevant text chunks from documents using vector similarity search.
- **Chat with Documents**: Uses **Google Gemini AI** to generate responses based on retrieved text.

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```
### 2️⃣ Create & Activate Virtual Environment
- On Windows (PowerShell)
    ```bash
    python -m venv venv
    venv\Scripts\Activate
    ```

### 3️⃣ Install Dependencies
    ```bash
    pip install -r requirements.txt

    ```

## 🔑 API Keys Setup

### 🌲 Pinecone Setup
- Go to Pinecone and sign up/log in.
- Create a new index with:
- Index Name: your_index_name
- Dimension: 768 (for Gemini embeddings)
- Metric: cosine
- Copy your Pinecone API key from the dashboard.
🤖 Google Gemini AI Setup
Go to Google AI Studio.
Generate an API Key for Gemini.