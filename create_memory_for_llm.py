"""
MediAssist AI — FAISS Vectorstore Creation Script

This script loads the medical PDF, chunks it, creates embeddings,
and stores them in a FAISS vector database.

Run this only if you need to rebuild the vectorstore:
    python create_memory_for_llm.py
"""

import sys
from pathlib import Path

# Ensure project root is importable
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.config import DATA_DIR, VECTORSTORE_DIR, CHUNK_SIZE, CHUNK_OVERLAP
from rag.vectorstore import get_embedding_model, rebuild_vectorstore


def main():
    """Rebuild the FAISS vectorstore from the medical PDF."""
    print("=" * 50)
    print("MediAssist AI — Vectorstore Rebuild")
    print("=" * 50)

    # Verify PDF exists
    pdf_files = list(DATA_DIR.glob("*.pdf"))
    if not pdf_files:
        print(f"❌ No PDF files found in {DATA_DIR}")
        print("   Please place your medical PDF in the data/ directory.")
        sys.exit(1)

    print(f"📄 Found PDF: {pdf_files[0].name}")
    print(f"📁 Output: {VECTORSTORE_DIR}")
    print(f"⚙️  Chunk size: {CHUNK_SIZE}, Overlap: {CHUNK_OVERLAP}")
    print()

    # Rebuild
    print("🔄 Rebuilding vectorstore...")
    success = rebuild_vectorstore()

    if success:
        print("✅ Vectorstore rebuilt successfully!")
        print(f"   Location: {VECTORSTORE_DIR}")
    else:
        print("❌ Failed to rebuild vectorstore.")
        print("   Check that all dependencies are installed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
