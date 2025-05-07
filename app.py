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


@app.route("/health")
def hello():
    return "healthy!"
