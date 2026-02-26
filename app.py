
import streamlit as st
import google.generativeai as genai
import os

# Set page config
st.set_page_config(page_title="Student AI Mental Health Companion")

st.title("🧠 Student AI Mental Health Companion Chatbot")
st.write("Talk freely. I'm here to support you ❤️")

# Add your Gemini API key here
GEMINI_API_KEY = "AIzaSyA3BfnrveotNuUzE1xRse8wpaGc6LNWclU"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# User input
user_input = st.text_input("You:")

if st.button("Send") and user_input:
    response = st.session_state.chat.send_message(user_input)
    st.write("🤖 AI:", response.text)
