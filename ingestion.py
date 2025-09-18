# backend/app/ingestion.py
import os
import faiss
import pickle
from typing import List
from embeddings import get_embedding
from config import VECTOR_DB_PATH, CHUNK_SIZE
import numpy as np


def split_text(text: str, chunk_size: int = CHUNK_SIZE) -> List[str]:
    """
    Split long text into smaller chunks.
    """
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def create_vector_store(documents: List[str]):
    """
    Create FAISS vector store from list of strings and save to disk.
    """
    vectors = [get_embedding(chunk) for doc in documents for chunk in split_text(doc)]
    vectors = np.array(vectors).astype("float32")
    dim = vectors.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(vectors)

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)
    faiss.write_index(index, os.path.join(VECTOR_DB_PATH, "index.faiss"))

    # Save original texts for retrieval
    with open(os.path.join(VECTOR_DB_PATH, "texts.pkl"), "wb") as f:
        pickle.dump(documents, f)
