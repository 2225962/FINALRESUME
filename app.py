from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "Resume Screening API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Example features (must match your training order)
    features = np.array([[
        data["experience"],
        data["projects"],
        data["skills_score"],
        data["certifications"],
        data["education_level"]
    ]])

    prediction = model.predict(features)[0]

    result = "Proceed to Interview" if prediction == 1 else "Reject"

    return jsonify({
        "prediction": int(prediction),
        "result": result
    })

if __name__ == "__main__":
    app.run()
