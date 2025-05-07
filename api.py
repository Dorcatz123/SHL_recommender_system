from fastapi import FastAPI
from pydantic import BaseModel
from shl_bot import main  # Your RAG logic here

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    answer = main(query.question)
    return {"question": query.question, "answer": answer}


@app.get("/health")
def hello():
    return "healthy!"


@app.get("/")
def root():
    return {"message": "RAG API is running. Use /ask to POST questions."}

