"""Movie quotes database module."""
import json
from dataclasses import dataclass
from typing import List, Optional
from pathlib import Path


@dataclass
class Quote:
    """Movie quote data structure."""
    id: str
    text: str
    movie: str
    character: str
    year: int
    emotions: List[str]
    themes: List[str]
    genre: str


class QuoteDatabase:
    """Manages movie quotes database."""
    
    def __init__(self, quotes_file: str):
        """Load quotes from JSON file."""
        self.quotes: List[Quote] = []
        self._load_quotes(quotes_file)
        self._index_by_emotion()
    
    def _load_quotes(self, quotes_file: str):
        """Load and validate quotes from JSON."""
        try:
            file_path = Path(quotes_file)
            if not file_path.exists():
                print(f"Warning: Quotes file not found: {quotes_file}")
                return
            
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for quote_data in data.get('quotes', []):
                try:
                    quote = Quote(**quote_data)
                    self.quotes.append(quote)
                except Exception as e:
                    print(f"Error loading quote {quote_data.get('id', 'unknown')}: {e}")
            
            print(f"Loaded {len(self.quotes)} quotes from database")
            
        except Exception as e:
            print(f"Error loading quotes file: {e}")
    
    def _index_by_emotion(self):
        """Create emotion-to-quotes index for faster lookup."""
        self.emotion_index = {}
        for quote in self.quotes:
            for emotion in quote.emotions:
                if emotion not in self.emotion_index:
                    self.emotion_index[emotion] = []
                self.emotion_index[emotion].append(quote)
    
    def get_all_quotes(self) -> List[Quote]:
        """Return all quotes."""
        return self.quotes
    
    def get_quotes_by_emotion(self, emotion: str) -> List[Quote]:
        """Get quotes filtered by emotion tag."""
        return self.emotion_index.get(emotion, [])
    
    def get_quote_by_id(self, quote_id: str) -> Optional[Quote]:
        """Get specific quote by ID."""
        for quote in self.quotes:
            if quote.id == quote_id:
                return quote
        return None
