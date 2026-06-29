import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path("model.pkl")

model = None


def load_model():
    global model
    if model is None:
        model = joblib.load(MODEL_PATH)


def preprocess(data):
    return np.array([[data["x"]]])


def predict(data):
    load_model()

    x = preprocess(data)

    pred = model.predict(x)[0]

    return {"prediction": float(pred)}
