import streamlit as st
import spacy

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.warning("Downloading spaCy English language model...")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Streamlit app
st.title("Requirements Generator")

# Input text area
text_input = st.text_area("Enter your text here:")

if st.button("Generate Requirements"):
    if text_input:
        # Process text with spaCy
        doc = nlp(text_input)

        # Extract sentences
        sentences = [sent.text.strip() for sent in doc.sents]

        # Display user story format
        st.subheader("User Story:")
        for i, sentence in enumerate(sentences):
            st.write(f"{sentence}:")

        # Display additional information
        st.subheader("Additional Information:")
        st.write(f"Extracted Sentences: {sentences}")

    else:
        st.warning("Please enter some text.")
