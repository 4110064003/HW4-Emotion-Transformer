"""Song matching module for music recommendations."""
from typing import List, Set
import random
from .database import Song, SongDatabase


class SongMatcher:
    """Matches emotions to relevant K-pop songs."""
    
    # Map emotions to compatible emotion tags
    EMOTION_MAPPINGS = {
        "sadness": ["sadness", "heartbreak", "bittersweet", "longing"],
        "anxiety": ["anxiety", "fear", "worry", "stress", "shyness"],
        "anger": ["anger", "frustration", "empowerment"],
        "loneliness": ["loneliness", "isolation", "longing"],
        "disappointment": ["disappointment", "defeat", "acceptance"],
        "fear": ["fear", "anxiety", "vulnerability"],
        "frustration": ["frustration", "anger", "determination"],
        "joy": ["joy", "happiness", "excitement", "confidence"],
        "neutral": ["hope", "comfort", "peace"]
    }
    
    def __init__(self, database: SongDatabase):
        """Initialize matcher with song database."""
        self.database = database
    
    def match_songs(self, emotion: str, count: int = 3, 
                    exclude_ids: Set[str] = None) -> List[Song]:
        """Match and rank songs for given emotion."""
        if exclude_ids is None:
            exclude_ids = set()
        
        # Get compatible emotion tags
        emotion_tags = self.EMOTION_MAPPINGS.get(emotion, [emotion])
        
        # Collect matching songs
        candidates = []
        for tag in emotion_tags:
            songs = self.database.get_songs_by_emotion(tag)
            candidates.extend(songs)
        
        # If no matches, use fallback general songs
        if not candidates:
            candidates = self._get_fallback_songs()
        
        # Remove duplicates and excluded songs
        seen_ids = set()
        unique_candidates = []
        for song in candidates:
            if song.id not in seen_ids and song.id not in exclude_ids:
                seen_ids.add(song.id)
                unique_candidates.append(song)
        
        # Rank songs
        ranked = self._rank_songs(unique_candidates, emotion)
        
        # Return top N
        return ranked[:count]
    
    def get_another_song(self, emotion: str, shown_ids: Set[str]) -> Song:
        """Get next song not in shown_ids."""
        matches = self.match_songs(emotion, count=10, exclude_ids=shown_ids)
        
        if matches:
            return matches[0]
        
        # If all exhausted, allow repeats but notify
        all_matches = self.match_songs(emotion, count=1, exclude_ids=set())
        return all_matches[0] if all_matches else self._get_generic_song()
    
    def _rank_songs(self, songs: List[Song], emotion: str) -> List[Song]:
        """Rank songs by relevance."""
        scored_songs = []
        
        for song in songs:
            score = 0
            
            # Exact emotion match
            if emotion in song.emotions:
                score += 10
            
            # Recent songs (favor newer releases)
            if song.year >= 2020:
                score += 3
            if song.year >= 2023:
                score += 2
            
            # Artist diversity (slightly prefer major artists)
            major_artists = ["BTS", "SEVENTEEN", "IU", "BLACKPINK"]
            if song.artist in major_artists:
                score += 2
            
            scored_songs.append((score, song))
        
        # Sort by score descending
        scored_songs.sort(key=lambda x: x[0], reverse=True)
        
        # Add some randomness to top results for variety
        top_songs = [s for _, s in scored_songs]
        if len(top_songs) > 5:
            # Shuffle top 5 to add variety
            top_5 = top_songs[:5]
            rest = top_songs[5:]
            random.shuffle(top_5)
            return top_5 + rest
        
        return top_songs
    
    def _get_fallback_songs(self) -> List[Song]:
        """Get general uplifting songs as fallback."""
        # Return songs with broad appeal
        all_songs = self.database.get_all_songs()
        fallback = [s for s in all_songs if "joy" in s.emotions or "hope" in s.emotions]
        return fallback if fallback else all_songs[:10]
    
    def _get_generic_song(self) -> Song:
        """Get a generic uplifting song as last resort."""
        all_songs = self.database.get_all_songs()
        if all_songs:
            return random.choice(all_songs)
        
        # Hardcoded fallback if database is empty
        from .database import Song
        return Song(
            id="fallback-1",
            title="Dynamite",
            artist="BTS",
            emotions=["joy"],
            theme="Uplifting energy and joy",
            genre="K-pop Disco",
            year=2020,
            spotify_url="https://open.spotify.com/track/5QDLhrAOJJdNAmCTJ8xMyW",
            youtube_url="https://www.youtube.com/watch?v=gdZLi9oWNZg",
            why_it_helps="充滿活力的節奏帶來快樂和正能量"
        )
