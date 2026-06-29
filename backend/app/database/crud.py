from sqlalchemy.orm import Session

from . import models, schemas


def create_document(db: Session, filename: str, file_path: str, faiss_path: str):
    db_doc = models.Document(
        filename=filename,
        file_path=file_path,
        faiss_path=faiss_path
    )
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc


def create_chat(db: Session, chat: schemas.ChatCreate):
    db_chat = models.ChatHistory(
        session_id=chat.session_id,
        question=chat.question,
        answer=chat.answer
    )

    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)

    return db_chat


def get_chat_history(db: Session, session_id: str):
    return (
        db.query(models.ChatHistory)
        .filter(models.ChatHistory.session_id == session_id)
        .order_by(models.ChatHistory.created_at)
        .all()
    )