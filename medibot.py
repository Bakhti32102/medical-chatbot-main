"""
MediAssist AI — Medical Information Assistant
Main entry point for the Streamlit application.

Run with: streamlit run medibot.py
"""

import sys
from pathlib import Path

# Ensure project root is importable
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.ui import main

if __name__ == "__main__":
    main()
