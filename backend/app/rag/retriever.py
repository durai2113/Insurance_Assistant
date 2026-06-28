"""Helpers for loading, retrieving, and reranking stored FAISS chunks."""

import os
import pickle
from pathlib import Path
from typing import List

import faiss
import numpy as np

from .embedding import get_model
from .reranker import rerank

BASE_DIR = Path(__file__).resolve().parents[1]


def retrieve_chunks(
    question: str,
    index_dir: str | None = None,
    top_k: int = 10,
) -> List[str]:
    """Retrieve and rerank the most relevant chunks for a question."""

    if index_dir is None:
        index_dir = str(BASE_DIR / "faiss_index")

    index_path = os.path.join(index_dir, "index.faiss")
    chunk_path = os.path.join(index_dir, "chunks.pkl")

    index = faiss.read_index(index_path)

    with open(chunk_path, "rb") as file_handle:
        chunks = pickle.load(file_handle)

    question_embedding = get_model().encode([question], convert_to_numpy=True)
    _distances, indices = index.search(
        np.array(question_embedding, dtype="float32"),
        top_k,
    )

    retrieved_chunks = [chunks[i] for i in indices[0]]
    return rerank(question, retrieved_chunks)
