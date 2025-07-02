# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/memory/memory_router.py
# Purpose: Master memory routing interface for real-time ingestion
# Tier: ΩΩΩΩΩ — Sovereign Memory Relay with Vector Store Only
# ============================================================

import uuid
from datetime import datetime

from agentic_ai.sovereign_memory import sovereign_memory

# === Deduplication Tracker ===
_recent_signal_hashes = set()

def _is_duplicate(text: str, timestamp: str) -> bool:
    """
    Checks if a signal has already been processed.
    """
    key = f"{text[:64]}::{timestamp}"
    if key in _recent_signal_hashes:
        return True
    _recent_signal_hashes.add(key)
    return False

def store_enriched(payload: dict):
    """
    Sovereign ingestion relay:
    - Deduplicates signals
    - Embeds text via sovereign memory
    - Stores vector and metadata
    """
    try:
        # === Extract and validate signal text ===
        text = payload.get("title") or payload.get("text") or ""
        if not text or len(text.strip()) < 12:
            print("⚠️ [MEMORY ROUTER] Skipped signal: empty or too short.")
            return

        timestamp = payload.get("timestamp") or datetime.utcnow().isoformat()

        if _is_duplicate(text, timestamp):
            print("🔁 [MEMORY ROUTER] Duplicate signal skipped.")
            return

        # === Use sovereign embedder
        embedding = payload.get("embedding") or sovereign_memory.embed_text(text)

        # === Store in Sovereign Reflex Memory
        sovereign_memory.store(
            text=text,
            metadata={
                "id": str(uuid.uuid4()),
                "tags": payload.get("tags", ["real_time", "rss", "signal"]),
                "emotion": payload.get("emotion", "neutral"),
                "urgency": payload.get("urgency", 0.5),
                "trust_score": payload.get("trust_score", 0.85),
                "entropy": payload.get("entropy", 0.4),
                "embedding": embedding,
                "timestamp": timestamp,
                "meta_layer": "real_time_ingest",
                "source": payload.get("source", "rss_feed"),
            }
        )

        print(f"[🧠 MEMORY ROUTER] Stored: {text[:80]}")

    except Exception as e:
        print(f"[❌ MEMORY ROUTER ERROR] {e}")