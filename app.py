import streamlit as st
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

st.title("📄 AI Document Chatbot")

# Embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Vector DB
db = Chroma(
    persist_directory="db",
    embedding_function=embeddings
)

# LLM
llm = OllamaLLM(
    model="phi3",
    temperature=0
)

# Retriever
retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

# Função para formatar contexto
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Prompt
prompt = ChatPromptTemplate.from_template("""
Responda com base apenas no contexto abaixo:

{context}

Pergunta: {question}
""")

# 🔥 RAG PIPELINE (Runnable)
rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

# UI
query = st.text_input("Pergunte algo sobre os documentos")

if query:
    with st.spinner("Pensando..."):
        response = rag_chain.invoke(query)
        st.write(response)