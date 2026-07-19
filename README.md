# 📚 RAG Project - Retrieval-Augmented Generation using LangChain, Mistral & ChromaDB

A Retrieval-Augmented Generation (RAG) application built with **Python**, **LangChain**, **Mistral AI**, **ChromaDB**, and **Streamlit**. This project allows users to ask questions about PDF documents and receive accurate, context-aware answers using semantic search and Large Language Models (LLMs).

---

## 🚀 Features

- 📄 Load PDF documents
- ✂️ Split documents into chunks
- 🔍 Generate embeddings using Mistral AI
- 🗂️ Store embeddings in ChromaDB
- ⚡ Semantic similarity search
- 🤖 Answer questions using Mistral LLM
- 💻 Simple Streamlit interface
- 🔐 Secure API key management using `.env`

---

## 🛠️ Tech Stack

- Python 3.11
- Streamlit
- LangChain
- Mistral AI
- ChromaDB
- PyPDF
- python-dotenv

---

# 📁 Project Structure

```
RAG_project/
│
├── app.py                     # Streamlit application
├── main.py                    # Main RAG pipeline
├── create_database.py         # Creates vector database
├── requirements.txt           # Required Python packages
├── .gitignore                 # Git ignored files
├── .env.example               # Environment variable template
│
├── vector_store/
│   ├── DB.py
│   └── vector_store.py        # ChromaDB operations
│
├── retrievers/
│   ├── mmr.py
│   └── arixv.py          # Similarity search logic
│
├── document loaders/
│   ├── __init__.py
│   └── pdf_loader.py          # PDF loading logic
│
├── data/
│   └── sample.pdf             # PDF documents
│
└── chroma_db/                 # Generated vector database
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/jeetgondaliya2-prog/RAG_project.git
```

```bash
cd RAG_project
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
MISTRAL_API_KEY=your_api_key_here
```

> **Important:** Never upload your `.env` file to GitHub.

---

# 📄 Create Vector Database

Run

```bash
python create_database.py
```

This will:

- Load PDF files
- Split documents
- Generate embeddings
- Store vectors in ChromaDB

---

# ▶️ Run the Application

### Streamlit

```bash
streamlit run app.py
```

or

```bash
python main.py
```

depending on your project.

---

# 🧠 How RAG Works

```
PDF Documents
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Embeddings (Mistral)
      │
      ▼
ChromaDB Vector Store
      │
      ▼
Retriever
      │
      ▼
Relevant Chunks
      │
      ▼
Mistral LLM
      │
      ▼
Final Answer
```

---

# 📦 Requirements

Some major packages used:

```
langchain
langchain-community
langchain-mistralai
chromadb
streamlit
python-dotenv
pypdf
```

Install everything with:

```bash
pip install -r requirements.txt
```

---

# 📸 Demo

You can add screenshots here.

Example:

```
assets/
    home.png
    output.png
```

---

# 🔒 Security

This project uses environment variables to store API keys.

The following files should **NOT** be uploaded:

```
.env
venv/
__pycache__/
chroma_db/
```

---

# 🎯 Future Improvements

- Multiple PDF support
- Chat history
- Conversation memory
- Hybrid Search
- Source citations
- PDF upload from UI
- Better UI/UX
- Support for multiple LLMs

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```
git checkout -b feature-name
```

3. Commit your changes

```
git commit -m "Added new feature"
```

4. Push to GitHub

```
git push origin feature-name
```

5. Open a Pull Request

---

# 👨‍💻 Author

**Jeet Gondaliya**

GitHub:
https://github.com/jeetgondaliya2-prog

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.
