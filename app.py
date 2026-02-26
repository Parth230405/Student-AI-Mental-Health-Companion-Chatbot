
import streamlit as st
import google.generativeai as genai
import os

# Set page config
st.set_page_config(page_title="Student AI Mental Health Companion")

st.title("🧠 Student AI Mental Health Companion Chatbot")
st.write("Talk freely. I'm here to support you ❤️")

# Add your Gemini API key here
GEMINI_API_KEY = "AIzaSyDgRJsh6E65tl_MqUm3SJE_Pkm9_gV7mP8"

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-1.5-flash")

# Initialize chat history
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# User input
user_input = st.text_input("You:")

user_input = st.text_input("You:", key="user_input")

if st.button("Send", key="send_button"):
    if user_input:
        try:
            response = st.session_state.chat.send_message(user_input)
            st.write("🤖 AI:", response.text)
        except Exception as e:
            st.error(f"Actual Error: {e}")
