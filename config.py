import streamlit as st
import google.generativeai as genai
import os

# Load API key from .env file
genai.configure(api_key=os.environ["API_KEY"])

def generate_text(prompt):
  model = genai.GenerativeModel("gemini-pro")
  response = model.generate_text(prompt=prompt)
  return response.text

st.title("Gemini Powered Text Generator")
user_input = st.text_input("Enter your prompt:")

if user_input:
  generated_text = generate_text(user_input)
  st.write(generated_text)