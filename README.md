# 📚 Virtual Research Assistant - AI-Powered Research Companion 🤖

Welcome to the Virtual Research Assistant project! This powerful tool helps researchers and students explore academic papers efficiently using the power of AI and Large Language Models.

## 🌟 Features

- 🔍 Search through ArXiv papers with intelligent query expansion
- 📊 Get AI-powered summaries of research papers
- ⚖️ Automated analysis of advantages and disadvantages
- 🎯 Clean and intuitive Streamlit interface
- 🔄 Integration with GROQ LLM for fast and accurate responses

## 🛠️ Installation

### Prerequisites
- Python 3.12
- Conda package manager
- GROQ API key ([Get it here](https://console.groq.com))

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rizwankaka/research-assistant-autogen.git
   cd research-assistant-autogen
   ```

2. **Create and activate Conda environment**
   ```bash
   conda create -p venv python==3.12 -y
   conda activate venv/
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Getting Started

1. **Set up your GROQ API key**
   - Sign up at [Groq Cloud](https://console.groq.com)
   - Generate an API key from the dashboard

2. **Run the application**
   ```bash
   streamlit run app.py
   ```

3. **Using the app**
   - Enter your GROQ API key in the sidebar
   - Type your research topic in the search bar
   - Click "Search" to get AI-analyzed research papers

## 🏗️ Project Structure

```
research-assistant/
├── app.py
├── agents.py
├── data_loader.py
├── requirements.txt
└── .streamlit/
    └── config.toml
```

## ✨ Features in Detail

- **Smart Paper Search**: Automatically expands search terms to find relevant papers
- **AI-Powered Summaries**: Get concise, relevant summaries of complex research papers
- **Advantage/Disadvantage Analysis**: Quick insights into paper strengths and limitations
- **User-Friendly Interface**: Clean, intuitive design for easy navigation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⭐ Support

If you found this project helpful, please give it a star on GitHub!

## 📞 Contact

For questions or feedback, please open an issue in the GitHub repository.

---

Made with ❤️ by RizwanRizwan for the community
