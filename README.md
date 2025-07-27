# END-TO-END-DATASCIENCE-PROJECT

COMPANY:CODETECH IT SOLUTIONS

NAME:MAHVEEN SULTANA

INTERN ID:CT04DZ47

DOMAIN:DATA SCIENCE

DURATION:4 WEEKS

MENTOR:NEELA SANTOSH

ENTER DESCRIPTION OF TASK:This project is built as part of CodTech's Internship Task 3: End-to-End Data Science Project, aimed at developing a complete ML-based web application from data collection to deployment. The final deliverable is a deployed API built using Flask, integrated with a machine learning model that predicts Iris flower species based on floral measurements


🔧 Tools & Technologies Used

1. Programming Language:

Python 3.x – Chosen for its rich ecosystem in machine learning and web frameworks.

2. Libraries Used:

scikit-learn – For model creation and training (RandomForestClassifier).

Flask – A lightweight web framework used to create the REST API.

joblib – For saving and loading the trained model efficiently.

NumPy – For numerical operations and feature handling.

3. Development Platform:

Visual Studio Code (VS Code) – The primary code editor used for development.

Command Prompt / Terminal – To run the Flask application locally.

4. API Testing Tool:

Postman – A powerful tool used to test the /predict API by sending POST requests with JSON input.

5. Version Control:

Git & GitHub – Used for managing source code versions and publishing the project for review.


🧠 Application of the Project
This project serves as a real-world demonstration of how machine learning models can be deployed into production using a simple API interface. The core application is Iris flower classification, a classic problem in machine learning involving classification of three flower types: Setosa, Versicolor, and Virginica.
The developed API can be used by any frontend, mobile application, or system that wants to access this ML prediction service. Such APIs are widely used in industries like:
Agriculture (Plant classification)
Healthcare (Predictive analytics)
E-commerce (Recommendation engines)
Customer Service (Chatbot models)
This project helps you understand the end-to-end data science pipeline, crucial for deploying ML models in real-world applications.


🔄 Project Workflow

1. Data Collection & Preprocessing
Used the standard Iris dataset from sklearn.datasets.
Preprocessing steps included:
Extracting features and target
Splitting data into training and test sets
Model training using RandomForestClassifier

2. Model Training

A Random Forest model was trained using scikit-learn.
The model showed high accuracy due to the simplicity of the Iris dataset.
Final model was saved using joblib.dump().

3. API Development with Flask

A Flask app (app.py) was created with two routes:
GET / – Displays a welcome message.
POST /predict – Accepts JSON input with flower features and returns prediction.
CORS or headers can be added for advanced usage in full-stack deployment.


4. Testing with Postman

Postman was used to send test JSON data:
{
  "features": [5.1, 3.5, 1.4, 0.2]
}

The API returned:
{
  "prediction": "setosa"
}

5. Packaging and Deployment

All dependencies were listed in requirements.txt.
README file was created explaining the project in detail.
Files like test_api.py were added to demonstrate how to test without Postman.

OUTPUT:
