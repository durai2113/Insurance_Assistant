from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.schemas import (QuestionRequest,QuestionResponse)
from app.database.dependency import get_db
from app.services.chat_service import ask_question

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/",response_model=QuestionResponse)
def chat(
    request: QuestionRequest,
    db: Session = Depends(get_db)
):
    answer = ask_question(
        db=db,
        session_id=request.session_id,
        question=request.question
    )

    return QuestionResponse(answer=answer)
