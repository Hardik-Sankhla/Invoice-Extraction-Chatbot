from PIL import Image
import io
from utils.logger import log_error

def process_uploaded_image(uploaded_file):
    try:
        image = Image.open(io.BytesIO(uploaded_file.getvalue()))
        return image
    except Exception as e:
        log_error(f"Image processing error: {e}")
        return None
