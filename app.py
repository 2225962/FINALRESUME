from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

# 🔹 Load website UI
@app.route("/")
def home():
    return render_template("index.html")

# 🔹 API for prediction
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = np.array([[
        data["experience"],
        data["projects"],
        data["skills_score"],
        data["certifications"],
        data["education_level"]
    ]])

    prediction = model.predict(features)[0]

    result = "Proceed to Interview" if prediction == 1 else "Reject"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
