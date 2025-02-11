import google.generativeai as genai
from config import Config
from utils.logger import log_error

# Configure Gemini API
genai.configure(api_key=Config.GOOGLE_API_KEY)

def get_gemini_response(input_text, image_data, prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content([input_text, image_data[0], prompt])
        return response.text
    except Exception as e:
        log_error(f"Gemini API error: {e}")
        return "Error generating response."
