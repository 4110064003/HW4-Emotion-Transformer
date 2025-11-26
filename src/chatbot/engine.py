"""Chatbot engine using AISuite."""
from typing import List, Dict
import aisuite as ai
from config.settings import settings


class ChatbotEngine:
    """Core conversation engine powered by AISuite."""
    
    SYSTEM_PROMPT = """You are an empathetic emotional support companion. Your role is to:
1. Listen actively and validate user feelings
2. Provide supportive, non-judgmental responses
3. Help users feel heard and understood
4. Be warm, genuine, and conversational

Important guidelines:
- Never dismiss or minimize user emotions
- Avoid toxic positivity (don't force happiness)
- Be compassionate and understanding
- Keep responses concise (2-3 sentences max)
- If user mentions crisis situation, acknowledge seriously

You are part of a larger system that also provides positive reframing and movie quotes,
so focus on being a good listener and offering emotional validation."""
    
    def __init__(self, provider: str = None, model: str = None):
        """Initialize chatbot with AISuite client."""
        self.provider = provider or settings.LLM_PROVIDER
        self.model = model or settings.MODEL_NAME
        self.conversation_history: List[Dict[str, str]] = []
        
        # Get API key
        api_key = settings.get_api_key(self.provider)
        if not api_key:
            raise ValueError(f"API key for {self.provider} not found")
        
        # Initialize AISuite client with API key in environment
        import os
        os.environ['OPENAI_API_KEY'] = api_key
        self.client = ai.Client()
        
        # Add system message to history
        self.conversation_history.append({
            "role": "system",
            "content": self.SYSTEM_PROMPT
        })
    
    def generate_response(self, message: str) -> str:
        """Generate response to user message."""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": message
        })
        
        try:
            # Call LLM
            response = self.client.chat.completions.create(
                model=f"{self.provider}:{self.model}",
                messages=self.conversation_history,
                temperature=settings.TEMPERATURE,
                max_tokens=settings.MAX_TOKENS
            )
            
            # Extract response text
            assistant_message = response.choices[0].message.content
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            print(f"Error generating response: {e}")
            error_response = "I'm here to listen. Could you tell me more about how you're feeling?"
            
            self.conversation_history.append({
                "role": "assistant",
                "content": error_response
            })
            
            return error_response
    
    def add_to_context(self, role: str, content: str):
        """Manually add message to conversation history."""
        self.conversation_history.append({
            "role": role,
            "content": content
        })
    
    def clear_context(self):
        """Reset conversation history."""
        self.conversation_history = [{
            "role": "system",
            "content": self.SYSTEM_PROMPT
        }]
    
    def get_context_length(self) -> int:
        """Get number of messages in history (excluding system message)."""
        return len(self.conversation_history) - 1
    
    def trim_context(self, max_messages: int = 10):
        """Keep only recent messages to manage context window."""
        # Always keep system message
        system_msg = self.conversation_history[0]
        
        # Keep only last N messages
        if len(self.conversation_history) > max_messages + 1:
            recent_messages = self.conversation_history[-(max_messages):]
            self.conversation_history = [system_msg] + recent_messages
