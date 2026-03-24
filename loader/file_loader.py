from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    UnstructuredWordDocumentLoader
)
from collections import defaultdict

def safe_load(loader):
    docs = []
    try:
        for doc in loader.lazy_load():
            # pega o caminho real do arquivo
            doc.metadata["file_name"] = doc.metadata.get("source", "desconhecido")
            docs.append(doc)
    except Exception as e:
        print(f"Erro ao carregar: {e}")  
    return docs
def format_docs(docs):
    grouped = defaultdict(list)

    for doc in docs:
        file = doc.metadata.get("file_name", "desconhecido")
        grouped[file].append(doc.page_content)

    output = ""

    for file, contents in grouped.items():
        output += f"\n📄 Arquivo: {file}\n"
        output += "\n".join(contents[:2])  # limita contexto

    return output
def load_all_docs():
    docs = []
    
    #PDF
    pdf_loader = DirectoryLoader(
        "docs",
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )
     # TXT
    txt_loader = DirectoryLoader(
        "docs",
        glob="**/*.txt",
        loader_cls=TextLoader
    )

    # CSV
    csv_loader = DirectoryLoader(
        "docs",
        glob="**/*.csv",
        loader_cls=CSVLoader
    )

    # DOCX
    docx_loader = DirectoryLoader(
        "docs",
        glob="**/*.docx",
        loader_cls=UnstructuredWordDocumentLoader
    )
    
    docs.extend(safe_load(pdf_loader))
    docs.extend(safe_load(txt_loader))
    docs.extend(safe_load(csv_loader))
    docs.extend(safe_load(docx_loader))

    return docs
    