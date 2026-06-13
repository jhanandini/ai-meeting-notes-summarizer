import os
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

st.set_page_config(page_title="AI Meeting Summarizer")
st.title("AI Meeting Summarizer")

# Input area
text = st.text_area("Paste your meeting notes here:", height=250)

if st.button("Generate Smart Summary"):
    if not text.strip():
        st.warning("Please paste some meeting notes first.")
    else:
        with st.spinner("Gemini is analyzing..."):
            # Updated Prompt for a professional output
            instructions = """
            You are a professional meeting assistant. Analyze the provided meeting notes and:
            1. Write a concise summary in 3-4 bullet points.
            2. Extract all 'Action Items' assigned to individuals.
            3. Use checkboxes for action items.
            """

            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=text,
                config=types.GenerateContentConfig(
                    system_instruction=instructions,
                    temperature=0.3,
                )
            )

            # Display Output
            st.markdown("---")
            st.markdown(response.text)