import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("walkrun.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Set page title and layout
st.set_page_config(page_title="Exercise Prediction", layout="wide")

# Custom styling
st.markdown(
    """
    <style>
        .main { text-align: center; }
        div.stButton > button { width: 100%; }
        div.block-container { padding-top: 1rem; }
        .st-emotion-cache-16txtl3 { align-items: center; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Exercise Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Determine if the user is regularly exercising or not</h4>", unsafe_allow_html=True)

# Create input form with columns for better UI
col1, col2, col3 = st.columns(3)

with col1:
    wrist = st.number_input("Wrist", value=0.0, step=0.01)
    acceleration_x = st.number_input("Acceleration X", value=0.0, step=0.01)
    acceleration_y = st.number_input("Acceleration Y", value=0.0, step=0.01)
    acceleration_z = st.number_input("Acceleration Z", value=0.0, step=0.01)

with col2:
    gyro_x = st.number_input("Gyro X", value=0.0, step=0.01)
    gyro_y = st.number_input("Gyro Y", value=0.0, step=0.01)
    gyro_z = st.number_input("Gyro Z", value=0.0, step=0.01)

with col3:
    month = st.number_input("Month", min_value=1, max_value=12, value=1)
    day = st.number_input("Day", min_value=1, max_value=31, value=1)
    hour = st.number_input("Hour", min_value=0, max_value=23, value=0)
    minute = st.number_input("Minute", min_value=0, max_value=59, value=0)
    second = st.number_input("Second", min_value=0, max_value=59, value=0)

# Convert input to NumPy array
input_data = np.array([[wrist, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z, month, day, hour, minute, second]])

# Centered Predict Button
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Predict", help="Click to predict whether the user is exercising or not"):
    prediction = model.predict(input_data)[0]
    exercise_status = "🛑 Not Exercising" if prediction == 0 else "✅ Regularly Exercising"

    # Display result with color styling
    st.markdown(
        f"<h2 style='text-align: center; color: {'#FF5733' if prediction == 0 else '#4CAF50'}'>{exercise_status}</h2>",
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)