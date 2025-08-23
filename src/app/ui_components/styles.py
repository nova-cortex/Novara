import streamlit as st


def load_css():
    st.markdown(
        """
    <style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

body {
    font-family: 'Inter', sans-serif;
    background: #0f0f0f;
    color: white;
}

.main-header {
    background: linear-gradient(45deg, #6366f1, #8b5cf6);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3);
}

.main-header h1 {
    color: white;
    margin: 0;
    font-size: 2.5rem;
    font-weight: 600;
}


.search-container {
    background: #1a1a1a;
    border-radius: 15px;
    margin-bottom: 2rem;
    border: 1px solid #333;
}


.movie-card {
    background: #1a1a1a;
    border-radius: 15px;
    margin: 1rem 0;
    border: 1px solid #333;
    transition: transform 0.3s ease;
}

.movie-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}


.detail-container {
    background: #1a1a1a;
    border-radius: 15px;
    margin: 2rem 0;
    border: 1px solid #333;
}


.ai-section {
    background: #2d1b69;
    border-radius: 15px;
    margin: 2rem 0;
    border: 1px solid #6366f1;
}


.watchlist-item {
    background: #1a1a1a;
    border-radius: 15px;
    border-left: 4px solid #10b981;
    border: 1px solid #333;
}


.rating-badge {
    background: #10b981;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-weight: 600;
    margin-right: 0.5rem;
    display: inline-block;
}


.genre-tag {
    background: #374151;
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.85rem;
    margin: 0.2rem;
    display: inline-block;
}


.action-button {
    background: linear-gradient(45deg, #6366f1, #8b5cf6);
    color: white;
    padding: 0.8rem 1.5rem;
    border: none;
    border-radius: 25px;
    text-decoration: none;
    display: inline-block;
    margin: 0.3rem;
    font-weight: 600;
    transition: transform 0.3s ease;
}

.action-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(99, 102, 241, 0.4);
}


.info-notice {
    background: #3b82f6;
    color: white;
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
    text-align: center;
    font-weight: 500;
}


.chat-message {
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
    border-left: 3px solid #6366f1;
}

.user-message {
    background: rgba(99, 102, 241, 0.1);
}

.ai-message {
    background: rgba(139, 92, 246, 0.1);
}


.ai-disclaimer {
    font-size: 0.8rem;
    color: #9ca3af;
    font-style: italic;
    margin-top: 1rem;
    padding: 0.5rem;
    background: rgba(156, 163, 175, 0.1);
    border-radius: 8px;
}


[data-testid="stSidebar"] {
    background: #1a1a1a !important;
}


::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #1a1a1a;
}

::-webkit-scrollbar-thumb {
    background: #6366f1;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #5856eb;
}

.loading {
    opacity: 0.7;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}
    </style>
    """,
        unsafe_allow_html=True,
    )
