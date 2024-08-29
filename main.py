from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.question_model import Question
from database.db import questions_collection
from routes.bot import ask_question as bot_ask_question  # Correct import

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def function():
    return {"success": True, "message": "API is working!"}

@app.post("/ask")
async def ask_question_endpoint(question: Question):
    # Try to find the question in the database
    question_doc = await questions_collection.find_one({"question": question.text})
    if question_doc:
        return {"answer": question_doc["answer"]}
    
    # Call the async function from bot.py and await it
    result = await bot_ask_question(question.text)
    return result
