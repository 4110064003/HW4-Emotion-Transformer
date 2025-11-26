"""
Emotion Transformer + Movie Quote Therapist
Main Streamlit Application

A chatbot that helps transform negative thoughts into positive perspectives
and provides inspirational movie quotes to match your emotional state.
"""

import streamlit as st
import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from config.settings import settings

# Set API key in environment for AISuite - must be done before importing AISuite
api_key = settings.get_api_key("openai")
if api_key:
    os.environ['OPENAI_API_KEY'] = api_key
    print(f"✓ API key configured (length: {len(api_key)})")
else:
    print("✗ No API key found in environment or secrets")

from src.chatbot.engine import ChatbotEngine
from src.emotion.analyzer import EmotionAnalyzer
from src.emotion.transformer import SentenceTransformer
from src.quotes.database import QuoteDatabase
from src.quotes.matcher import QuoteMatcher
from src.music.database import SongDatabase
from src.music.matcher import SongMatcher
from src.image.generator import ComfortImageGenerator, MoviePosterFetcher
from src.ui import (
    display_header,
    display_disclaimer,
    display_emotion_analysis,
    display_transformation,
    display_movie_quote,
    display_song_card,
    display_favorites_sidebar,
    display_user_message,
    get_custom_css
)


# Page configuration
st.set_page_config(
    page_title="Emotion Transformer",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)


def initialize_session_state():
    """Initialize Streamlit session state variables."""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    
    if 'shown_quotes' not in st.session_state:
        st.session_state.shown_quotes = set()
    
    if 'shown_songs' not in st.session_state:
        st.session_state.shown_songs = set()
    
    if 'favorites' not in st.session_state:
        st.session_state.favorites = []
    
    if 'playlist' not in st.session_state:
        st.session_state.playlist = []
    
    if 'transformation_style' not in st.session_state:
        st.session_state.transformation_style = "gentle"
    
    if 'message_count' not in st.session_state:
        st.session_state.message_count = 0
    
    if 'initialized' not in st.session_state:
        st.session_state.initialized = False
    
    if 'show_images' not in st.session_state:
        st.session_state.show_images = True
    
    if 'show_posters' not in st.session_state:
        st.session_state.show_posters = True


def initialize_components():
    """Initialize core components (cached)."""
    # Validate API key
    is_valid, message = settings.validate_api_key()
    if not is_valid:
        st.error(message)
        st.stop()
    
    # Initialize components
    try:
        if 'chatbot' not in st.session_state:
            st.session_state.chatbot = ChatbotEngine()
        
        if 'analyzer' not in st.session_state:
            st.session_state.analyzer = EmotionAnalyzer(st.session_state.chatbot.client)
        
        if 'transformer' not in st.session_state:
            st.session_state.transformer = SentenceTransformer(
                st.session_state.chatbot.client,
                style=st.session_state.transformation_style
            )
        
        if 'quote_db' not in st.session_state:
            st.session_state.quote_db = QuoteDatabase("data/quotes.json")
        
        if 'quote_matcher' not in st.session_state:
            st.session_state.quote_matcher = QuoteMatcher(st.session_state.quote_db)
        
        # Initialize song database and matcher
        if 'song_db' not in st.session_state:
            st.session_state.song_db = SongDatabase("data/songs.json")
        
        if 'song_matcher' not in st.session_state:
            st.session_state.song_matcher = SongMatcher(st.session_state.song_db)
        
        # Initialize image generator (optional, will use fallback if DALL-E fails)
        if 'image_generator' not in st.session_state:
            st.session_state.image_generator = ComfortImageGenerator(st.session_state.chatbot.client)
        
        # Initialize poster fetcher with optional TMDB API key
        if 'poster_fetcher' not in st.session_state:
            tmdb_key = settings.get_api_key("tmdb") if hasattr(settings, 'get_api_key') else None
            st.session_state.poster_fetcher = MoviePosterFetcher(api_key=tmdb_key)
        
        st.session_state.initialized = True
        
    except Exception as e:
        st.error(f"❌ Error initializing app: {str(e)}")
        st.info("Please check your API key configuration and try again.")
        st.stop()


def sidebar_settings():
    """Display sidebar with settings and info."""
    st.sidebar.title("⚙️ Settings")
    
    # Transformation style selector
    style_display = st.sidebar.radio(
        "Transformation Style",
        options=list(settings.TRANSFORMATION_STYLES.keys()),
        index=0,
        help="Choose how the bot reframes your thoughts"
    )
    
    # Update style if changed
    new_style = settings.TRANSFORMATION_STYLES[style_display]
    if new_style != st.session_state.transformation_style:
        st.session_state.transformation_style = new_style
        if 'transformer' in st.session_state:
            st.session_state.transformer.set_style(new_style)
    
    st.sidebar.markdown("---")
    
    # Image settings
    st.sidebar.subheader("🎨 Visual Features")
    st.session_state.show_posters = st.sidebar.checkbox(
        "Show movie posters", 
        value=st.session_state.show_posters,
        help="Display movie posters with quotes"
    )
    
    st.sidebar.markdown("---")
    
    # Favorites section
    display_favorites_sidebar()
    
    st.sidebar.markdown("---")
    
    # Session stats
    st.sidebar.subheader("📊 Session Stats")
    st.sidebar.metric("Messages sent", st.session_state.message_count)
    st.sidebar.metric("Quotes viewed", len(st.session_state.shown_quotes))
    st.sidebar.metric("Songs played", len(st.session_state.shown_songs))
    st.sidebar.metric("Favorites saved", len(st.session_state.favorites) + len(st.session_state.playlist))
    
    # Clear conversation button
    if st.sidebar.button("🆕 Start New Conversation"):
        if st.sidebar.button("✅ Confirm Clear"):
            st.session_state.messages = []
            st.session_state.conversation_history = []
            st.session_state.message_count = 0
            st.session_state.shown_quotes = set()
            st.session_state.shown_songs = set()
            if 'chatbot' in st.session_state:
                st.session_state.chatbot.clear_context()
            st.rerun()
    
    st.sidebar.markdown("---")
    
    # About section
    with st.sidebar.expander("ℹ️ About"):
        st.markdown("""
        **Emotion Transformer** helps you:
        - 🔄 Reframe negative thoughts positively
        - 🎬 Find inspiring movie quotes
        - 😊 Improve emotional awareness
        
        Built with:
        - Python + AISuite + Streamlit
        - 50+ curated movie quotes
        - Multiple transformation styles
        
        **Not a replacement for professional mental health care.**
        """)


def process_user_input(user_input: str):
    """Process user input and generate response."""
    # Increment message count
    st.session_state.message_count += 1
    
    # Check rate limit
    if st.session_state.message_count > settings.MAX_MESSAGES_PER_SESSION:
        st.warning(f"⚠️ You've reached the message limit ({settings.MAX_MESSAGES_PER_SESSION}) for this session. Please start a new conversation.")
        return
    
    # Store user input in conversation history
    conversation_entry = {
        'user_input': user_input,
        'timestamp': st.session_state.message_count
    }
    
    # Show loading
    with st.spinner("Analyzing emotions..."):
        # Analyze emotion
        emotion_result = st.session_state.analyzer.analyze_emotion(user_input)
    
    # Store emotion result
    conversation_entry['emotion'] = emotion_result
    
    # If crisis, stop here
    if emotion_result.is_crisis:
        conversation_entry['is_crisis'] = True
        st.session_state.conversation_history.append(conversation_entry)
        return
    
    # Generate transformation
    with st.spinner("Reframing your thought..."):
        transformed = st.session_state.transformer.transform(
            user_input,
            emotion_result.primary_emotion
        )
    
    # Store transformation
    conversation_entry['transformed'] = transformed
    
    # Match quotes
    with st.spinner("Finding perfect quotes..."):
        quotes = st.session_state.quote_matcher.match_quotes(
            emotion_result.primary_emotion,
            count=2,
            exclude_ids=st.session_state.shown_quotes
        )
    
    # Store quotes
    conversation_entry['quotes'] = quotes
    for quote in quotes:
        st.session_state.shown_quotes.add(quote.id)
    
    # Match songs
    with st.spinner("Finding perfect K-pop songs..."):
        songs = st.session_state.song_matcher.match_songs(
            emotion_result.primary_emotion,
            count=2,
            exclude_ids=st.session_state.shown_songs
        )
    
    # Store songs
    conversation_entry['songs'] = songs
    for song in songs:
        st.session_state.shown_songs.add(song.id)
    
    # Add to conversation history
    st.session_state.conversation_history.append(conversation_entry)
    
    # Force rerun to display
    st.rerun()
    
    # Match quotes
    st.markdown("### 🎬 Inspirational Movie Quotes")
    with st.spinner("Finding perfect quotes..."):
        quotes = st.session_state.quote_matcher.match_quotes(
            emotion_result.primary_emotion,
            count=2,
            exclude_ids=st.session_state.shown_quotes
        )
    
    # Display quotes
    if quotes:
        for i, quote in enumerate(quotes):
            st.session_state.shown_quotes.add(quote.id)
            
            # Display quote
            wants_another = display_movie_quote(quote, key_suffix=f"{st.session_state.message_count}_{i}")
            
            # Handle "try another" click
            if wants_another:
                new_quote = st.session_state.quote_matcher.get_another_quote(
                    emotion_result.primary_emotion,
                    st.session_state.shown_quotes
                )
                if new_quote:
                    st.session_state.shown_quotes.add(new_quote.id)
                    display_movie_quote(new_quote, key_suffix=f"new_{st.session_state.message_count}_{i}")
    else:
        st.info("No matching quotes found for this emotion. Try expressing your feelings differently!")
    
    st.markdown("---")


def display_conversation_history():
    """Display the full conversation history."""
    if not st.session_state.conversation_history:
        return
    
    st.markdown("### 📜 Conversation History")
    
    for entry in st.session_state.conversation_history:
        # User message
        with st.container():
            display_user_message(entry['user_input'])
            
            # Check if crisis
            if entry.get('is_crisis'):
                st.markdown("### 🧠 Emotion Analysis")
                display_emotion_analysis(entry['emotion'])
                st.markdown("---")
                continue
            
            # Emotion analysis
            st.markdown("### 🧠 Emotion Analysis")
            display_emotion_analysis(entry['emotion'])
            
            # Transformation
            st.markdown("### ✨ Positive Reframing")
            display_transformation(
                entry['user_input'], 
                entry['transformed'], 
                key_suffix=f"history_{entry['timestamp']}"
            )
            
            # Quotes
            st.markdown("### 🎬 Inspirational Movie Quotes")
            if entry.get('quotes'):
                for i, quote in enumerate(entry['quotes']):
                    display_movie_quote(
                        quote, 
                        key_suffix=f"history_{entry['timestamp']}_{i}",
                        show_poster=st.session_state.show_posters
                    )
            
            # Songs
            st.markdown("### 🎵 K-pop Therapy")
            if entry.get('songs'):
                for i, song in enumerate(entry['songs']):
                    display_song_card(
                        song,
                        key_suffix=f"history_{entry['timestamp']}_{i}"
                    )
            
            st.markdown("---")


def main():
    """Main application function."""
    # Initialize
    initialize_session_state()
    
    # Display header
    display_header()
    display_disclaimer()
    
    # Initialize components
    if not st.session_state.initialized:
        with st.spinner("Initializing AI components..."):
            initialize_components()
    
    # Sidebar
    sidebar_settings()
    
    # Main content area
    st.markdown("### 💬 Share Your Thoughts")
    st.markdown("Tell me what's on your mind, and I'll help you see things from a different perspective.")
    
    # Display conversation history first
    display_conversation_history()
    
    # Chat input
    user_input = st.chat_input("Type your thoughts here...")
    
    if user_input:
        process_user_input(user_input)
    
    # Display welcome message if no history
    if st.session_state.message_count == 0:
        st.info("👋 Hi! I'm here to help you transform negative thoughts into positive perspectives. Share what's on your mind to get started!")


if __name__ == "__main__":
    main()
