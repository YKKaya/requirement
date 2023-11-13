import streamlit as st
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Streamlit app
st.title("Requirements Generator")

# Input text area
text_input = st.text_area("Enter your text here:")

if st.button("Generate Requirements"):
    if text_input:
        # Process text with spaCy
        doc = nlp(text_input)

        # Extract entities and dependencies
        entities = {ent.text: ent.label_ for ent in doc.ents}
        dependencies = {token.text: token.dep_ for token in doc}

        # Display user story format
        st.subheader("User Story:")
        st.write("As a:")
        st.write("I want:")
        st.write("So that:")

        st.subheader("Given:")
        st.write("When:")
        st.write("Then:")

        # Display additional information
        st.subheader("Additional Information:")
        st.write(f"Entities: {entities}")
        st.write(f"Dependencies: {dependencies}")

    else:
        st.warning("Please enter some text.")
