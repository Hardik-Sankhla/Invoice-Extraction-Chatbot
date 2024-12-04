import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
from streamlit_lottie import st_lottie
import requests

# Set page configuration
st.set_page_config(page_title="LLama 3.2 Vision AI Chatbot", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

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
        #border: 2px solid #00acee;  /* Border color for images */
        border-radius: 10px;
    }
    .banner-container {
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Load environment variables
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the model and get a response
def get_gemini_response(input_text, image_data, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text

# Function to load Lottie animations from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load the banner and logo images
logo_path = r"E:\MLOPS\LMA3.1INVEXT\Images\Invoizer.png"  # Update the path to your actual logo
banner_path = r"E:\MLOPS\LMA3.1INVEXT\Images\CoverImg.png"  # Path to your banner image
logo = Image.open(logo_path)
banner = Image.open(banner_path)
lottie_animation = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_u4yrau.json")

# Sidebar with logo and animation
with st.sidebar:
    st.image(logo, width=250)  # Adjusted width to make the logo smaller
    st_lottie(lottie_animation, height=200, key="ai_animation")
    st.header("🔍 How to Use")
    st.write("""
        - Input your question in the text box.
        - Upload an image of an invoice (jpg, jpeg, png).
        - Click 'Analyze Image' to get a response from the AI.
    """)
    st.write("Developed by Hardik Sankhla")

# Main app content
# Display banner image at the top
st.image(banner, use_column_width=True)

# Display the title
st.markdown('<div class="title">Invoice Q&A Chatbot</div>', unsafe_allow_html=True)

st.subheader("Ask Your Question:")
input_text = st.text_input("Enter your question or prompt", key="input_prompt")

st.subheader("Upload Invoice Image:")
uploaded_file = st.file_uploader("Upload an invoice image (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)

if st.button("Analyze Image"):
    if uploaded_file and input_text:
        st.spinner('🔄 Analyzing the image...')
    else:
        st.error("Please provide both a prompt and an image.")

# Footer
st.markdown("""
    <div style="text-align:center; margin-top: 50px;">
    Developed with 💡 and 💻 by Hardik Sankhla
    </div>
""", unsafe_allow_html=True)
