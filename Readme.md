# AI Document Chatbot (RAG)

Chatbot que responde perguntas sobre documentos PDF usando Retrieval-Augmented Generation.

## Tecnologias

- Python
- LangChain
- ChromaDB
- Ollama
- Streamlit

## Modelos utilizados

- nomic-embed-text (embeddings)
- phi3 (LLM)

## Como rodar
É recomendado criar um ambiente virtual para instalar as dependências e evitar conflitos com outras versões de pacotes Python.

### Criar virtual environment
No Windows:
```bash
python -m venv venv
venv\Scripts\activate

### 1 Instalar dependências

pip install -r requirements.txt

### 2 Instalar modelos

ollama pull nomic-embed-text  
ollama pull phi3

### 3 Adicionar PDFs

Coloque arquivos na pasta docs/

### 4 Criar o banco vetorial

python ingest.py

### 5 Rodar o chatbot

streamlit run app.py


## Arquitetura

Architecture

PDF Documents
↓
Text Chunking
↓
Embeddings (nomic-embed-text)
↓
Vector Database (ChromaDB)
↓
Retriever
↓
LLM (phi3)
↓
Answer Generation
