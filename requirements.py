import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

# Streamlit app
st.title("Dynamic User Story Generator")

# Input text area
text_input = st.text_area("Enter your text here:")

if st.button("Generate User Story"):
    if text_input:
        # Preprocess text for summarization
        input_ids = tokenizer.encode("summarize: " + text_input, return_tensors="pt", max_length=512)

        # Generate summary
        summary_ids = model.generate(input_ids, max_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        # Display the generated user story
        st.subheader("Generated User Story:")
        st.write(summary)

    else:
        st.warning("Please enter some text.")
