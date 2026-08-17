import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("stress_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page settings
st.set_page_config(
    page_title="Student Stress Prediction",
    page_icon="🧠",
    layout="wide"
)

# Title
st.title("🧠 Student Stress Level Prediction")

st.write(
    "Predict student stress level using academic and lifestyle factors."
)

st.info(
    "This application is an educational project and is not a medical diagnosis."
)

st.divider()

# Input section
st.header("Enter Student Information")

col1, col2 = st.columns(2)

with col1:

    study_hours = st.slider(
        "Study Hours per Day",
        0, 12, 4
    )

    sleep_hours = st.slider(
        "Sleep Hours per Day",
        0, 12, 7
    )

    attendance = st.slider(
        "Attendance Percentage",
        0, 100, 80
    )

    exam_pressure = st.selectbox(
        "Exam Pressure",
        ["Low", "Medium", "High"]
    )

with col2:

    assignment_load = st.selectbox(
        "Assignment Load",
        ["Low", "Medium", "High"]
    )

    physical_activity = st.slider(
        "Physical Activity Hours per Week",
        0, 15, 3
    )

    screen_time = st.slider(
        "Screen Time Hours per Day",
        0, 15, 5
    )

    academic_performance = st.slider(
        "Academic Performance",
        0, 100, 70
    )

# Convert text values to numbers
exam_pressure_value = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}[exam_pressure]

assignment_load_value = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}[assignment_load]

st.divider()

# Prediction button
if st.button("🔍 Predict Stress Level", use_container_width=True):

    input_data = pd.DataFrame({
        "study_hours": [study_hours],
        "sleep_hours": [sleep_hours],
        "attendance": [attendance],
        "exam_pressure": [exam_pressure_value],
        "assignment_load": [assignment_load_value],
        "physical_activity": [physical_activity],
        "screen_time": [screen_time],
        "academic_performance": [academic_performance]
    })

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == "Low":

        st.success("🟢 LOW STRESS")

        st.write(
            "The entered information indicates a relatively low stress pattern."
        )

    elif prediction == "Moderate":

        st.warning("🟡 MODERATE STRESS")

        st.write(
            "The entered information indicates a moderate stress pattern. "
            "Better time management, adequate sleep, and regular breaks may help."
        )

    else:

        st.error("🔴 HIGH STRESS")

        st.write(
            "The entered information indicates a high stress pattern. "
            "Consider seeking appropriate academic or wellness support."
        )

    st.subheader("Entered Student Information")

    st.dataframe(input_data)