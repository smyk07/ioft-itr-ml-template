from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import PredictRequest
from model_interface import predict

app = FastAPI(title="ML Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend alive, pls pwn me"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict_route(data: PredictRequest):
    result = predict(data.model_dump())
    return result
