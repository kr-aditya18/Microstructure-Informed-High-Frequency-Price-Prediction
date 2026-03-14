# 📈 Microstructure-Informed High Frequency Price Prediction

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![License](https://img.shields.io/badge/Project-ML%20Deployment-green)

This project predicts whether a **stock price will go UP or DOWN** using a **Machine Learning model (Random Forest)** and deploys it through a **Flask web application**.

The project demonstrates a **complete ML pipeline**, including:

- Data preprocessing  
- Feature engineering  
- Model training  
- Model evaluation  
- Model deployment using Flask  

---

# 🖥️ Application Preview


# 🚀 How to Run This Project

Follow these commands step-by-step.

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/stock-price-prediction-app.git
```

---

## 2️⃣ Go Into the Project Folder

```bash
cd stock-price-prediction-app
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

After activation your terminal should look like:

```
(venv)
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Installed libraries include:

- Flask  
- scikit-learn  
- numpy  
- joblib  

---

## 6️⃣ Run the Application

```bash
python app.py
```

You should see:

```
Running on http://127.0.0.1:5000
```

---

## 7️⃣ Open the Web Application

Open your browser and go to:

```
http://127.0.0.1:5000
```

You will see the **Stock Price Prediction Interface**.

---

# 🧪 Example Input Values

Use realistic values similar to the dataset.

| Feature | Example |
|------|------|
| Open | 0.45 |
| High | 0.47 |
| Low | 0.44 |
| Close | 0.46 |
| Volume | 3000000 |
| MA10 | 0.45 |
| MA50 | 0.46 |
| Price Change | 0.01 |

Then click **Predict**.

---

# 🧠 Machine Learning Pipeline

This project follows the standard ML development workflow:

1️⃣ Problem Definition  
2️⃣ Data Collection  
3️⃣ Data Preprocessing  
4️⃣ Exploratory Data Analysis (EDA)  
5️⃣ Feature Engineering  
6️⃣ Train-Test Split  
7️⃣ Model Selection  
8️⃣ Model Training  
9️⃣ Model Evaluation  
🔟 Hyperparameter Tuning  
1️⃣1️⃣ Model Deployment  
1️⃣2️⃣ Web Interface using Flask  

---

# 📂 Project Structure

```
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
├── notebooks
│   └── stock_price_prediction.ipynb
│
└── screenshots
    └── app_ui.png
```

---

# ⚙️ Technologies Used

- Python  
- Flask  
- scikit-learn  
- NumPy  
- Joblib  
- HTML / Bootstrap  

---

# 📊 Future Improvements

Possible improvements for this project:

- Add **prediction confidence (%)**
- Use **live stock market API**
- Add **data visualization dashboard**
- Deploy on **AWS / Render / Docker**

---

# 👨‍💻 Author

**Aditya Kumar Verma**  
B.Tech Information Technology  
Noida Institute of Engineering and Technology (NIET)

GitHub: https://github.com/kr-aditya18
