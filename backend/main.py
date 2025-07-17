from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from enum import Enum

from controllers.transformer import sentiment_analysis

app = FastAPI()

class PredictType(BaseModel):
    text: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/predict")
async def predict(predict_data: PredictType):
    return sentiment_analysis(predict_data.text)
