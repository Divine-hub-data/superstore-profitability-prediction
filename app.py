import streamlit as st
import joblib
import pandas as pd

#load trained model
model = joblib.load('decision_tree_model.pkl')

#load feature column
feature_columns = joblib.load('feature_columns.pkl')

st.title('Superstore Profitability Prediction App')


st.write('This application predicts whether a retail transaction'
         ' will be profitable or unprofitable')

# sales input
sales = st.number_input('Enter Sales Amount',
                        min_value= 0.0)

#Quantity input
quantity = st.number_input('Enter Quantity',
                        min_value= 1)

#Discount input
discount = st.number_input('Enter Discount',
                        min_value= 0.0,
                        max_value= 1.0)

# Category selection
category = st.selectbox('Select Category',
                        options=['Furniture', 'Office Supplies', 'Technology'])

#segment input
segment = st.selectbox('Select Segment',
                        options=['Consumer', 'Corporate', 'Home Office'])

# Region input
region = st.selectbox('Select Region',
                        options=['East', 'Central', 'South', 'West'])

# create input dataframe
input_data = {
    'Sales': [sales],
    'Quantity': [quantity],
    'Discount': [discount],
    'Category': [category],
    'Segment': [segment],
    'Region': [region]
}

# Convert into DataFrame

input_df = pd.DataFrame(input_data)


# One-Hot Encode Input
input_encoded = pd.get_dummies(input_df)

# Align input column with training column
input_encoded = input_encoded.reindex(
    columns=feature_columns,
    fill_value=0)

# Prediction button
if st.button('Predict'):

    prediction = model.predict(input_encoded)

    if prediction[0] == 'profitable':
        st.success(
            'This transaction is predicted to be PROFITABLE.'
            )
    else:
        st.error(
            'This transaction is predicted to be UNPROFITABLE'
            )
