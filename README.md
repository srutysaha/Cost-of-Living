# 🏙️ Cost of Living Predictor

A comprehensive machine learning application that predicts **Rental Prices**, **PG (Paying Guest) Accommodation Rates**, and **Uber Fare Estimates** based on various features such as location, amenities, time, and more. The project utilizes data pipelines and trained models deployed via **Streamlit** for user-friendly web access.

---

## 📌 Project Overview

This project aims to provide users with an estimated cost of living in major Indian cities by combining multiple predictive models:
- 🏠 **Rent Predictor** (Random Forest)
- 🛏️ **PG Price Estimator** (Decision Tree)
- 🚕 **Uber Fare Calculator** (Random Forest)

---

## 🔍 Features

- Predict rent based on BHK, furnishing, location, area, etc.
- Estimate PG accommodation costs based on gender, amenities, and city.
- Forecast Uber fare using pickup/drop coordinates and passenger count.
- User-friendly interface built using Streamlit.
- Interactive visualizations for model insights.

---

## 💡 Technologies Used

| Area                  | Tech Stack                                    |
|-----------------------|-----------------------------------------------|
| Programming Language  | Python 3.x                                    |
| Web UI                | Streamlit                                     |
| ML Models             | Random Forest, Decision Tree                  |
| Preprocessing         | OneHotEncoder, OrdinalEncoder, StandardScaler |
| Visualization         | Seaborn, Matplotlib                           |
| Model Saving          | cloudpickle                                   |
| Version Control       | Git, GitHub, Git LFS                          |

---

## 📂 Directory Structure

 ``` bash
cost-of-living/
├── app.py # Streamlit app
├── rent_pipeline.pkl # Trained Rent model
├── pg_price_pipeline.pkl # Trained PG model
├── fare_pipeline.pkl # Trained Uber model
├── rent.csv # Dataset: Rent
├── pg.csv # Dataset: PG
├── uber.csv # Dataset: Uber fares
├── requirements.txt # Project dependencies
└── README.md # You're reading it!
```

---


🌐 **Live App**: [Click here to try it!](https://cost-of-living.streamlit.app/)

---

## 🚀 How to Use

1. Visit the Streamlit app using the link above.
2. Enter your inputs in the sidebar:
   - Rent: city, type, furnishing, BHK, etc.
   - PG: city, gender, food/wifi/AC availability
   - Transportation: location, passenger count
3. Click **"Predict"** to see the estimated prices.

No installation required — works directly in your browser!

Built with ❤️ by Sruty Saha


