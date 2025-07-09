# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: utils/embedder_loader.py
# Tier: Utility — Safe Embedder Loader (Meta-Tensor Safe)
# ============================================================

from sentence_transformers import SentenceTransformer

def load_embedder(model_name="all-MiniLM-L6-v2", device="cpu"):
    return SentenceTransformer(model_name, device=device)