"""Custom styling for Streamlit app."""


def get_custom_css() -> str:
    """Return custom CSS for the app."""
    return """
    <style>
    /* Main container */
    .main {
        padding: 1rem;
    }
    
    /* Quote card styling */
    .quote-card {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f2ff 100%);
        border-left: 4px solid #4A90E2;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }
    
    .quote-text {
        font-size: 1.25rem;
        font-style: italic;
        color: #2C3E50;
        margin-bottom: 0.75rem;
        line-height: 1.6;
    }
    
    .quote-attribution {
        font-size: 0.875rem;
        color: #7f8c8d;
        font-weight: 500;
    }
    
    /* Transformation card */
    .transformation-card {
        background: linear-gradient(135deg, #fff9e6 0%, #fffaed 100%);
        border-left: 4px solid #7ED321;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }
    
    .original-text {
        color: #7f8c8d;
        font-style: italic;
        margin-bottom: 0.5rem;
    }
    
    .transformed-text {
        color: #2C3E50;
        font-weight: 500;
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    
    .arrow {
        color: #7ED321;
        font-size: 1.5rem;
        margin: 0.5rem 0;
    }
    
    /* Emotion indicator */
    .emotion-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        background: #e8f4f8;
        border-radius: 20px;
        margin: 0.5rem 0;
        font-weight: 600;
    }
    
    .intensity-bar {
        height: 8px;
        background: #e0e0e0;
        border-radius: 4px;
        overflow: hidden;
        margin-top: 0.5rem;
    }
    
    .intensity-fill {
        height: 100%;
        background: linear-gradient(90deg, #7ED321 0%, #4A90E2 100%);
        transition: width 0.3s ease;
    }
    
    /* Crisis alert */
    .crisis-alert {
        background: #ffe6e6;
        border-left: 4px solid #E74C3C;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 8px;
    }
    
    /* Buttons */
    .stButton > button {
        border-radius: 20px;
        padding: 0.5rem 1.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Chat messages */
    .user-message {
        background: #e8f4f8;
        padding: 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        text-align: right;
    }
    
    .bot-message {
        background: #f5f5f5;
        padding: 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
    }
    
    /* Disclaimer */
    .disclaimer {
        background: #fff9e6;
        border: 1px solid #f39c12;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-size: 0.875rem;
        color: #856404;
    }
    
    /* Header */
    .app-header {
        text-align: center;
        padding: 2rem 0;
    }
    
    .app-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #4A90E2;
        margin-bottom: 0.5rem;
    }
    
    .app-tagline {
        font-size: 1.1rem;
        color: #7f8c8d;
    }
    </style>
    """


def get_intensity_color(intensity: float) -> str:
    """Get color for emotion intensity."""
    if intensity >= 0.7:
        return "#E74C3C"  # Red for high intensity
    elif intensity >= 0.4:
        return "#F39C12"  # Orange for medium
    else:
        return "#7ED321"  # Green for low
