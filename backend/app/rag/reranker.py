"""Utilities for reranking retrieved chunks."""

from functools import lru_cache

from app.utils.config import CROSS_ENCODER_MODEL

try:
    from sentence_transformers import CrossEncoder
except ImportError as exc:  # pragma: no cover - handled at runtime
    CrossEncoder = None
    CROSS_ENCODER_IMPORT_ERROR = exc
else:
    CROSS_ENCODER_IMPORT_ERROR = None


@lru_cache(maxsize=1)
def get_model():
    """Load the reranking model only when we actually need it."""

    if CrossEncoder is None:
        raise RuntimeError(
            "sentence-transformers is not installed. Install project dependencies "
            "to rerank chunks."
        ) from CROSS_ENCODER_IMPORT_ERROR

    return CrossEncoder(CROSS_ENCODER_MODEL, local_files_only=True)


def rerank(question: str, chunks: list[str], top_k: int = 3):
    """Rank chunks by how well they match the question."""

    if not chunks:
        return []

    question_chunk_pairs = [[question, chunk] for chunk in chunks]

    try:
        scores = get_model().predict(question_chunk_pairs)
    except (OSError, RuntimeError, ValueError):
        return chunks[:top_k]

    scored_chunks = list(zip(chunks, scores))
    scored_chunks.sort(key=lambda item: item[1], reverse=True)

    return [chunk for chunk, _score in scored_chunks[:top_k]]
