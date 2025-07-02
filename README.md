# Simple RAG Application

This is a simple, modularized RAG (Retrieval-Augmented Generation) application that uses LangChain and Ollama to answer questions about a document.

## Features

- **Modular Design:** The code is separated into modules for configuration, data loading, and chat logic.
- **Extensible:** Easily add new data sources or change the LLM model.
- **History-Aware:** The chatbot remembers the conversation history to answer follow-up questions.

## Getting Started

### Prerequisites

- Python 3.7+
- Ollama (and a downloaded model like `mistral:instruct`)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Ollama server:**

   ```bash
   ollama serve
   ```

### Usage

To start the chat application, run the following command:

```bash
python main.py
```

You can then ask questions about the LangChain paper, and the chatbot will do its best to answer them.

## Project Structure

```
.gitignore
app/
    __init__.py
    chat.py
    config.py
    data_loader.py
main.py
rag_db/
    ...
README.md
requirements.txt
```

- **`main.py`**: The entry point of the application.
- **`app/`**: Contains the core application logic.
  - **`config.py`**: Stores configuration variables.
  - **`data_loader.py`**: Handles loading and processing the data.
  - **`chat.py`**: Manages the chat logic and RAG chain.
- **`requirements.txt`**: Lists the Python dependencies.
- **`rag_db/`**: The directory where the Chroma vector database is stored.

## Customization

- **Change the LLM:** Modify the `LLM_MODEL` variable in `app/config.py`.
- **Use a different document:** Change the `PDF_URL` in `app/config.py`.
- **Adjust the chunking strategy:** Modify the `CHUNK_SIZE` and `CHUNK_OVERLAP` variables in `app/config.py`.
