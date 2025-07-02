

# ------------------------------------------------------------
# 2.  Ollama chat LLM  (start `ollama serve` separately)
# ------------------------------------------------------------
LLM_MODEL = "mistral:instruct"

# ------------------------------------------------------------
# 3. Embedding model
# ------------------------------------------------------------
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# ------------------------------------------------------------
# 4. Load PDF → split → embed in Chroma
# ------------------------------------------------------------
PDF_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "96-FDF8f7coh0ooim7NyEQ/langchain-paper.pdf"
)
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
PERSIST_DIRECTORY = "rag_db"

# ------------------------------------------------------------
# 5. Prompts
# ------------------------------------------------------------
CONDENSE_PROMPT_SYSTEM = "Turn the follow‑up user question into a standalone question. Take chat history into account."
ANSWER_PROMPT_SYSTEM = "You are a helpful agent. If unsure, answer exactly \"I don't know.\""

