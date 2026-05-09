import streamlit as st
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

nlp = spacy.load("en_core_web_sm")

st.title("🗒️ AI Meeting Notes Summarizer")

text = st.text_area("Paste your meeting notes here:", height=250)

if st.button("Generate Summary"):

    if len(text.strip()) == 0:
        st.warning("Please paste some meeting notes first.")

    else:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary_sentences = summarizer(parser.document, 3)

        st.subheader("📋 Summary")
        for sentence in summary_sentences:
            st.write("• " + str(sentence))

        doc = nlp(text)
        actions = []

        for sent in doc.sents:
            if "will" in sent.text or "should" in sent.text:
                actions.append(sent.text)

        st.subheader("✅ Action Items")

        if actions:
            for a in actions:
                st.write("- " + a)
        else:
            st.write("No action items detected.")