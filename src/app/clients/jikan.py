import requests
import streamlit as st
from typing import Dict, List, Optional


class JikanClient:
    def __init__(self):
        self.session = requests.Session()

    def search_anime(self, query: str) -> List[Dict]:
        try:
            url = f"https://api.jikan.moe/v4/anime?q={query}&limit=10"
            response = self.session.get(url, timeout=10)
            data = response.json()
            return data.get("data", [])
        except Exception as e:
            st.error(f"Error searching anime: {e}")
            return []

    def get_anime_details(self, anime_id: str) -> Optional[Dict]:
        try:
            url = f"https://api.jikan.moe/v4/anime/{anime_id}"
            response = self.session.get(url, timeout=10)
            return response.json().get("data")
        except Exception as e:
            st.error(f"Error getting anime details: {e}")
            return None
