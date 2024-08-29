from fastapi import HTTPException
from database.db import questions_collection

async def ask_question(question: str):
    # Try to find the question in the database
    question_doc = await questions_collection.find_one({"question": question})
    if question_doc:
        return {"question": question_doc["question"], "answer": question_doc["answer"]}
    else:
        raise HTTPException(status_code=404, detail="Answer not found")
