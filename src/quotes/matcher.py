"""Quote matching module."""
from typing import List, Set
import random
from .database import Quote, QuoteDatabase


class QuoteMatcher:
    """Matches emotions to relevant movie quotes."""
    
    # Map emotions to compatible emotion tags
    EMOTION_MAPPINGS = {
        "sadness": ["sadness", "despair", "hopelessness", "loss"],
        "anxiety": ["anxiety", "fear", "worry", "stress", "uncertainty"],
        "anger": ["anger", "frustration", "bitterness"],
        "loneliness": ["loneliness", "isolation"],
        "disappointment": ["disappointment", "failure", "defeat", "regret"],
        "fear": ["fear", "anxiety", "scared"],
        "frustration": ["frustration", "anger", "impatience"],
        "joy": ["joy", "happiness"],
        "neutral": []  # Will use general inspirational quotes
    }
    
    def __init__(self, database: QuoteDatabase):
        """Initialize matcher with quote database."""
        self.database = database
    
    def match_quotes(self, emotion: str, count: int = 3, 
                    exclude_ids: Set[str] = None) -> List[Quote]:
        """Match and rank quotes for given emotion."""
        if exclude_ids is None:
            exclude_ids = set()
        
        # Get compatible emotion tags
        emotion_tags = self.EMOTION_MAPPINGS.get(emotion, [emotion])
        
        # Collect matching quotes
        candidates = []
        for tag in emotion_tags:
            quotes = self.database.get_quotes_by_emotion(tag)
            candidates.extend(quotes)
        
        # If no matches, use fallback general quotes
        if not candidates:
            candidates = self._get_fallback_quotes()
        
        # Remove duplicates and excluded quotes
        seen_ids = set()
        unique_candidates = []
        for quote in candidates:
            if quote.id not in seen_ids and quote.id not in exclude_ids:
                seen_ids.add(quote.id)
                unique_candidates.append(quote)
        
        # Rank quotes
        ranked = self._rank_quotes(unique_candidates, emotion)
        
        # Return top N
        return ranked[:count]
    
    def get_another_quote(self, emotion: str, shown_ids: Set[str]) -> Quote:
        """Get next quote not in shown_ids."""
        matches = self.match_quotes(emotion, count=10, exclude_ids=shown_ids)
        
        if matches:
            return matches[0]
        
        # If all exhausted, allow repeats but notify
        all_matches = self.match_quotes(emotion, count=1, exclude_ids=set())
        return all_matches[0] if all_matches else self._get_generic_quote()
    
    def _rank_quotes(self, quotes: List[Quote], emotion: str) -> List[Quote]:
        """Rank quotes by relevance."""
        scored_quotes = []
        
        for quote in quotes:
            score = 0
            
            # Exact emotion match
            if emotion in quote.emotions:
                score += 10
            
            # Recent/popular movies (subjective, but let's favor more recent)
            if quote.year >= 2000:
                score += 3
            if quote.year >= 2010:
                score += 2
            
            # Genre diversity (slightly prefer animations and dramas)
            if quote.genre in ["animation", "drama"]:
                score += 2
            
            scored_quotes.append((score, quote))
        
        # Sort by score descending
        scored_quotes.sort(key=lambda x: x[0], reverse=True)
        
        # Add some randomness to top results for variety
        top_quotes = [q for _, q in scored_quotes]
        if len(top_quotes) > 5:
            # Shuffle top 5 to add variety
            top_5 = top_quotes[:5]
            rest = top_quotes[5:]
            random.shuffle(top_5)
            return top_5 + rest
        
        return top_quotes
    
    def _get_fallback_quotes(self) -> List[Quote]:
        """Get general inspirational quotes as fallback."""
        # Return quotes with broad appeal
        all_quotes = self.database.get_all_quotes()
        fallback = [q for q in all_quotes if "hope" in q.themes or "perseverance" in q.themes]
        return fallback if fallback else all_quotes[:10]
    
    def _get_generic_quote(self) -> Quote:
        """Get a generic inspirational quote as last resort."""
        all_quotes = self.database.get_all_quotes()
        if all_quotes:
            return random.choice(all_quotes)
        
        # Hardcoded fallback if database is empty
        from .database import Quote
        return Quote(
            id="fallback-1",
            text="Keep going. You're doing better than you think.",
            movie="General Wisdom",
            character="Life",
            year=2024,
            emotions=["all"],
            themes=["encouragement"],
            genre="wisdom"
        )
