# backend/app/main.py
from flask import Flask, request, jsonify
from llama_cpp import Llama
import os
from dotenv import load_dotenv
from ingestion import create_vector_store, split_text
import PyPDF2

# Load environment variables
load_dotenv()
MODEL_PATH = os.getenv("MODEL_PATH")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./data/vectordb")

# Initialize the LLaMA model
llm = Llama(model_path=MODEL_PATH)

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "QuerySage LLaMA-3 API running locally!"})

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "Missing 'question' in request body"}), 400

    question = data["question"]

    try:
        # Generate answer from LLaMA
        resp = llm(
            question,
            max_tokens=200,
            stop=["\n\n"],
            temperature=0.7
        )
        answer = resp["choices"][0]["text"]
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Parse text from file
    text_content = ""
    if file.filename.lower().endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text_content += page.extract_text() or ""
    elif file.filename.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text_content = f.read()
    else:
        return jsonify({"error": "Unsupported file type"}), 400

    # Split text into chunks and create/update vector store
    chunks = split_text(text_content, CHUNK_SIZE)
    create_vector_store(chunks)

    return jsonify({"message": f"{file.filename} ingested successfully!", "chunks": len(chunks)})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
