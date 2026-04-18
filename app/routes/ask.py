from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.bedrock_service import query_knowledge_base

router = APIRouter()

class AskRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_question(payload: AskRequest):
    question = payload.question.strip()

    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    result = query_knowledge_base(question)

    return result