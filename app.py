
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Student AI Mental Health Companion")

st.title("🧠 Student AI Mental Health Companion Chatbot")
st.write("Talk freely. I'm here to support you ❤️")

# Use your Gemini API key
genai.configure(api_key="AIzaSyBozIGtICjU7ytovYo9RQGUZ0UZJcPR6yE")

# Use latest working free model
model = genai.GenerativeModel("gemini-1.5-flash")

# Chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

user_input = st.text_input("You:", key="user_input")

if st.button("Send", key="send_button"):
    if user_input:
        try:
            response = st.session_state.chat.send_message(user_input)
            st.write("🤖 AI:", response.text)
        except Exception as e:
            st.error(f"Actual Error: {e}")
