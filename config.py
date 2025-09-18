# backend/app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./data/vectordb")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
