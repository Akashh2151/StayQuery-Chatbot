import os
import streamlit as st
from streamlit_chat import message

class ChatHistory:
    
    def __init__(self):
        self.history = st.session_state.get("history", [])
        st.session_state["history"] = self.history

    def default_greeting(self):
        return "Hey there! 👋"

    def default_prompt(self, topic):
        return f"Hello! Ask me anything about {topic} 🤗"

    def initialize_user_history(self):
        if "user" not in st.session_state:
            st.session_state["user"] = [self.default_greeting()]

    def initialize_assistant_history(self, identifier):
        if "assistant" not in st.session_state:
            st.session_state["assistant"] = [self.default_prompt(identifier)]

    def initialize(self, identifier):
        self.initialize_user_history()
        self.initialize_assistant_history(identifier)

    def reset(self, identifier):
        st.session_state["history"] = []
        self.initialize(identifier)

    def append(self, mode, message):
        if mode in st.session_state:
            st.session_state[mode].append(message)
        else:
            st.error(f"Session state does not have key '{mode}'")

    def generate_messages(self, container):
        user_msgs = st.session_state.get("user", [])
        assistant_msgs = st.session_state.get("assistant", [])
        with container:
            for i, (user_msg, assistant_msg) in enumerate(zip(user_msgs, assistant_msgs)):
                message(user_msg, is_user=True, key=f"history_{i}_user", avatar_style="big-smile")
                message(assistant_msg, key=f"history_{i}_assistant", avatar_style="thumbs")
