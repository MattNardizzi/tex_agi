# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/processors/embedder.py
# Purpose: Convert textual signals into dense embeddings
# Tier: ΩΩΩ — Embedding Layer for Vectorized Cognition
# ============================================================

from sentence_transformers import SentenceTransformer
import torch

# === Load Model (auto-download if missing) ===
try:
    print("[📦] Loading embedding model: all-MiniLM-L6-v2...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
    model = model.to(device)
    print(f"[✅] Embedding model ready on {device.upper()}")
except Exception as e:
    print(f"[❌ EMBEDDER INIT ERROR] Failed to load model: {e}")
    model = None

# === Embed single string ===
def embed_text(text: str) -> list:
    if not model or not text.strip():
        return []
    try:
        return model.encode(text, normalize_embeddings=True).tolist()
    except Exception as e:
        print(f"[EMBEDDING ERROR] ❌ {e}")
        return []

# === Embed batch of strings ===
def batch_embed_texts(texts: list) -> list:
    if not model or not texts:
        return [[] for _ in texts]
    try:
        return model.encode(texts, normalize_embeddings=True).tolist()
    except Exception as e:
        print(f"[BATCH EMBEDDING ERROR] ❌ {e}")
        return [[] for _ in texts]