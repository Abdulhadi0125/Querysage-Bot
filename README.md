# QuerySage 🤖📚  
An AI-powered chatbot built with **LLaMA 3 (local inference)** + **FAISS vector database** + **Flask backend** + **Streamlit frontend**.  

QuerySage is designed to work as your personal AI assistant with **document understanding** – you can upload PDFs, TXT, or images (OCR-ready) and get instant answers based on the content.  

---

## ✨ Features
- 🔗 **RAG (Retrieval Augmented Generation)** – query over your own PDFs, TXT, or files.
- ⚡ **Local Inference** – runs on **LLaMA 3** locally (no API costs, no data leakage).
- 📊 **FAISS Vector Store** – fast and efficient similarity search.
- 🖥 **Streamlit Frontend** – clean, ChatGPT-like UI branded as *QuerySage*.
- 🧩 **Flask Backend** – lightweight REST API serving model and document ingestion.
- 📂 **Dynamic File Uploads** – instantly ingest new files without rebuilding the vector DB.
- 🛡 **Customizable** – swap models, change chunk size, or embeddings.

---

## 📂 Project Structure
QuerySage/
│
├── backend/
│ ├── app/
│ │ ├── main.py # Flask API
│ │ ├── ingestion.py # Vector store creation
│ │ ├── embeddings.py # SentenceTransformers embeddings
│ │ ├── config.py # Config/env setup
│ └── models/llama-3/ # Local GGUF LLaMA model
│
├── frontend/
│ ├── app.py # Streamlit app (ChatGPT-style UI)
│
├── data/
│ └── vectordb/ # FAISS index + stored docs
│
├── .env # Model paths, configs
└── requirements.txt

yaml
Copy code

---

## 🚀 Getting Started

### 1. Clone Repo
```bash
git clone https://github.com/your-username/QuerySage.git
cd QuerySage
2. Setup Environment
bash
Copy code
conda create -n querysage-env python=3.10 -y
conda activate querysage-env
pip install -r requirements.txt
3. Configure Environment
Create a .env file:

ini
Copy code
MODEL_PATH=./models/llama-3/Llama-3.1-8B-Mistral-7B-v0.3-mix.IQ3_M.gguf
VECTOR_DB_PATH=./data/vectordb
CHUNK_SIZE=500
4. Run Backend
bash
Copy code
cd backend
python app/main.py
Server runs at → http://127.0.0.1:8000

5. Run Frontend
bash
Copy code
cd frontend
streamlit run app.py
Frontend runs at → http://localhost:8501

📖 Usage
Ask questions directly in chat (general knowledge via LLaMA).

Upload PDF/TXT → instantly ingested into FAISS → chatbot answers from the file.

Soon: image-to-text (OCR) ingestion 🚀.

🛠 Tech Stack
Model: LLaMA 3 (GGUF with llama.cpp)

Vector DB: FAISS

Embeddings: SentenceTransformers (all-MiniLM-L6-v2)

Backend: Flask

Frontend: Streamlit

Language: Python 3.10

📸 Demo

🌟 Future Enhancements
Add OCR for scanned PDFs & images.

Deploy with Docker.

Add multi-user chat sessions.

Integrate advanced LLaMA quantization for faster inference.

🙌 Acknowledgments
Meta AI – LLaMA 3

llama.cpp

SentenceTransformers

FAISS
