import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure the Gemini API
genai.configure(api_key=st.secrets['gemini_api_key'])

# Load the Gemini model (you can use other models like 'gemini-pro-vision' if needed)
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")

# Streamlit UI
st.title("Tilapia Fish Detector 🐟")
st.write("Upload a fish image to identify if it's Tilapia and check for infections.")

# File uploader
uploaded_file = st.file_uploader("Upload Fish Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Fish", use_container_width=True)  # ✅ Updated parameter

    st.write("Analyzing the image...")

    # Send image to Gemini
    try:
        response = model.generate_content([
            "You are an expert in fish biology and pathology. Based on the image, determine:\n"
            "1. Is the fish a Tilapia?\n"
            "2. If it is, is it infected? Consider visible signs like lesions, discoloration, swelling, or parasites.\n"
            "Reply ONLY with one of the following options:\n"
            "- 'This is not a Tilapia.'\n"
            "- 'This is a healthy Tilapia.'\n"
            "- 'This is an infected Tilapia.'",
            image
        ])

        answer = response.text.strip()
        st.subheader("Result:")
        st.success(answer)

    except Exception as e:
        st.error(f"Error analyzing image: {e}")
