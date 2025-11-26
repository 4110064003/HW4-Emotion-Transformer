# Implementation Tasks

## 1. Project Setup and Infrastructure

- [ ] 1.1 Initialize Git repository with `.gitignore` for Python
- [ ] 1.2 Create project directory structure (`src/`, `data/`, `config/`, `.streamlit/`)
- [ ] 1.3 Create `requirements.txt` with dependencies:
  - [ ] aisuite
  - [ ] streamlit
  - [ ] python-dotenv
  - [ ] (optional) pydantic for data validation
- [ ] 1.4 Create `.streamlit/config.toml` for Streamlit settings
- [ ] 1.5 Create `.streamlit/secrets.toml.example` template for API keys
- [ ] 1.6 Set up virtual environment and install dependencies
- [ ] 1.7 Create `README.md` with project description and setup instructions
- [ ] 1.8 Add license file (MIT or appropriate)

## 2. Configuration Management

- [ ] 2.1 Create `config/settings.py` for centralized configuration
- [ ] 2.2 Implement environment variable loading with python-dotenv
- [ ] 2.3 Define configuration classes/dictionaries:
  - [ ] LLM provider settings (model, temperature, max_tokens)
  - [ ] Rate limiting parameters
  - [ ] UI theme settings
  - [ ] Crisis resource information
- [ ] 2.4 Add configuration validation on startup
- [ ] 2.5 Document required environment variables in README

## 3. Movie Quotes Database

- [ ] 3.1 Create `data/quotes.json` file
- [ ] 3.2 Define JSON schema for quote structure
- [ ] 3.3 Curate and add minimum 50 quotes covering all emotion categories:
  - [ ] 10+ quotes for sadness/hope
  - [ ] 10+ quotes for anxiety/courage
  - [ ] 8+ quotes for anger/justice
  - [ ] 8+ quotes for loneliness/connection
  - [ ] 8+ quotes for disappointment/perseverance
  - [ ] 6+ quotes for fear/bravery
- [ ] 3.4 Create `src/quotes/database.py` to load and validate quotes
- [ ] 3.5 Implement quote search and filtering functions
- [ ] 3.6 Add duplicate detection and validation logic

## 4. Emotion Analysis Module

- [ ] 4.1 Create `src/emotion/analyzer.py`
- [ ] 4.2 Implement emotion detection using AISuite LLM:
  - [ ] Design prompt template for emotion classification
  - [ ] Parse LLM response into structured emotion data
  - [ ] Handle multi-label emotion detection
  - [ ] Calculate emotion intensity scores
- [ ] 4.3 Create `src/emotion/transformer.py`
- [ ] 4.4 Implement sentence transformation logic:
  - [ ] Design prompts for different transformation styles (gentle, humorous, direct, CBT)
  - [ ] Generate positive reframings while avoiding toxic positivity
  - [ ] Maintain authenticity in transformations
- [ ] 4.5 Implement crisis detection:
  - [ ] Define crisis keywords and patterns
  - [ ] Create crisis response templates
  - [ ] Include resource links (988 hotline, etc.)
- [ ] 4.6 Add emotion-to-theme mapping dictionary
- [ ] 4.7 Create fallback responses for edge cases

## 5. Quote Matching System

- [ ] 5.1 Create `src/quotes/matcher.py`
- [ ] 5.2 Implement emotion-to-quote matching algorithm:
  - [ ] Tag-based filtering by emotion category
  - [ ] Ranking by relevance score
  - [ ] Session-based duplicate avoidance
- [ ] 5.3 Add "try another quote" functionality:
  - [ ] Track shown quotes per session
  - [ ] Cycle through available quotes
  - [ ] Handle quote exhaustion gracefully
- [ ] 5.4 Implement quote formatting and attribution display
- [ ] 5.5 Add fallback quotes for unmatched emotions

## 6. AISuite Chatbot Core

- [ ] 6.1 Create `src/chatbot/engine.py`
- [ ] 6.2 Initialize AISuite client with provider configuration
- [ ] 6.3 Implement conversation context management:
  - [ ] Store message history in session state
  - [ ] Format context for LLM prompts
  - [ ] Implement context window management
- [ ] 6.4 Create core chat response generation function
- [ ] 6.5 Implement error handling:
  - [ ] API timeout handling with retry logic
  - [ ] Invalid API key detection
  - [ ] Graceful degradation for API failures
- [ ] 6.6 Add rate limiting:
  - [ ] Track messages per session
  - [ ] Display usage warnings
  - [ ] Implement token usage estimation (optional)
- [ ] 6.7 Implement provider fallback mechanism
- [ ] 6.8 Create system prompt templates for empathetic responses

## 7. Streamlit UI - Layout and Structure

- [ ] 7.1 Create `app.py` as main Streamlit entry point
- [ ] 7.2 Set up page configuration (title, icon, layout)
- [ ] 7.3 Create welcome header with app title and tagline
- [ ] 7.4 Add disclaimer banner about not replacing professional help
- [ ] 7.5 Initialize Streamlit session state variables:
  - [ ] Message history
  - [ ] Current emotion
  - [ ] Shown quotes
  - [ ] Favorite quotes
  - [ ] Transformation style preference
  - [ ] Session statistics
- [ ] 7.6 Create main chat container with scrollable area
- [ ] 7.7 Implement chat input box and send button

## 8. Streamlit UI - Message Display Components

- [ ] 8.1 Create `src/ui/components.py` for reusable UI components
- [ ] 8.2 Implement `display_user_message()` function
- [ ] 8.3 Implement `display_emotion_analysis()` function with emoji indicators
- [ ] 8.4 Implement `display_transformation()` function:
  - [ ] Show original → transformed text
  - [ ] Add "Reframe differently" button
  - [ ] Style with visual distinction (colors, arrows)
- [ ] 8.5 Implement `display_movie_quote()` function:
  - [ ] Quote card design with styling
  - [ ] Attribution formatting
  - [ ] "Try another quote" button
  - [ ] Favorite (heart) button
- [ ] 8.6 Add loading animations for processing states
- [ ] 8.7 Create error message display component

## 9. Streamlit UI - Sidebar and Settings

- [ ] 9.1 Create sidebar layout
- [ ] 9.2 Add transformation style selector:
  - [ ] Radio buttons for Gentle, Humorous, Direct, CBT styles
  - [ ] Style descriptions/tooltips
  - [ ] Persist selection in session state
- [ ] 9.3 Add favorites section:
  - [ ] Display favorited quotes
  - [ ] Remove from favorites functionality
  - [ ] "Export favorites" button
- [ ] 9.4 Add session statistics display (optional):
  - [ ] Message count
  - [ ] Session duration
  - [ ] Approximate cost estimate
- [ ] 9.5 Add "Start new conversation" button with confirmation
- [ ] 9.6 Add "About" section with project info

## 10. Interactive Features

- [ ] 10.1 Implement "Try another quote" button logic:
  - [ ] Fetch new quote from same emotion
  - [ ] Update UI with smooth transition
  - [ ] Handle quote exhaustion
- [ ] 10.2 Implement "Reframe differently" button logic:
  - [ ] Generate alternative transformation
  - [ ] Optionally change style
  - [ ] Show loading state
- [ ] 10.3 Implement quote favoriting:
  - [ ] Add/remove from favorites list
  - [ ] Visual feedback (filled heart icon)
  - [ ] Persist in session state
- [ ] 10.4 Implement export favorites functionality:
  - [ ] Generate formatted text file
  - [ ] Streamlit download button
  - [ ] Include all quotes with attribution
- [ ] 10.5 Implement conversation reset/clear functionality

## 11. Custom Styling

- [ ] 11.1 Create `src/ui/styles.py` for CSS customization
- [ ] 11.2 Define custom CSS for:
  - [ ] Color palette (calming blues, greens)
  - [ ] Typography (fonts, sizes, line heights)
  - [ ] Message cards styling
  - [ ] Button styling
  - [ ] Quote cards with borders/shadows
- [ ] 11.3 Inject custom CSS into Streamlit app
- [ ] 11.4 Add emoji and iconography throughout UI
- [ ] 11.5 Ensure responsive design for mobile/tablet
- [ ] 11.6 Test visual hierarchy and readability

## 12. Integration and Workflow

- [ ] 12.1 Integrate all modules in `app.py`:
  - [ ] Import chatbot engine, emotion analyzer, transformer, quote matcher
  - [ ] Wire up user input → processing → display pipeline
- [ ] 12.2 Implement main conversation loop:
  - [ ] User submits message
  - [ ] Detect emotion
  - [ ] Generate transformation
  - [ ] Match and display quotes
  - [ ] Update conversation history
- [ ] 12.3 Add crisis detection check in conversation loop
- [ ] 12.4 Implement error handling across all components
- [ ] 12.5 Test complete user flow from input to output

## 13. Testing and Quality Assurance

- [ ] 13.1 Manual testing of core features:
  - [ ] Submit various negative statements and verify transformations
  - [ ] Test all emotion categories
  - [ ] Verify quote matching accuracy
  - [ ] Test "try another quote" with exhaustion
  - [ ] Test "reframe differently" functionality
  - [ ] Test favoriting and export
- [ ] 13.2 Test error scenarios:
  - [ ] Invalid/missing API key
  - [ ] API timeouts
  - [ ] Network failures
  - [ ] Empty or malformed inputs
- [ ] 13.3 Test different transformation styles (Gentle, Humorous, Direct, CBT)
- [ ] 13.4 Test rate limiting behavior
- [ ] 13.5 Test crisis detection with sample inputs
- [ ] 13.6 Test UI responsiveness on mobile and desktop
- [ ] 13.7 Test accessibility (keyboard navigation, screen reader basics)
- [ ] 13.8 Verify no API keys or secrets in code

## 14. Documentation

- [ ] 14.1 Complete `README.md` with:
  - [ ] Project overview and features
  - [ ] Installation instructions
  - [ ] API key setup guide
  - [ ] Usage instructions
  - [ ] Screenshots/demo GIF
  - [ ] Deployment guide
  - [ ] Contributing guidelines (if applicable)
  - [ ] License information
- [ ] 14.2 Add inline code comments and docstrings
- [ ] 14.3 Create `DEPLOYMENT.md` for Streamlit Cloud deployment steps
- [ ] 14.4 Document environment variables in `.env.example`
- [ ] 14.5 Add disclaimer and ethical considerations section

## 15. Deployment Preparation

- [ ] 15.1 Test locally with `streamlit run app.py`
- [ ] 15.2 Verify all dependencies in `requirements.txt`
- [ ] 15.3 Create GitHub repository
- [ ] 15.4 Push code to GitHub with proper `.gitignore`
- [ ] 15.5 Verify no secrets are committed
- [ ] 15.6 Set up Streamlit Cloud account
- [ ] 15.7 Link GitHub repo to Streamlit Cloud
- [ ] 15.8 Configure secrets in Streamlit Cloud dashboard
- [ ] 15.9 Deploy to Streamlit Cloud
- [ ] 15.10 Test deployed application
- [ ] 15.11 Update README with live demo link

## 16. Final Polish and Submission

- [ ] 16.1 Add loading states for better UX
- [ ] 16.2 Optimize quote database (add more quotes if needed)
- [ ] 16.3 Fine-tune transformation prompts based on testing
- [ ] 16.4 Review and improve error messages
- [ ] 16.5 Add "Share" button for social media (optional)
- [ ] 16.6 Create project demo video or screenshots
- [ ] 16.7 Prepare assignment submission materials:
  - [ ] GitHub repository link
  - [ ] Live Streamlit app link
  - [ ] Demo video or screenshots
  - [ ] Written report (if required by course)
- [ ] 16.8 Final code review and cleanup
- [ ] 16.9 Test one more time end-to-end
- [ ] 16.10 Submit assignment

## Notes
- Each section can be tackled sequentially or with some parallelization
- Core functionality (1-6, 12) should be completed first
- UI (7-11) can be developed iteratively alongside core features
- Testing (13) should be ongoing throughout development
- Deployment (15) requires completed and tested code
