"""Quote database and matching package."""
from .database import Quote, QuoteDatabase
from .matcher import QuoteMatcher

__all__ = ['Quote', 'QuoteDatabase', 'QuoteMatcher']
