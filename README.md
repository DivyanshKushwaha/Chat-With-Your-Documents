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
- Give command in powershell 
    ```bash
    pip install -r requirements.txt
    ```
- If <b>pinecone[grpc]</b> module gives error while installing, Give this command 
    ```bash 
    pip install "pinecone[grpc]"
    ```


## 🔑 API Keys Setup

### 🌲 Pinecone Setup
- Go to Pinecone and sign up/log in.
- Create a new index with:
- Index Name: your_index_name
- Dimension: 768 (for Gemini embeddings)
- Metric: cosine
- Copy your Pinecone API key from the dashboard.


### 🤖 Google Gemini AI Setup
Go to Google AI Studio.
Generate an API Key for Gemini.

## 📂 Environment Variables
- Create a .env file in the project root and add
    ```bash
    PINECONE_API_KEY=your-pinecone-api-key
    GEMINI_API_KEY=your-gemini-api-key
    ```
## ▶️ Running the Application
- Once everything is set up, launch the application 
    ```bash 
    streamlit run app.py 
    ```

## 📜 File Structure
- After running and uploading a document you will see structure like 
    ```bash 
    📂 RAG-Chatbot
    ├── 📂 data
    │   ├── 📂 uploads  # Uploaded documents
    ├── 📂 utils
    │   ├── db.py       # Pinecone VectorStore Management
    │   ├── file_handler.py # Handles file uploads & text extraction
    │   ├── llm.py      # Google Gemini AI LLM integration
    │   ├── rag.py      # RAG pipeline (retrieval + generation)
    ├── app.py          # Streamlit frontend
    ├── requirements.txt # Dependencies
    ├── .env            # API Keys (not committed)
    └── README.md       # Project Documentation
    ```
