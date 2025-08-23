import streamlit as st
from app.utils.watchlist import add_to_watchlist, save_movie_info


def display_movie_details(movie_id: str, api_client, ai_client):
    movie = api_client.get_movie_details(movie_id)
    if not movie:
        st.error("Could not load movie details")
        return

    st.markdown("---")
    st.markdown(
        '<div class="info-notice">🔍 Detailed Movie Information</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="detail-container">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        if movie.get("Poster") and movie["Poster"] != "N/A":
            st.image(movie["Poster"], width=300)

    with col2:
        st.markdown(f"# {movie.get('Title', 'Unknown')}")
        st.markdown(f"**Year:** {movie.get('Year', 'Unknown')}")
        st.markdown(f"**Runtime:** {movie.get('Runtime', 'Unknown')}")
        st.markdown(f"**Director:** {movie.get('Director', 'Unknown')}")

        if movie.get("imdbRating"):
            st.markdown(
                f'<span class="rating-badge">IMDb: {movie["imdbRating"]}</span>',
                unsafe_allow_html=True,
            )

        if movie.get("Genre"):
            genres = movie["Genre"].split(", ")
            genre_html = "".join(
                [f'<span class="genre-tag">{genre}</span>' for genre in genres]
            )
            st.markdown(genre_html, unsafe_allow_html=True)

        st.markdown(f"**Cast:** {movie.get('Actors', 'Unknown')}")

    if movie.get("Plot"):
        with st.expander("📖 Plot Synopsis", expanded=True):
            st.write(movie["Plot"])

    st.markdown("### 🎬 Quick Actions")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🎬 Add to Watchlist", help="Save to your personal watchlist"):
            add_to_watchlist(movie, "movie")

    with col2:
        if st.button("📤 Save Movie Info", help="Download movie information"):
            save_movie_info(movie)

    with col3:
        if st.button("🤖 AI Features", help="Explore AI-powered insights"):
            st.session_state.show_ai_features = True
            st.rerun()

    if st.session_state.get("show_ai_features", False):
        st.markdown('<div class="ai-section">', unsafe_allow_html=True)
        st.markdown("### 🤖 AI-Powered Features")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["🔍 Summary", "💡 Why Watch", "🎯 Similar Movies", "💬 Chat"]
        )

        with tab1:
            if st.button("🔍 Generate AI Summary", key="summary_btn"):
                if movie.get("Plot"):
                    with st.spinner("Generating summary..."):
                        summary = ai_client.generate_summary(movie["Plot"])
                        st.markdown(f"**AI Summary:**")
                        st.write(summary)
                        st.markdown(
                            '<p class="ai-disclaimer">🤖 AI-generated • May be imperfect</p>',
                            unsafe_allow_html=True,
                        )

        with tab2:
            if st.button("💡 Generate Recommendation", key="why_watch_btn"):
                if movie.get("Plot"):
                    with st.spinner("Generating recommendation..."):
                        why_watch = ai_client.generate_why_watch(
                            movie.get("Title", ""),
                            movie.get("Plot", ""),
                            movie.get("Genre", ""),
                        )
                        st.markdown(f"**Why You Should Watch:**")
                        st.write(why_watch)
                        st.markdown(
                            '<p class="ai-disclaimer">🤖 AI-generated • May be imperfect</p>',
                            unsafe_allow_html=True,
                        )

        with tab3:
            mood = st.selectbox(
                "Select Mood:",
                [
                    "general",
                    "date night",
                    "family",
                    "action",
                    "horror",
                    "comedy",
                    "thriller",
                    "drama",
                ],
            )
            if st.button("🎯 Find Similar Movies", key="similar_btn"):
                with st.spinner("Finding similar movies..."):
                    recommendations = ai_client.generate_similar_recommendations(
                        movie.get("Title", ""), movie.get("Genre", ""), mood
                    )
                    st.markdown(f"**Similar Movies for {mood} mood:**")
                    for rec in recommendations:
                        if rec.strip():
                            st.write(rec)
                    st.markdown(
                        '<p class="ai-disclaimer">🤖 AI-generated • May be imperfect</p>',
                        unsafe_allow_html=True,
                    )

        with tab4:
            st.markdown("### 💬 Chat about this Movie")

            if f"chat_initialized_{movie_id}" not in st.session_state:
                movie_context = f"{movie.get('Title', 'Unknown')} ({movie.get('Year', 'Unknown')}): {movie.get('Plot', 'No plot available')}"
                if ai_client.initialize_chat(movie_context):
                    st.session_state[f"chat_initialized_{movie_id}"] = True
                    st.session_state[f"chat_history_{movie_id}"] = []
                else:
                    st.error("Failed to initialize chat")

            if f"chat_initialized_{movie_id}" in st.session_state:
                if f"chat_history_{movie_id}" in st.session_state:
                    for chat in st.session_state[f"chat_history_{movie_id}"]:
                        if chat["role"] == "user":
                            st.markdown(
                                f'<div class="chat-message user-message"><strong>You:</strong> {chat["message"]}</div>',
                                unsafe_allow_html=True,
                            )
                        else:
                            st.markdown(
                                f'<div class="chat-message ai-message"><strong>AI:</strong> {chat["message"]}</div>',
                                unsafe_allow_html=True,
                            )

                user_question = st.text_input(
                    "Ask anything about this movie:",
                    placeholder="e.g., What's the main theme? Who are the main characters?",
                    key=f"chat_input_{movie_id}",
                )

                col1, col2 = st.columns([1, 4])
                with col1:
                    if st.button("💬 Send", key=f"chat_send_{movie_id}"):
                        if user_question.strip():
                            st.session_state[f"chat_history_{movie_id}"].append(
                                {"role": "user", "message": user_question}
                            )

                            with st.spinner("AI is thinking..."):
                                ai_response = ai_client.chat_about_movie(user_question)
                                st.session_state[f"chat_history_{movie_id}"].append(
                                    {"role": "ai", "message": ai_response}
                                )

                            st.rerun()

                with col2:
                    if st.button("🗑️ Clear Chat", key=f"chat_clear_{movie_id}"):
                        st.session_state[f"chat_history_{movie_id}"] = []
                        st.rerun()

                st.markdown(
                    '<p class="ai-disclaimer">💬 Chat powered by Google Gemini • Responses may be imperfect</p>',
                    unsafe_allow_html=True,
                )

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
