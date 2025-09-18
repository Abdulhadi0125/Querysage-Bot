# backend/app/embeddings.py
from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")  # lightweight, fast

def get_embedding(text: str) -> np.ndarray:
    """
    Convert a string into a vector embedding.
    """
    return embedding_model.encode(text, normalize_embeddings=True)
