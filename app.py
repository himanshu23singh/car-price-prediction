from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("car_price_model.pkl")


@app.route("/")
def home():

    # Get the OneHotEncoder from the saved pipeline
    categorical_encoder = (
        model.named_steps["preprocessor"]
        .named_transformers_["cat"]
    )

    # Categorical columns order:
    # 0 = car_name
    # 1 = brand
    # 2 = model
    # 3 = seller_type
    # 4 = fuel_type
    # 5 = transmission_type

    brands = categorical_encoder.categories_[1]

    return render_template(
        "index.html",
        brands=brands
    )


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)

    return {
        "predicted_price": prediction[0]
    }


if __name__ == "__main__":
    app.run(debug=True, port=5001)