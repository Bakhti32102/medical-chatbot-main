"""
MediAssist AI - Premium Medical AI Assistant Interface
A polished healthcare-grade UI powered by RAG.
"""

import streamlit as st
import sys
from pathlib import Path

# Ensure project root is in path for imports
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.config import (
    APP_NAME,
    APP_TAGLINE,
    MEDICAL_DISCLAIMER,
    GROQ_MODEL,
    is_groq_configured,
)
from core.prompts import WELCOME_MESSAGE
from rag.vectorstore import load_vectorstore, check_vectorstore_status
from services.llm_service import get_llm, check_llm_status
from services.rag_service import create_rag_chain, query_medical_knowledge
from app.styles import get_main_css
from utils.formatters import format_all_sources


# ============================
# PAGE CONFIG
# ============================
st.set_page_config(
    page_title=f"{APP_NAME} — Medical AI Assistant",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply premium CSS
st.markdown(get_main_css(), unsafe_allow_html=True)


# ============================
# SVG ICON SYSTEM
# ============================
ICON_LOGO_SVG = """
<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="2" width="28" height="28" rx="8" fill="url(#logo-grad)"/>
  <path d="M16 8v16M8 16h16" stroke="white" stroke-width="2.8" stroke-linecap="round"/>
  <path d="M11 11l10 10M21 11l-10 10" stroke="rgba(255,255,255,0.3)" stroke-width="1.2" stroke-linecap="round"/>
  <defs>
    <linearGradient id="logo-grad" x1="2" y1="2" x2="30" y2="30">
      <stop stop-color="#1B6CA8"/>
      <stop offset="1" stop-color="#14B8A6"/>
    </linearGradient>
  </defs>
</svg>
"""

# Medical-AI Hero Visual (neural network + medical cross concept)
ICON_HERO_SVG = """
<svg width="280" height="280" viewBox="0 0 280 280" fill="none" xmlns="http://www.w3.org/2000/svg"
     style="max-width:280px;max-height:280px;display:block;margin:0 auto;">
  <defs>
    <linearGradient id="hg" x1="0" y1="0" x2="280" y2="280">
      <stop offset="0%" stop-color="#0F4C75"/>
      <stop offset="50%" stop-color="#1B6CA8"/>
      <stop offset="100%" stop-color="#14B8A6"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="45%" r="50%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.12)"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0)"/>
    </radialGradient>
    <linearGradient id="pg" x1="95" y1="140" x2="185" y2="140">
      <stop stop-color="rgba(255,255,255,0.9)"/>
      <stop offset="1" stop-color="rgba(200,240,255,0.9)"/>
    </linearGradient>
  </defs>
  <rect width="280" height="280" rx="20" fill="url(#hg)"/>
  <rect width="280" height="280" rx="20" fill="url(#glow)"/>
  <!-- Grid dots -->
  <g opacity="0.06" fill="white">
    <circle cx="40" cy="40" r="1.5"/><circle cx="70" cy="40" r="1.5"/><circle cx="100" cy="40" r="1.5"/><circle cx="130" cy="40" r="1.5"/><circle cx="160" cy="40" r="1.5"/><circle cx="190" cy="40" r="1.5"/><circle cx="220" cy="40" r="1.5"/><circle cx="250" cy="40" r="1.5"/>
    <circle cx="40" cy="70" r="1.5"/><circle cx="70" cy="70" r="1.5"/><circle cx="100" cy="70" r="1.5"/><circle cx="130" cy="70" r="1.5"/><circle cx="160" cy="70" r="1.5"/><circle cx="190" cy="70" r="1.5"/><circle cx="220" cy="70" r="1.5"/><circle cx="250" cy="70" r="1.5"/>
    <circle cx="40" cy="100" r="1.5"/><circle cx="70" cy="100" r="1.5"/><circle cx="100" cy="100" r="1.5"/><circle cx="160" cy="100" r="1.5"/><circle cx="190" cy="100" r="1.5"/><circle cx="220" cy="100" r="1.5"/><circle cx="250" cy="100" r="1.5"/>
    <circle cx="40" cy="130" r="1.5"/><circle cx="70" cy="130" r="1.5"/><circle cx="100" cy="130" r="1.5"/><circle cx="190" cy="130" r="1.5"/><circle cx="220" cy="130" r="1.5"/><circle cx="250" cy="130" r="1.5"/>
    <circle cx="40" cy="160" r="1.5"/><circle cx="70" cy="160" r="1.5"/><circle cx="100" cy="160" r="1.5"/><circle cx="160" cy="160" r="1.5"/><circle cx="190" cy="160" r="1.5"/><circle cx="220" cy="160" r="1.5"/><circle cx="250" cy="160" r="1.5"/>
    <circle cx="40" cy="190" r="1.5"/><circle cx="70" cy="190" r="1.5"/><circle cx="100" cy="190" r="1.5"/><circle cx="130" cy="190" r="1.5"/><circle cx="160" cy="190" r="1.5"/><circle cx="190" cy="190" r="1.5"/><circle cx="220" cy="190" r="1.5"/><circle cx="250" cy="190" r="1.5"/>
    <circle cx="40" cy="220" r="1.5"/><circle cx="70" cy="220" r="1.5"/><circle cx="100" cy="220" r="1.5"/><circle cx="130" cy="220" r="1.5"/><circle cx="160" cy="220" r="1.5"/><circle cx="190" cy="220" r="1.5"/><circle cx="220" cy="220" r="1.5"/><circle cx="250" cy="220" r="1.5"/>
    <circle cx="40" cy="250" r="1.5"/><circle cx="70" cy="250" r="1.5"/><circle cx="100" cy="250" r="1.5"/><circle cx="130" cy="250" r="1.5"/><circle cx="160" cy="250" r="1.5"/><circle cx="190" cy="250" r="1.5"/><circle cx="220" cy="250" r="1.5"/><circle cx="250" cy="250" r="1.5"/>
  </g>
  <!-- Neural network connections -->
  <g stroke="rgba(255,255,255,0.12)" stroke-width="1" fill="none">
    <line x1="45" y1="55" x2="100" y2="105"/>
    <line x1="235" y1="55" x2="180" y2="105"/>
    <line x1="45" y1="225" x2="100" y2="175"/>
    <line x1="235" y1="225" x2="180" y2="175"/>
    <line x1="100" y1="105" x2="140" y2="125"/>
    <line x1="180" y1="105" x2="140" y2="125"/>
    <line x1="100" y1="175" x2="140" y2="155"/>
    <line x1="180" y1="175" x2="140" y2="155"/>
    <line x1="75" y1="140" x2="100" y2="140"/>
    <line x1="180" y1="140" x2="205" y2="140"/>
  </g>
  <!-- Neural nodes -->
  <g fill="rgba(255,255,255,0.2)">
    <circle cx="45" cy="55" r="4"/><circle cx="235" cy="55" r="4"/>
    <circle cx="45" cy="225" r="4"/><circle cx="235" cy="225" r="4"/>
    <circle cx="100" cy="105" r="3.5"/><circle cx="180" cy="105" r="3.5"/>
    <circle cx="100" cy="175" r="3.5"/><circle cx="180" cy="175" r="3.5"/>
    <circle cx="75" cy="140" r="3"/><circle cx="205" cy="140" r="3"/>
  </g>
  <!-- Pulse waveform -->
  <path d="M75 140 L95 140 L105 115 L118 165 L130 120 L142 160 L152 130 L162 150 L172 140 L205 140"
        stroke="url(#pg)" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- Medical cross -->
  <g transform="translate(140,140)">
    <rect x="-14" y="-5" width="28" height="10" rx="5" fill="white" opacity="0.9"/>
    <rect x="-5" y="-14" width="10" height="28" rx="5" fill="white" opacity="0.9"/>
  </g>
</svg>
"""

# Suggestion card SVG icons (16x16, consistent style)
ICON_SVG_HEART = """<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 14s-5.5-3.5-5.5-7A3 3 0 018 4.5 3 3 0 0113.5 7C13.5 10.5 8 14 8 14z" stroke="currentColor" stroke-width="1.3" fill="none"/><path d="M5 8.5h6M8 6v5" stroke="currentColor" stroke-width="0.8" opacity="0.5"/></svg>"""
ICON_SVG_BRAIN = """<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 2C5.5 2 4 4 4 6c-1.5 0-3 1.5-3 3s1.5 3 3 3c0 1.5 1.5 3 4 3s4-1.5 4-3c1.5 0 3-1.5 3-3s-1.5-3-3-3c0-2-1.5-4-4-4z" stroke="currentColor" stroke-width="1.3" fill="none"/><path d="M8 3v10M5 5.5c1 1 2 1.5 3 1.5M11 5.5c-1 1-2 1.5-3 1.5M5 9.5c1-1 2-1.5 3-1.5M11 9.5c-1-1-2-1.5-3-1.5" stroke="currentColor" stroke-width="0.8" opacity="0.5"/></svg>"""
ICON_SVG_DROP = """<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 2L4 8a4 4 0 108 0L8 2z" stroke="currentColor" stroke-width="1.3" fill="none"/><path d="M6 9.5a2 2 0 002 2" stroke="currentColor" stroke-width="0.8" opacity="0.5"/></svg>"""
ICON_SVG_LUNGS = """<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 3v10" stroke="currentColor" stroke-width="1.2"/><path d="M8 5C6 5 4 6 4 8.5S5 13 8 13" stroke="currentColor" stroke-width="1.3" fill="none"/><path d="M8 5C10 5 12 6 12 8.5S11 13 8 13" stroke="currentColor" stroke-width="1.3" fill="none"/><path d="M5.5 7.5c.5-.3 1-.5 1.5-.5M10.5 7.5c-.5-.3-1-.5-1.5-.5" stroke="currentColor" stroke-width="0.7" opacity="0.4"/></svg>"""
ICON_SVG_PILL = """<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="3" y="6" width="10" height="4" rx="2" stroke="currentColor" stroke-width="1.3" fill="none" transform="rotate(-45 8 8)"/><line x1="5.5" y1="10.5" x2="10.5" y2="5.5" stroke="currentColor" stroke-width="0.8" opacity="0.4"/></svg>"""
ICON_SVG_BONE = """<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M4 4c-1 0-2 .5-2 1.5S3 7 4 7l8 8c1 0 2-.5 2-1.5S13 12 12 12L4 4z" stroke="currentColor" stroke-width="1.3" fill="none"/><circle cx="3" cy="5" r="1.2" stroke="currentColor" stroke-width="0.8" fill="none"/><circle cx="5" cy="3.5" r="1.2" stroke="currentColor" stroke-width="0.8" fill="none"/><circle cx="13" cy="11" r="1.2" stroke="currentColor" stroke-width="0.8" fill="none"/><circle cx="11" cy="12.5" r="1.2" stroke="currentColor" stroke-width="0.8" fill="none"/></svg>"""


# ============================
# SIDEBAR
# ============================
def render_sidebar():
    """Render the premium sidebar."""
    with st.sidebar:
        # Brand
        st.markdown(f"""
            <div class="sb-brand">
                <div class="sb-brand-icon">{ICON_LOGO_SVG}</div>
                <h1>{APP_NAME}</h1>
                <p class="sb-tagline">Medical AI Assistant</p>
            </div>
        """, unsafe_allow_html=True)

        # Actions
        st.markdown('<div class="sb-section"><div class="sb-section-label">Actions</div></div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("💬 New Chat", use_container_width=True):
                st.session_state.messages = []
                st.rerun()
        with col2:
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.messages = []
                st.rerun()

        st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

        # Knowledge Base
        st.markdown('<div class="sb-section"><div class="sb-section-label">Knowledge Base</div></div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="sb-item">
                <span class="sb-icon">📚</span>
                <span>The Gale Encyclopedia of Medicine</span>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

        # System Status
        st.markdown('<div class="sb-section"><div class="sb-section-label">System Status</div></div>', unsafe_allow_html=True)

        vs_status = check_vectorstore_status()
        vs_color = "green" if vs_status["vectorstore_loaded"] else "red"
        vs_label = "Loaded" if vs_status["vectorstore_loaded"] else "Unavailable"

        st.markdown(f"""
            <div class="sb-status-row">
                <span class="sb-status-dot {vs_color}"></span>
                <span>RAG: {vs_label}</span>
            </div>
        """, unsafe_allow_html=True)

        llm_status = check_llm_status()
        llm_color = "green" if llm_status["connected"] else ("amber" if llm_status["configured"] else "red")
        llm_label = "Connected" if llm_status["connected"] else ("Configured" if llm_status["configured"] else "Unavailable")

        st.markdown(f"""
            <div class="sb-status-row">
                <span class="sb-status-dot {llm_color}"></span>
                <span>AI Model: {llm_label}</span>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div class="sb-status-row" style="padding-left:1.6rem; font-size:0.72rem; opacity:0.55;">
                <span>{GROQ_MODEL}</span>
            </div>
        """, unsafe_allow_html=True)

        # Rebuild option if needed
        if not vs_status["vectorstore_loaded"]:
            st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)
            if st.button("🔄 Rebuild Vectorstore", use_container_width=True):
                with st.spinner("Rebuilding..."):
                    from rag.vectorstore import rebuild_vectorstore
                    success = rebuild_vectorstore()
                    if success:
                        st.success("Rebuilt!")
                        st.rerun()
                    else:
                        st.error("Failed.")

        # Disclaimer at bottom
        st.markdown(f"""
            <div class="sb-disclaimer">
                ⚕️ {MEDICAL_DISCLAIMER[:180]}...
            </div>
        """, unsafe_allow_html=True)


# ============================
# TOP HEADER
# ============================
def render_top_header():
    """Render the clean top navigation bar."""
    llm_status = check_llm_status()
    is_connected = llm_status["connected"]

    status_class = "connected" if is_connected else "disconnected"
    status_text = "AI Online" if is_connected else "AI Offline"

    st.markdown(f"""
        <div class="top-header">
            <div class="top-header-left">
                <div class="top-header-logo">{ICON_LOGO_SVG}</div>
                <div>
                    <div class="top-header-title">{APP_NAME}</div>
                    <div class="top-header-subtitle">Medical AI Assistant</div>
                </div>
            </div>
            <div class="top-header-right">
                <div class="status-pill {status_class}">
                    <span class="dot"></span>
                    {status_text}
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


# ============================
# WELCOME / HERO SCREEN
# ============================
def render_welcome_screen():
    """Render the premium welcome screen with two-column layout."""
    # Two-column hero: text left, visual right
    left_col, right_col = st.columns([55, 45], gap="medium")

    with left_col:
        st.markdown(f"""
            <div class="ma-welcome-left">
                <h1 class="ma-welcome-title">Welcome to <span class="gradient-text">MediAssist AI</span></h1>
                <p class="ma-welcome-subtitle">Your intelligent medical information assistant</p>
                <p class="ma-welcome-desc">
                    Powered by a comprehensive medical knowledge base, MediAssist AI provides
                    grounded, evidence-based health information to help you understand symptoms,
                    conditions, treatments, and general medical topics.
                </p>
                <div class="ma-hero-badges">
                    <div class="ma-hero-badge"><span class="badge-icon">{ICON_SVG_HEART}</span> RAG Powered</div>
                    <div class="ma-hero-badge"><span class="badge-icon">{ICON_SVG_DROP}</span> Medical Knowledge</div>
                    <div class="ma-hero-badge"><span class="badge-icon">{ICON_SVG_BRAIN}</span> Evidence Based</div>
                    <div class="ma-hero-badge"><span class="badge-icon">{ICON_SVG_LUNGS}</span> Safety First</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with right_col:
        st.markdown(f"""
            <div class="ma-welcome-visual">
                <div class="ma-hero-card">
                    <div class="ma-hero-card-bg"></div>
                    <div class="ma-hero-card-icon">{ICON_HERO_SVG}</div>
                    <div class="ma-hero-card-ring ring-1"></div>
                    <div class="ma-hero-card-ring ring-2"></div>
                    <div class="ma-hero-card-ring ring-3"></div>
                    <div class="ma-hero-card-label">AI-Powered Medical Knowledge</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Suggested questions
    st.markdown('<p class="ma-suggestions-heading">Try asking about</p>', unsafe_allow_html=True)

    suggestions = [
        (ICON_SVG_HEART, "What are the common symptoms of hypertension?"),
        (ICON_SVG_BRAIN, "What causes migraine headaches?"),
        (ICON_SVG_DROP, "What is anemia?"),
        (ICON_SVG_LUNGS, "What are the symptoms of asthma?"),
        (ICON_SVG_PILL, "Explain diabetes in simple terms."),
        (ICON_SVG_BONE, "What is osteoporosis and who is at risk?"),
    ]

    cols = st.columns(2)
    for i, (icon_svg, question) in enumerate(suggestions):
        with cols[i % 2]:
            if st.button(
                f"{question}",
                key=f"suggestion_{i}",
                use_container_width=True,
            ):
                st.session_state.messages.append({"role": "user", "content": question})
                st.rerun()

    # Disclaimer
    st.markdown(f"""
        <div class="ma-disclaimer">
            <strong>⚕️ Medical Disclaimer:</strong> {MEDICAL_DISCLAIMER}
        </div>
    """, unsafe_allow_html=True)


# ============================
# CHAT MESSAGE RENDERING
# ============================
def render_assistant_message(response: dict):
    """Render an assistant message with premium styling."""
    answer = response.get("answer", "")
    sources = response.get("sources", [])
    error = response.get("error")

    if error:
        st.markdown(f"""
            <div class="ma-error">
                <div class="error-title">⚠️ Error Processing Request</div>
                <div class="error-message">{error}</div>
            </div>
        """, unsafe_allow_html=True)
        return

    if not answer:
        st.markdown("""
            <div class="ma-limited">
                <strong>ℹ️ Unable to generate response</strong><br>
                Please try rephrasing your question or consult a healthcare professional.
            </div>
        """, unsafe_allow_html=True)
        return

    # Check for insufficient knowledge indicators
    insufficient_phrases = [
        "does not contain enough information",
        "insufficient information",
        "not available in the knowledge base",
        "not contain enough information to answer",
        "unable to provide information",
    ]
    is_insufficient = any(phrase.lower() in answer.lower() for phrase in insufficient_phrases)

    if is_insufficient:
        st.markdown(f"""
            <div class="ma-limited">
                <strong>ℹ️ Limited Information Available</strong><br>
                {answer}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(answer)

    # Render sources
    if sources:
        source_text = format_all_sources(sources)
        if source_text:
            with st.expander("📚 Medical Sources", expanded=False):
                st.markdown(source_text)
                if sources and sources[0].get("content_preview"):
                    st.markdown("---")
                    st.markdown("**Context Preview:**")
                    st.markdown(
                        f'<div class="ma-context-preview">'
                        f'{sources[0]["content_preview"]}</div>',
                        unsafe_allow_html=True,
                    )


# ============================
# MAIN APPLICATION
# ============================
def main():
    """Main application entry point."""
    render_sidebar()

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Top header
    render_top_header()

    # Render welcome screen or chat history
    if not st.session_state.messages:
        render_welcome_screen()
    else:
        # Render existing messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                if message["role"] == "assistant":
                    render_assistant_message(message["content"])
                else:
                    st.markdown(message["content"])

    # Chat input
    prompt = st.chat_input("Ask a medical question...")

    if prompt and prompt.strip():
        if not prompt.strip():
            st.toast("Please enter a medical question.", icon="⚠️")
            return

        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Searching medical knowledge base..."):
                vectorstore = load_vectorstore()
                llm = get_llm()

                if vectorstore is None:
                    response = {
                        "answer": "",
                        "sources": [],
                        "success": False,
                        "error": "Medical knowledge base is not available. Please check that the FAISS vectorstore exists in vectorstore/db_faiss/.",
                    }
                elif llm is None:
                    response = {
                        "answer": "",
                        "sources": [],
                        "success": False,
                        "error": "AI model is not available. Please configure your GROQ_API_KEY in the .env file.",
                    }
                else:
                    try:
                        chain = create_rag_chain(llm, vectorstore)

                        # Build chat history for context
                        chat_history = ""
                        history_messages = st.session_state.messages[-6:]
                        for msg in history_messages:
                            role = msg["role"]
                            content = msg["content"]
                            if isinstance(content, dict):
                                content = content.get("answer", "")
                            if content:
                                label = "User" if role == "user" else "Assistant"
                                chat_history += f"{label}: {content[:300]}\n"

                        response = query_medical_knowledge(chain, prompt, chat_history=chat_history)
                    except Exception as e:
                        response = {
                            "answer": "",
                            "sources": [],
                            "success": False,
                            "error": f"Unexpected error: {str(e)}",
                        }

            render_assistant_message(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    # Footer disclaimer
    if st.session_state.messages:
        st.markdown(f"""
            <div class="ma-footer-disclaimer">
                {MEDICAL_DISCLAIMER}
            </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
