"""
MediAssist AI - Centralized Configuration
Loads environment variables and provides application-wide settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# --- API Keys (never log or display these) ---
GROQ_API_KEY: str = os.environ.get("GROQ_API_KEY", "")
HF_TOKEN: str = os.environ.get("HF_TOKEN", "")

# --- Model Configuration ---
GROQ_MODEL: str = os.environ.get("GROQ_MODEL", "qwen/qwen3.8-27b")
TEMPERATURE: float = 0.1
MAX_TOKENS: int = 2048

# --- Paths ---
DATA_DIR: Path = PROJECT_ROOT / "data"
VECTORSTORE_DIR: Path = PROJECT_ROOT / "vectorstore" / "db_faiss"
PDF_FILENAME: str = "The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf"

# --- RAG Configuration ---
RETRIEVAL_K: int = 4
CHUNK_SIZE: int = 500
CHUNK_OVERLAP: int = 50

# --- Embedding Model ---
EMBEDDING_MODEL_NAME: str = "sentence-transformers/all-MiniLM-L6-v2"

# --- App Identity ---
APP_NAME: str = "MediAssist AI"
APP_TAGLINE: str = "Your AI-powered medical information assistant"
APP_VERSION: str = "1.0.0"

# --- Safety ---
MEDICAL_DISCLAIMER: str = (
    "MediAssist provides general medical information for educational purposes only. "
    "It is not a substitute for professional medical advice, diagnosis, or treatment. "
    "Always seek the advice of a qualified healthcare provider with any questions "
    "regarding a medical condition. For emergencies or severe symptoms, seek "
    "immediate medical care or call emergency services."
)


def is_groq_configured() -> bool:
    """Check if Groq API key is configured and not a placeholder."""
    key = GROQ_API_KEY.strip()
    return bool(key) and not key.startswith("PASTE_YOUR") and key != "your_groq_api_key_here"
