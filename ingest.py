from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from loader.file_loader import load_all_docs

docs_path = "docs"
all_docs = load_all_docs()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

docs = splitter.split_documents(all_docs)

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="db"
)

db.persist()

print("Vector DB criada")