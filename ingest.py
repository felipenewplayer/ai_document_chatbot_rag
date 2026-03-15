from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
import os

docs_path = "docs"
all_docs = []

for file in os.listdir(docs_path):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(docs_path, file))
        all_docs.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

docs = text_splitter.split_documents(all_docs)

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