📈 Microstructure-Informed High Frequency Price Prediction

This project predicts whether a stock price will go UP or DOWN using a Machine Learning model (Random Forest) and deploys it using a Flask web application.

The project demonstrates the complete ML pipeline, from data preprocessing and model training to deployment with a web interface.

🚀 How to Run This Project

Follow the commands below step-by-step.

1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/stock-price-prediction-app.git
2️⃣ Go Into the Project Folder
cd stock-price-prediction-app
3️⃣ Create Virtual Environment
python -m venv venv
4️⃣ Activate Virtual Environment
Windows
venv\Scripts\activate
Mac / Linux
source venv/bin/activate

After activation your terminal should look like:

(venv)
5️⃣ Install Required Libraries
pip install -r requirements.txt

This installs the necessary dependencies:

Flask

scikit-learn

numpy

joblib

6️⃣ Run the Application
python app.py

You should see:

Running on http://127.0.0.1:5000
7️⃣ Open the Web Application

Open your browser and go to:

http://127.0.0.1:5000

You will see the Stock Price Prediction Web Interface.

🧪 Example Input Values

Use realistic values similar to the dataset.

Feature	Example
Open	0.45
High	0.47
Low	0.44
Close	0.46
Volume	3000000
MA10	0.45
MA50	0.46
Price Change	0.01

Click Predict to see the prediction.

🧠 Machine Learning Pipeline

The following ML workflow was implemented:

Problem Definition

Data Collection

Data Preprocessing

Exploratory Data Analysis (EDA)

Feature Engineering

Train-Test Split

Model Selection

Model Training

Model Evaluation

Hyperparameter Tuning

Model Deployment

Web Interface using Flask

📂 Project Structure
stock-price-prediction-app
│
├── app.py
├── requirements.txt
├── README.md
├── stock_price_model.pkl
│
├── templates
│   └── index.html
│
├── dataset
│   └── AAPL.csv
│
└── notebooks
    └── stock_price_prediction.ipynb
⚙️ Technologies Used

Python

Flask

scikit-learn

NumPy

Joblib

HTML / Bootstrap

👨‍💻 Author

Aditya Kumar Verma
B.Tech Information Technology
Noida Institute of Engineering and Technology (NIET)
