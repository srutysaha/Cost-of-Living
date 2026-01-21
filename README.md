# 🏙️ Cost of Living Predictor

A comprehensive **machine learning–based web application** that estimates **Rental Prices**, **PG (Paying Guest) Accommodation Costs**, and **Urban Travel Fares** using real-world data and trained predictive models.

The application is built with **Python + Streamlit**, providing a clean and interactive interface for users to explore cost-of-living estimates across major Indian cities.

---

## 📌 Project Overview

This project combines multiple machine learning pipelines to help users understand and compare different components of urban living expenses:

* 🏠 **Rent Price Predictor** – estimates monthly rent using property and location features
* 🛏️ **PG Cost Estimator** – predicts PG accommodation charges based on amenities and demographics
* 🚕 **Travel Fare Estimator** – forecasts approximate travel fares using distance and passenger data

Each model is trained independently and integrated into a single Streamlit application.

---

## 🔍 Key Features

* Rent prediction using **BHK, furnishing type, area, and city**
* PG price estimation based on **gender, amenities, and location**
* Travel fare calculation using **pickup/drop coordinates and passenger count**
* Simple and intuitive **Streamlit UI**
* Interactive data visualizations for better understanding
* Pre-trained pipelines for fast inference

---

## 💡 Technologies Used

| Category             | Tools / Libraries                             |
| -------------------- | --------------------------------------------- |
| Programming Language | Python 3.x                                    |
| Web Framework        | Streamlit                                     |
| Machine Learning     | Random Forest, Decision Tree                  |
| Data Preprocessing   | OneHotEncoder, OrdinalEncoder, StandardScaler |
| Visualization        | Seaborn, Matplotlib                           |
| Model Serialization  | cloudpickle                                   |
| Version Control      | Git, GitHub, Git LFS                          |

---

## 📂 Project Structure

```bash
cost-of-living/
├── app.py                    # Streamlit application
├── rent_pipeline.pkl         # Trained Rent prediction pipeline
├── pg_price_pipeline.pkl     # Trained PG price pipeline
├── fare_pipeline.pkl         # Trained Travel fare pipeline
├── rent.csv                  # Rent dataset
├── pg.csv                    # PG dataset
├── uber.csv                  # Travel fare dataset
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## 🚀 Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/cost-of-living-predictor.git
cd cost-of-living
```

### 2️⃣ Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Launch the App

```bash
streamlit run app.py
```

---

## 📈 Models Used

* **Rent Prediction**: Random Forest Regressor
* **PG Price Estimation**: Decision Tree Regressor
* **Travel Fare Estimation**: Random Forest Regressor

All models are saved as **pipelines**, ensuring consistent preprocessing during inference.
