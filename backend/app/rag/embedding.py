"""Helpers for loading the embedding model and generating vectors."""

import os
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")


@lru_cache(maxsize=1)
def get_model():
    """Return a cached sentence-transformer model instance."""

    try:
        from sentence_transformers import (  # pylint: disable=import-outside-toplevel
            SentenceTransformer,
        )
    except ImportError as exc:  # pragma: no cover - handled at runtime
        raise RuntimeError(
            "sentence-transformers is not installed. "
            "Install project dependencies to create embeddings."
        ) from exc

    if not EMBEDDING_MODEL:
        raise RuntimeError("EMBEDDING_MODEL is not configured.")

    return SentenceTransformer(EMBEDDING_MODEL)


def create_embeddings(chunks):
    """Create NumPy embeddings for a list of text chunks."""

    return get_model().encode(chunks, convert_to_numpy=True)
