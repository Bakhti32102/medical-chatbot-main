"""
MediAssist AI - Formatters
Utility functions for formatting sources, responses, and display elements.
"""

from pathlib import Path
from typing import List, Dict, Any


def extract_document_name(source_path: str) -> str:
    """Extract a clean document name from a file path."""
    if not source_path:
        return "Unknown Document"

    path = Path(source_path)
    name = path.stem.replace("_", " ").replace("-", " ")

    # Clean up common patterns
    name = name.replace("The Gale Encyclopedia of Medicine Second", "The Gale Encyclopedia of Medicine")
    name = name.replace("The GALE ENCYCLOPEDIA of MEDICINE SECOND", "The Gale Encyclopedia of Medicine")
    name = name.replace("the gale encyclopedia of medicine second", "The Gale Encyclopedia of Medicine")

    return name if name else "Medical Reference"


def format_source_info(source: Dict[str, Any]) -> str:
    """Format a single source into readable text."""
    doc_name = extract_document_name(source.get("document", ""))
    page = source.get("page")

    parts = [f"📄 **{doc_name}**"]
    if page is not None:
        parts.append(f"   Page {page}")

    return "\n".join(parts)


def format_all_sources(sources: List[Dict[str, Any]]) -> str:
    """Format all sources into a readable display string."""
    if not sources:
        return ""

    formatted = []
    for i, source in enumerate(sources, 1):
        doc_name = extract_document_name(source.get("document", ""))
        page = source.get("page")

        entry = f"**{i}.** 📄 {doc_name}"
        if page is not None:
            entry += f" — Page {page}"
        formatted.append(entry)

    return "\n".join(formatted)


def truncate_text(text: str, max_length: int = 200) -> str:
    """Truncate text to a maximum length with ellipsis."""
    if not text or len(text) <= max_length:
        return text
    return text[:max_length].rsplit(" ", 1)[0] + "..."
