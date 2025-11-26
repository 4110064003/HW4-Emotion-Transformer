"""Configuration settings for the Emotion Transformer chatbot."""
import os
from typing import Optional
import streamlit as st


class Settings:
    """Application configuration settings."""
    
    # LLM Configuration
    LLM_PROVIDER: str = "openai"
    MODEL_NAME: str = "gpt-4o-mini"
    TEMPERATURE: float = 0.7
    MAX_TOKENS: int = 500
    TIMEOUT_SECONDS: int = 10
    
    # Rate Limiting
    MAX_MESSAGES_PER_SESSION: int = 50
    
    # UI Configuration
    APP_TITLE: str = "✨ Emotion Transformer"
    APP_TAGLINE: str = "Turn negative thoughts into positive perspectives with AI and movie wisdom 🎬"
    
    # Crisis Resources
    CRISIS_HOTLINE: str = "988"
    CRISIS_MESSAGE: str = """
    🆘 **If you're in crisis, please reach out for professional help:**
    
    - **988 Suicide & Crisis Lifeline**: Call or text 988
    - **Crisis Text Line**: Text HOME to 741741
    - **International Association for Suicide Prevention**: https://www.iasp.info/resources/Crisis_Centres/
    
    You don't have to go through this alone. Professional help is available 24/7.
    """
    
    # Transformation Styles
    TRANSFORMATION_STYLES = {
        "Gentle 🤗": "gentle",
        "Humorous 😄": "humorous",
        "Direct 🎯": "direct",
        "CBT 🧠": "cbt"
    }
    
    # Emotion Categories
    EMOTIONS = [
        "sadness", "anxiety", "anger", "loneliness", 
        "disappointment", "fear", "frustration", "joy", "neutral"
    ]
    
    EMOTION_EMOJIS = {
        "sadness": "😢",
        "anxiety": "😰",
        "anger": "😠",
        "loneliness": "😔",
        "disappointment": "😞",
        "fear": "😨",
        "frustration": "😤",
        "joy": "😊",
        "neutral": "😐"
    }
    
    @staticmethod
    def get_api_key(provider: str = "openai") -> Optional[str]:
        """Get API key from environment or Streamlit secrets."""
        key_name = f"{provider.upper()}_API_KEY"
        
        # Try Streamlit secrets first (for deployed app)
        if hasattr(st, 'secrets') and key_name in st.secrets:
            return st.secrets[key_name]
        
        # Fall back to environment variable (for local dev)
        return os.getenv(key_name)
    
    @staticmethod
    def validate_api_key() -> tuple[bool, str]:
        """Validate that at least one API key is configured."""
        openai_key = Settings.get_api_key("openai")
        
        if openai_key:
            return True, "OpenAI API key found"
        
        return False, """
        ⚠️ **API Key Not Found**
        
        Please set up your OpenAI API key:
        
        **For local development:**
        1. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`
        2. Add your OpenAI API key
        
        **For Streamlit Cloud:**
        1. Go to your app settings
        2. Add `OPENAI_API_KEY` in the Secrets section
        
        Get your API key from: https://platform.openai.com/api-keys
        """


# Export singleton instance
settings = Settings()
