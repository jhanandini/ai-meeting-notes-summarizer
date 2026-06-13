# 🗒️ AI Meeting Notes Summarizer

A simple tool that turns long, messy meeting notes into clear summaries and actionable points. Built using **Streamlit** and **Google Gemini 2.5 Flash**.

## Features
- Automatic text summarization
- Action item extraction
- Clean web interface

## Tech Stack
Python, Streamlit, Google Gemini 2.5 Flash API

## How To Run

**Step 1 - Install libraries**
pip install streamlit google-genai python-dotenv

**Step 2 - Set up API Key**
Create a .env file in your project folder and add your key: GOOGLE_API_KEY="your_api_key_here"

**Step 3 - Run the app**
streamlit run app.py
