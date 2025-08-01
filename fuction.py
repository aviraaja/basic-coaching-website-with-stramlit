from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize the OpenAI chat model
model = ChatGroq(model_name="llama-3.1-8b-instant") # You can also try: "llama3-8b-8192", etc.)

# Streamlit UI
st.header('Reasearch Lab')

user_input = st.text_input('Enter your prompt:')

if st.button('Summarize'):
    if user_input:
        result = model.invoke(user_input)
        st.write(result.content)
    else:
        st.warning("Please enter a prompt before clicking summarize.")
