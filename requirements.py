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

        # Extract entities and dependencies
        entities = {ent.text: ent.label_ for ent in doc.ents}
        dependencies = {token.text: token.dep_ for token in doc}

        # Determine roles dynamically
        roles = set(entities.values())
        if "USER" in roles:
            user_role = "User"
        else:
            user_role = ""

        if "ACTION" in roles:
            action_role = "I want"
        else:
            action_role = ""

        if "GOAL" in roles:
            goal_role = "So that"
        else:
            goal_role = ""

        # Display user story format
        st.subheader("User Story:")
        st.write(f"As a: {user_role}")
        st.write(f"{action_role}:")
        st.write(f"{goal_role}:")

        st.subheader("Given:")
        st.write("When:")
        st.write("Then:")

        # Display additional information
        st.subheader("Additional Information:")
        st.write(f"Entities: {entities}")
        st.write(f"Dependencies: {dependencies}")

    else:
        st.warning("Please enter some text.")
