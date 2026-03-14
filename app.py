from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("stock_price_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = [
        float(request.form["open"]),
        float(request.form["high"]),
        float(request.form["low"]),
        float(request.form["close"]),
        float(request.form["volume"]),
        float(request.form["ma10"]),
        float(request.form["ma50"]),
        float(request.form["price_change"])
    ]

    prediction = model.predict([data])

    if prediction[0] == 1:
        result = "Stock Price will go UP"
    else:
        result = "Stock Price will go DOWN"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)