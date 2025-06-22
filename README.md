# 🤖 Physics RAG Chatbot

A Retrieval-Augmented Generation chatbot built using LangChain, GPT-2, FAISS, and HuggingFace embeddings. This bot answers Physics-related questions using a knowledge base of 30+ physics documents.

## Features
- Loads and parses 30+ DOCX Physics documents
- Uses sentence embeddings (MiniLM) and FAISS for retrieval
- GPT-2 model generates answers
- Comes with Gradio and Tkinter frontends

## Tech Stack
- LangChain
- HuggingFace Transformers & SentenceTransformers
- FAISS
- Gradio (chat UI)
- Python (docx2txt, tkinter)

## Run Instructions
```bash
git clone https://github.com/IffaKashif/physics-chatbot-rag
cd physics-chatbot-rag
pip install -r requirements.txt
python chatbot_gradio.py
