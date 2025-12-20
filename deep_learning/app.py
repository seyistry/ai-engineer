import os
from dotenv import load_dotenv
import streamlit as st
from google import genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
def create_chat(model="gemini-2.5-flash"):
    """Start a new chat."""
    return client.chats.create(model=model)
def send_message(chat, message: str):
    """Send a message in the chat session and get response."""
    return chat.send_message(message)
# Streamlit UI setup
st.set_page_config(page_title="Gemini Chatbot", layout="wide")
st.title("Gemini Chatbot")
# Initialize session state
if "chat" not in st.session_state:
    # create a new Gemini chat session
    st.session_state.chat = create_chat()
if "messages" not in st.session_state:
    # store conversation history
    st.session_state.messages = [
        {"role": "system", "content": "You are the best product designer in silicon valley."}
    ]
# Display chat messages
for msg in st.session_state.messages:
    # st.chat_message supports "user" or "assistant"
    role = "assistant" if msg["role"] == "assistant" else "user"
    with st.chat_message(role):
        st.markdown(msg["content"])
# Input from user
user_input = st.chat_input("Type your message…")
if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Display in UI immediately
    with st.chat_message("user"):
        st.markdown(user_input)
    # Send to Gemini
    resp = send_message(st.session_state.chat, user_input)
    bot_reply = resp.text
    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)