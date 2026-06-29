from pydantic import BaseModel


class PredictRequest(BaseModel):
    x: float


class PredictResponse(BaseModel):
    prediction: float
    confidence: float
