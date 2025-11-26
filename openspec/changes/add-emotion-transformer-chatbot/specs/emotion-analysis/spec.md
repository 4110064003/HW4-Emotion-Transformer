# Emotion Analysis Specification

## ADDED Requirements

### Requirement: Emotion Detection
The system SHALL analyze user input text to identify emotional states including sadness, anxiety, anger, frustration, stress, loneliness, and disappointment.

**Rationale**: Accurate emotion detection is critical for providing appropriate movie quotes and reframing strategies tailored to the user's emotional state.

#### Scenario: Detect sadness
- **GIVEN** user inputs "I feel so alone and nobody understands me"
- **WHEN** emotion analysis is performed
- **THEN** primary emotion is identified as "sadness"
- **AND** secondary emotion may include "loneliness"
- **AND** intensity score is provided (e.g., 0.8 on 0-1 scale)

#### Scenario: Detect multiple emotions
- **GIVEN** user inputs "I'm angry at myself for failing and worried about what others think"
- **WHEN** emotion analysis is performed
- **THEN** multiple emotions are detected: anger, anxiety
- **AND** each emotion has individual intensity score
- **AND** primary emotion is determined for response prioritization

#### Scenario: Detect neutral or positive input
- **GIVEN** user inputs "The weather is nice today"
- **WHEN** emotion analysis is performed
- **THEN** neutral or positive sentiment is detected
- **AND** system responds with encouragement to share deeper feelings
- **OR** engages in light conversation

### Requirement: Sentence Transformation
The system SHALL reframe negative statements into positive, constructive perspectives while maintaining authenticity and avoiding toxic positivity.

**Rationale**: The core feature is helping users see alternative perspectives; transformations must feel genuine and helpful, not dismissive.

#### Scenario: Transform complaint into opportunity
- **GIVEN** user inputs "It's raining and I forgot my umbrella, what an awful day"
- **WHEN** transformation is requested
- **THEN** output includes positive reframe like "The rain will cool things down and make everything smell fresh"
- **AND** acknowledges the inconvenience without dismissing feelings
- **AND** maintains conversational tone

#### Scenario: Transform failure into learning
- **GIVEN** user inputs "I failed my exam, I'm so stupid"
- **WHEN** transformation is requested
- **THEN** output reframes as growth opportunity
- **AND** challenges negative self-talk ("stupid")
- **AND** suggests concrete perspective like "This shows which areas need more focus"

#### Scenario: Avoid toxic positivity
- **GIVEN** user inputs "My loved one passed away"
- **WHEN** transformation is requested
- **THEN** response validates grief without forced positivity
- **AND** offers gentle perspective like "It's okay to feel this pain; it shows how much they meant to you"
- **AND** does not minimize serious loss

### Requirement: Crisis Detection
The system SHALL identify potentially critical mental health situations and provide appropriate resources.

**Rationale**: An emotional support chatbot must recognize when professional help is needed and direct users to appropriate resources.

#### Scenario: Detect self-harm indicators
- **GIVEN** user inputs messages suggesting self-harm or suicidal ideation
- **WHEN** crisis detection is performed
- **THEN** system immediately displays crisis resources
- **AND** provides hotline numbers (e.g., 988 Suicide & Crisis Lifeline)
- **AND** pauses normal chatbot functionality until user acknowledges

#### Scenario: Severe distress without crisis
- **GIVEN** user expresses overwhelming but non-critical distress
- **WHEN** emotion intensity exceeds threshold (e.g., 0.9)
- **THEN** system suggests professional support gently
- **AND** continues providing emotional support
- **AND** includes disclaimer about chatbot limitations

### Requirement: Transformation Style Options
The system SHALL offer multiple transformation styles: gentle, humorous, direct, and cognitive-behavioral.

**Rationale**: Different users respond to different approaches; customization improves effectiveness and user satisfaction.

#### Scenario: Gentle transformation style
- **GIVEN** user selects "gentle" style
- **WHEN** transformation is generated
- **THEN** output uses soft, nurturing language
- **AND** validates feelings extensively before reframing
- **AND** uses phrases like "I hear you" and "It's understandable"

#### Scenario: Humorous transformation style
- **GIVEN** user selects "humorous" style
- **WHEN** transformation is generated for appropriate context
- **THEN** output includes light, playful reframing
- **AND** uses appropriate humor without mockery
- **AND** maintains supportive undertone

#### Scenario: Cognitive-behavioral style
- **GIVEN** user selects "CBT" style
- **WHEN** transformation is generated
- **THEN** output identifies cognitive distortion (e.g., catastrophizing)
- **AND** provides structured thought challenge
- **AND** suggests evidence-based alternative thought

### Requirement: Emotion History Tracking
The system SHALL track emotional patterns within a session to provide insights (optional enhancement).

**Rationale**: Helping users recognize patterns in their emotional responses can increase self-awareness.

#### Scenario: Session emotion summary
- **GIVEN** user has completed conversation with 10+ messages
- **WHEN** user requests session summary
- **THEN** system displays most frequent emotions detected
- **AND** shows progression (e.g., "Started anxious, ended hopeful")
- **AND** visualizes with simple emoji or color indicators

## Emotion Categories

| Emotion | Keywords | Intensity Indicators | Default Response Strategy |
|---------|----------|---------------------|--------------------------|
| Sadness | sad, depressed, down, hopeless | Very, extremely, completely | Validate + gentle reframe |
| Anxiety | worried, anxious, nervous, stressed | Can't stop, overwhelming | Acknowledge + grounding |
| Anger | angry, furious, frustrated, mad | So, really, extremely | Validate + redirect energy |
| Loneliness | alone, lonely, isolated, nobody | No one, nobody, always | Connect + perspective |
| Disappointment | disappointed, let down, failed | Total, complete, utter | Normalize + opportunity |
| Fear | scared, afraid, terrified, panicked | Really, so, extremely | Reassure + practical steps |
| Frustration | frustrated, annoyed, irritated | Keep, always, constantly | Acknowledge + problem-solve |

## Transformation Strategies

### Cognitive Reframing Patterns
1. **Perspective Shift**: "What if you looked at it this way..."
2. **Silver Lining**: "While X is challenging, Y is an opportunity..."
3. **Growth Mindset**: "This difficulty is teaching you..."
4. **Temporal**: "This feeling is temporary; remember when..."
5. **Comparison**: "Compared to past challenges you've overcome..."
6. **Gratitude Injection**: "Despite X, you still have Y..."
