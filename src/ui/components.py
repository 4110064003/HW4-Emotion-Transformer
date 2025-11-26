"""UI components for Streamlit app."""
import streamlit as st
from src.emotion.analyzer import EmotionResult
from src.quotes.database import Quote
from config.settings import settings


def display_header():
    """Display app header with title and tagline."""
    st.markdown("""
        <div class="app-header">
            <div class="app-title">✨ Emotion Transformer</div>
            <div class="app-tagline">Turn negative thoughts into positive perspectives with AI and movie wisdom 🎬</div>
        </div>
    """, unsafe_allow_html=True)


def display_disclaimer():
    """Display disclaimer about professional help."""
    st.markdown("""
        <div class="disclaimer">
            💡 <strong>Note:</strong> This is an AI-powered support tool, not a replacement for professional mental health care. 
            If you're experiencing a crisis or need professional support, please reach out to a licensed therapist or crisis hotline.
        </div>
    """, unsafe_allow_html=True)


def display_emotion_analysis(emotion_result: EmotionResult):
    """Display emotion analysis result."""
    if emotion_result.is_crisis:
        display_crisis_alert()
        return
    
    emotion = emotion_result.primary_emotion
    intensity = emotion_result.intensity
    emoji = settings.EMOTION_EMOJIS.get(emotion, "😐")
    
    st.markdown(f"""
        <div class="emotion-badge">
            {emoji} <strong>{emotion.capitalize()}</strong> 
            (Intensity: {intensity:.1f})
        </div>
    """, unsafe_allow_html=True)
    
    # Intensity bar
    from .styles import get_intensity_color
    color = get_intensity_color(intensity)
    st.markdown(f"""
        <div class="intensity-bar">
            <div class="intensity-fill" style="width: {intensity*100}%; background: {color};"></div>
        </div>
    """, unsafe_allow_html=True)
    
    if emotion_result.secondary_emotions:
        st.caption(f"Also detected: {', '.join(emotion_result.secondary_emotions)}")


def display_crisis_alert():
    """Display crisis resources."""
    st.markdown(f"""
        <div class="crisis-alert">
            {settings.CRISIS_MESSAGE}
        </div>
    """, unsafe_allow_html=True)


def display_transformation(original: str, transformed: str, key_suffix: str = ""):
    """Display original and transformed sentences."""
    st.markdown(f"""
        <div class="transformation-card">
            <div class="original-text">💭 Your thought: "{original}"</div>
            <div class="arrow">↓</div>
            <div class="transformed-text">✨ Positive perspective: {transformed}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Reframe button
    if st.button("🔄 Reframe differently", key=f"reframe_{key_suffix}"):
        return True
    return False


def display_movie_quote(quote: Quote, key_suffix: str = "", show_poster: bool = True):
    """Display movie quote card with optional poster."""
    # Create columns for poster and quote
    if show_poster:
        col_poster, col_quote = st.columns([1, 2])
        
        with col_poster:
            # Get movie poster
            poster_fetcher = getattr(st.session_state, 'poster_fetcher', None)
            if poster_fetcher:
                poster_url = poster_fetcher.search_movie_poster(quote.movie, quote.year)
                try:
                    st.image(poster_url, use_container_width=True, caption=f"🎬 {quote.movie}")
                    # Add link to search for movie
                    movie_search = quote.movie.replace(" ", "+")
                    st.markdown(f"[🔍 Search for this movie](https://www.google.com/search?q={movie_search}+{quote.year}+movie)", unsafe_allow_html=True)
                except Exception as e:
                    print(f"Error displaying poster: {e}")
        
        with col_quote:
            st.markdown(f"""
                <div class="quote-card">
                    <div class="quote-text">"{quote.text}"</div>
                    <div class="quote-attribution">
                        — {quote.character}, <em>{quote.movie}</em> ({quote.year})
                    </div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="quote-card">
                <div class="quote-text">"{quote.text}"</div>
                <div class="quote-attribution">
                    — {quote.character}, <em>{quote.movie}</em> ({quote.year})
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("❤️ Save to favorites", key=f"fav_{quote.id}_{key_suffix}"):
            if 'favorites' not in st.session_state:
                st.session_state.favorites = []
            if quote.id not in [q.id for q in st.session_state.favorites]:
                st.session_state.favorites.append(quote)
                st.success("Added to favorites!")
    
    with col2:
        if st.button("🎬 Try another quote", key=f"another_{quote.id}_{key_suffix}"):
            return True
    
    return False


def display_loading(message: str = "Thinking..."):
    """Display loading indicator."""
    with st.spinner(message):
        return True


def display_favorites_sidebar():
    """Display favorites in sidebar."""
    if 'favorites' not in st.session_state or not st.session_state.favorites:
        st.sidebar.info("No favorite quotes yet. Click the ❤️ button to save quotes!")
    else:
        st.sidebar.subheader("❤️ Your Favorite Quotes")
        
        for quote in st.session_state.favorites:
            st.sidebar.markdown(f"""
                <div style="background: #f0f8ff; padding: 0.75rem; margin: 0.5rem 0; border-radius: 6px; font-size: 0.875rem;">
                    <em>"{quote.text}"</em><br>
                    <small>— {quote.movie} ({quote.year})</small>
                </div>
            """, unsafe_allow_html=True)
        
        # Export button
        if st.sidebar.button("📥 Export Favorites"):
            export_favorites()
    
    # My Playlist section
    st.sidebar.markdown("---")
    if 'playlist' not in st.session_state or not st.session_state.playlist:
        st.sidebar.info("No songs in playlist yet. Click the ❤️ button to add K-pop songs!")
    else:
        st.sidebar.subheader("🎵 My Playlist")
        
        for song in st.session_state.playlist:
            st.sidebar.markdown(f"""
                <div style="background: linear-gradient(135deg, rgba(102,126,234,0.1) 0%, rgba(118,75,162,0.1) 100%); 
                     padding: 0.75rem; margin: 0.5rem 0; border-radius: 6px; font-size: 0.875rem;
                     border-left: 3px solid #667eea;">
                    <strong>{song.title}</strong><br>
                    <small>🎤 {song.artist}</small>
                </div>
            """, unsafe_allow_html=True)
        
        # Export playlist button
        if st.sidebar.button("📥 Export Playlist"):
            export_playlist()


def export_favorites():
    """Export favorites as text file."""
    if 'favorites' not in st.session_state or not st.session_state.favorites:
        return
    
    text = "My Favorite Motivational Quotes\n"
    text += "=" * 50 + "\n\n"
    
    for i, quote in enumerate(st.session_state.favorites, 1):
        text += f"{i}. \"{quote.text}\"\n"
        text += f"   — {quote.character}, {quote.movie} ({quote.year})\n\n"
    
    st.sidebar.download_button(
        label="💾 Download as TXT",
        data=text,
        file_name="my_favorite_quotes.txt",
        mime="text/plain"
    )


def export_playlist():
    """Export playlist as text file."""
    if 'playlist' not in st.session_state or not st.session_state.playlist:
        return
    
    text = "My K-pop Therapy Playlist 🎵\n"
    text += "=" * 50 + "\n\n"
    
    for i, song in enumerate(st.session_state.playlist, 1):
        text += f"{i}. {song.title} - {song.artist}\n"
        text += f"   Genre: {song.genre} ({song.year})\n"
        text += f"   Spotify: {song.spotify_url}\n"
        text += f"   YouTube: {song.youtube_url}\n\n"
    
    st.sidebar.download_button(
        label="💾 Download as TXT",
        data=text,
        file_name="my_kpop_playlist.txt",
        mime="text/plain"
    )


def display_user_message(message: str):
    """Display user message."""
    st.markdown(f"""
        <div class="user-message">
            {message}
        </div>
    """, unsafe_allow_html=True)


def display_song_card(song, key_suffix: str = ""):
    """Display K-pop song recommendation card."""
    st.markdown("### 🎵 K-pop Recommendation")
    
    # Song info
    st.markdown(f"""
        <div class="quote-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
            <div style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem;">
                🎤 {song.title}
            </div>
            <div style="font-size: 1.1rem; margin-bottom: 1rem; opacity: 0.9;">
                by {song.artist}
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 0.75rem; border-radius: 8px; margin: 1rem 0;">
                <strong>🎯 Why this helps:</strong><br>
                {song.why_it_helps}
            </div>
            <div style="font-size: 0.875rem; opacity: 0.8;">
                {song.genre} • {song.year}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # YouTube link - using direct markdown link
    st.markdown(f"""
        <div style="margin: 1rem 0; text-align: center;">
            <a href="{song.youtube_url}" target="_blank" rel="noopener noreferrer" 
               style="display: inline-block; background: #FF0000; color: white; 
                      padding: 1rem 2rem; border-radius: 8px; text-decoration: none;
                      font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                📺 Watch on YouTube
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    # Display URL for debugging
    st.caption(f"🔗 {song.youtube_url}")
    
    # Action buttons
    col3, col4 = st.columns([1, 1])
    
    with col3:
        if st.button("❤️ Add to playlist", key=f"playlist_{song.id}_{key_suffix}"):
            if 'playlist' not in st.session_state:
                st.session_state.playlist = []
            if song.id not in [s.id for s in st.session_state.playlist]:
                st.session_state.playlist.append(song)
                st.success("Added to your playlist!")
    
    with col4:
        if st.button("🎵 Try another song", key=f"another_song_{song.id}_{key_suffix}"):
            return True
    
    return False


def display_comfort_image(emotion: str, key_suffix: str = ""):
    """Display AI-generated comfort image based on emotion."""
    st.markdown("### 🎨 Comfort Image for You")
    
    # Check if we have image generator
    image_gen = getattr(st.session_state, 'image_generator', None)
    
    if image_gen:
        try:
            # Get image URL
            image_url = image_gen.generate_comfort_image(emotion)
            if image_url:
                st.image(image_url, use_container_width=True, caption=f"A peaceful scene to comfort your {emotion}")
            else:
                st.info("💡 Image temporarily unavailable")
        except Exception as e:
            print(f"Error displaying comfort image: {e}")
            st.info("💡 Image temporarily unavailable")
    else:
        # Simple fallback without generator
        st.info("💡 Enable image generation to see personalized comfort images!")

