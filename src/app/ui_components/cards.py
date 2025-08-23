import streamlit as st
from typing import Dict


def display_movie_card(movie: Dict):
    with st.container():
        st.markdown('<div class="movie-card">', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 3])

        with col1:
            if movie.get("Poster") and movie["Poster"] != "N/A":
                st.image(movie["Poster"], width=180)
            else:
                st.markdown(
                    '<div style="width: 180px; height: 250px; background: linear-gradient(135deg, #374151 0%, #1f2937 100%); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #9ca3af;">🎬 No Poster</div>',
                    unsafe_allow_html=True,
                )

        with col2:
            st.markdown(f"### {movie.get('Title', 'Unknown')}")
            st.markdown(f"**Year:** {movie.get('Year', 'Unknown')}")
            st.markdown(f"**Type:** {movie.get('Type', 'Unknown').title()}")

            if st.button(
                f"🎬 View Details",
                key=f"movie_{movie.get('imdbID')}",
                help="Click to see full movie details below",
            ):
                st.session_state.selected_movie = movie.get("imdbID")
                st.session_state.content_type = "movie"
                st.info(
                    "🔍 **Movie details are displayed below. Scroll down to view the complete information.**"
                )
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)


def display_anime_card(anime: Dict):
    with st.container():
        st.markdown('<div class="movie-card">', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 3])

        with col1:
            if anime.get("images", {}).get("jpg", {}).get("image_url"):
                st.image(anime["images"]["jpg"]["image_url"], width=180)
            else:
                st.markdown(
                    '<div style="width: 180px; height: 250px; background: linear-gradient(135deg, #374151 0%, #1f2937 100%); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #9ca3af;">🎌 No Image</div>',
                    unsafe_allow_html=True,
                )

        with col2:
            st.markdown(f"### {anime.get('title', 'Unknown')}")
            st.markdown(f"**Episodes:** {anime.get('episodes', 'Unknown')}")
            st.markdown(f"**Score:** {anime.get('score', 'N/A')}/10")
            st.markdown(f"**Status:** {anime.get('status', 'Unknown')}")

            if st.button(
                f"🎌 View Details",
                key=f"anime_{anime.get('mal_id')}",
                help="Click to see full anime details below",
            ):
                st.session_state.selected_anime = anime.get("mal_id")
                st.session_state.content_type = "anime"
                st.info(
                    "🔍 **Anime details are displayed below. Scroll down to view the complete information.**"
                )
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)
