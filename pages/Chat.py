import os
import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

from modules.chatbot import Chatbot
from modules.history import ChatHistory
from modules.utils import Utilities
from modules.sidebar import Sidebar
from modules.layout import Layout
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from streamlit_chat import message

# Streamlit page configuration
st.set_page_config(layout="wide", page_icon="💬", page_title="Chat-Bot 🤖")

# Instantiate main components
layout, sidebar, utils = Layout(), Sidebar(), Utilities()
history = ChatHistory()  # Chat history manager

def setup_environment():
    user_api_key = utils.load_api_key()
    if not user_api_key:
        layout.show_api_key_missing()
    else:
        os.environ["OPENAI_API_KEY"] = user_api_key
    
def connect_to_database():
    db_config = {
        'host': 'localhost',
        'database': 'test', 
        'user': 'root',
        'password': 'roott'
    }
    try:
        conn = mysql.connector.connect(**db_config)
        st.success('Successfully connected to the database.')
        return conn
    except Error as e:
        st.error(f"Error while connecting to MySQL: {str(e)}")
        return None

def load_data(conn):
    if conn:
        query = "SELECT * FROM hotel_bookings"
        data = pd.read_sql(query, conn)
        return data
    return None

def app():
     # Create ChatHistory instance
    chat_history = ChatHistory()
    layout.show_header("MySQL Database Interaction")
    setup_environment()
    conn = connect_to_database()
    data = load_data(conn)
    
    # Initialize chat history for some identifier, e.g., "hotel_bookings"
    chat_history.initialize("hotel_bookings")
    
    if data is not None:
        st.write("Preview of the data loaded from the database:")
        st.dataframe(data.head())

        agent = create_pandas_dataframe_agent(OpenAI(), data)
        is_ready, user_input = layout.prompt_form()
        
        if is_ready:
            try:
                response = agent.run(user_input)
                history.append("user", user_input)
                history.append("assistant", response)
                history.generate_messages(st.container())
            except Exception as e:
                st.error(f"Error during query execution: {str(e)}")
                
    if conn and conn.is_connected():
        conn.close()
        st.info("Database connection closed.")

if __name__ == "__main__":
    app()
