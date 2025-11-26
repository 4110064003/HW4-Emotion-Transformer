"""Image generation module for comfort images."""
from typing import Optional
import urllib.parse
import requests


class ComfortImageGenerator:
    """Generates comforting images based on emotions using Unsplash."""
    
    # Mapping emotions to Unsplash search queries
    UNSPLASH_QUERIES = {
        "sadness": "peaceful,sunset,ocean,calm,hope",
        "anxiety": "forest,nature,calm,tranquil,peace",
        "anger": "mountain,waterfall,serene,peaceful,nature",
        "loneliness": "cozy,warm,home,comfort,peaceful",
        "disappointment": "sunrise,hope,new-beginning,dawn,optimism",
        "fear": "safe,cozy,shelter,warm,security",
        "frustration": "zen,garden,meditation,calm,balance",
        "joy": "flowers,happiness,vibrant,sunny,cheerful",
        "neutral": "landscape,peaceful,nature,harmony,calm"
    }
    
    def __init__(self, client=None):
        """Initialize image generator."""
        # Client parameter kept for compatibility but not used
        pass
    
    def generate_comfort_image(self, emotion: str) -> Optional[str]:
        """
        Generate a comforting image URL based on emotion.
        Returns Unsplash image URL.
        """
        return self.get_fallback_image_url(emotion)
    
    def get_fallback_image_url(self, emotion: str) -> str:
        """Get an image URL from Unsplash based on emotion."""
        query = self.UNSPLASH_QUERIES.get(emotion.lower(), self.UNSPLASH_QUERIES["neutral"])
        # Use Unsplash Source API for beautiful, curated images
        # Adding a random seed based on emotion to get consistent but varied images
        seed = hash(emotion) % 1000
        return f"https://source.unsplash.com/1024x768/?{query}&sig={seed}"


class MoviePosterFetcher:
    """Fetches movie posters from TMDB (The Movie Database)."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize poster fetcher with optional TMDB API key."""
        self.api_key = api_key
        self.tmdb_base_url = "https://api.themoviedb.org/3"
        self.tmdb_image_base = "https://image.tmdb.org/t/p/w500"
        
    def search_movie_poster(self, movie_title: str, year: Optional[int] = None) -> Optional[str]:
        """
        Search for movie poster URL using TMDB API.
        Returns poster URL or fallback if not found or API key missing.
        """
        if not self.api_key:
            # Try OMDb API as fallback (free, no registration needed for basic use)
            return self._search_omdb(movie_title, year)
        
        try:
            # Search for movie on TMDB
            search_url = f"{self.tmdb_base_url}/search/movie"
            params = {
                "api_key": self.api_key,
                "query": movie_title
            }
            if year:
                params["year"] = year
            
            response = requests.get(search_url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get("results") and len(data["results"]) > 0:
                poster_path = data["results"][0].get("poster_path")
                if poster_path:
                    return f"{self.tmdb_image_base}{poster_path}"
            
            # If no poster found, try OMDb as fallback
            return self._search_omdb(movie_title, year)
            
        except Exception as e:
            print(f"Error fetching from TMDB: {e}")
            return self._search_omdb(movie_title, year)
    
    def _search_omdb(self, movie_title: str, year: Optional[int] = None) -> str:
        """
        Search OMDb API for movie poster.
        Note: OMDb now requires personal API key, so we'll use fallback with movie poster image search.
        """
        try:
            # Try with a working OMDb API key if user has one
            # For demo, we'll go straight to fallback with a movie-themed image
            
            # Use a movie poster search from a different source
            # TMDb has a public image CDN we can use for common movies
            return self._search_tmdb_public(movie_title, year)
            
        except Exception as e:
            print(f"Error fetching from OMDb: {e}")
            return self.get_fallback_poster_url(movie_title)
    
    def _search_tmdb_public(self, movie_title: str, year: Optional[int] = None) -> str:
        """
        Try to fetch movie poster from TMDb without API key using title-based URL.
        This is a workaround for demo purposes.
        """
        # For well-known movies, we can construct poster URLs
        # Otherwise fallback to a nice placeholder
        
        # Clean movie title for URL
        clean_title = movie_title.lower().replace(" ", "-").replace(":", "").replace("'", "")
        
        # Try IMDb poster proxy (free service)
        try:
            # Use Movie of the Night API (free, no key needed)
            api_url = f"https://api.movieofthenight.com/api/v1/movies/search"
            params = {"title": movie_title}
            
            response = requests.get(api_url, params=params, timeout=3)
            if response.status_code == 200:
                data = response.json()
                if data and len(data) > 0 and "posterUrl" in data[0]:
                    return data[0]["posterUrl"]
        except:
            pass
        
        # Fallback to styled placeholder
        return self.get_fallback_poster_url(movie_title)
    
    def get_fallback_poster_url(self, movie_title: str) -> str:
        """Get a fallback image with movie-themed aesthetic."""
        # Clean and encode the movie title
        clean_title = movie_title.strip()
        
        # Use DiceBear API for movie-themed avatars (free, reliable)
        # Or use a movie poster template image
        encoded_title = urllib.parse.quote(clean_title)
        
        # Create a movie poster styled placeholder using placeholder.com
        # Format: 400x600 (standard movie poster ratio 2:3)
        seed = abs(hash(movie_title)) % 1000
        
        # Use a more cinematic placeholder with gradient
        # Alternative: use a service that generates film strip themed images
        return f"https://placehold.co/400x600/1a1a2e/eee?text={encoded_title}&font=roboto"


