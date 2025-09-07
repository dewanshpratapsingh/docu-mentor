from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
# --- Use the full 'src.' path for imports ---
from src.services import rag_service

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post("/ask")
async def ask(query: Query):
    if not query.question:
        raise HTTPException(status_code=400, detail="Question is required.")
    
    try:
        answer = await rag_service.ask_question(query.question)
        return {"answer": answer}
    except Exception as e:
        print(f"Error processing question: {e}")
        raise HTTPException(status_code=500, detail="Failed to process the question.")