import os
import base64
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
from groq import Groq  # Groq API for making requests

# Load environment variables
load_dotenv()  # Load API keys from .env file

# Function to encode the image to base64
def encode_image(image_file):
    return base64.b64encode(image_file.getvalue()).decode("utf-8")

# Initialize Streamlit app
st.set_page_config(page_title="Llama Invoice Q&A Chatbot")
st.header("Llama Invoice Q&A Chatbot")

# Input prompt section
input_prompt = """
    You are an expert in understanding invoices.
    You will receive input images as invoices &
    you will have to answer questions based on the input image.
"""

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Initialize Groq client
client = Groq()

# Submit button
if st.button("Tell me about the image"):
    if uploaded_file and input_text:
        # Encode the image to base64 format
        base64_image = encode_image(uploaded_file)

        # Prepare the request payload for the Groq API
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": input_text},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ]

        # Call Groq API to get the response
        try:
            response = client.chat.completions.create(
                model="llama-3.2-90b-vision-preview",  # Use the specified model
                messages=messages,
                temperature=0,  # Set temperature for deterministic response
                max_tokens=1024,
                top_p=1,
                stream=False
            )

            # Display the response from the Groq model
            st.subheader("The Response is")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please provide both a prompt and an image.")

# Clear inputs button
if st.button("Clear"):
    st.experimental_rerun()
