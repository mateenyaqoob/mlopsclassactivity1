from fastapi import FastAPI
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")
app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML Model API is running!"}

@app.post("/predict")
def predict(features: list):
    prediction = model.predict([np.array(features)])
    return {"prediction": int(prediction[0])}
