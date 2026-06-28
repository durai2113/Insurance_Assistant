from pydantic import BaseModel
from datetime import datetime


class ChatCreate(BaseModel):
    session_id: str
    question: str
    answer: str


class ChatResponse(BaseModel):
    id: int
    session_id: str
    question: str
    answer: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class QuestionRequest(BaseModel):
    session_id: str
    question: str


class QuestionResponse(BaseModel):
    answer: str