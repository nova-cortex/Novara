import streamlit as st
from app.utils.watchlist import add_to_watchlist, save_anime_info


def display_anime_details(anime_id: str, api_client, ai_client):
    anime = api_client.get_anime_details(anime_id)
    if not anime:
        st.error("Could not load anime details")
        return

    st.markdown("---")
    st.markdown(
        '<div class="info-notice">🔍 Detailed Anime Information</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="detail-container">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        if anime.get("images", {}).get("jpg", {}).get("large_image_url"):
            st.image(anime["images"]["jpg"]["large_image_url"], width=300)

    with col2:
        st.markdown(f"# {anime.get('title', 'Unknown')}")
        st.markdown(f"**Episodes:** {anime.get('episodes', 'Unknown')}")
        st.markdown(f"**Status:** {anime.get('status', 'Unknown')}")
        st.markdown(f"**Score:** {anime.get('score', 'N/A')}/10")
        st.markdown(
            f"**Studio:** {', '.join([studio['name'] for studio in anime.get('studios', [])])}"
        )

        if anime.get("genres"):
            genre_html = "".join(
                [
                    f'<span class="genre-tag">{genre["name"]}</span>'
                    for genre in anime["genres"]
                ]
            )
            st.markdown(genre_html, unsafe_allow_html=True)

    if anime.get("synopsis"):
        with st.expander("📖 Synopsis", expanded=True):
            st.write(anime["synopsis"])

    st.markdown("### 🎌 Quick Actions")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(
            "🎌 Add to Watchlist",
            key=f"anime_add_watchlist_{anime_id}",
            help="Save to your personal watchlist",
        ):
            add_to_watchlist(anime, "anime")

    with col2:
        if st.button(
            "📤 Save Anime Info",
            key=f"anime_save_info_{anime_id}",
            help="Download anime information",
        ):
            save_anime_info(anime)

    with col3:
        if st.button(
            "🤖 AI Features",
            key=f"anime_ai_features_{anime_id}",
            help="Explore AI-powered insights",
        ):
            st.session_state.show_ai_features = True
            st.rerun()

    if st.session_state.get("show_ai_features", False):
        st.markdown('<div class="ai-section">', unsafe_allow_html=True)
        st.markdown("### 🤖 AI-Powered Features")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["🔍 Summary", "💡 Why Watch", "🎯 Similar Anime", "💬 Chat"]
        )

        with tab1:
            if st.button("🔍 Generate AI Summary", key=f"anime_summary_btn_{anime_id}"):
                if anime.get("synopsis"):
                    with st.spinner("Generating summary..."):
                        summary = ai_client.generate_summary(anime["synopsis"])
                        st.markdown(f"**AI Summary:**")
                        st.write(summary)
                        st.markdown(
                            '<p class="ai-disclaimer">🤖 AI-generated • May be imperfect</p>',
                            unsafe_allow_html=True,
                        )

        with tab2:
            if st.button(
                "💡 Generate Recommendation", key=f"anime_why_watch_btn_{anime_id}"
            ):
                if anime.get("synopsis"):
                    with st.spinner("Generating recommendation..."):
                        genre_names = ", ".join(
                            [genre["name"] for genre in anime.get("genres", [])]
                        )
                        why_watch = ai_client.generate_why_watch(
                            anime.get("title", ""),
                            anime.get("synopsis", ""),
                            genre_names,
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
                    "action",
                    "romance",
                    "comedy",
                    "drama",
                    "thriller",
                    "slice of life",
                    "fantasy",
                ],
                key=f"anime_mood_select_{anime_id}",
            )
            if st.button("🎯 Find Similar Anime", key=f"anime_similar_btn_{anime_id}"):
                with st.spinner("Finding similar anime..."):
                    genre_names = ", ".join(
                        [genre["name"] for genre in anime.get("genres", [])]
                    )
                    recommendations = ai_client.generate_similar_recommendations(
                        anime.get("title", ""), genre_names, mood
                    )
                    st.markdown(f"**Similar Anime for {mood} mood:**")
                    for rec in recommendations:
                        if rec.strip():
                            st.write(rec)
                    st.markdown(
                        '<p class="ai-disclaimer">🤖 AI-generated • May be imperfect</p>',
                        unsafe_allow_html=True,
                    )

        with tab4:
            st.markdown("### 💬 Chat about this Anime")

            if f"chat_initialized_{anime_id}" not in st.session_state:
                anime_context = f"{anime.get('title', 'Unknown')}: {anime.get('synopsis', 'No synopsis available')}"
                if ai_client.initialize_chat(anime_context):
                    st.session_state[f"chat_initialized_{anime_id}"] = True
                    st.session_state[f"chat_history_{anime_id}"] = []
                else:
                    st.error("Failed to initialize chat")

            if f"chat_initialized_{anime_id}" in st.session_state:
                if f"chat_history_{anime_id}" in st.session_state:
                    for chat in st.session_state[f"chat_history_{anime_id}"]:
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
                    "Ask anything about this anime:",
                    placeholder="e.g., What's the main theme? Who are the main characters?",
                    key=f"anime_chat_input_{anime_id}",
                )

                col1, col2 = st.columns([1, 4])
                with col1:
                    if st.button("💬 Send", key=f"anime_chat_send_{anime_id}"):
                        if user_question.strip():
                            st.session_state[f"chat_history_{anime_id}"].append(
                                {"role": "user", "message": user_question}
                            )

                            with st.spinner("AI is thinking..."):
                                ai_response = ai_client.chat_about_movie(user_question)
                                st.session_state[f"chat_history_{anime_id}"].append(
                                    {"role": "ai", "message": ai_response}
                                )

                            st.rerun()

                with col2:
                    if st.button("🗑️ Clear Chat", key=f"anime_chat_clear_{anime_id}"):
                        st.session_state[f"chat_history_{anime_id}"] = []
                        st.rerun()

                st.markdown(
                    '<p class="ai-disclaimer">💬 Chat powered by Google Gemini • Responses may be imperfect</p>',
                    unsafe_allow_html=True,
                )

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
