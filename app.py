import streamlit as st
import pickle
import numpy as np

# Load the trained Random Forest model
with open("RF_sat.pk1", "rb") as file:
    model = pickle.load(file)

st.title("✈️ Flight Passenger Satisfaction Prediction")

st.write("Fill the passenger details below:")

# Input fields for all 22 features
Gender = st.selectbox("Gender", ["Male", "Female"])
Customer_Type = st.selectbox("Customer Type", ["Loyal Customer", "Disloyal Customer"])
Age = st.slider("Age", 10, 100, 30)
Type_of_Travel = st.selectbox("Type of Travel", ["Business travel", "Personal Travel"])
Class = st.selectbox("Class", ["Business", "Eco", "Eco Plus"])
Flight_Distance = st.number_input("Flight Distance", min_value=100, max_value=5000, step=1)

Inflight_wifi_service = st.slider("Inflight Wifi Service (0-5)", 0, 5, 3)
Departure_Arrival_time_convenient = st.slider("Departure/Arrival Time Convenient (0-5)", 0, 5, 3)
Ease_of_Online_booking = st.slider("Ease of Online Booking (0-5)", 0, 5, 3)
Gate_location = st.slider("Gate Location (0-5)", 0, 5, 3)
Food_and_drink = st.slider("Food and Drink (0-5)", 0, 5, 3)
Online_boarding = st.slider("Online Boarding (0-5)", 0, 5, 3)
Seat_comfort = st.slider("Seat Comfort (0-5)", 0, 5, 3)
Inflight_entertainment = st.slider("Inflight Entertainment (0-5)", 0, 5, 3)
On_board_service = st.slider("On-board Service (0-5)", 0, 5, 3)
Leg_room_service = st.slider("Leg Room Service (0-5)", 0, 5, 3)
Baggage_handling = st.slider("Baggage Handling (0-5)", 0, 5, 3)
Checkin_service = st.slider("Check-in Service (0-5)", 0, 5, 3)
Inflight_service = st.slider("Inflight Service (0-5)", 0, 5, 3)
Cleanliness = st.slider("Cleanliness (0-5)", 0, 5, 3)

Departure_Delay = st.number_input("Departure Delay in Minutes", 0, 1000, 0)
Arrival_Delay = st.number_input("Arrival Delay in Minutes", 0, 1000, 0)

# Manual Label Encoding based on how you trained the model
Gender = 1 if Gender == "Male" else 0
Customer_Type = 1 if Customer_Type == "Loyal Customer" else 0
Type_of_Travel = 1 if Type_of_Travel == "Business travel" else 0
Class = 0 if Class == "Business" else (1 if Class == "Eco" else 2)

# Make prediction
if st.button("Predict Satisfaction"):
    input_data = np.array([[
        Gender, Customer_Type, Age, Type_of_Travel, Class,
        Flight_Distance, Inflight_wifi_service,
        Departure_Arrival_time_convenient, Ease_of_Online_booking,
        Gate_location, Food_and_drink, Online_boarding, Seat_comfort,
        Inflight_entertainment, On_board_service, Leg_room_service,
        Baggage_handling, Checkin_service, Inflight_service,
        Cleanliness, Departure_Delay, Arrival_Delay
    ]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ The passenger is **Satisfied**.")
    else:
        st.error("❌ The passenger is **Not Satisfied**.")
