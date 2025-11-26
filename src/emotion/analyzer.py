"""Emotion analysis module."""
from dataclasses import dataclass
from typing import List
import json
import aisuite as ai
from config.settings import settings


@dataclass
class EmotionResult:
    """Result of emotion analysis."""
    primary_emotion: str
    intensity: float
    secondary_emotions: List[str]
    is_crisis: bool = False


class EmotionAnalyzer:
    """Analyzes emotional content of text."""
    
    CRISIS_KEYWORDS = [
        "kill myself", "end my life", "want to die", "better off dead",
        "hurt myself", "suicide", "no point living", "can't go on",
        "end it all", "not worth living"
    ]
    
    def __init__(self, client: ai.Client):
        """Initialize emotion analyzer with AISuite client."""
        self.client = client
    
    def analyze_emotion(self, text: str) -> EmotionResult:
        """Analyze emotional content of text."""
        # Check for crisis first
        is_crisis = self._check_crisis(text)
        
        # If crisis, return immediately
        if is_crisis:
            return EmotionResult(
                primary_emotion="crisis",
                intensity=1.0,
                secondary_emotions=[],
                is_crisis=True
            )
        
        # Create emotion detection prompt
        prompt = self._create_emotion_prompt(text)
        
        try:
            # Call LLM for emotion analysis
            messages = [{"role": "user", "content": prompt}]
            response = self.client.chat.completions.create(
                model=f"{settings.LLM_PROVIDER}:{settings.MODEL_NAME}",
                messages=messages,
                temperature=0.3,  # Lower temperature for more consistent analysis
                max_tokens=200
            )
            
            # Parse response
            result_text = response.choices[0].message.content
            emotion_data = self._parse_emotion_response(result_text)
            
            return EmotionResult(**emotion_data)
            
        except Exception as e:
            print(f"Error in emotion analysis: {e}")
            # Fallback to neutral
            return EmotionResult(
                primary_emotion="neutral",
                intensity=0.5,
                secondary_emotions=[]
            )
    
    def _check_crisis(self, text: str) -> bool:
        """Check if text contains crisis keywords."""
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.CRISIS_KEYWORDS)
    
    def _create_emotion_prompt(self, text: str) -> str:
        """Create prompt for emotion detection."""
        return f"""Analyze the emotional content of the following message. Identify:
1. Primary emotion (sadness, anxiety, anger, loneliness, disappointment, fear, frustration, joy, neutral)
2. Intensity (0.0 to 1.0, where 0.0 is very mild and 1.0 is very intense)
3. Any secondary emotions (list up to 2)

Message: "{text}"

Respond in this exact JSON format (no markdown, just plain JSON):
{{
  "primary_emotion": "...",
  "intensity": 0.0,
  "secondary_emotions": []
}}"""
    
    def _parse_emotion_response(self, response: str) -> dict:
        """Parse LLM response into emotion data."""
        try:
            # Remove markdown code blocks if present
            response = response.strip()
            if response.startswith("```"):
                # Remove ```json or ``` prefix
                response = response.split("\n", 1)[1] if "\n" in response else response[3:]
            if response.endswith("```"):
                response = response.rsplit("```", 1)[0]
            
            response = response.strip()
            
            # Parse JSON
            data = json.loads(response)
            
            # Validate and normalize
            return {
                "primary_emotion": data.get("primary_emotion", "neutral"),
                "intensity": float(data.get("intensity", 0.5)),
                "secondary_emotions": data.get("secondary_emotions", []),
                "is_crisis": False
            }
        except Exception as e:
            print(f"Error parsing emotion response: {e}")
            print(f"Response was: {response}")
            # Return default
            return {
                "primary_emotion": "neutral",
                "intensity": 0.5,
                "secondary_emotions": [],
                "is_crisis": False
            }
