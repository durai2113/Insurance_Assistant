"""Utilities for building and storing the FAISS vector index."""

import pickle
from pathlib import Path

import faiss
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[1]
INDEX_DIR = BASE_DIR / "faiss_index"

INDEX_DIR.mkdir(parents=True, exist_ok=True)


def save_index(chunks, embeddings):
    """Persist a FAISS index and its source chunks to disk."""

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    # FAISS expects float32 vectors here.
    index.add(np.asarray(embeddings, dtype="float32"))  # pylint: disable=no-value-for-parameter

    faiss.write_index(index, str(INDEX_DIR / "index.faiss"))

    with open(INDEX_DIR / "chunks.pkl", "wb") as file_handle:
        pickle.dump(chunks, file_handle)
