import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Backend URL
backend_url = "http://127.0.0.1:8000/data"

st.title("PPG Data Visualization")

# Fetching data from the FastAPI backend
def get_data():
    try:
        response = requests.get(backend_url)
        response.raise_for_status()
        return response.json()["data"]
    except requests.exceptions.HTTPError as err:
        st.error(f"HTTP error occurred: {err}")
    except Exception as err:
        st.error(f"An error occurred: {err}")

data = get_data()

if data:
    # Convert the data into a Pandas DataFrame
    df = pd.DataFrame(data)

    # Page navigation
    page = st.sidebar.selectbox(
        "Select a Page",
        ["Home", "Heart Rate Chart", "SpO2 Rate Chart", "PPG Waveform"]
    )

    if page == "Home":
        st.write("## User SPO2 and Heart Rate Data")
        st.write(df)

    elif page == "Heart Rate Chart":
        st.write("## Heart Rate Chart")

        fig, ax = plt.subplots()
        ax.plot(df.index, df["user_heart_rate"], label="Heart Rate (bpm)", color="red")
        ax.set_xlabel("Sample Index")
        ax.set_ylabel("Heart Rate (bpm)")
        ax.set_title("Heart Rate Over Time")
        ax.legend()
        st.pyplot(fig)

    elif page == "SpO2 Rate Chart":
        st.write("## SpO2 Rate Chart")

        fig, ax = plt.subplots()
        ax.plot(df.index, df["user_spo2"], label="SpO2 (%)", color="blue")
        ax.set_xlabel("Sample Index")
        ax.set_ylabel("SpO2 (%)")
        ax.set_title("SpO2 Levels Over Time")
        ax.legend()
        st.pyplot(fig)

    elif page == "PPG Waveform":
        st.write("## PPG Waveform")

        fig, ax = plt.subplots()
        ax.plot(df.index, df["ppg_waveform"], label="PPG Waveform", color="green")
        ax.set_xlabel("Sample Index")
        ax.set_ylabel("PPG Signal")
        ax.set_title("PPG Waveform")
        ax.legend()
        st.pyplot(fig)

else:
    st.write("No data available")
