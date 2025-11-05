from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
import numpy as np
import pandas as pd
import joblib

from app.preprocessing import preprocess_input
from app.utils import format_prediction_result

app = FastAPI()

model = None
scaler = None
column_names = None
le_encoder = None

@app.on_event("startup")
def load_model():
    global model
    global scaler
    global column_names
    global le_encoder
    model = joblib.load("models/final_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    column_names = joblib.load("models/column_names.pkl")
    le_encoder = joblib.load("models/label_encoder.pkl")

class UserInput(BaseModel):
    social_energy: float
    alone_time_preference: float
    talkativeness: float
    deep_reflection: float
    group_comfort: float
    party_liking: float
    listening_skill: float
    empathy: float
    creativity: float
    organization: float
    leadership: float
    risk_taking: float
    public_speaking_comfort: float
    curiosity: float
    routine_preference: float
    excitement_seeking: float
    friendliness: float
    emotional_stability: float
    planning: float
    spontaneity: float
    adventurousness: float
    reading_habit: float
    sports_interest: float
    online_social_usage: float
    travel_desire: float
    gadget_usage: float
    work_style_collaborative: float
    decision_speed: float
    stress_handling: float


@app.get("/")
def home():
    return {"message": "Personality Detector"}

@app.post("/predict")
async def predict_personality(input_data: UserInput):
    try:
        input_dict = input_data.dict()
        df = pd.DataFrame(input_dict, index=[0], columns=column_names)

        preprocessed_data = preprocess_input(df, scaler)

        predicted_label, ambivert_percent, extrovert_percent, introvert_precent = \
            format_prediction_result(preprocessed_data, model, le_encoder)
        
        return {"predicted_personality": predicted_label,
                "ambivert_percent": ambivert_percent,
                "extrovert_percent": extrovert_percent,
                "introvert_percent": introvert_precent}
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input data: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
