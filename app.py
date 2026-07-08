import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Content Monetization Modeler",
    page_icon="📈",
    layout="centered"
)

# Model Path
MODEL_PATH = Path("models") / "content_monetization_model.joblib"

# Load Model
def load_model():
    if not MODEL_PATH.exists():
        return None
    return joblib.load(MODEL_PATH)

artifact = load_model()

# App Title
st.title("📈 Content Monetization Modeler")
st.write("Predict YouTube Ad Revenue based on video performance.")

# Check Model
if artifact is None:
    st.error("❌ Model file not found. Please train the model first.")
    st.stop()

model = artifact["model"]
feature_columns = artifact["columns"]

# Input Section
st.subheader("🎥 Enter Video Details")

col1, col2 = st.columns(2)

with col1:
    views = st.number_input("Views", min_value=0, value=10000, step=1000)
    likes = st.number_input("Likes", min_value=0, value=500, step=50)
    comments = st.number_input("Comments", min_value=0, value=50, step=5)
    watch_time_minutes = st.number_input(
        "Watch Time (Minutes)",
        min_value=0.0,
        value=2500.0,
        step=100.0,
    )

with col2:
    video_length_minutes = st.number_input(
        "Video Length (Minutes)",
        min_value=1.0,
        value=10.0,
        step=1.0,
    )

    subscribers = st.number_input(
        "Subscribers",
        min_value=0,
        value=50000,
        step=1000,
    )

    category = st.selectbox(
        "Category",
        ["Education", "Gaming", "Music", "Entertainment", "Sports", "News"],
    )

    device = st.selectbox(
        "Device",
        ["Mobile", "Desktop", "TV", "Tablet"],
    )

    country = st.selectbox(
        "Country",
        ["India", "United States", "Canada", "United Kingdom", "Australia"],
    )

# Feature Engineering
engagement_rate = (likes + comments) / (views + 1)
watch_ratio = watch_time_minutes / (video_length_minutes + 1)

# Create Input DataFrame
input_data = pd.DataFrame([
    {
        "views": views,
        "likes": likes,
        "comments": comments,
        "watch_time_minutes": watch_time_minutes,
        "video_length_minutes": video_length_minutes,
        "subscribers": subscribers,
        "engagement_rate": engagement_rate,
        "watch_ratio": watch_ratio,
        "category": category,
        "device": device,
        "country": country,
    }
])

# One-Hot Encoding
input_encoded = pd.get_dummies(input_data)

# Match Training Columns
input_encoded = input_encoded.reindex(
    columns=feature_columns,
    fill_value=0
)

# Predict
if st.button("💰 Predict Revenue"):

    prediction_usd = model.predict(input_encoded)[0]

    # USD to INR Conversion
    usd_to_inr = 86
    prediction_inr = prediction_usd * usd_to_inr

    st.success("✅ Prediction Successful!")

    st.subheader("💵 Predicted Revenue")

    st.metric(
        label="Revenue (USD)",
        value=f"${prediction_usd:,.2f}"
    )

    st.metric(
        label="Revenue (INR)",
        value=f"₹{prediction_inr:,.2f}"
    )

    st.info(
        "The INR value is calculated using an approximate exchange rate of **1 USD = ₹86**."
    )