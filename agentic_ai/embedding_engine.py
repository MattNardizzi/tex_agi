# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agentic_ai/embedding_engine.py
# Tier: ΩΩΩΩ — Sovereign Embedding Engine
# Purpose: Converts input text into normalized embeddings for Qdrant
# ============================================================

from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text: str) -> list:
    """
    Converts input text into a normalized embedding vector.
    """
    return _model.encode(text, normalize_embeddings=True).tolist()