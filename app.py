import streamlit as st
from services.gemini_service import get_gemini_response
from services.image_processor import process_uploaded_image
from utils.logger import log_info, log_error
from config import Config
from PIL import Image

# Set Streamlit page configuration
st.set_page_config(page_title="Gemini Invoice Analyzer", page_icon="🧾", layout="wide")

# App title
st.title("Gemini Invoice Analyzer 🧾🤖")

# Input text for user queries
input_text = st.text_input("Enter your question or prompt", key="input_prompt")

# File uploader for invoice images
uploaded_file = st.file_uploader("Upload an invoice image (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file:
    image = process_uploaded_image(uploaded_file)
    if image:
        st.image(image, caption="Uploaded Invoice", use_column_width=True)
    else:
        st.error("Error processing uploaded image.")

# Analyze button to process invoice
if st.button("Analyze Image"):
    if uploaded_file and input_text:
        try:
            image_data = [{"mime_type": uploaded_file.type, "data": uploaded_file.getvalue()}]
            response = get_gemini_response(input_text, image_data, "You are an expert in understanding invoices.")
            st.subheader("Response:")
            st.write(response)
            log_info("Successfully processed invoice.")
        except Exception as e:
            st.error("Error processing the invoice. Please try again.")
            log_error(f"Processing error: {e}")
    else:
        st.error("Please provide both a prompt and an image.")
        log_error("Missing input fields.")
