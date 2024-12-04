import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
import base64
import requests

# Set page configuration
st.set_page_config(page_title="Gemini Image Demo", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

# Custom CSS to apply the new color palette, background color, and adjust the logo size
st.markdown("""
    <style>
    .stApp {
        background-color: #1f1f1f;  /* Dark background color */
    }
    .title {
        color: #00acee;  /* Light blue color for the title */
        font-family: 'Verdana', sans-serif;
        font-size: 45px;
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        color: #ffa500;  /* Orange shade for subheaders */
        font-size: 22px;
        margin-top: 20px;
    }
    .stButton>button {
        background-color: #333;  /* Dark button color */
        color: white;
        border-radius: 10px;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #555;  /* Hover effect with lighter shade */
    }
    .stImage {
        border-radius: 10px;
    }
    .banner-container {
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Load environment variables
load_dotenv()

# Load the banner and logo images
logo_path = r"D:\LLMOPS\App\Gemini-Invoizer\Images\Invoizer.png"  # Update the path to your actual logo
banner_path = r"D:\LLMOPS\App\Gemini-Invoizer\Images\coverimg.png"  # Path to your banner image
logo = Image.open(logo_path)
banner = Image.open(banner_path)

# Sidebar with logo
with st.sidebar:
    st.image(logo, width=250)  # Adjusted width to make the logo smaller
    st.header("🔍 How to Use")
    st.write("""
        - Input your question in the text box.
        - Upload an image of an invoice (jpg, jpeg, png).
        - Click 'Analyze Image' to get a response from the AI.
    """)
    st.write("Developed by Hardik Sankhla")

# Display banner image at the top
st.image(banner, use_column_width=True)

# Display the title
st.markdown('<div class="title">Gemini Q&A Chatbot</div>', unsafe_allow_html=True)

# Initialize Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini model
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Function to prepare image data for model input
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Input prompt section
input_prompt = """
    You are an expert in understanding invoices.
    You will receive input images as invoices &
    you will have to answer questions based on the input image.
"""

# Input fields
st.subheader("Ask Your Question:")
input_text = st.text_input("Enter your question or prompt", key="input_prompt")

st.subheader("Upload Invoice Image:")
uploaded_file = st.file_uploader("Upload an invoice image (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

# Display uploaded image if available
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)

# Analyze Image button
if st.button("Analyze Image"):
    if uploaded_file and input_text:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input_text)
        
        # Display response
        st.subheader("The Response is")
        st.write(response)
    else:
        st.error("Please provide both a prompt and an image.")

# Footer
st.markdown("""
    <div style="text-align:center; margin-top: 50px;">
    Developed with 💡 and 💻 by Hardik Sankhla
    </div>
""", unsafe_allow_html=True)
