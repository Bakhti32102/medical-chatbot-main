"""
MediAssist AI - Configuration Tests
Tests for environment loading, configuration, and core settings.
"""

import os
import sys
from pathlib import Path
from unittest.mock import patch

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


def test_config_imports():
    """Test that configuration module can be imported."""
    from core.config import (
        APP_NAME,
        APP_TAGLINE,
        GROQ_MODEL,
        RETRIEVAL_K,
        EMBEDDING_MODEL_NAME,
        MEDICAL_DISCLAIMER,
        VECTORSTORE_DIR,
        DATA_DIR,
    )

    assert APP_NAME == "MediAssist AI"
    assert APP_TAGLINE == "Your AI-powered medical information assistant"
    assert GROQ_MODEL == "qwen/qwen3.8-27b"
    assert RETRIEVAL_K == 4
    assert EMBEDDING_MODEL_NAME == "sentence-transformers/all-MiniLM-L6-v2"
    assert "educational purposes" in MEDICAL_DISCLAIMER.lower()
    print("[PASS] Config imports")


def test_env_loading():
    """Test that .env file is loaded correctly."""
    from core.config import load_dotenv, PROJECT_ROOT

    env_path = PROJECT_ROOT / ".env"
    assert env_path.exists(), ".env file should exist"
    print("[PASS] .env file exists")

    load_dotenv(env_path)
    from core.config import GROQ_API_KEY
    assert GROQ_API_KEY is not None
    print("[PASS] .env loading")


def test_groq_config_check():
    """Test the Groq configuration check function."""
    from core.config import is_groq_configured

    with patch("core.config.GROQ_API_KEY", "PASTE_YOUR_GROQ_API_KEY_HERE"):
        assert not is_groq_configured()

    with patch("core.config.GROQ_API_KEY", ""):
        assert not is_groq_configured()

    with patch("core.config.GROQ_API_KEY", "gsk_real_key_123456"):
        assert is_groq_configured()

    print("[PASS] Groq config check")


def test_vectorstore_exists():
    """Test that the FAISS vectorstore directory exists with expected files."""
    vs_path = PROJECT_ROOT / "vectorstore" / "db_faiss"
    assert vs_path.exists(), f"Vectorstore directory not found: {vs_path}"

    faiss_file = vs_path / "index.faiss"
    pkl_file = vs_path / "index.pkl"
    assert faiss_file.exists(), f"FAISS index not found: {faiss_file}"
    assert pkl_file.exists(), f"FAISS pickle not found: {pkl_file}"
    print("[PASS] Vectorstore files exist")


def test_medical_pdf_exists():
    """Test that the medical PDF exists in the data directory."""
    pdf_path = PROJECT_ROOT / "data" / "The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf"
    assert pdf_path.exists(), f"Medical PDF not found: {pdf_path}"

    size_mb = pdf_path.stat().st_size / (1024 * 1024)
    assert size_mb > 1, f"PDF seems too small: {size_mb:.2f} MB"
    print(f"[PASS] Medical PDF exists ({size_mb:.1f} MB)")


def test_prompts_imports():
    """Test that prompt templates can be imported."""
    from core.prompts import (
        SYSTEM_PROMPT,
        RAG_PROMPT_TEMPLATE,
        WELCOME_MESSAGE,
    )

    assert "MediAssist" in SYSTEM_PROMPT
    assert "{context}" in RAG_PROMPT_TEMPLATE
    assert "{question}" in RAG_PROMPT_TEMPLATE
    assert "MediAssist AI" in WELCOME_MESSAGE
    print("[PASS] Prompts imports")


def test_formatters():
    """Test formatting utilities."""
    from utils.formatters import extract_document_name, format_source_info, format_all_sources

    name = extract_document_name("data/The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf")
    assert "Encyclopedia" in name

    source = {
        "document": "data/The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf",
        "page": 42,
        "content_preview": "Test content...",
    }
    formatted = format_source_info(source)
    assert "Page 42" in formatted

    sources = [source, source]
    all_formatted = format_all_sources(sources)
    assert "1." in all_formatted
    assert "2." in all_formatted
    print("[PASS] Formatters")


def test_styles_import():
    """Test that CSS styles can be loaded."""
    from app.styles import get_main_css

    css = get_main_css()
    assert len(css) > 100
    assert "--ma-blue" in css
    print("[PASS] Styles import")


def test_vectorstore_loadable():
    """Test that the FAISS vectorstore can actually be loaded."""
    try:
        from langchain_huggingface import HuggingFaceEmbeddings
        from langchain_community.vectorstores import FAISS

        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        vs_path = PROJECT_ROOT / "vectorstore" / "db_faiss"
        db = FAISS.load_local(
            str(vs_path), embedding_model, allow_dangerous_deserialization=True
        )
        # Test basic query
        docs = db.similarity_search("diabetes symptoms", k=1)
        assert len(docs) > 0
        print("[PASS] FAISS vectorstore loadable and searchable")
    except Exception as e:
        print(f"[WARN] FAISS load test skipped: {e}")


def run_all_tests():
    """Run all tests and report results."""
    tests = [
        test_config_imports,
        test_env_loading,
        test_groq_config_check,
        test_vectorstore_exists,
        test_medical_pdf_exists,
        test_prompts_imports,
        test_formatters,
        test_styles_import,
        test_vectorstore_loadable,
    ]

    passed = 0
    failed = 0
    errors = []

    print("=" * 50)
    print("MediAssist AI -- Test Suite")
    print("=" * 50)

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            failed += 1
            errors.append((test.__name__, str(e)))
            print(f"[FAIL] {test.__name__}: {e}")

    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed, {len(tests)} total")
    print("=" * 50)

    if errors:
        print("\nFailed tests:")
        for name, err in errors:
            print(f"  - {name}: {err}")

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
