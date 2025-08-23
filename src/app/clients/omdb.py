import os
import requests
import streamlit as st
from typing import Dict, List, Optional


class OMDBClient:
    def __init__(self):
        self.omdb_key = os.getenv("OMDB_API_KEY")
        self.session = requests.Session()

    def search_movies(self, query: str) -> List[Dict]:
        try:
            url = f"http://www.omdbapi.com/?s={query}&type=movie&apikey={self.omdb_key}"
            response = self.session.get(url, timeout=10)
            data = response.json()

            if data.get("Response") == "True":
                return data.get("Search", [])
            return []
        except Exception as e:
            st.error(f"Error searching movies: {e}")
            return []

    def get_movie_details(self, imdb_id: str) -> Optional[Dict]:
        try:
            url = (
                f"http://www.omdbapi.com/?i={imdb_id}&plot=full&apikey={self.omdb_key}"
            )
            response = self.session.get(url, timeout=10)
            return response.json()
        except Exception as e:
            st.error(f"Error getting movie details: {e}")
            return None
