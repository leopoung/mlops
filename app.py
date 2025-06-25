from flask import Flask, request, jsonify
import mlflow.pyfunc
import pandas as pd

model = mlflow.pyfunc.load_model("mlruns/490308476172365607/models/m-c1b49869402c4d5c8217d65da7ae7e17/artifacts")
 
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    predictions = model.predict(df)
    return jsonify(predictions.tolist())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
