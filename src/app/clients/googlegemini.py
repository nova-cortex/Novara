import os
import streamlit as st
import google.generativeai as genai
from typing import List


class GeminiAI:
    def __init__(self):
        try:
            api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
            self.chat_session = None
        except Exception as e:
            st.error(f"Error initializing Gemini: {e}")
            self.model = None

    def initialize_chat(self, movie_context: str):
        if not self.model:
            return False

        try:
            context_prompt = f"""You are a knowledgeable movie expert discussing "{movie_context}". 
            Answer questions about this movie in a conversational, engaging way. 
            Keep responses concise but informative. You can discuss plot, themes, characters, 
            production details, and recommendations."""

            self.chat_session = self.model.start_chat(history=[])

            self.chat_session.send_message(context_prompt)
            return True
        except Exception as e:
            st.error(f"Error initializing chat: {e}")
            return False

    def chat_about_movie(self, message: str) -> str:
        if not self.model:
            return "AI service unavailable"

        try:
            if not self.chat_session:
                self.chat_session = self.model.start_chat(history=[])
            
            response = self.chat_session.send_message(message)
            return response.text
        except Exception as e:
            return f"Error in chat: {str(e)}"

    def generate_summary(self, plot: str) -> str:
        if not self.model:
            return "AI service unavailable"

        try:
            prompt = f"Summarize the following plot in exactly 2 sentences without spoilers. Convince me to watch this movie in the most human way possible.'{plot}'"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating summary: {e}"

    def generate_why_watch(self, title: str, plot: str, genre: str) -> str:
        if not self.model:
            return "AI service unavailable"

        try:
            prompt = f"Write one persuasive sentence to convince a 20-35 year old to watch '{title}' (Genre: {genre}). Plot: {plot}. Convince me to watch this movie in the most human way possible. "
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating recommendation: {e}"

    def generate_similar_recommendations(
        self, title: str, genre: str, mood: str = "general"
    ) -> List[str]:
        if not self.model:
            return ["AI service unavailable"]

        try:
            prompt = f"Recommend 5 similar movies/shows to '{title}' (Genre: {genre}) for mood '{mood}'. Give each with one-line reason. Format as numbered list."
            response = self.model.generate_content(prompt)
            return [str(item) for item in response.text.split("\n")]
        except Exception as e:
            return [f"Error generating recommendations: {e}"]