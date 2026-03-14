# Microstructure-Informed High Frequency Price Prediction

This project predicts whether a stock price will increase or decrease using machine learning.

The model was trained using Random Forest and deployed using a Flask web application.

## Project Pipeline

1. Problem Definition
2. Data Collection
3. Data Preprocessing
4. Exploratory Data Analysis
5. Feature Engineering
6. Train-Test Split
7. Model Selection
8. Model Training
9. Model Evaluation
10. Hyperparameter Tuning
11. Model Deployment
12. UI Interface

## Setup Instructions

### 1 Create virtual environment

python -m venv venv

### 2 Activate environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

### 3 Install dependencies

pip install -r requirements.txt

### 4 Run application

python app.py

### 5 Open browser

http://127.0.0.1:5000

## Example Input

Open: 0.45  
High: 0.47  
Low: 0.44  
Close: 0.46  
Volume: 3000000  
MA10: 0.45  
MA50: 0.46  
Price Change: 0.01

## Output

Prediction: Stock Price will go UP or DOWN