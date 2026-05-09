# 🗒️ AI Meeting Notes Summarizer

A Python NLP web app that automatically summarizes meeting notes 
and extracts action items.

## Features
- Automatic text summarization
- Action item extraction
- Simple web interface

## Tech Stack
Python, spaCy, sumy, Streamlit

## How To Run

**Step 1 — Install libraries**
pip install streamlit spacy sumy

**Step 2 — Download language models**
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

**Step 3 — Run the app**
streamlit run app.py

**Step 4 — Open browser**
http://localhost:8501
