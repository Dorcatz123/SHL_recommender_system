from fastapi import FastAPI
from pydantic import BaseModel
from shl_bot import main  # Your RAG logic here

app = FastAPI()

class Query(BaseModel):
    question: str
    api_key: str
    
@app.post("/ask")
def ask(payload: Query):
    answer = main(payload.question, payload.api_key)
    return {"question": query.question, "answer": answer}


@app.get("/health")
def hello():
    return "healthy!"


@app.get("/")
def root():
    return {"message": "RAG API is running. Use /ask to POST questions."}

