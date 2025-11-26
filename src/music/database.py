"""Song database module for music recommendations."""
import json
from dataclasses import dataclass
from typing import List, Optional
from pathlib import Path


@dataclass
class Song:
    """K-pop song data structure."""
    id: str
    title: str
    artist: str
    emotions: List[str]
    theme: str
    genre: str
    year: int
    spotify_url: str
    youtube_url: str
    why_it_helps: str


class SongDatabase:
    """Manages songs database."""
    
    def __init__(self, songs_file: str):
        """Load songs from JSON file."""
        self.songs: List[Song] = []
        self._load_songs(songs_file)
        self._index_by_emotion()
    
    def _load_songs(self, songs_file: str):
        """Load and validate songs from JSON."""
        try:
            file_path = Path(songs_file)
            if not file_path.exists():
                print(f"Warning: Songs file not found: {songs_file}")
                return
            
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Handle both list format and dict with 'songs' key
            songs_data = data if isinstance(data, list) else data.get('songs', [])
            
            for song_data in songs_data:
                try:
                    song = Song(**song_data)
                    self.songs.append(song)
                except Exception as e:
                    print(f"Error loading song {song_data.get('id', 'unknown')}: {e}")
            
            print(f"Loaded {len(self.songs)} songs from database")
            
        except Exception as e:
            print(f"Error loading songs file: {e}")
    
    def _index_by_emotion(self):
        """Create emotion-to-songs index for faster lookup."""
        self.emotion_index = {}
        for song in self.songs:
            for emotion in song.emotions:
                if emotion not in self.emotion_index:
                    self.emotion_index[emotion] = []
                self.emotion_index[emotion].append(song)
    
    def get_all_songs(self) -> List[Song]:
        """Return all songs."""
        return self.songs
    
    def get_songs_by_emotion(self, emotion: str) -> List[Song]:
        """Get songs filtered by emotion tag."""
        return self.emotion_index.get(emotion, [])
    
    def get_song_by_id(self, song_id: str) -> Optional[Song]:
        """Get specific song by ID."""
        for song in self.songs:
            if song.id == song_id:
                return song
        return None
