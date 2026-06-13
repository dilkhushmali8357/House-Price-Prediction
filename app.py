import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction")

area = st.number_input("Area (sq ft)", value=2000)

bedrooms = st.number_input("Bedrooms", value=3)

bathrooms = st.number_input("Bathrooms", value=2)

stories = st.number_input("Stories", value=2)

mainroad = st.selectbox(
    "Main Road Access",
    ["yes", "no"]
)

guestroom = st.selectbox(
    "Guest Room",
    ["yes", "no"]
)

basement = st.selectbox(
    "Basement",
    ["yes", "no"]
)

hotwaterheating = st.selectbox(
    "Hot Water Heating",
    ["yes", "no"]
)

airconditioning = st.selectbox(
    "Air Conditioning",
    ["yes", "no"]
)

parking = st.number_input(
    "Parking Spaces",
    value=1
)

prefarea = st.selectbox(
    "Preferred Area",
    ["yes", "no"]
)

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["furnished",
     "semi-furnished",
     "unfurnished"]
)

# Encoding

binary = {
    "yes":1,
    "no":0
}

furnishing = {
    "furnished":0,
    "semi-furnished":1,
    "unfurnished":2
}

input_data = pd.DataFrame({
    "area":[area],
    "bedrooms":[bedrooms],
    "bathrooms":[bathrooms],
    "stories":[stories],
    "mainroad":[binary[mainroad]],
    "guestroom":[binary[guestroom]],
    "basement":[binary[basement]],
    "hotwaterheating":[binary[hotwaterheating]],
    "airconditioning":[binary[airconditioning]],
    "parking":[parking],
    "prefarea":[binary[prefarea]],
    "furnishingstatus":[furnishing[furnishingstatus]]
})

if st.button("Predict Price"):

    prediction = model.predict(input_data)

    st.success(
        f"Predicted House Price: ₹ {prediction[0]:,.0f}"
    )