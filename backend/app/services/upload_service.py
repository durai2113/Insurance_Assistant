"""Service helpers for storing and processing uploaded PDFs."""

import shutil
from pathlib import Path

from fastapi import UploadFile

from app.rag.pdf_reader import extract_text
from app.rag.chunker import split_text
from app.rag.embedding import create_embeddings
from app.rag.vector_store import save_index

from sqlalchemy.orm import Session
from app.database import crud

BASE_DIR = Path(__file__).resolve().parents[1]
UPLOAD_FOLDER = BASE_DIR / "uploads"

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


def save_pdf(file: UploadFile) -> str:
    """Persist the uploaded file to the local uploads directory."""

    safe_filename = Path(file.filename or "uploaded.pdf").name
    file_path = UPLOAD_FOLDER / safe_filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(file_path)


def process_pdf(file_path: str, db: Session, filename: str):
    """Extract text, create embeddings, and store the FAISS index."""

    text = extract_text(file_path)
    if not text.strip():
        raise ValueError(
            "The uploaded PDF does not contain extractable text."
        )

    chunks = split_text(text)
    if not chunks:
        raise ValueError(
            "The uploaded PDF could not be split into searchable chunks."
        )

    embeddings = create_embeddings(chunks)

    save_index(chunks, embeddings)

    # Save to PostgreSQL
    crud.create_document(
        db=db,
        filename=filename,
        file_path=file_path,
        faiss_path="faiss_index/index.faiss"
    )
