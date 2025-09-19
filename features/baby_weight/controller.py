# controllers/predict_controller.py

import pickle
import pandas as pd

# Function to clean and convert form data into a proper format
def clean_form_data(form_data):

    # Extract and convert form inputs to appropriate types
    height = round(float(form_data["height"]) * 12, 2)  # feet to inches
    weight = round(float(form_data["weight"]) * 2.205, 2)  # kg to pounds

    gestation = float(form_data["gestation"])
    parity = form_data["parity"]
    age = float(form_data["age"])
    height = float(height)
    weight = float(weight)
    smoke = float(form_data["smoke"])

    # Return a dictionary suitable for DataFrame creation
    return {
        "gestation": [gestation],
        "parity": [parity],
        "age": [age],
        "height": [height],
        "weight": [weight],
        "smoke": [smoke],
    }


def make_prediction(form_data):

    # Clean and format the input data
    cleaned_data = clean_form_data(form_data)
    df = pd.DataFrame(cleaned_data)

    # Load the trained machine learning model from disk
    with open("models/model.pkl", "rb") as pkl_file:
        model = pickle.load(pkl_file)

    # Predict and convert ounces to KG
    prediction = model.predict(df)
    return round(float(prediction / 35.274), 2)
