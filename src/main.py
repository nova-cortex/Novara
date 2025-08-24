"""
Project: novara
Author: ukr
License: MIT
Repository: https://github.com/nova-cortex/novara
"""

import streamlit as st
from app.utils.api_keys import load_env_variables, check_api_keys
from app.ui_components.styles import load_css
from app.ui_components.cards import display_movie_card, display_anime_card
from app.ui_components.movie_details import display_movie_details
from app.ui_components.anime_details import display_anime_details
from app.clients.omdb import OMDBClient
from app.clients.jikan import JikanClient
from app.clients.googlegemini import GeminiAI
from app.ui_components.watchlist_display import display_watchlist

load_env_variables()

st.set_page_config(
    page_title="Novara", page_icon="🎬", layout="wide", initial_sidebar_state="expanded"
)


def main():
    load_css()

    st.markdown(
        """
    <div class="main-header">
        <h1>🎬 Novara</h1>
    </div>
    """,
        unsafe_allow_html=True,
    )

    if not check_api_keys():
        return

    try:
        omdb_client = OMDBClient()
        jikan_client = JikanClient()
        gemini_ai = GeminiAI()
    except Exception as e:
        st.error(f"Error initializing services: {e}")
        return

    with st.sidebar:
        st.markdown("### 🎯 Navigation")
        page = st.selectbox("Choose Section:", ["🔍 Search", "📚 Watchlist"])

        if page == "🔍 Search":
            st.markdown("### Search Options")
            content_type = st.radio("Content Type:", ["🎬 Movies", "🎌 Anime"])

            if content_type == "🎬 Movies":
                st.session_state.search_type = "movies"
            else:
                st.session_state.search_type = "anime"

        if "watchlist" not in st.session_state:
            st.session_state.watchlist = []

        if "watchlist" in st.session_state:
            st.markdown("### 📊 Your Stats")
            total_items = len(st.session_state.watchlist)
            movies_count = len(
                [item for item in st.session_state.watchlist if item["type"] == "movie"]
            )
            anime_count = len(
                [item for item in st.session_state.watchlist if item["type"] == "anime"]
            )

            st.markdown(f"**Total Items:** {total_items}")
            st.markdown(f"**Movies:** {movies_count}")
            st.markdown(f"**Anime:** {anime_count}")

    if page == "🔍 Search":
        st.markdown('<div class="search-container">', unsafe_allow_html=True)

        search_query = st.text_input(
            "🔍 Search for movies or anime...",
            placeholder="e.g., Inception, Naruto, The Matrix, Attack on Titan",
            help="Enter the title of a movie or anime you want to search for",
        )

        col1, col2 = st.columns([1, 1])
        with col1:
            search_button = st.button(
                "🔎 Search", type="primary", help="Click to search"
            )
        with col2:
            if st.button("🔄 Clear Results", help="Clear current search results"):
                for key in [
                    "search_results",
                    "selected_movie",
                    "selected_anime",
                    "show_ai_features",
                ]:
                    if key in st.session_state:
                        del st.session_state[key]
                st.success("🗑️ Search results cleared!")

        st.markdown("</div>", unsafe_allow_html=True)

        if search_button and search_query:
            with st.spinner("🔍 Searching..."):
                if st.session_state.get("search_type") == "movies":
                    results = omdb_client.search_movies(search_query)
                    st.session_state.search_results = results
                    st.session_state.result_type = "movies"
                else:
                    results = jikan_client.search_anime(search_query)
                    st.session_state.search_results = results
                    st.session_state.result_type = "anime"

                if results:
                    st.success(f"✅ Found {len(results)} results!")
                else:
                    st.warning(
                        "😞 No results found. Try different keywords or check spelling."
                    )

        if st.session_state.get("search_results"):
            st.markdown(
                f"### 📋 Search Results ({len(st.session_state.search_results)} found)"
            )

            result_emoji = (
                "🎬" if st.session_state.get("result_type") == "movies" else "🎌"
            )
            result_type_name = (
                "Movies" if st.session_state.get("result_type") == "movies" else "Anime"
            )
            st.markdown(f"**{result_emoji} Showing {result_type_name}**")

            if st.session_state.get("result_type") == "movies":
                for movie in st.session_state.search_results:
                    display_movie_card(movie)
            else:
                for anime in st.session_state.search_results:
                    display_anime_card(anime)

        if st.session_state.get("selected_movie"):
            display_movie_details(
                st.session_state.selected_movie, omdb_client, gemini_ai
            )

        if st.session_state.get("selected_anime"):
            display_anime_details(
                st.session_state.selected_anime, jikan_client, gemini_ai
            )

    elif page == "📚 Watchlist":
        display_watchlist()

    st.markdown(
        """
    <div style="margin-top: 3rem; text-align: center; border-top: 1px solid rgba(255,255,255,0.1);">
        <p style="color: #9ca3af; font-size: 0.9rem;">
            🎬 Powered by OMDB, Jikan & Google Gemini APIs<br>
            Made with ❤️ using Streamlit • Your entertainment companion
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    if "watchlist" not in st.session_state:
        st.session_state.watchlist = []

    if "search_type" not in st.session_state:
        st.session_state.search_type = "movies"

    main()
