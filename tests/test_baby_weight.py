import sys
import os

# Add project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from features.baby_weight.controller import clean_form_data, make_prediction

def test_clean_form_data():
    raw = {
        "gestation": "280",
        "parity": "1",
        "age": "30",
        "height": "5.5",
        "weight": "60",
        "smoke": "0"
    }
    cleaned = clean_form_data(raw)
    assert isinstance(cleaned, dict)
    assert cleaned["height"][0] == 66.0  # 5.5 * 12
    assert round(cleaned["weight"][0], 2) == 132.3  # 60 * 2.205

def test_prediction(monkeypatch):

    # Mock model for testing
    # class MockModel:
    #     def predict(self, df):
    #         return [1000]

    # monkeypatch.setattr("baby_weight.model.load_model", lambda: MockModel())

    test_data = {
        "gestation": 280,
        "parity": "1",
        "age": 30,
        "height": 66.0,
        "weight": 132.3,
        "smoke": 0.0
    }
    result = make_prediction(test_data)
    assert result == round(1000 / 35.274, 2)
