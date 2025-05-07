from fastapi import FastAPI
from pydantic import BaseModel
from shl_bot import main  # Your RAG logic here

app = FastAPI()

class Query(BaseModel):
    question: str
class API(BaseModel):
    api_key: str
@app.post("/ask")
def ask(query: Query, api_key: API.api_key ):
    answer = main(query.question, API.api_key)
    return {"question": query.question, "answer": answer}


@app.get("/health")
def hello():
    return "healthy!"


@app.get("/")
def root():
    return {"message": "RAG API is running. Use /ask to POST questions."}

