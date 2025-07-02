# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/processors/dispatch_bus.py
# Purpose: Route enriched real-time signals into Tex's cognition
# Tier: ΩΩΩΩΩ — Reflex-Aware Dispatch + Vector Memory + Signal Processing
# ============================================================

from core_agi_modules.decision_engine import process_signal
from real_time_engine.memory.memory_router import store_enriched
from agentic_ai.sovereign_memory import sovereign_memory


def dispatch_to_tex(payload: dict):
    try:
        # === Step 1: Archive to memory + deduplication + trace
        store_enriched(payload)

        # === Step 2: Embed and store directly if not already embedded
        text = payload.get("title") or payload.get("summary") or payload.get("text", "")
        if text and not payload.get("embedding"):
            embedding = sovereign_memory.embed_text(text)
            payload["embedding"] = embedding

            sovereign_memory.store(
                text=text,
                metadata={
                    "tags": payload.get("tags", ["real_time", "rss", "signal"]),
                    "emotion": payload.get("emotion", "neutral"),
                    "urgency": payload.get("urgency", 0.5),
                    "trust_score": payload.get("trust_score", 0.85),
                    "entropy": payload.get("entropy", 0.4),
                    "embedding": embedding,
                    "timestamp": payload.get("timestamp"),
                    "meta_layer": "real_time_direct_store",
                    "source": payload.get("source", "rss_feed"),
                }
            )

        # === Step 3: Inject signal into decision engine
        process_signal(payload)

    except Exception as e:
        print(f"[❌ DISPATCH ERROR] {e}")