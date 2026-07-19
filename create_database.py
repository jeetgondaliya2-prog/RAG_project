from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma

# Load PDF
loader = PyPDFLoader("GRU.pdf")
docs = loader.load()

print(f"Pages loaded: {len(docs)}")

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)

print(f"Chunks created: {len(chunks)}")
print("\nFirst chunk:\n")
print(chunks[0].page_content[:500])

# Create embedding model
embedding_model = MistralAIEmbeddings(
    model="mistral-embed"
)

# Create Chroma DB
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma-db"
)

print("\nChroma database created successfully!")