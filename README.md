# LangChain Updated

> A modern, production-ready implementation showcasing expertise in building scalable, intelligent applications with Large Language Models (LLMs).

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Overview

**LangChain Updated** is a comprehensive demonstration of full-stack development with modern AI/ML technologies. This project showcases how to build scalable, intelligent applications that leverage LLMs, advanced prompt engineering, vector databases, and RAG (Retrieval Augmented Generation) capabilities. It serves as both a learning resource and a production-ready template for enterprise AI applications.

## 🚀 Key Features

- **🤖 LLM Integration**: Seamless integration with OpenAI, Hugging Face, and other major LLM providers
- **✍️ Prompt Engineering**: Advanced prompt templates and sophisticated chain composition patterns
- **💾 Memory Management**: Intelligent conversation history management with context awareness
- **🔍 Retrieval Augmented Generation (RAG)**: Document processing and semantic search capabilities
- **🏗️ Modular Architecture**: Clean, reusable components following SOLID principles
- **⚙️ Production-Ready**: Enterprise-grade error handling, logging, and monitoring
- **🧪 Fully Tested**: Comprehensive unit and integration tests
- **📚 Well-Documented**: Clear documentation and code examples

## 💡 Technical Highlights

### Core Capabilities
- **Intelligent Agents**: Build autonomous agents that can reason and take actions
- **Multi-Source RAG**: Combine multiple data sources with intelligent retrieval
- **Streaming Support**: Real-time response streaming for better UX
- **Memory Optimization**: Efficient conversation management and context windows
- **Custom Chains**: Build complex workflows with chained LLM operations

### Technical Skills Demonstrated
| Area | Technologies |
|------|--------------|
| **Backend** | Python 3.8+, OOP, Async/Await, REST APIs |
| **AI/ML** | LLMs, Embeddings, Vector Databases, NLP |
| **Software Engineering** | Design Patterns, Testing, CI/CD, Documentation |
| **Architecture** | Microservices, Scalability, Production Deployment |

## 🛠️ Tech Stack

```
┌─────────────────────────────────────────────┐
│  Core Framework: LangChain                  │
├─────────────────────────────────────────────┤
│  Language:          Python 3.8+             │
│  LLM Providers:     OpenAI, HuggingFace     │
│  Vector DB:        Pinecone, FAISS, etc.    │
│  Data Processing:  Pandas, NumPy            │
│  Testing:          pytest, unittest         │
│  Async Runtime:    AsyncIO                  │
│  Logging:          Python logging           │
└─────────────────────────────────────────────┘
```

## 📁 Project Structure

```
langchainupdated/
├── src/
│   ├── chains/              # LLM chain compositions
│   ├── agents/              # Autonomous agent implementations
│   ├── memory/              # Conversation and context management
│   ├── rag/                 # RAG pipeline and retrieval logic
│   ├── prompts/             # Prompt templates and engineering
│   ├── embeddings/          # Embedding integrations
│   └── utils/               # Utility functions and helpers
├── tests/
│   ├── unit/                # Unit tests
│   └── integration/         # Integration tests
├── examples/
│   ├── basic_chain.py       # Simple chain examples
│   ├── rag_pipeline.py      # RAG implementation example
│   ├── agent_example.py     # Agent creation example
│   └── memory_example.py    # Memory management example
├── config/
│   ├── settings.py          # Configuration management
│   └── .env.example         # Environment variables template
├── docs/
│   ├── SETUP.md             # Installation and setup guide
│   ├── USAGE.md             # Usage examples and tutorials
│   └── API.md               # API reference documentation
├── requirements.txt         # Python dependencies
├── setup.py                 # Package installation
├── pytest.ini              # Testing configuration
└── README.md               # This file
```

## 🚦 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager
- API keys for LLM providers (OpenAI, HuggingFace, etc.)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Bhakti1998/langchainupdated.git
   cd langchainupdated
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp config/.env.example .env
   # Edit .env with your API keys and configuration
   ```

5. **Run tests** (optional)
   ```bash
   pytest tests/
   ```

### Basic Usage

```python
from langchain.llms import OpenAI
from langchainupdated.chains import SimpleChain

# Initialize LLM
llm = OpenAI(temperature=0.7)

# Create and run a simple chain
chain = SimpleChain(llm=llm)
result = chain.run("What is the capital of France?")
print(result)
```

For more detailed examples, see the [examples/](examples/) directory and [USAGE.md](docs/USAGE.md).

## 📚 Documentation

- **[Setup Guide](docs/SETUP.md)** - Detailed installation and configuration instructions
- **[Usage Guide](docs/USAGE.md)** - Comprehensive usage examples and tutorials
- **[API Reference](docs/API.md)** - Complete API documentation
- **[Architecture](docs/ARCHITECTURE.md)** - System design and architecture overview

## 💻 Example Use Cases

### 1. Question Answering System
```python
from langchainupdated.rag import RAGPipeline

rag = RAGPipeline(vector_db="pinecone")
answer = rag.query("What is LangChain?")
```

### 2. Multi-Turn Conversation
```python
from langchainupdated.memory import ConversationManager

chat = ConversationManager(memory_type="buffer")
response = chat.ask("Hello! How are you?")
```

### 3. Intelligent Agent
```python
from langchainupdated.agents import Agent

agent = Agent(tools=["search", "calculator"])
result = agent.execute("What is 25 * 4 plus the current date?")
```

## 🧪 Testing

Run the full test suite:

```bash
# All tests
pytest

# Specific test file
pytest tests/unit/test_chains.py

# With coverage report
pytest --cov=src tests/
```

## 🔐 Security Considerations

- **API Keys**: Never commit API keys. Use environment variables and `.env` files (added to `.gitignore`)
- **Dependencies**: Regularly update dependencies to patch security vulnerabilities
- **Input Validation**: All user inputs are validated before processing
- **Error Handling**: Sensitive information is not exposed in error messages

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure:
- Code follows PEP 8 style guidelines
- All tests pass
- New features include appropriate tests
- Documentation is updated

## 📋 Requirements

Key dependencies:
- `langchain>=0.0.200` - Core LangChain framework
- `openai>=0.27.0` - OpenAI API integration
- `pinecone-client>=2.2.0` - Vector database
- `python-dotenv>=0.21.0` - Environment configuration
- `pytest>=7.0.0` - Testing framework

See [requirements.txt](requirements.txt) for the complete list.

## 📈 Performance & Scalability

- **Async Support**: Full async/await support for concurrent operations
- **Caching**: Built-in response caching to reduce API calls
- **Batch Processing**: Support for processing multiple queries efficiently
- **Connection Pooling**: Optimized database connections

## 🐛 Troubleshooting

### Common Issues

**Issue**: "API Key not found"
- **Solution**: Ensure your `.env` file contains the required API keys

**Issue**: "Vector database connection failed"
- **Solution**: Check your Pinecone credentials and network connectivity

**Issue**: "Out of context window"
- **Solution**: Implement memory management or reduce input size

For more help, see [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Bhakti1998**
- GitHub: [@Bhakti1998](https://github.com/Bhakti1998)

## 🙏 Acknowledgments

- LangChain community and documentation
- OpenAI and other LLM providers
- Contributors and maintainers

## 📞 Support & Feedback

- **Issues**: Report bugs or feature requests on [GitHub Issues](https://github.com/Bhakti1998/langchainupdated/issues)
- **Discussions**: Join community discussions on [GitHub Discussions](https://github.com/Bhakti1998/langchainupdated/discussions)
- **Email**: Contact via GitHub profile

---

**Made with ❤️ by Bhakti1998**

⭐ If you find this project helpful, please consider giving it a star!
