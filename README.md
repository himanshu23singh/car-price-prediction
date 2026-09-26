# 🚗 Car Price Prediction

A machine learning project that predicts the selling price of used cars based on features such as brand, year, kilometers driven, fuel type, transmission, and other vehicle-related attributes.

## 📌 Project Overview

This project uses machine learning regression techniques to predict the price of a used car.

The dataset contains information about used cars and their selling prices. The data was cleaned, processed, and used to train regression models.

## 📂 Project Structure

```text
car-price-prediction/
│
├── data/
├── notebooks/
├── car_price_model.pkl
├── requirements.txt
├── .gitignore

🧹 Data Preprocessing

The dataset was prepared before model training.

The preprocessing included:

* Handling missing values
* Removing unnecessary columns
* Checking duplicate records
* Handling categorical features
* Encoding categorical variables
* Splitting the dataset into training and testing sets
* Preparing numerical features for machine learning

🔧 Feature Engineering

Relevant features were selected from the dataset to improve the prediction process.

The model uses vehicle-related information such as:

* Car brand/model
* Year
* Kilometers driven
* Fuel type
* Transmission
* Number of previous owners
* Other available vehicle features

🤖 Model Training

Different machine learning techniques were explored for predicting car prices.

The project uses regression because the target variable, car selling price, is a continuous numerical value.

Model Used

Random Forest Regressor

Random Forest combines multiple decision trees and averages their predictions to produce the final price prediction.

⚙️ Model Optimization

Hyperparameter tuning was performed using:

* RandomizedSearchCV
* Cross-validation

Parameters such as:

* n_estimators
* max_depth
* max_features
* min_samples_split
* min_samples_leaf

were explored to improve the model.

📊 Model Evaluation

The regression model was evaluated using appropriate regression metrics such as:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

These metrics were used to evaluate how accurately the model predicts car prices.

🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook
* Git
* GitHub
