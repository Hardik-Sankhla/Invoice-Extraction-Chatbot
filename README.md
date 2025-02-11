# 🥾 Gemini Invoice Analyzer 🤖

**AI-Powered Invoice Processing Web Application**

## 📌 Overview

Gemini Invoice Analyzer is an advanced AI-based web application designed to process invoices using **Google’s Gemini AI**. The application enables users to upload invoice images and extract relevant details through **natural language queries**. It provides a seamless **LLM-powered** invoice analysis experience with an interactive interface.

---

## 🚀 Features

- **📸 Invoice Image Upload**: Supports `.jpg`, `.jpeg`, and `.png` file formats.
- **🤖 AI-Powered Analysis**: Uses **Gemini 1.5 Pro** for accurate invoice understanding.
- **🔍 Custom Query Support**: Allows users to extract **specific invoice details** via text input.
- **💜 Text Extraction (OCR)**: Converts invoice images into text for AI-based processing.
- **📊 Intelligent Response Generation**: Provides structured and relevant insights.
- **💾 Secure & Efficient Processing**: Ensures user data is handled safely.

---

## 🏠 Technologies Utilized

- **Programming Language**: Python 🐍
- **Web Framework**: Streamlit 🎨
- **AI Model**: Google Gemini API 🤖
- **Image Processing**: OpenCV & PIL 🎨
- **OCR (Optical Character Recognition)**: Tesseract OCR 💡
- **Logging & Debugging**: Logging Module 💜
- **Configuration Handling**: Environment Variables `.env` ⚙️
- **Cloud Services**: Google AI Services ☁️

---

## 🎮 Application Workflow

1⃣ **Upload an Invoice Image**  
2⃣ **Enter a Query (e.g., "What is the total amount?")**  
3⃣ **Process Image & Extract Text via OCR**  
4⃣ **Send Query & Extracted Data to Gemini AI**  
5⃣ **Display AI-Generated Invoice Analysis**  

---

## 🛠️ Installation & Setup

### 🔹 Clone the Repository
```bash
git clone https://github.com/Hardik-Sankhla/Invoice-Extraction-Chatbot.git
cd Invoice-Extraction-Chatbot
```

### 🔹 Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Configure API Keys
Create a `.env` file in the root directory and add your Google Gemini API Key:
```bash
GEMINI_API_KEY="your_google_gemini_api_key"
```

### 🔹 Run the Application
```bash
streamlit run app.py
```
Open the browser and go to `http://localhost:8501` to access the application.

---

## 💂️‍ File Structure

```bash
Invoice-Extraction-Chatbot/
│
├── services/
│   ├── gemini_service.py  # Handles API calls to Gemini AI
│   ├── image_processor.py  # Processes uploaded invoice images
│
├── utils/
│   ├── logger.py  # Logs application events and errors
│
├── config/
│   ├── config.py  # Manages API key and configuration settings
│
├── static/  # Contains UI assets (if any)
│
├── app.py  # Main Streamlit application
├── requirements.txt  # Dependencies
├── README.md  # Project documentation
└── .env  # API keys and sensitive configurations
```

---

## 💡 Usage Guide

### 🎮 Uploading Invoice Image  
- Click on **"Upload an invoice image"** and select a valid file (`.jpg`, `.jpeg`, `.png`).

### 🔍 Asking Invoice-Related Questions  
- Enter a query like **"What is the invoice date?"**, **"Extract the vendor name."**, etc.

### 🚀 Processing and AI Analysis  
- Click **"Analyze Image"** to extract text and process it with Gemini AI.

### 💜 Viewing Results  
- AI-generated insights appear under the **"Response"** section.

---

## 🔧 Troubleshooting

🔹 **Issue: Streamlit App Not Starting**  
👉 Run `streamlit clean` and restart the app.  

🔹 **Issue: API Key Error**  
👉 Ensure `GEMINI_API_KEY` is correctly set in the `.env` file.

🔹 **Issue: No Response from AI**  
👉 Check internet connectivity and API request limits.

---

## 📈 Future Scope

👉 **Multi-Format Support**: Extend to PDFs and scanned documents.  
👉 **Enhanced Data Extraction**: Automate invoice field detection using AI.  
👉 **Database Integration**: Store extracted invoice details for future analysis.  
👉 **User Authentication**: Add login/signup features for personalized access.  

---

## 🤝 Contributing

Want to improve **Gemini Invoice Analyzer**? Follow these steps:

1⃣ **Fork the repository**  
2⃣ **Create a new branch** (`git checkout -b feature-branch`)  
3⃣ **Commit your changes** (`git commit -m "Added new feature"`)  
4⃣ **Push to your branch** (`git push origin feature-branch`)  
5⃣ **Create a Pull Request** 🚀  

---

## 📜 License
This project is licensed under the **MIT License**.  

📩 **Author**: [Hardik Sankhla](https://github.com/Hardik-Sankhla)  
🔗 **GitHub Repository**: [Gemini-Invoice-Analyzer](https://github.com/Hardik-Sankhla/Gemini-Invoice-Analyzer)

---

## 🎯 Conclusion
The **Gemini Invoice Analyzer** provides an **intelligent, AI-powered** approach to extracting and analyzing invoice details efficiently. Future enhancements aim to **extend document compatibility, enhance AI accuracy, and integrate smart automation** for large-scale business applications. 🚀
