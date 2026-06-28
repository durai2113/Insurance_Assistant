"""Business logic for chat requests and persisted chat history."""

from sqlalchemy.orm import Session

from ..database import crud, schemas
from ..rag.llm import generate_answer
from ..rag.prompt_builder import build_prompt
from ..rag.retriever import retrieve_chunks


def ask_question(
    db: Session,
    session_id: str,
    question: str,
):
    """Answer a user question and store the chat exchange."""

    chunks = retrieve_chunks(question)
    prompt = build_prompt(question, chunks)
    answer = generate_answer(prompt)

    chat = schemas.ChatCreate(
        session_id=session_id,
        question=question,
        answer=answer,
    )

    crud.create_chat(db, chat)
    return answer
