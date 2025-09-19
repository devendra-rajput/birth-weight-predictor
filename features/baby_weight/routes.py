from flask import Blueprint, render_template, request

# Custom imports
from .validation import BabyWeightForm
from .controller import make_prediction

predict_bp = Blueprint('predict', __name__)

# Route for the home page (GET request only)
@predict_bp.route("/",  methods=["GET", "POST"])
def predict_baby_weight():

    form = BabyWeightForm()
    response = None

    if request.method == "GET":
        # Render the main form (index.html)
        return render_template("index.html", form=form, form_data=())
    
    else:

        if form.validate_on_submit():
            # Use validated form data
            prediction_result = make_prediction(form.data)
            response = {"prediction": prediction_result}
        else:
            pass

        return render_template("index.html", form=form, response=response, form_data=form.data)

        # # Get form data from POST request
        # form_data = request.form

        # prediction_result = make_prediction(form_data)

        # # Create a dictionary to pass the prediction to the template
        # response = {"prediction": prediction_result}

        # # Render the form again, now with prediction displayed
        # return render_template("index.html", response=response, form_data=form_data)
