# IELTS Writing Evaluator – MCP + RAG (Codespaces Safe)

This project implements a fully local IELTS Writing Evaluator using:

- RAG (SentenceTransformers + FAISS)
- Qwen2.5-3B-Instruct (Hugging Face, local)
- Model Context Protocol (MCP)
- FastMCP server
- Streamlit frontend

## Run in GitHub Codespaces

pip install -r requirements.txt
python server.py
streamlit run app.py
