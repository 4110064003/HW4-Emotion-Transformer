# Project Context

## Purpose
Personal AI chatting machine built for AIOT HW4. This project creates an interactive chatbot interface using AISuite library, deployed on Streamlit for web access and hosted on GitHub for version control and sharing.

## Tech Stack
- **Language**: Python 3.x
- **AI Framework**: AISuite (unified interface for multiple LLM providers)
- **Web Framework**: Streamlit (for UI and deployment)
- **Version Control**: Git/GitHub
- **Deployment**: Streamlit Cloud

## Project Conventions

### Code Style
- Follow PEP 8 Python style guide
- Use snake_case for functions and variables
- Use PascalCase for class names
- Maximum line length: 88 characters (Black formatter standard)
- Use type hints where applicable
- Include docstrings for all functions and classes

### Architecture Patterns
- **Separation of Concerns**: Keep UI logic (Streamlit) separate from business logic (AISuite integration)
- **Configuration Management**: Use environment variables or config files for API keys
- **Modular Design**: Break down functionality into reusable modules
- **Session State**: Leverage Streamlit's session state for conversation history

### Testing Strategy
- Manual testing through Streamlit interface
- Test with different AISuite providers (OpenAI, Anthropic, etc.)
- Validate conversation flow and history persistence
- Test error handling for API failures

### Git Workflow
- **Main branch**: Production-ready code for Streamlit deployment
- **Feature branches**: `feature/[feature-name]` for new capabilities
- **Commit messages**: Use conventional commits format
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation
  - `chore:` for maintenance tasks

## Domain Context
- **AIOT Course Project**: This is a homework assignment (HW4) focusing on AI integration
- **Chatbot Domain**: Conversational AI, natural language processing
- **User Experience**: Simple, intuitive interface for chatting with AI
- **Multi-Provider Support**: Should work with various LLM providers via AISuite

## Important Constraints
- **API Key Management**: Must securely handle API keys (use Streamlit secrets)
- **Cost Awareness**: Monitor API usage to avoid unexpected charges
- **Streamlit Limitations**: Consider Streamlit Cloud's resource limits
- **Academic Context**: Must meet course assignment requirements
- **Public Repository**: Code will be public on GitHub (no hardcoded secrets)

## External Dependencies
- **AISuite Library**: Unified interface for LLM providers
- **LLM Providers**: OpenAI, Anthropic Claude, Google Gemini, or others via AISuite
- **Streamlit Cloud**: For hosting and deployment
- **GitHub**: For repository hosting and version control
