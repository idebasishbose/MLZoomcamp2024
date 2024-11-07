import pickle
from flask import Flask
from flask import request
from flask import jsonify

app = Flask("churn")
input_file = "model1.bin"
dv_file = "dv.bin"

with open(input_file, "rb") as f_in:
    model = pickle.load(f_in)
with open(dv_file, "rb") as f_in:
    dv = pickle.load(f_in)


@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]

    result = {"subscription probability:": round(y_pred, 3)}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
