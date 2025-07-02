# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/identity_compressor.py
# Tier: Reflex Identity Cortex — Belief Summary + Compression
# Purpose: Compresses recent belief updates into a long-term identity vector.
# ============================================================

from agentic_ai.milvus_memory_router import memory_router
from tex_signal_spine import dispatch_signal
from datetime import datetime

def compress_identity_beliefs():
    """
    Compresses past beliefs and signals into long-term identity summary entries.
    """
    try:
        # Pull recent memories
        recent = memory_router.recall_recent(minutes=15, top_k=10)

        # Filter belief updates
        beliefs = [
            r.get("summary", "")
            for r in recent
            if "belief_update" in r.get("tags", "")
        ]

        if not beliefs:
            print("🧠 [COMPRESSOR] No belief updates to compress.")
            return

        # Compress based on frequency
        dominant = max(set(beliefs), key=beliefs.count)
        summary = f"Tex has consistently believed: '{dominant}'"

        # Store compressed identity vector
        memory_router.store(
            text=summary,
            metadata={
                "timestamp": datetime.utcnow().isoformat(),
                "tags": ["identity_summary", "belief_update", "persistent_self"],
                "entropy": 0.3,
                "emotion_vector": [0.6, 0.4, 0.0, 0.0],
                "meta_layer": "identity_compression"
            }
        )

        dispatch_signal("identity_compression", payload={"summary": summary})
        print("🧠 [COMPRESSOR] Identity belief compressed and signal dispatched.")

    except Exception as e:
        print(f"❌ [COMPRESSOR ERROR] {e}")