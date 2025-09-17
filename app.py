# Import required libraries
from flask import Flask, render_template, request
import pickle
import pandas as pd

# Initialize Flask application
app = Flask(__name__)

# Function to clean and convert form data into a proper format
def clean_form_data(form_data):
    # Extract and convert form inputs to appropriate types
    gestation = float(form_data["gestation"])
    parity = form_data["parity"]                # Kept as string; should be converted if needed
    age = float(form_data["age"])
    height = float(form_data["height"])
    weight = float(form_data["weight"])
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

# Route for the home page (GET request only)
@app.route("/",  methods=["GET"])
def home():
    # Render the main form (index.html)
    return render_template("index.html", form_data=())

# Route to handle prediction (POST request from the form)
@app.route("/prediction", methods=["POST"])
def prediction():
    # Get form data from POST request
    form_data = request.form

    # Clean and format the input data
    formated_data = clean_form_data(form_data)
    baby_df = pd.DataFrame(formated_data)

    # Load the trained machine learning model from disk
    with open("models/model.pkl", "rb") as pklFile:
        model = pickle.load(pklFile)

    # Make prediction using the input data
    prediction = model.predict(baby_df)
    prediction = round(float(prediction), 2)  # Round prediction to 2 decimal places

    # Create a dictionary to pass the prediction to the template
    response = {"prediction": prediction}

    # Render the form again, now with prediction displayed
    return render_template("index.html", response=response, form_data=form_data)

# Run the Flask app in debug mode when this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
