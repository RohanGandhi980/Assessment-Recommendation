from fastapi import FastAPI, Query
from pydantic import BaseModel
from data_loader import load_data
from train_model import train_model
from recommend_engine import recommend_assessment

app = FastAPI(title="SHL Assessment Recommendation API")

train_df, _ = load_data("Gen_AI Dataset.xlsx")
vectorizer, train_vectors = train_model(train_df)

class RecResponse(BaseModel):
    Query: str
    Recommended_Assessment_Name: str
    Recommended_Assessment: str
    Similarity_Score: float
    Explanation: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/recommend", response_model=list[RecResponse])
def recommend(q: str = Query(..., min_length=2), k: int = 3):
    return recommend_assessment(q, vectorizer, train_vectors, train_df, top_k=k)
