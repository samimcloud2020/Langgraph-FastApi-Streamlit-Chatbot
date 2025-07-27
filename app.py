import streamlit as st
import requests
import json
import uuid

# Streamlit page configuration
st.set_page_config(page_title="Medical Chatbot", page_icon="🏥", layout="centered")

# Initialize session state for conversation history and thread ID
if "messages" not in st.session_state:
    st.session_state.messages = []
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())  # Unique thread ID for each session

# FastAPI endpoint URL (assuming FastAPI runs on localhost:8000)
API_URL = "http://127.0.0.1:8000/chat"

# Streamlit UI
st.title("🏥 Medical Chatbot")
st.write("Ask health-related questions and get information powered by reliable sources. Always consult a healthcare professional for medical advice.")

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user message
user_input = st.chat_input("Type your question here (e.g., 'What are the symptoms of diabetes?')")

if user_input:
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare payload for FastAPI
    payload = {
        "messages": [user_input],
        "thread_id": st.session_state.thread_id
    }

    # Send request to FastAPI backend
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  # Raise exception for bad status codes
        bot_response = response.json().get("response", "Error: No response from server")

        # Add bot response to session state
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        with st.chat_message("assistant"):
            st.markdown(bot_response)
    except requests.RequestException as e:
        error_message = f"Error communicating with the server: {str(e)}"
        st.session_state.messages.append({"role": "assistant", "content": error_message})
        with st.chat_message("assistant"):
            st.markdown(error_message)

# Add a button to clear conversation history
if st.button("Clear Conversation"):
    st.session_state.messages = []
    st.session_state.thread_id = str(uuid.uuid4())  # Generate new thread ID
    st.experimental_rerun()