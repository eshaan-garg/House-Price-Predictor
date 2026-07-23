# House Price Predictor

A Streamlit web app that predicts house prices in India (in Lakhs) using Linear Regression.

## Features

- Predicts price based on: BHK, bathrooms, built-up area, carpet area, floor number, total floors, property age, parking spaces, security score, distance to city center, and distance to metro.
- Interactive sliders and input fields for easy data entry.

## Setup

```bash
pip install streamlit scikit-learn pandas
```

## Run

```bash
streamlit run main.py
```

Open http://localhost:8501 in your browser.

## Dataset

The model is trained on `housing_price_dataset.csv` (50,000 entries) with an R2 score of ~0.73.
