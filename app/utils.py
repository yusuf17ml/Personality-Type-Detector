def format_prediction_result(preprocessed_data, model, le_encoder) -> tuple:
    prediction = model.predict(preprocessed_data)
    proba = model.predict_proba(preprocessed_data).tolist()[0]

    predicted_label = le_encoder.inverse_transform(prediction)[0]
    
    ambivert_percent = round(proba[0] * 100, 2)
    extrovert_percent = round(proba[1] * 100, 2)
    introvert_precent = round(proba[2] * 100, 2)
    return predicted_label, ambivert_percent, extrovert_percent, introvert_precent