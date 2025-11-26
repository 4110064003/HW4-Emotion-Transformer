# Movie Quotes Specification

## ADDED Requirements

### Requirement: Quote Database Structure
The system SHALL maintain a structured database of motivational movie quotes with metadata for emotion-based matching.

**Rationale**: A well-organized quote database enables efficient retrieval of contextually relevant quotes that resonate with users' emotional states.

#### Scenario: Quote data structure
- **GIVEN** system initializes quote database
- **WHEN** quote is loaded
- **THEN** each quote contains: text, movie title, character, year, emotions tags, themes, and context
- **AND** quotes are validated for completeness
- **AND** duplicate quotes are prevented

#### Scenario: Initial quote collection
- **GIVEN** application deployment
- **WHEN** database is populated
- **THEN** minimum 50 quotes covering all emotion categories
- **AND** quotes span multiple genres (drama, comedy, action, animation)
- **AND** quotes are from recognizable, popular films

### Requirement: Emotion-to-Quote Matching
The system SHALL match detected emotions to relevant motivational quotes using semantic similarity and tag-based filtering.

**Rationale**: Quotes must feel personally relevant to maximize emotional impact and user engagement.

#### Scenario: Match quote to sadness
- **GIVEN** user's emotion is detected as "sadness" with intensity 0.7
- **WHEN** quote matching is performed
- **THEN** system retrieves 2-3 quotes tagged with "sadness" or "hope"
- **AND** quotes have uplifting, comforting themes
- **AND** quotes are ranked by relevance score

#### Scenario: Match quote to anxiety
- **GIVEN** user's emotion is detected as "anxiety"
- **WHEN** quote matching is performed
- **THEN** system retrieves quotes about courage, facing fears, or overcoming
- **AND** prioritizes quotes with calming or empowering tone
- **AND** avoids quotes that might increase anxiety

#### Scenario: Multi-emotion matching
- **GIVEN** user has multiple detected emotions (anger + disappointment)
- **WHEN** quote matching is performed
- **THEN** system finds quotes addressing both emotions
- **OR** selects quotes for primary emotion
- **AND** provides variety in quote selection

### Requirement: Quote Retrieval and Ranking
The system SHALL retrieve and rank quotes based on contextual relevance, avoiding repetition within sessions.

**Rationale**: Users should receive diverse, fresh quotes; repeated quotes diminish impact and engagement.

#### Scenario: Retrieve top quotes
- **GIVEN** emotion and intensity are identified
- **WHEN** quote retrieval is requested
- **THEN** system returns 2-3 highest-ranked quotes
- **AND** ranking considers emotion match, theme relevance, and variety
- **AND** quotes not shown in current session are prioritized

#### Scenario: "Try another quote" functionality
- **GIVEN** user clicks "Try another quote" button
- **WHEN** new quote is requested
- **THEN** system provides different quote from same emotion category
- **AND** previously shown quotes are excluded
- **AND** if all quotes exhausted, earliest quote can be re-shown with notification

#### Scenario: No matching quotes
- **GIVEN** rare or untagged emotion is detected
- **WHEN** quote matching finds no results
- **THEN** system uses fallback general inspirational quotes
- **AND** logs the gap for database improvement
- **AND** user experience remains smooth

### Requirement: Quote Attribution and Formatting
The system SHALL display quotes with proper attribution including movie title, character, and year.

**Rationale**: Attribution adds credibility, helps users remember favorite quotes, and respects intellectual property.

#### Scenario: Display quote with full attribution
- **GIVEN** quote is selected for display
- **WHEN** rendered in UI
- **THEN** quote text is shown in quotation marks
- **AND** attribution format: "— Character, Movie Title (Year)"
- **AND** movie title is visually distinct (e.g., italics or bold)

#### Scenario: Long quote truncation
- **GIVEN** quote exceeds 200 characters
- **WHEN** displayed in UI
- **THEN** quote is truncated with "..." if needed for layout
- **AND** full quote available on hover or click
- **OR** quote is excluded from database during curation

### Requirement: Quote Favoriting and Export
The system SHALL allow users to save favorite quotes and export their collection.

**Rationale**: Users may want to revisit meaningful quotes; this feature increases value and engagement.

#### Scenario: Save favorite quote
- **GIVEN** user views a quote
- **WHEN** user clicks "Save to favorites" (heart icon)
- **THEN** quote is added to session favorites list
- **AND** visual indicator shows quote is favorited
- **AND** user can access favorites from sidebar or menu

#### Scenario: Export favorites
- **GIVEN** user has saved 3+ favorite quotes
- **WHEN** user clicks "Export favorites"
- **THEN** system generates formatted text file
- **AND** file includes all quotes with attribution
- **AND** file is downloadable as .txt or .md format

#### Scenario: Session persistence
- **GIVEN** user has favorited quotes in session
- **WHEN** user refreshes page
- **THEN** favorites are lost (no backend storage in v1)
- **AND** user is warned before refresh (optional)
- **AND** export functionality is prominently displayed

### Requirement: Quote Database Expansion
The system SHALL support easy addition of new quotes by administrators or through configuration files.

**Rationale**: Database should grow over time; easy maintenance encourages quote curation and quality improvement.

#### Scenario: Add quote via JSON file
- **GIVEN** administrator wants to add new quotes
- **WHEN** quotes are added to `data/quotes.json`
- **THEN** JSON schema is validated on load
- **AND** invalid quotes are logged and skipped
- **AND** application does not crash on malformed data

#### Scenario: Quote validation rules
- **GIVEN** new quote is being added
- **WHEN** validation is performed
- **THEN** quote text is non-empty and under 300 characters
- **AND** movie title and at least one emotion tag are present
- **AND** duplicate text is rejected
- **AND** validation errors are clearly reported

## Quote Database Schema

```json
{
  "quotes": [
    {
      "id": "unique-id",
      "text": "Quote text here",
      "movie": "Movie Title",
      "character": "Character Name",
      "year": 1999,
      "emotions": ["sadness", "hope"],
      "themes": ["perseverance", "redemption"],
      "context": "Brief context if needed",
      "genre": "drama"
    }
  ]
}
```

## Emotion Tag Mapping

| Emotion Category | Quote Themes to Match |
|------------------|----------------------|
| Sadness | Hope, comfort, resilience, healing |
| Anxiety | Courage, facing fears, calm, control |
| Anger | Justice, channeling energy, forgiveness |
| Loneliness | Connection, belonging, self-worth |
| Disappointment | Second chances, perseverance, trying again |
| Fear | Bravery, overcoming, inner strength |
| Frustration | Patience, persistence, progress |

## Initial Quote Examples

1. **Sadness/Hope**
   - "Get busy living, or get busy dying." — Andy Dufresne, The Shawshank Redemption (1994)

2. **Anxiety/Courage**
   - "Courage is not the absence of fear, but rather the judgment that something else is more important than fear." — Ambrose Redmoon (quoted in Princess Diaries, 2001)

3. **Disappointment/Perseverance**
   - "Just keep swimming." — Dory, Finding Nemo (2003)

4. **Anger/Forgiveness**
   - "Holding onto anger is like drinking poison and expecting the other person to die." — (Buddha, quoted in various films)

5. **Loneliness/Self-Worth**
   - "You is kind. You is smart. You is important." — Aibileen Clark, The Help (2011)

*(System should launch with 50-100 curated quotes)*
