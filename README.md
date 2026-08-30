# 🩺 MediAssist AI

**MediAssist AI** is a medical information assistant powered by Retrieval-Augmented Generation (RAG). It uses the Gale Encyclopedia of Medicine as its knowledge base, FAISS for vector search, and Groq-hosted LLMs for generating grounded medical responses.

> ⚠️ **Educational Use Only:** MediAssist AI provides general medical information for educational purposes. It is **not** a substitute for professional medical advice, diagnosis, or treatment. For emergencies or severe symptoms, always seek immediate medical care.

---

## 🏗️ Architecture

```
medical-chatbot-main/
├── medibot.py              # Entry point (streamlit run medibot.py)
├── app/
│   ├── ui.py               # Main Streamlit UI
│   └── styles.py           # CSS styles
├── core/
│   ├── config.py           # Centralized configuration
│   └── prompts.py          # System & RAG prompt templates
├── rag/
│   └── vectorstore.py      # FAISS vectorstore management
├── services/
│   ├── llm_service.py      # Groq LLM integration
│   └── rag_service.py      # RAG chain service
├── utils/
│   └── formatters.py       # Source & text formatting
├── data/
│   └── The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf
├── vectorstore/
│   └── db_faiss/           # Pre-built FAISS vector database
├── tests/
│   └── test_config.py      # Configuration & integration tests
├── .env                    # API keys (not committed)
├── .env.example            # Template for API keys
├── .gitignore              # Git ignore rules
└── requirements.txt        # Pinned Python dependencies
```

---

## 📋 Requirements

- **Python 3.10+** (recommended: Python 3.12)
- **Groq API key** — Get one free at [console.groq.com](https://console.groq.com/)
- **~4 GB disk space** for dependencies (PyTorch, sentence-transformers)
- **~2 GB RAM** for loading embeddings and FAISS index

---

## 🚀 Installation

### 1. Clone / Download the Project

```bash
cd medical-chatbot-main
```

### 2. Create a Virtual Environment

```bash
# Using venv
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` and add your Groq API key:

```
GROQ_API_KEY=gsk_your_actual_key_here
GROQ_MODEL=qwen/qwen3.8-27b
```

> **Note:** The `HF_TOKEN` is only needed if you want to rebuild the FAISS vectorstore from scratch.

---

## ▶️ Run the Application

```bash
streamlit run medibot.py
```

The application will open in your browser at `http://localhost:8501`.

---

## 📚 Knowledge Base

MediAssist AI uses the **Gale Encyclopedia of Medicine (Second Edition)** as its medical knowledge base. The PDF is processed into chunks, embedded using `sentence-transformers/all-MiniLM-L6-v2`, and stored in a FAISS vector database.

### Pre-built Vector Database

The project includes a pre-built FAISS index at `vectorstore/db_faiss/`. No rebuilding is needed for normal operation.

### Rebuilding the Vector Database

If you need to rebuild the vectorstore (e.g., after updating the PDF):

1. Ensure you have a valid `HF_TOKEN` in your `.env` file
2. Run the rebuild script:
   ```bash
   python create_memory_for_llm.py
   ```
3. Or use the "Rebuild Vectorstore" button in the sidebar

---

## 🔑 API Keys

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | ✅ Yes | Groq API key for LLM access |
| `GROQ_MODEL` | Optional | Groq model name (default: `qwen/qwen3.8-27b`) |
| `HF_TOKEN` | Optional | HuggingFace token (only for vectorstore rebuild) |

**Where to get keys:**
- Groq: [console.groq.com](https://console.groq.com/)
- HuggingFace: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) (only if rebuilding vectorstore)

---

## 🧪 Testing

Run the test suite:

```bash
python tests/test_config.py
```

Tests verify:
- Configuration loading
- `.env` file presence
- FAISS vectorstore integrity
- Medical PDF availability
- Prompt template correctness
- Formatting utilities
- CSS styles

---

## 🛡️ Safety & Disclaimer

MediAssist AI is designed as an **educational medical information tool**:

- **Does NOT diagnose** patients or provide definitive medical conclusions
- **Does NOT prescribe** medications or recommend specific treatments
- **Does NOT fabricate** medical statistics, studies, or citations
- **Clearly indicates** when the knowledge base lacks sufficient information
- **Encourages** consulting licensed healthcare professionals
- **Recognizes** potentially emergency situations and recommends seeking immediate care

The application displays a medical disclaimer in the UI to remind users of these limitations.

---

## 📄 License

This project is for educational and research purposes.
