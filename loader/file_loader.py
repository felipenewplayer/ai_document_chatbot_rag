from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    UnstructuredWordDocumentLoader
)


def safe_load(loader, source):
    docs = []
    try:
        for doc in loader.lazy_load():
            doc.metadata["source"] = source
            docs.append(doc)
    except Exception as e:
        print(f"Erro ao carregar{source}:{e}")  
    return docs

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
    

    docs.extend(safe_load(pdf_loader, "pdf"))
    docs.extend(safe_load(txt_loader, "txt"))
    docs.extend(safe_load(csv_loader, "csv"))
    docs.extend(safe_load(docx_loader, "docx"))

    return docs
    