"""Sentence transformation module."""
import aisuite as ai
import os
from config.settings import settings


class SentenceTransformer:
    """Transforms negative statements into positive perspectives."""
    
    STYLE_PROMPTS = {
        "gentle": """The user said: "{original}"
They are feeling {emotion}. Gently reframe this statement into a more positive, 
hopeful perspective while validating their feelings. Be warm and compassionate.
Avoid toxic positivity. Keep it conversational and under 100 words.
Start by acknowledging their feelings, then offer the alternative perspective.""",
        
        "humorous": """The user said: "{original}"
Reframe this with light humor and playfulness, while remaining supportive. 
Add a touch of wit to help them smile. Don't mock their feelings.
Keep it under 100 words and end on an encouraging note.""",
        
        "direct": """The user said: "{original}"
Provide a straightforward, practical positive reframe. Be clear and actionable.
Focus on what they can control or do next. Keep it under 80 words.""",
        
        "cbt": """The user said: "{original}"
Using CBT principles, identify any cognitive distortion (catastrophizing, 
black-and-white thinking, overgeneralization, etc.) and provide a rational, 
evidence-based alternative perspective. Be gentle but clear. Under 100 words."""
    }
    
    def __init__(self, client: ai.Client, style: str = "gentle"):
        """Initialize transformer with AISuite client and style."""
        self.client = client
        self.style = style
        # Ensure API key is in environment
        if not os.environ.get('OPENAI_API_KEY'):
            api_key = settings.get_api_key("openai")
            if api_key:
                os.environ['OPENAI_API_KEY'] = api_key
    
    def transform(self, original: str, emotion: str = "negative") -> str:
        """Transform negative statement into positive perspective."""
        # Get prompt template for style
        prompt_template = self.STYLE_PROMPTS.get(self.style, self.STYLE_PROMPTS["gentle"])
        prompt = prompt_template.format(original=original, emotion=emotion)
        
        try:
            # Call LLM for transformation
            messages = [{"role": "user", "content": prompt}]
            response = self.client.chat.completions.create(
                model=f"{settings.LLM_PROVIDER}:{settings.MODEL_NAME}",
                messages=messages,
                temperature=0.7,
                max_tokens=300
            )
            
            transformed = response.choices[0].message.content.strip()
            return transformed
            
        except Exception as e:
            error_msg = f"Transformation error: {type(e).__name__}: {str(e)}"
            print(error_msg)
            # Return a fallback message instead of raising exception
            return f"I hear you. It's okay to feel {emotion}. You're not alone in this, and these feelings are valid. Sometimes just acknowledging how we feel is an important first step."
    
    def set_style(self, style: str):
        """Change transformation style."""
        if style in self.STYLE_PROMPTS:
            self.style = style
