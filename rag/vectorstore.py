"""
MediAssist AI - Vectorstore Manager
Handles FAISS vector database loading, validation, and management.
"""

import streamlit as st
from pathlib import Path
from typing import Optional

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from core.config import (
    VECTORSTORE_DIR,
    EMBEDDING_MODEL_NAME,
    DATA_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    HF_TOKEN,
)


@st.cache_resource
def get_embedding_model() -> HuggingFaceEmbeddings:
    """Load and cache the embedding model."""
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)


@st.cache_resource
def load_vectorstore() -> Optional[FAISS]:
    """Load the FAISS vectorstore from disk. Returns None if unavailable."""
    try:
        embedding_model = get_embedding_model()
        if not VECTORSTORE_DIR.exists():
            st.toast("⚠️ Vectorstore directory not found", icon="⚠️")
            return None

        db = FAISS.load_local(
            str(VECTORSTORE_DIR),
            embedding_model,
            allow_dangerous_deserialization=True,
        )
        return db
    except Exception as e:
        st.toast(f"⚠️ Failed to load vectorstore: {e}", icon="⚠️")
        return None


def check_vectorstore_status() -> dict:
    """Check the status of the vectorstore and embedding model."""
    status = {
        "vectorstore_exists": VECTORSTORE_DIR.exists(),
        "embedding_model": EMBEDDING_MODEL_NAME,
        "vectorstore_loaded": False,
        "error": None,
    }

    if status["vectorstore_exists"]:
        try:
            db = load_vectorstore()
            if db is not None:
                status["vectorstore_loaded"] = True
                # Get document count if available
                try:
                    status["document_count"] = len(db.index_to_docstore_id)
                except Exception:
                    status["document_count"] = "unknown"
        except Exception as e:
            status["error"] = str(e)

    return status


def rebuild_vectorstore() -> bool:
    """Rebuild the FAISS vectorstore from the medical PDF.
    
    Returns True if rebuild was successful, False otherwise.
    Requires HuggingFace token for embedding generation.
    """
    try:
        from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
        from langchain_text_splitters import RecursiveCharacterTextSplitter

        embedding_model = get_embedding_model()

        # Load PDF
        pdf_path = DATA_DIR
        if not pdf_path.exists():
            return False

        loader = DirectoryLoader(str(pdf_path), glob="*.pdf", loader_cls=PyPDFLoader)
        documents = loader.load()

        if not documents:
            return False

        # Split into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )
        text_chunks = text_splitter.split_documents(documents)

        # Create FAISS index
        db = FAISS.from_documents(text_chunks, embedding_model)

        # Save locally
        VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)
        db.save_local(str(VECTORSTORE_DIR))

        return True
    except Exception:
        return False
