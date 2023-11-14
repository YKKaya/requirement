# Import streamlit and other libraries
import streamlit as st
import spacy
import re

# Load a pre-trained NLP model
nlp = spacy.load("en_core_web_sm")

# Define a function to extract user stories from text
def extract_user_stories(text):
  # Split the text into sentences
  sentences = [sent.text for sent in nlp(text).sents]
  # Initialize an empty list to store user stories
  user_stories = []
  # Loop through each sentence
  for sent in sentences:
    # Check if the sentence contains the word "want"
    if "want" in sent.lower():
      # Extract the subject and the object of the sentence
      subject = ""
      object = ""
      for token in nlp(sent):
        if token.dep_ == "nsubj":
          subject = token.text
        if token.dep_ == "dobj":
          object = token.text
      # Format the user story as "As a <subject>, I want <object>"
      user_story = f"As a {subject}, I want {object}"
      # Append the user story to the list
      user_stories.append(user_story)
  # Return the list of user stories
  return user_stories

# Define a function to extract acceptance criteria from text
def extract_acceptance_criteria(text):
  # Split the text into sentences
  sentences = [sent.text for sent in nlp(text).sents]
  # Initialize an empty list to store acceptance criteria
  acceptance_criteria = []
  # Loop through each sentence
  for sent in sentences:
    # Check if the sentence contains the word "when" or "then"
    if "when" in sent.lower() or "then" in sent.lower():
      # Extract the condition and the outcome of the sentence
      condition = ""
      outcome = ""
      for token in nlp(sent):
        if token.dep_ == "advcl":
          condition = token.text
        if token.dep_ == "ROOT":
          outcome = token.text
      # Format the acceptance criterion as "Given <condition>, When <outcome>"
      acceptance_criterion = f"Given {condition}, When {outcome}"
      # Append the acceptance criterion to the list
      acceptance_criteria.append(acceptance_criterion)
  # Return the list of acceptance criteria
  return acceptance_criteria

# Define a function to extract additional information from text
def extract_additional_information(text):
  # Split the text into sentences
  sentences = [sent.text for sent in nlp(text).sents]
  # Initialize an empty list to store additional information
  additional_information = []
  # Loop through each sentence
  for sent in sentences:
    # Check if the sentence does not contain the words "want", "when", or "then"
    if "want" not in sent.lower() and "when" not in sent.lower() and "then" not in sent.lower():
      # Append the sentence to the list
      additional_information.append(sent)
  # Return the list of additional information
  return additional_information

# Create a streamlit app
st.title("Streamlit App for Requirements Extraction")

# Create a text area for user input
user_input = st.text_area("Enter your text here")

# Create a button to process the user input
if st.button("Extract Requirements"):
  # Extract user stories from the user input
  user_stories = extract_user_stories(user_input)
  # Extract acceptance criteria from the user input
  acceptance_criteria = extract_acceptance_criteria(user_input)
  # Extract additional information from the user input
  additional_information = extract_additional_information(user_input)
  # Display the results in different sections
  st.header("User Stories")
  st.write(user_stories)
  st.header("Acceptance Criteria")
  st.write(acceptance_criteria)
  st.header("Additional Information")
  st.write(additional_information)
