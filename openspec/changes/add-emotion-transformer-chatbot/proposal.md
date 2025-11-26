# Proposal: Emotion Transformer + Movie Quote Therapist Chatbot

## Why

Students and individuals experiencing negative emotions or stressful situations often lack immediate, accessible support for emotional reframing. Traditional therapy is expensive and not always available, while self-help resources can feel impersonal. This project addresses the need for an immediate, engaging, and uplifting conversational tool that helps users:

1. **Reframe negative thoughts** into positive perspectives using cognitive reframing techniques
2. **Find inspiration** through relevant motivational movie quotes that resonate with their emotional state
3. **Develop emotional awareness** by understanding their own emotional patterns

This chatbot serves as a personal emotional support companion, making mental wellness tools accessible through a simple, friendly interface.

## What Changes

This proposal introduces a complete AI-powered emotional support chatbot system with the following capabilities:

- **Chatbot Core Engine**: AISuite-powered conversation system with context retention and multi-turn dialogue support
- **Emotion Analysis Module**: Intelligent emotion detection and classification (sadness, anxiety, anger, frustration, etc.)
- **Sentence Transformation**: Converts negative statements into positive, constructive perspectives while maintaining authenticity
- **Movie Quote Database**: Curated collection of motivational quotes from popular films, matched to emotional contexts
- **Interactive Streamlit UI**: Clean, responsive interface with real-time responses and visual emotion indicators
- **Conversation History**: Session-based chat history with ability to revisit past transformations
- **User Preferences**: Customizable settings for transformation style (gentle/humorous/direct) and quote genres

### Key Features

1. **Dual Response System**:
   - Positive reframing of user's negative input
   - 2-3 relevant motivational movie quotes with film titles

2. **Smart Emotion Detection**:
   - Multi-label emotion classification
   - Intensity scoring (mild, moderate, severe)
   - Context-aware matching

3. **Interactive Elements**:
   - "Try another quote" button
   - "Reframe differently" option
   - Save favorite quotes feature
   - Export conversation option

4. **Safety Features**:
   - Crisis detection with resource recommendations
   - Empathetic fallback responses
   - Clear disclaimer about not replacing professional help

## Impact

### Affected Specs
- **NEW**: `chatbot-core` - Core conversation engine and AISuite integration
- **NEW**: `emotion-analysis` - Emotion detection and classification system
- **NEW**: `movie-quotes` - Quote database and retrieval system  
- **NEW**: `ui-interface` - Streamlit user interface components

### Affected Code
- **NEW**: `app.py` - Main Streamlit application entry point
- **NEW**: `src/chatbot/engine.py` - AISuite conversation handler
- **NEW**: `src/emotion/analyzer.py` - Emotion detection module
- **NEW**: `src/emotion/transformer.py` - Sentence reframing logic
- **NEW**: `src/quotes/database.py` - Movie quotes data structure
- **NEW**: `src/quotes/matcher.py` - Quote-to-emotion matching algorithm
- **NEW**: `src/ui/components.py` - Reusable UI components
- **NEW**: `src/ui/styles.py` - Custom CSS and styling
- **NEW**: `config/settings.py` - Configuration management
- **NEW**: `data/quotes.json` - Movie quotes dataset
- **NEW**: `requirements.txt` - Python dependencies
- **NEW**: `.streamlit/config.toml` - Streamlit deployment config
- **NEW**: `.streamlit/secrets.toml.example` - API key template
- **NEW**: `README.md` - Project documentation
- **NEW**: `.gitignore` - Git ignore rules

### Technical Dependencies
- `aisuite` - Multi-LLM provider interface
- `streamlit` - Web UI framework
- `python-dotenv` - Environment variable management
- `pydantic` - Data validation (optional)

### Deployment Considerations
- Requires API keys for LLM providers (OpenAI, Anthropic, etc.)
- Streamlit Cloud deployment with secrets management
- GitHub repository with proper `.gitignore` for secrets
- Estimated API cost: ~$0.01-0.05 per conversation (varies by provider)

### User Experience Impact
- **Learning Curve**: Minimal - simple chat interface
- **Performance**: Real-time responses (2-5 seconds typical)
- **Accessibility**: Web-based, mobile-friendly
- **Privacy**: No data storage beyond session (can be enhanced later)

## Success Criteria

1. ✅ User can input negative thoughts and receive positive reframings
2. ✅ System accurately detects emotions (>80% user satisfaction in testing)
3. ✅ Movie quotes are contextually relevant to user's emotional state
4. ✅ UI is intuitive and visually appealing
5. ✅ Successfully deployed to Streamlit Cloud
6. ✅ GitHub repository is well-documented and shareable
7. ✅ Meets AIOT HW4 assignment requirements

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Inappropriate emotion detection | Implement fallback empathetic responses |
| API quota/cost overrun | Add usage tracking, implement rate limiting |
| Sensitive mental health content | Include crisis resources, clear disclaimers |
| Quote copyright concerns | Use public domain quotes or fair use policy |
| Poor transformation quality | Provide multiple transformation styles, user feedback |

## Future Enhancements (Out of Scope)

- User accounts and persistent history
- Multi-language support
- Voice input/output
- Therapist escalation feature
- Analytics dashboard for emotional patterns
- Community-contributed quotes
- Mobile native app version
