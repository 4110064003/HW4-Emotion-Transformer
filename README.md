# 🎭 Emotion Transformer - K-pop Music Therapy Chatbot

Transform negative thoughts into positive perspectives with AI-powered emotional support, K-pop music therapy, and inspirational movie quotes! 🎬🎵

Built for AIOT HW4 - A personal AI chatting machine that helps reframe negative emotions and provides K-pop music recommendations matched to your emotional state.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)
![AISuite](https://img.shields.io/badge/AISuite-Latest-green.svg)

## 🚀 Live Demo

**Try it now:** [https://7114064042-emotion-transformer.streamlit.app/](https://7114064042-emotion-transformer.streamlit.app/)

## 🌟 Features

### 🧠 Emotion Analysis
- Automatically detects emotional states (sadness, anxiety, anger, etc.)
- Measures emotion intensity (0.0 to 1.0)
- Identifies multiple emotions simultaneously
- Crisis detection with resource recommendations

### ✨ Positive Reframing
Transform negative thoughts into constructive perspectives with 4 different styles:
- **Gentle** 🤗 - Warm, compassionate, validating
- **Humorous** 😄 - Light, playful, uplifting
- **Direct** 🎯 - Straightforward, actionable, practical
- **CBT** 🧠 - Cognitive Behavioral Therapy approach

### 🎵 K-pop Music Therapy
- **50+ K-pop songs** from BTS, SEVENTEEN, IU, BLACKPINK, and more
- Emotion-based song matching algorithm
- Direct YouTube links for instant listening
- Playlist favorites system
- Export playlists as TXT files

### 🎬 Movie Quote Therapist
- 51+ curated inspirational movie quotes
- Smart emotion-to-quote matching
- Favorite quotes feature
- Export your collection as text file

### 💬 Interactive Interface
- Real-time AI responses (2-5 seconds)
- Beautiful, calming UI design
- Session management
- Usage statistics
- Mobile-friendly

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- OpenAI API key (get one at [platform.openai.com](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd HW4
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up API key**

Copy the secrets template:
```bash
copy .streamlit\secrets.toml.example .streamlit\secrets.toml
```

Edit `.streamlit/secrets.toml` and add your API key:
```toml
OPENAI_API_KEY = "your-actual-api-key-here"
```

4. **Run the app**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 How to Use

1. **Share your thoughts**: Type negative feelings or thoughts in the chat input
2. **See emotion analysis**: View detected emotions with intensity indicators
3. **Get positive reframe**: Read the transformed positive perspective
4. **Browse movie quotes**: Enjoy 2-3 inspirational quotes matched to your emotion
5. **Interact**:
   - ❤️ Save favorite quotes
   - 🔄 Try different quotes
   - ✨ Reframe differently
   - 🆕 Start new conversation

## 🎯 Example Usage

**Input**: "I failed my exam, I'm so stupid"

**Emotion**: Disappointment (0.8)

**Transformation**: "This exam revealed areas that need more focus - it's a learning opportunity, not a measure of your intelligence. You have the capacity to improve."

**Movie Quote**: *"Why do we fall? So we can learn to pick ourselves up."* — Batman Begins

## 🏗️ Project Structure

```
HW4/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
│
├── .streamlit/
│   ├── config.toml                 # Streamlit configuration
│   └── secrets.toml.example        # API key template
│
├── config/
│   └── settings.py                 # App configuration
│
├── data/
│   └── quotes.json                 # 50+ movie quotes database
│
├── src/
│   ├── chatbot/
│   │   └── engine.py               # AISuite chatbot core
│   ├── emotion/
│   │   ├── analyzer.py             # Emotion detection
│   │   └── transformer.py          # Sentence transformation
│   ├── quotes/
│   │   ├── database.py             # Quote loader
│   │   └── matcher.py              # Emotion-quote matching
│   └── ui/
│       ├── components.py           # UI components
│       └── styles.py               # Custom CSS
│
└── openspec/                       # Project documentation
    ├── project.md
    └── changes/
        └── add-emotion-transformer-chatbot/
            ├── proposal.md
            ├── tasks.md
            ├── design.md
            └── specs/
```

## 🔧 Configuration

### Transformation Styles

Change style in the sidebar:
- **Gentle**: Warm, compassionate validation
- **Humorous**: Light-hearted, playful
- **Direct**: Practical, actionable advice
- **CBT**: Cognitive Behavioral Therapy approach

### Settings

Edit `config/settings.py` to customize:
- LLM model (`gpt-4o-mini`, `gpt-4`, etc.)
- Temperature, max tokens
- Rate limits
- UI theme colors

## 🌐 Deployment to Streamlit Cloud

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit: Emotion Transformer chatbot"
git remote add origin <your-repo-url>
git push -u origin main
```

2. **Deploy on Streamlit Cloud**
- Go to [share.streamlit.io](https://share.streamlit.io)
- Sign in with GitHub
- Click "New app"
- Select your repository
- Main file: `app.py`
- Click "Advanced settings" → "Secrets"
- Add: `OPENAI_API_KEY = "your-key-here"`
- Click "Deploy"

3. **Share your app!**
Your app will be live at: `https://[your-app-name].streamlit.app`

## 📊 Features Summary

| Feature | Status |
|---------|--------|
| Emotion Detection | ✅ |
| Positive Reframing | ✅ |
| Movie Quotes (50+) | ✅ |
| Multiple Transformation Styles | ✅ |
| Crisis Detection | ✅ |
| Favorites System | ✅ |
| Export Quotes | ✅ |
| Session Management | ✅ |
| Rate Limiting | ✅ |
| Mobile Responsive | ✅ |

## 🛡️ Safety & Privacy

- **No data storage**: All conversations exist only in your browser session
- **Crisis detection**: Automatically detects crisis language and provides resources
- **Rate limiting**: 50 messages per session to prevent abuse
- **Disclaimer**: Clear notice that this doesn't replace professional help
- **API key security**: Never commit secrets to git

## 🎓 Academic Context

This project is created for **AIOT HW4** at National Taipei University of Technology.

**Learning Objectives Met**:
- ✅ AI integration with AISuite
- ✅ Natural language processing
- ✅ User interface design with Streamlit
- ✅ Python project structure and modularity
- ✅ Cloud deployment
- ✅ Git version control
- ✅ Documentation and presentation

## 📝 Tech Stack

- **Language**: Python 3.9+
- **AI Framework**: AISuite (multi-LLM support)
- **LLM Provider**: OpenAI GPT-4o-mini
- **Web Framework**: Streamlit
- **Deployment**: Streamlit Cloud
- **Version Control**: Git/GitHub

## 🤝 Contributing

This is a personal academic project, but suggestions are welcome!

## 📄 License

MIT License - Feel free to use this for learning purposes

## 🙏 Acknowledgments

- Movie quotes curated from popular films
- AISuite library for unified LLM access
- Streamlit for the amazing web framework
- OpenAI for GPT models
- NTUT AIOT course instructors

## 💡 Future Enhancements

- [ ] User accounts with persistent history
- [ ] Multi-language support
- [ ] Voice input/output
- [ ] More quote sources (books, speeches)
- [ ] Emotion trend analytics
- [ ] Community quote contributions
- [ ] Mobile native app

## 📧 Contact

For questions about this project:
- GitHub Issues: [Create an issue](link-to-issues)
- Course: AIOT HW4

---

**Remember**: This is a supportive tool, not a replacement for professional mental health care. If you're experiencing a crisis, please contact:
- **988 Suicide & Crisis Lifeline**: Call or text 988
- **Crisis Text Line**: Text HOME to 741741

Made with ❤️ for emotional wellness and AI learning
