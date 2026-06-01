# Superstore Profitability Prediction

## Project Overview

This project analyzes retail sales data from a Superstore business to identify factors affecting profitability and predict whether a transaction will be profitable or unprofitable using machine learning.

---

## Business Problem

The company experiences inconsistent profitability across:
- regions,
- product categories,
- customer segments,
- and discount levels.

The goal is to:
1. Identify key drivers of profit and loss.
2. Build a machine learning model that predicts transaction profitability.
3. Deploy the model as an interactive web application.

---

## Key Insights

- High discounts strongly reduce profitability.
- The Central region experiences significant losses.
- Furniture sub-categories such as Tables and Furnishings were highly unprofitable.
- Technology products generally performed better.

---

## Machine Learning Models Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn

---

## Deployment

The final model was deployed using Streamlit to create an interactive prediction application.

Users can input:
- Sales
- Quantity
- Discount
- Category
- Segment
- Region

and receive a profitability prediction instantly.

---

## Repository Structure

```plaintext
├── app.py
├── requirements.txt
├── README.md
├── decision_tree_model.pkl
├── feature_columns.pkl
└── notebooks/
```

---

## Author

Divine Obadeyin