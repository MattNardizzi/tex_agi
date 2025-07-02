# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: agentic_ai/sovereign_memory.py
# Tier: ΩΩΩ∞Ω∞Ω — Unified Reflex Memory Layer (Chrono + Milvus)
# Purpose: Hybrid wrapper to synchronize vector memory (Milvus) and temporal trace (ChronoFabric)
# ============================================================

from datetime import datetime
import numpy as np

from agentic_ai.milvus_memory_router import memory_router as milvus
from quantum_layer.chronofabric import encode_event_to_fabric

class SovereignMemory:
    def __init__(self):
        self.vector = milvus
        self.chrono = encode_event_to_fabric

    def store(self, text: str, metadata: dict):
        # === Default vector store ===
        self.vector.store(text=text, metadata=metadata)

        # === Auto-synchronize with ChronoFabric ===
        try:
            emotion = metadata.get("emotion", "neutral")
            urgency = float(metadata.get("urgency", 0.5))
            entropy = float(metadata.get("entropy", 0.4))
            pressure = float(metadata.get("pressure_score", 0.5))
            tension = float(metadata.get("tension", 0.0))
            tags = metadata.get("tags", ["sovereign_memory"])

            self.chrono(
                raw_text=text,
                emotion_vector=[urgency, entropy, pressure, tension],
                entropy_level=entropy,
                tags=tags
            )
        except Exception as e:
            print(f"[SOVEREIGN MEMORY] Chrono sync failed: {e}")

    def store_vector_trace(self, content: str, tags=None, signal_type="general", metadata: dict = None):
        self.vector.store_vector_trace(
            content=content,
            tags=tags or ["sovereign_trace"],
            signal_type=signal_type
        )
        try:
            self.chrono(
                raw_text=content,
                emotion_vector=[0.6, 0.4, 0.0, 0.0],
                entropy_level=0.4,
                tags=tags or ["sovereign_trace"]
            )
        except Exception as e:
            print(f"[SOVEREIGN MEMORY] Trace chrono sync failed: {e}")

    def embed_text(self, text: str):
        return self.vector.embed_text(text)

    def query_by_tags(self, tags: list, top_k: int = 10):
        return self.vector.query_by_tags(tags, top_k=top_k)

    def recall_recent(self, minutes: int = 5, top_k: int = 25, filters: dict = None):
        return self.vector.recall_recent(minutes=minutes, top_k=top_k)

# === Instantiation ===
sovereign_memory = SovereignMemory()
memory_router = sovereign_memory  # Compatibility alias for legacy reflex calls