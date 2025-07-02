# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/vector_layer/fusion_engine.py
# Tier Ω∞ — Vector Fusion Engine (Final Form)
# Purpose: Fuses related memory fragments into high-trust, sovereign-logged traces
# ============================================================

from datetime import datetime
import hashlib
from agentic_ai.sovereign_memory import sovereign_memory

# === Fusion Registry (Optional Deduplication Cache) ===
seen_signatures = set()

# === Utilities ===
def fusion_signature(text):
    return hashlib.sha256(text.encode()).hexdigest()

def estimate_trust(text_list):
    return round(min(1.0, 0.8 + 0.01 * len(text_list)), 4)

# === Fusion Logic ===
def fuse_related_vectors(text_list, tags=None, emotion="neutral"):
    """
    Merges a list of memory fragments into a fused vector with alignment metadata,
    stores the vector trace in sovereign memory.
    """
    if not text_list or len(text_list) < 2:
        print("⚠️ [FUSION] Not enough memories to fuse.")
        return None

    fused_text = " | ".join(text_list)
    now = datetime.utcnow().isoformat()
    parent_ids = [fusion_signature(t) for t in text_list]
    sig = fusion_signature(fused_text)

    if sig in seen_signatures:
        print("⚠️ [FUSION] Duplicate synthesis detected — skipping.")
        return None
    seen_signatures.add(sig)

    trust = estimate_trust(text_list)

    metadata = {
        "emotion": emotion,
        "tags": tags or ["fused", "semantic"],
        "agent_id": "TEX",
        "trust_score": trust,
        "timestamp": now,
        "parent_ids": parent_ids,
        "mutation_id": sig
    }

    print(f"🔗 [FUSION] Merging {len(text_list)} memories → Trust: {trust}")

    # ✅ Store the fused trace into sovereign reflex memory
    sovereign_memory.store_vector_trace(
        content=fused_text,
        tags=metadata["tags"],
        signal_type="fusion_event",
        metadata=metadata
    )

    return {
        "vector": None,  # Optional: add vector result if you calculate externally
        "text": fused_text,
        "metadata": metadata,
        "signature": sig
    }