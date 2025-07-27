# app.py
from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

app = Flask(__name__)

# Load and train model
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'iris_model.pkl')

@app.route('/')
def home():
    return "Welcome to the Iris Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(data['features'])])
    pred_class = iris.target_names[prediction[0]]
    return jsonify({'prediction': pred_class})

if __name__ == '__main__':
    app.run(debug=True)
