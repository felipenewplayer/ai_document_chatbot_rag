import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.chains import RetrievalQA

st.title("📄 AI Document Chatbot")

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

db = Chroma(
    persist_directory="db",
    embedding_function=embeddings
)

llm = OllamaLLM(
    model="phi3",
    temperature=0
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(
        search_kwargs={"k":3}
    )
)

query = st.text_input("Pergunte algo sobre os documentos")

if query:
    with st.spinner("Pensando..."):
        response = qa.invoke({"query": query})
        st.write(response["result"])