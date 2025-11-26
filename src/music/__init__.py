"""Music recommendation module for emotion-based song matching."""

from .database import Song, SongDatabase
from .matcher import SongMatcher

__all__ = ["Song", "SongDatabase", "SongMatcher"]
