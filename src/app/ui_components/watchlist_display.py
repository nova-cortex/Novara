import streamlit as st
from datetime import datetime
from app.utils.watchlist import (
    save_movie_info,
    save_anime_info,
    create_downloadable_txt,
)


def display_watchlist():
    if "watchlist" not in st.session_state or not st.session_state.watchlist:
        st.markdown(
            """
        <div class="search-container" style="text-align: center; padding: 3rem;">
            <h2>📚 Your Watchlist is Empty</h2>
            <p>Start adding some movies or anime to build your collection!</p>
            <p>🎬 Search for movies and anime, then click "Add to Watchlist"</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        return

    st.markdown(f"### 📚 Your Watchlist ({len(st.session_state.watchlist)} items)")

    col1, col2, col3 = st.columns(3)
    with col1:
        filter_type = st.selectbox("Filter by type:", ["All", "Movies", "Anime"])
    with col2:
        sort_by = st.selectbox(
            "Sort by:",
            ["Date Added (Newest)", "Date Added (Oldest)", "Title A-Z", "Title Z-A"],
        )
    with col3:
        if st.button("📥 Download Full Watchlist"):
            download_full_watchlist()

    filtered_watchlist = st.session_state.watchlist.copy()

    if filter_type == "Movies":
        filtered_watchlist = [
            item for item in filtered_watchlist if item["type"] == "movie"
        ]
    elif filter_type == "Anime":
        filtered_watchlist = [
            item for item in filtered_watchlist if item["type"] == "anime"
        ]

    if sort_by == "Date Added (Newest)":
        filtered_watchlist.sort(key=lambda x: x["added_date"], reverse=True)
    elif sort_by == "Date Added (Oldest)":
        filtered_watchlist.sort(key=lambda x: x["added_date"])
    elif sort_by == "Title A-Z":
        filtered_watchlist.sort(key=lambda x: x["title"].lower())
    elif sort_by == "Title Z-A":
        filtered_watchlist.sort(key=lambda x: x["title"].lower(), reverse=True)

    for i, item in enumerate(filtered_watchlist):
        st.markdown('<div class="watchlist-item">', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 3, 1])

        with col1:
            if (
                item["type"] == "movie"
                and item.get("poster")
                and item["poster"] != "N/A"
            ):
                st.image(item["poster"], width=100)
            elif item["type"] == "anime" and item.get("image"):
                st.image(item["image"], width=100)
            else:
                emoji = "🎬" if item["type"] == "movie" else "🎌"
                st.markdown(
                    f'<div style="width: 100px; height: 140px; background: linear-gradient(135deg, #374151 0%, #1f2937 100%); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 2rem;">{emoji}</div>',
                    unsafe_allow_html=True,
                )

        with col2:
            st.markdown(f"### {item['title']}")
            if item["type"] == "movie":
                st.markdown(f"**Year:** {item['year']}")
                st.markdown(f"**Type:** Movie")
                with st.expander("📖 Plot"):
                    st.write(item["plot"])
            else:
                st.markdown(f"**Episodes:** {item['episodes']}")
                st.markdown(f"**Type:** Anime")
                with st.expander("📖 Synopsis"):
                    st.write(item["synopsis"])

            st.markdown(f"**Added:** {item['added_date']}")

        with col3:
            st.markdown("### Actions")
            if st.button(
                "🗑️ Remove",
                key=f"remove_{i}_{item['title']}",
                help="Remove from watchlist",
            ):
                for j, orig_item in enumerate(st.session_state.watchlist):
                    if (
                        orig_item["title"] == item["title"]
                        and orig_item["added_date"] == item["added_date"]
                    ):
                        st.session_state.watchlist.pop(j)
                        st.success(f"Removed '{item['title']}' from watchlist")
                        st.rerun()
                        break

            if st.button(
                "📥 Save Info",
                key=f"save_{i}_{item['title']}",
                help="Download item info",
            ):
                if item["type"] == "movie":
                    movie_data = {
                        "Title": item["title"],
                        "Year": item["year"],
                        "Plot": item["plot"],
                        "Poster": item.get("poster", ""),
                        "imdbRating": item.get("imdbRating", "Unknown"),
                        "Director": item.get("Director", "Unknown"),
                        "Actors": item.get("Actors", "Unknown"),
                        "Genre": item.get("Genre", "Unknown"),
                        "Runtime": item.get("Runtime", "Unknown"),
                    }
                    save_movie_info(movie_data)
                else:
                    anime_data = {
                        "title": item["title"],
                        "episodes": item["episodes"],
                        "synopsis": item["synopsis"],
                        "status": item.get("status", "Unknown"),
                        "score": item.get("score", "N/A"),
                        "studios": item.get("studios", []),
                        "genres": item.get("genres", []),
                    }
                    save_anime_info(anime_data)

        st.markdown("</div>", unsafe_allow_html=True)


def download_full_watchlist():
    watchlist_content = f"""📚 MY COMPLETE WATCHLIST
{'='*60}
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Total Items: {len(st.session_state.watchlist)}

"""

    movies = [item for item in st.session_state.watchlist if item["type"] == "movie"]
    anime = [item for item in st.session_state.watchlist if item["type"] == "anime"]

    if movies:
        watchlist_content += f"\n🎬 MOVIES ({len(movies)} items)\n" + "-" * 40 + "\n"
        for i, item in enumerate(movies, 1):
            watchlist_content += f"\n{i}. {item['title']} ({item['year']})\n"
            watchlist_content += f"   Added: {item['added_date']}\n"
            watchlist_content += f"   Plot: {item['plot'][:200]}...\n"

    if anime:
        watchlist_content += f"\n\n🎌 ANIME ({len(anime)} items)\n" + "-" * 40 + "\n"
        for i, item in enumerate(anime, 1):
            watchlist_content += (
                f"\n{i}. {item['title']} ({item['episodes']} episodes)\n"
            )
            watchlist_content += f"   Added: {item['added_date']}\n"
            watchlist_content += f"   Synopsis: {item['synopsis'][:200]}...\n"

    watchlist_content += f"\n\n{'='*60}\nGenerated by Novara"

    st.markdown(
        create_downloadable_txt(watchlist_content, "complete_watchlist.txt"),
        unsafe_allow_html=True,
    )
