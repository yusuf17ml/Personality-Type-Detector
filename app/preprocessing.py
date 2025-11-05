import pandas as pd

def preprocess_input(df: pd.DataFrame, scaler):
    try:
        preprocessed_data = scaler.transform(df)
        return preprocessed_data
    except Exception as e:
        raise ValueError(f"Error in preprocessing input data: {e}")
