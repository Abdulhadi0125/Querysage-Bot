# frontend/app.py
from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)
BACKEND_URL = "http://127.0.0.1:8000"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        resp = requests.post(f"{BACKEND_URL}/ask", json={"question": question})
        answer = resp.json().get("answer", "No answer received")
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Send file to backend for ingestion
    with open(file_path, "rb") as f:
        files = {"file": (file.filename, f)}
        resp = requests.post(f"{BACKEND_URL}/upload", files=files)
    return jsonify(resp.json())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
