"""
MediAssist AI - LLM Service
Handles Groq LLM initialization and configuration.
"""

import streamlit as st
from typing import Optional

from langchain_groq import ChatGroq

from core.config import GROQ_API_KEY, GROQ_MODEL, TEMPERATURE, MAX_TOKENS, is_groq_configured


@st.cache_resource
def get_llm() -> Optional[ChatGroq]:
    """Initialize and cache the Groq LLM client.
    
    Returns None if API key is not configured.
    """
    if not is_groq_configured():
        return None

    try:
        llm = ChatGroq(
            model_name=GROQ_MODEL,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            groq_api_key=GROQ_API_KEY,
        )
        return llm
    except Exception:
        return None


def check_llm_status() -> dict:
    """Check the status of the LLM connection."""
    status = {
        "configured": is_groq_configured(),
        "model": GROQ_MODEL,
        "connected": False,
        "error": None,
    }

    if not status["configured"]:
        status["error"] = "GROQ_API_KEY not configured"
        return status

    try:
        llm = get_llm()
        if llm is not None:
            status["connected"] = True
        else:
            status["error"] = "Failed to initialize LLM"
    except Exception as e:
        status["error"] = str(e)

    return status
