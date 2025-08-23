import os
import streamlit as st
from dotenv import load_dotenv


def load_env_variables():
    load_dotenv()


def check_api_keys():
    required_keys = {
        "GOOGLE_GEMINI_API_KEY": os.getenv("GOOGLE_GEMINI_API_KEY"),
        "OMDB_API_KEY": os.getenv("OMDB_API_KEY"),
    }

    missing_keys = [key for key, value in required_keys.items() if not value]

    if missing_keys:
        st.error(f"❌ Missing API keys: {', '.join(missing_keys)}")
        st.info("Please add the missing API keys to your .env file")
        return False

    return True
