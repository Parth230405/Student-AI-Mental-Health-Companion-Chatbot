
import streamlit as st
from google import genai

st.set_page_config(page_title="Student AI Mental Health Companion")

st.title("🧠 Student AI Mental Health Companion Chatbot")
st.write("Talk freely. I'm here to support you ❤️")

# Create Gemini client
client = genai.Client(api_key="AIzaSyBxrOdHqhjh5qcM7bvziq2iiwbcN2KyvGk")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", key="user_input")

if st.button("Send", key="send_button"):
    if user_input:
        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=user_input,
            )

            st.session_state.history.append(("You", user_input))
            st.session_state.history.append(("AI", response.text))

        except Exception as e:
            st.error(f"Actual Error: {e}")

# Display chat history
for role, message in st.session_state.history:
    if role == "You":
        st.write(f"🧑 You: {message}")
    else:
        st.write(f"🤖 AI: {message}")
