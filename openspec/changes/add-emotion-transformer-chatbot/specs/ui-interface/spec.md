# UI Interface Specification

## ADDED Requirements

### Requirement: Streamlit Application Layout
The system SHALL provide a clean, intuitive Streamlit interface with chat-based interaction and clear visual hierarchy.

**Rationale**: User experience is critical for emotional support tools; interface must feel welcoming, non-judgmental, and easy to navigate.

#### Scenario: Initial landing page
- **GIVEN** user opens application URL
- **WHEN** page loads
- **THEN** welcoming header with app title and tagline is displayed
- **AND** brief usage instructions are visible
- **AND** disclaimer about not replacing professional help is shown
- **AND** chat input box is ready and focused

#### Scenario: Responsive layout
- **GIVEN** user accesses app on different devices
- **WHEN** page renders
- **THEN** layout adapts to mobile, tablet, and desktop screens
- **AND** all interactive elements remain accessible
- **AND** text remains readable at all viewport sizes

### Requirement: Chat Message Display
The system SHALL display conversation history with clear distinction between user messages, emotion analysis, transformations, and movie quotes.

**Rationale**: Clear visual separation helps users understand different types of responses and improves readability.

#### Scenario: Display user message
- **GIVEN** user submits a message
- **WHEN** message is rendered
- **THEN** message appears with user avatar/icon
- **AND** message is right-aligned or has distinct styling
- **AND** timestamp is visible
- **AND** message is added to scrollable history

#### Scenario: Display emotion analysis result
- **GIVEN** system detects user's emotion
- **WHEN** analysis is displayed
- **THEN** emotion label is shown with emoji indicator
- **AND** intensity is visualized (e.g., color, bar, or scale)
- **AND** analysis appears before transformation and quotes
- **AND** styling is subtle, non-intrusive

#### Scenario: Display positive transformation
- **GIVEN** negative sentence is transformed
- **WHEN** transformation is rendered
- **THEN** original and transformed text are both visible
- **AND** arrow or transition indicator shows the change
- **AND** transformation is highlighted or in distinct color (e.g., green tone)
- **AND** "Reframe differently" button is available

#### Scenario: Display movie quotes
- **GIVEN** 2-3 quotes are matched to emotion
- **WHEN** quotes are rendered
- **THEN** each quote is in distinct card or box
- **AND** quote text is emphasized (larger, italic, or styled)
- **AND** attribution (movie, character, year) is clearly shown
- **AND** "Try another quote" button is available per quote

### Requirement: Interactive Elements
The system SHALL provide interactive buttons and controls for quote cycling, transformation options, and conversation management.

**Rationale**: Interactivity increases engagement and gives users control over their experience.

#### Scenario: "Try another quote" button
- **GIVEN** user sees displayed quotes
- **WHEN** user clicks "Try another quote"
- **THEN** new quote from same emotion category is fetched
- **AND** quote replaces current quote with smooth transition
- **AND** button is disabled if no more quotes available
- **AND** tooltip explains when quotes are exhausted

#### Scenario: "Reframe differently" button
- **GIVEN** transformation is displayed
- **WHEN** user clicks "Reframe differently"
- **THEN** alternative transformation is generated
- **AND** transformation style may vary (gentle, humorous, direct)
- **AND** user can cycle through multiple reframes
- **AND** loading indicator appears during generation

#### Scenario: Save to favorites
- **GIVEN** user views a quote
- **WHEN** user clicks heart/star icon
- **THEN** quote is added to favorites list
- **AND** icon changes to "filled" state
- **AND** feedback animation confirms save
- **AND** user can access favorites from sidebar

#### Scenario: Clear conversation
- **GIVEN** user has ongoing conversation
- **WHEN** user clicks "Start new conversation"
- **THEN** confirmation dialog appears
- **AND** upon confirmation, chat history is cleared
- **AND** session state is reset
- **AND** user starts fresh with new session ID

### Requirement: Sidebar Configuration
The system SHALL provide a sidebar for settings, preferences, and favorites management.

**Rationale**: Advanced options should be accessible but not clutter the main chat interface.

#### Scenario: Transformation style selector
- **GIVEN** user opens sidebar
- **WHEN** settings are displayed
- **THEN** radio buttons or dropdown for style selection (Gentle, Humorous, Direct, CBT)
- **AND** selected style is highlighted
- **AND** style applies to subsequent transformations
- **AND** style choice persists within session

#### Scenario: API provider selection (optional)
- **GIVEN** multiple LLM providers are configured
- **WHEN** user opens sidebar
- **THEN** dropdown shows available providers (OpenAI, Anthropic, etc.)
- **AND** current provider is indicated
- **AND** user can switch providers mid-session
- **AND** conversation context is maintained across providers

#### Scenario: View favorites
- **GIVEN** user has saved favorite quotes
- **WHEN** user clicks "Favorites" in sidebar
- **THEN** list of all favorited quotes is displayed
- **AND** quotes show full text and attribution
- **AND** user can remove quotes from favorites
- **AND** "Export all" button is available

#### Scenario: Usage statistics (optional)
- **GIVEN** user is in active session
- **WHEN** sidebar displays stats
- **THEN** message count is shown
- **AND** session duration is displayed
- **AND** approximate API cost is estimated
- **AND** stats reset on new session

### Requirement: Visual Feedback and Loading States
The system SHALL provide clear visual feedback for loading, processing, and errors.

**Rationale**: Users need to know the system is working; unexpected silence or delays cause frustration and abandonment.

#### Scenario: Message processing indicator
- **GIVEN** user submits message
- **WHEN** system is processing (AI call in progress)
- **THEN** loading spinner or "thinking" animation is displayed
- **AND** input box is disabled during processing
- **AND** estimated time may be shown (e.g., "Analyzing... ~3s")

#### Scenario: Quote loading animation
- **GIVEN** user clicks "Try another quote"
- **WHEN** new quote is being fetched
- **THEN** smooth transition animation plays
- **AND** loading state is indicated
- **AND** button is temporarily disabled
- **AND** animation completes within 1 second

#### Scenario: Error display
- **GIVEN** API call fails or error occurs
- **WHEN** error is encountered
- **THEN** user-friendly error message is displayed
- **AND** technical details are hidden (but logged)
- **AND** suggested actions are provided (e.g., "Please try again")
- **AND** conversation history is preserved

### Requirement: Custom Styling and Branding
The system SHALL apply custom CSS to create a warm, supportive visual theme.

**Rationale**: Visual design influences emotional response; a thoughtfully designed interface enhances the supportive experience.

#### Scenario: Color scheme
- **GIVEN** application loads
- **WHEN** UI is rendered
- **THEN** soft, calming color palette is applied (e.g., blues, greens, pastels)
- **AND** high contrast is maintained for readability
- **AND** colors align with emotional support theme

#### Scenario: Typography
- **GIVEN** text is displayed
- **WHEN** page is rendered
- **THEN** readable, friendly font is used (e.g., sans-serif)
- **AND** font sizes are appropriate for content type
- **AND** line spacing enhances readability
- **AND** quote text uses distinct styling (italic, larger size)

#### Scenario: Emoji and iconography
- **GIVEN** emotions are displayed
- **WHEN** rendered in UI
- **THEN** appropriate emoji represents each emotion (😢 💪 😰 etc.)
- **AND** icons for buttons are intuitive (❤️ 🔄 📥 ✨)
- **AND** emoji enhance without overwhelming interface

### Requirement: Accessibility
The system SHALL follow basic accessibility best practices for inclusive design.

**Rationale**: Emotional support should be accessible to all users, including those with disabilities.

#### Scenario: Keyboard navigation
- **GIVEN** user navigates with keyboard only
- **WHEN** user tabs through interface
- **THEN** all interactive elements are accessible
- **AND** focus indicators are visible
- **AND** tab order is logical
- **AND** chat input is easily reachable

#### Scenario: Screen reader compatibility
- **GIVEN** user uses screen reader
- **WHEN** content is read aloud
- **THEN** message content is clearly announced
- **AND** button labels are descriptive
- **AND** ARIA labels are present where needed
- **AND** page structure uses semantic HTML

#### Scenario: Text scaling
- **GIVEN** user increases browser text size
- **WHEN** page re-renders
- **THEN** text scales appropriately
- **AND** layout remains functional
- **AND** no content is cut off or overlapped

## UI Components Structure

### Main Layout
```
[Header: App Title & Tagline]
[Disclaimer Banner]
---
[Sidebar]               [Main Chat Area]
- Settings              - Message History
- Transformation Style    - User Message
- Favorites               - Emotion Analysis
- Usage Stats             - Transformation
- Export                  - Movie Quotes (cards)
                        [Input Box]
                        [Send Button]
```

### Message Card Components
1. **User Message Card**: Avatar, text, timestamp
2. **Emotion Card**: Emoji, label, intensity bar
3. **Transformation Card**: Original → Transformed, reframe button
4. **Quote Card**: Quote text, attribution, favorite button, try another button

### Color Palette Suggestions
- **Primary**: #4A90E2 (calm blue)
- **Secondary**: #7ED321 (encouraging green)
- **Background**: #F5F7FA (soft gray)
- **Text**: #2C3E50 (dark gray)
- **Accent**: #F39C12 (warm orange)
- **Error**: #E74C3C (soft red)
- **Success**: #2ECC71 (green)

### Typography Scale
- **Header**: 2.5rem, bold
- **Subheader**: 1.5rem, semi-bold
- **Body**: 1rem, regular
- **Quote**: 1.25rem, italic
- **Attribution**: 0.875rem, light
- **Button**: 0.875rem, medium
