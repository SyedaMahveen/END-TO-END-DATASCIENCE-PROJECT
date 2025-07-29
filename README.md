# END-TO-END-DATASCIENCE-PROJECT

COMPANY:CODETECH IT SOLUTIONS

NAME:MAHVEEN SULTANA

INTERN ID:CT04DZ47

DOMAIN:DATA SCIENCE

DURATION:4 WEEKS

MENTOR:NEELA SANTOSH

ENTER DESCRIPTION OF TASK:
This project is developed as part of Task 3 of the CodTech Internship, where the primary objective is to build and deploy a complete machine learning pipeline. The goal is to develop a production-ready web application that predicts the species of Iris flowers based on floral measurements such as petal and sepal length and width. The solution includes everything from data preprocessing to model deployment using Flask, and testing the API using Postman and browser-based UI.


🧰 Tools & Technologies Used

💻 Programming Language:
Python 3.x – Chosen for its vast support for machine learning, data manipulation, and web frameworks.

📦 Python Libraries:
scikit-learn – Used for data loading, preprocessing, and training a machine learning model (RandomForestClassifier).
Flask – Lightweight web framework for building RESTful APIs and rendering web pages.
NumPy – Used for handling numerical input and converting features.
Pickle – To save and load the trained model in .pkl format.

🧪 Testing Tool:

Postman – Used to test the deployed API by sending POST requests with form data to simulate frontend interaction.

🖥️ Development Environment:
Visual Studio Code (VS Code) – Used as the primary code editor to write and run all scripts.

🌐 Deployment:
Flask Development Server – The Flask app was run locally on http://127.0.0.1:5000/ for testing both via Postman and browser.

📁 Version Control:
Git & GitHub – Used for version control and project sharing, with all code files uploaded to a public GitHub repository.


🌍 Real-World Applications

This project simulates how machine learning models can be deployed for real-world applications through APIs. Though based on a classic dataset (Iris), the principles demonstrated here apply to a wide range of fields:

🌾 Agriculture – Plant species classification, disease detection.
🏥 Healthcare – Predictive diagnosis using patient data.
🛍️ E-commerce – Product categorization and recommendations.
🤖 AI Chatbots – Integrating ML predictions in conversational interfaces.
📱 Mobile Apps – Real-time predictions from backend ML models.


🔁 Project Workflow

1. Data Collection & Preprocessing:
Loaded the Iris dataset from sklearn.datasets.
Split the data into features and target.
Divided dataset into training and testing sets.
Trained a RandomForestClassifier for prediction.
Achieved high accuracy due to the simplicity of the dataset.
Saved the trained model using pickle.dump() as model.pkl.


2. Model Training File (iris.py):
Script written to handle the entire training process.
Executed once to generate model.pkl which is reused in the API.

🚀 How the Project Was Run:

1. Executed iris.py to train and save the model.

2. Created app.py to:

Load the model,Create / route to render HTML formCreate /predict route to accept form input and return prediction

3. Created index.html to provide a basic web form for user input.

4. Ran app.py using:
pthon app.py
The Flask server started at http://127.0.0.1:5000/.

5. Tested Using Web Browser:
Opened the server URL
Input the 4 feature values
Received prediction in browser via the web interface.

6. Tested Using Postman:
Selected POST method
URL: http://127.0.0.1:5000/predict
Body → x-www-form-urlencoded:

sepal_length: 5.1
sepal_width: 3.5
petal_length: 1.4
petal_width: 0.2

Response:

{
  "prediction": "Iris-setosa"
}

OUTPUT:
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/da8247d6-3a1c-4b61-9b66-415235a853ab" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/7f12ce8e-3b48-4933-ba20-2d43e917d3c9" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/27e9db46-2e3e-4a4c-a95b-049f014b94fc" />
