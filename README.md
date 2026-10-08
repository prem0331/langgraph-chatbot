# LangGraph Chatbot with SQLite Persistence

A conversational AI chatbot built with **LangGraph**, **Groq LLM**, and **Streamlit**, featuring persistent conversation history using SQLite.

## Features

- **LangGraph** for stateful conversation management
- **Groq (GPT-OSS-20B)** for fast, high-quality LLM responses
- **Streamlit** for clean, interactive web UI
- **SQLite Persistence** via `langgraph-checkpoint-sqlite` - conversations survive restarts
- **Streaming Responses** - tokens appear in real-time
- **Multi-thread Conversations** - switch between different chat threads
- **Thread Management** - create new chats, view history

## Project Structure

```
langgraph-chatbot/
├── chatbot_backend.py    # LangGraph workflow, SQLite checkpointer, Groq LLM
├── chatbot_frontend.py   # Streamlit UI, thread management, streaming
├── chatbot.db            # SQLite database (auto-created)
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Quick Start

### Prerequisites

- Python 3.10+
- Groq API key (get one at [console.groq.com](https://console.groq.com))

### Installation

```bash
# Clone or navigate to project
cd langgraph-chatbot

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Set your Groq API key in `chatbot_backend.py`:

```python
llm = ChatGroq(
    api_key="YOUR_GROQ_API_KEY_HERE",  # Replace with your key
    model="openai/gpt-oss-20b",
    temperature=0.7,
    max_tokens=1024,
    streaming=True,
)
```

### Run the App

```bash
streamlit run chatbot_frontend.py
```

Open http://localhost:8501 in your browser.

## Usage

1. **Start Chatting** - Type messages in the chat input
2. **New Chat** - Click "New chat" in sidebar to start fresh conversation
3. **Switch Threads** - Click any thread ID in sidebar to resume that conversation
4. **Persistence** - All conversations saved to `chatbot.db` automatically

## Dependencies

- `streamlit` - Web UI framework
- `langgraph` - Stateful graph workflows
- `langgraph-checkpoint-sqlite` - SQLite persistence for LangGraph
- `langchain-groq` - Groq LLM integration
- `langchain-core` - Core LangChain abstractions
- `sqlite3` - Built-in Python SQLite support

## Architecture

```
User Input → Streamlit Frontend → LangGraph Workflow → Groq LLM
                ↓                        ↓
         Session State            SQLite Checkpointer
                ↓                        ↓
         Display Messages ←────────── Chat History
```

## API Reference

### `chatbot_backend.py`

- `chatbot` - Compiled LangGraph workflow with SQLite checkpointer
- `retrive_all_threads()` - Get all conversation thread IDs from database
- `chatstate` - TypedDict defining message state structure

### `chatbot_frontend.py`

- `retrive_msgs(thread_id)` - Load messages for a specific thread
- `generate_thread_id()` - Create unique thread identifier
- `reset()` - Start new conversation thread

## License

MIT License - Feel free to use and modify.