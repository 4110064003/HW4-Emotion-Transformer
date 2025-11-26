# Technical Design Document

## Architecture Overview

This document outlines the technical architecture for the Emotion Transformer + Movie Quote Therapist chatbot, built with Python, AISuite, and Streamlit.

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     Streamlit Web UI                        │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐    │
│  │  Chat Input │  │   Sidebar    │  │  Message Display │    │
│  │    Area     │  │   Settings   │  │      Area        │    │
│  └─────────────┘  └──────────────┘  └──────────────────┘    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer (app.py)               │
│  - Session state management                                 │
│  - User input handling                                      │
│  - Component orchestration                                  │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  Chatbot    │  │   Emotion   │  │    Quote    │
│   Engine    │  │   Analysis  │  │   Matcher   │
│             │  │             │  │             │
│ - Context   │  │ - Analyzer  │  │ - Database  │
│ - LLM calls │  │ - Transform │  │ - Matching  │
│ - Rate      │  │ - Crisis    │  │ - Ranking   │
│   limiting  │  │   detection │  │             │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                │                │
       └────────────────┼────────────────┘
                        │
                        ▼
           ┌───────────────────────┐
           │   AISuite Library     │
           │  (LLM Abstraction)    │
           └───────────────────────┘
                        │
         ┌──────────────┼──────────────┐
         ▼              ▼              ▼
    ┌────────┐    ┌──────────┐   ┌─────────┐
    │ OpenAI │    │ Anthropic│   │  Google │
    │   API  │    │    API   │   │   API   │
    └────────┘    └──────────┘   └─────────┘
```

## Technology Stack

### Core Technologies
- **Python 3.9+**: Primary programming language
- **AISuite**: Unified interface for multiple LLM providers
- **Streamlit 1.30+**: Web UI framework for rapid development
- **python-dotenv**: Environment variable management

### LLM Providers (via AISuite)
- OpenAI (GPT-4o-mini recommended for cost-effectiveness)
- Anthropic Claude (alternative option)
- Google Gemini (optional)

### Deployment
- **Streamlit Cloud**: Hosting platform
- **GitHub**: Version control and CI/CD integration

## Module Design

### 1. Configuration Module (`config/settings.py`)

**Purpose**: Centralized configuration management

```python
# Pseudo-structure
class Settings:
    # LLM Configuration
    llm_provider: str = "openai"
    model_name: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_tokens: int = 500
    timeout_seconds: int = 10
    
    # Rate Limiting
    max_messages_per_session: int = 50
    
    # UI Configuration
    app_title: str = "Emotion Transformer"
    theme_color: str = "#4A90E2"
    
    # Crisis Resources
    crisis_hotline: str = "988"
    crisis_resources: list[str]
    
    # API Keys (from environment)
    openai_api_key: str
    anthropic_api_key: str (optional)
```

**Key Decisions**:
- Use Pydantic for type validation (optional but recommended)
- Load secrets from environment variables (`.env` locally, Streamlit secrets in production)
- Provide sensible defaults for all non-secret configuration

### 2. Chatbot Engine (`src/chatbot/engine.py`)

**Purpose**: Core conversation management and LLM interaction

**Key Components**:

#### ChatbotEngine Class
```python
class ChatbotEngine:
    def __init__(self, provider: str, model: str):
        # Initialize AISuite client
        # Set up provider configuration
        
    def generate_response(self, message: str, context: list) -> str:
        # Format conversation history
        # Call LLM with system prompt
        # Handle errors and retries
        # Return response text
        
    def add_to_context(self, role: str, content: str):
        # Append message to conversation history
        # Manage context window size
        
    def clear_context(self):
        # Reset conversation history
```

**System Prompt Template**:
```
You are an empathetic emotional support companion. Your role is to:
1. Listen actively and validate user feelings
2. Provide supportive, non-judgmental responses
3. Help reframe negative thoughts into positive perspectives
4. Encourage self-compassion and growth

Important guidelines:
- Never dismiss or minimize user emotions
- Avoid toxic positivity (don't force happiness)
- Be warm, genuine, and conversational
- If user mentions crisis situation, direct to professional resources
```

**Error Handling Strategy**:
- **Timeout**: Retry once with exponential backoff, then show fallback message
- **Invalid Key**: Display setup instructions immediately
- **Rate Limit**: Show friendly message about temporary pause
- **Network Error**: Suggest checking connection, allow retry

### 3. Emotion Analysis Module (`src/emotion/analyzer.py`)

**Purpose**: Detect emotions and classify intensity

**Key Components**:

#### EmotionAnalyzer Class
```python
class EmotionAnalyzer:
    def analyze_emotion(self, text: str) -> EmotionResult:
        # Call LLM with emotion detection prompt
        # Parse response into structured format
        # Return emotion labels and intensities
        
class EmotionResult:
    primary_emotion: str  # e.g., "sadness"
    secondary_emotions: list[str]  # e.g., ["loneliness"]
    intensity: float  # 0.0 to 1.0
    is_crisis: bool  # True if crisis detected
```

**Emotion Detection Prompt**:
```
Analyze the emotional content of the following message. Identify:
1. Primary emotion (sadness, anxiety, anger, loneliness, disappointment, fear, frustration, joy, neutral)
2. Intensity (0.0 to 1.0)
3. Any secondary emotions
4. Whether this indicates a mental health crisis (self-harm, suicidal ideation)

Message: {user_message}

Respond in this exact JSON format:
{
  "primary_emotion": "...",
  "intensity": 0.0,
  "secondary_emotions": [],
  "is_crisis": false
}
```

**Crisis Keywords**: "hurt myself", "end it all", "no point living", "better off dead", etc.

### 4. Sentence Transformer (`src/emotion/transformer.py`)

**Purpose**: Reframe negative statements into positive perspectives

**Key Components**:

#### SentenceTransformer Class
```python
class SentenceTransformer:
    def __init__(self, style: str = "gentle"):
        # Set transformation style
        
    def transform(self, original: str, emotion: str) -> str:
        # Generate positive reframing based on style
        # Return transformed sentence
```

**Transformation Prompt Templates** (by style):

**Gentle Style**:
```
The user said: "{original}"
They are feeling {emotion}. Gently reframe this statement into a more positive, 
hopeful perspective while validating their feelings. Be warm and compassionate.
Avoid toxic positivity. Keep it conversational and under 100 words.
```

**Humorous Style**:
```
The user said: "{original}"
Reframe this with light humor and playfulness, while remaining supportive. 
Add a touch of wit to help them smile. Don't mock their feelings.
```

**Direct Style**:
```
The user said: "{original}"
Provide a straightforward, practical positive reframe. Be clear and actionable.
Focus on what they can control or do next.
```

**CBT Style**:
```
The user said: "{original}"
Identify the cognitive distortion (catastrophizing, black-and-white thinking, etc.)
and provide a rational, evidence-based alternative perspective. Use CBT principles.
```

### 5. Quote Database (`src/quotes/database.py`)

**Purpose**: Load, validate, and manage movie quotes

**Data Structure** (`data/quotes.json`):
```json
{
  "quotes": [
    {
      "id": "shawshank-1",
      "text": "Get busy living, or get busy dying.",
      "movie": "The Shawshank Redemption",
      "character": "Andy Dufresne",
      "year": 1994,
      "emotions": ["sadness", "hope"],
      "themes": ["perseverance", "choice"],
      "genre": "drama"
    }
  ]
}
```

**Key Components**:

#### QuoteDatabase Class
```python
class QuoteDatabase:
    def __init__(self, quotes_file: str):
        # Load quotes from JSON
        # Validate schema
        # Index by emotion tags
        
    def get_all_quotes(self) -> list[Quote]:
        # Return all quotes
        
    def get_quotes_by_emotion(self, emotion: str) -> list[Quote]:
        # Filter quotes by emotion tag
        
    def validate_quote(self, quote: dict) -> bool:
        # Check required fields
        # Validate data types
```

**Validation Rules**:
- `text`: Non-empty, max 300 characters
- `movie`, `character`: Required strings
- `year`: Integer, reasonable range (1900-2030)
- `emotions`: At least one valid emotion tag
- `id`: Unique within database

### 6. Quote Matcher (`src/quotes/matcher.py`)

**Purpose**: Match emotions to relevant quotes with ranking

**Key Components**:

#### QuoteMatcher Class
```python
class QuoteMatcher:
    def __init__(self, database: QuoteDatabase):
        # Store reference to quote database
        # Initialize shown quotes tracker
        
    def match_quotes(self, emotion: str, count: int = 3, 
                     exclude: list[str] = []) -> list[Quote]:
        # Filter by emotion tags
        # Rank by relevance
        # Exclude already shown quotes
        # Return top N quotes
        
    def get_another_quote(self, emotion: str, shown_ids: list[str]) -> Quote:
        # Get next quote not in shown_ids
        # Handle exhaustion case
```

**Ranking Algorithm**:
1. **Exact emotion match**: +10 points
2. **Theme overlap**: +5 points per matching theme
3. **Genre diversity**: +2 points if different from recently shown
4. **Recency penalty**: -3 points if shown in last 5 quotes
5. Sort by score descending, return top results

### 7. UI Components (`src/ui/components.py`)

**Purpose**: Reusable Streamlit UI components

**Key Functions**:

```python
def display_user_message(message: str, timestamp: str):
    # Render user message with styling
    
def display_emotion_analysis(emotion: EmotionResult):
    # Show emotion with emoji and intensity bar
    
def display_transformation(original: str, transformed: str, 
                          on_reframe_click: callable):
    # Show original → transformed with button
    
def display_movie_quote(quote: Quote, on_favorite_click: callable,
                       on_try_another_click: callable):
    # Render quote card with buttons
    
def display_loading(message: str = "Thinking..."):
    # Show loading spinner with message
    
def display_error(error_message: str):
    # Styled error alert
```

### 8. Custom Styling (`src/ui/styles.py`)

**Purpose**: CSS customization for Streamlit

**Approach**: Inject custom CSS using `st.markdown()` with `unsafe_allow_html=True`

**Key Styles**:
- Message cards with borders and shadows
- Color-coded emotion indicators
- Quote cards with distinct styling
- Button hover effects
- Responsive layout adjustments

```python
def get_custom_css() -> str:
    return """
    <style>
    .quote-card {
        background: #f0f8ff;
        border-left: 4px solid #4A90E2;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    /* More styles... */
    </style>
    """
```

## Data Flow

### Complete User Interaction Flow

1. **User inputs message** → Stored in session state
2. **Message sent to ChatbotEngine** → Add to context
3. **Emotion Analysis** → EmotionAnalyzer.analyze_emotion()
4. **Crisis Check** → If crisis, show resources and pause
5. **Sentence Transformation** → SentenceTransformer.transform()
6. **Quote Matching** → QuoteMatcher.match_quotes()
7. **Display Results**:
   - User message (timestamp)
   - Emotion analysis (emoji, label, intensity)
   - Transformation (original → new)
   - Movie quotes (2-3 cards)
8. **User interactions**:
   - "Try another quote" → Get next quote
   - "Reframe differently" → Generate new transformation
   - "Favorite" → Add to favorites list
9. **Conversation continues** → Back to step 1

## Session State Management

Streamlit session state variables:

```python
if 'messages' not in st.session_state:
    st.session_state.messages = []  # Conversation history
if 'shown_quotes' not in st.session_state:
    st.session_state.shown_quotes = set()  # Track shown quote IDs
if 'favorites' not in st.session_state:
    st.session_state.favorites = []  # Favorited quotes
if 'transformation_style' not in st.session_state:
    st.session_state.transformation_style = "gentle"
if 'message_count' not in st.session_state:
    st.session_state.message_count = 0
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = ChatbotEngine(...)  # Persist chatbot instance
```

## Security and Privacy Considerations

### API Key Management
- **Local Development**: Use `.env` file (never commit!)
- **Production**: Use Streamlit secrets (`.streamlit/secrets.toml`)
- **Validation**: Check for API key presence on startup, show setup instructions if missing

### Data Privacy
- **No persistent storage**: All data exists only in session state
- **No logging of personal data**: Don't log user messages to external services
- **Clear sessions**: Data is cleared when user closes browser

### Rate Limiting
- **Per-session limits**: Max 50 messages per session
- **Warning at 80%**: Alert user when approaching limit
- **Cost protection**: Estimate token usage and warn if high

## Performance Considerations

### Response Time Optimization
- **LLM Model Choice**: Use smaller, faster models (e.g., GPT-4o-mini) for cost and speed
- **Concurrent Requests**: Don't make sequential API calls; consider parallel emotion + transformation if possible
- **Caching**: Streamlit's `@st.cache_data` for quote database loading

### Streamlit Cloud Limitations
- **Memory**: ~1GB RAM limit, keep quote database reasonable (<100KB)
- **Timeout**: 5-minute request timeout, ensure API calls complete within this
- **Cold starts**: First load may be slow; optimize imports

## Error Recovery Strategies

| Error Type | Detection | Recovery Action |
|------------|-----------|-----------------|
| API Timeout | Request exceeds 10s | Retry once, then show fallback response |
| Invalid API Key | Auth error on init | Display setup instructions, don't crash |
| Rate Limit | 429 status code | Show "Please wait" message, retry after delay |
| Network Error | Connection failure | Suggest checking connection, allow manual retry |
| Empty Input | User submits blank | Prompt for input, don't call API |
| Quote Exhaustion | No more quotes | Show message, allow cycling back to first |
| Crisis Detected | Keyword match | Override normal flow, show resources immediately |

## Testing Strategy

### Manual Testing Checklist
1. **Happy Path**: Normal conversation → emotion → transformation → quotes
2. **Edge Cases**: Empty input, very long input, nonsensical input
3. **All Emotions**: Test each emotion category
4. **All Styles**: Test gentle, humorous, direct, CBT transformations
5. **Interactions**: Try another quote, reframe differently, favorites
6. **Error Scenarios**: Invalid API key, timeout simulation
7. **Crisis Detection**: Test with crisis keywords
8. **Rate Limiting**: Send 50+ messages
9. **UI Responsiveness**: Test on mobile, tablet, desktop
10. **Session Reset**: Clear conversation and verify state reset

### Future Automated Testing (Out of Scope for v1)
- Unit tests for emotion analyzer parsing
- Integration tests for quote matching
- UI component tests with Selenium

## Deployment Architecture

### Local Development
```
Developer Machine
├── Python 3.9+ with venv
├── .env file with API keys
├── Run: streamlit run app.py
└── Access: http://localhost:8501
```

### Production (Streamlit Cloud)
```
GitHub Repository
└── Linked to Streamlit Cloud
    ├── Secrets configured in dashboard
    ├── Auto-deploy on push to main branch
    └── Public URL: https://[app-name].streamlit.app
```

## Future Enhancements (Post-v1)

1. **User Accounts**: Persistent history and favorites across sessions
2. **Advanced Analytics**: Emotion trends over time, insights dashboard
3. **Multi-language**: Translate transformations and quotes
4. **Voice Interface**: Speech-to-text input, text-to-speech output
5. **Therapist Escalation**: Option to connect with licensed professionals
6. **Community Quotes**: User-submitted quotes with moderation
7. **Mobile App**: React Native or Flutter version
8. **A/B Testing**: Compare transformation styles for effectiveness
9. **Fine-tuned Model**: Custom model trained on therapy conversations (ethical considerations required)

## Architectural Decisions Rationale

### Why AISuite?
- **Provider Flexibility**: Easy to switch between OpenAI, Anthropic, Google
- **Cost Optimization**: Choose cheaper models when appropriate
- **Fallback Support**: If one provider is down, switch to another
- **Unified Interface**: Single API regardless of backend LLM

### Why Streamlit?
- **Rapid Development**: Build UI quickly without frontend expertise
- **Built-in Components**: Chat, sidebar, file upload, etc. out of the box
- **Easy Deployment**: Streamlit Cloud integration with GitHub
- **Python Native**: No context switching between languages

### Why No Database?
- **Simplicity**: Session state sufficient for prototype/assignment
- **Cost**: No database hosting fees
- **Privacy**: No persistent storage means no data to secure
- **Future-proof**: Can add database later if needed (e.g., PostgreSQL, Firebase)

### Why JSON for Quotes?
- **Simplicity**: Easy to edit and version control
- **Portability**: Works anywhere Python runs
- **No Dependencies**: No database driver needed
- **Performance**: Fast loading for small dataset (<1000 quotes)

---

## Summary

This architecture prioritizes:
1. **Simplicity**: Easy to understand and maintain
2. **Modularity**: Clear separation of concerns
3. **Flexibility**: Easy to swap LLM providers or add features
4. **User Experience**: Fast, responsive, empathetic interactions
5. **Deployment-Ready**: Works seamlessly on Streamlit Cloud

The design supports the core goal of providing immediate, accessible emotional support through positive reframing and inspirational movie quotes.
