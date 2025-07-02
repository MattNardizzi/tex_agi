# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: quantum_layer/memory_core/memory_cortex.py
# Tier ΩΩΩΩΩ+++ — Final Sovereign Memory Engine (Vector Fusion, Reflex Entropy, Intent-Lined)
# ============================================================

from datetime import datetime
from core_agi_modules.vector_layer.heat_tracker import ReflexHeatTracker, adjust_token_weights
from core_agi_modules.intent_object import IntentObject
from utils.logging_utils import log
from agentic_ai.sovereign_memory import sovereign_memory  # ✅ Sovereign memory engine

class MemoryCortex:
    def __init__(self):
        self.recent_memory = []
        self.heat_engine = ReflexHeatTracker()

    def store(self, event: dict, tags: list = None, urgency: float = 0.5, emotion: str = "neutral", intent_desc: str = "memory_log"):
        """
        Reflexively stores an event with sovereign metadata, reflex heat, token weights, and quantum-evaluated embedding.
        """
        from agi_orchestrators.quantum_orchestrator import trigger_quantum_evaluation
        quantum = trigger_quantum_evaluation

        tags = tags or []
        timestamp = datetime.utcnow().isoformat()
        content = str(event)
        trust_score = event.get("trust_score", 1.0)

        # === Intent Object Lineage ===
        intent = IntentObject(intent_desc, source="memory_cortex")
        intent.log_trace("memory_cortex", "event stored to sovereign memory")

        # === Reflex Heat Signature ===
        heat = self.heat_engine.calculate_heat(emotion, timestamp)

        # === Sovereign Vector Embedding ===
        summary_text = f"Memory Event: urgency={urgency}, trust={trust_score}, emotion={emotion}"
        vector = quantum.embed(summary_text)

        # === Token Weight Calculation ===
        token_weight = adjust_token_weights(
            vector=vector,
            metadata_dict={
                "emotion": emotion,
                "urgency": urgency,
                "trust_score": trust_score
            },
            heat=heat
        )

        # === Sovereign Metadata Block ===
        metadata = {
            "tags": tags + ["memory_cortex", "sovereign_store"],
            "urgency": urgency,
            "emotion": emotion,
            "timestamp": timestamp,
            "trust_score": trust_score,
            "token_weight": token_weight,
            "heat": heat,
            "intent_id": intent.id
        }

        # === Store into Reflex Log and Sovereign Memory
        payload = {
            "text": content,
            "vector": vector,
            "metadata": metadata
        }

        try:
            sovereign_memory.store(**payload)
            log.info(f"[MEMORY_CORTEX] 🧠 Stored sovereign memory: {intent_desc} | Tags: {tags} | Heat: {heat:.3f}")
        except Exception as e:
            log.warning(f"[MEMORY_CORTEX] ⚠️ Failed to store in sovereign memory: {e}")

        self.recent_memory.append({"event": content, **metadata})
        if len(self.recent_memory) > 50:
            self.recent_memory = self.recent_memory[-50:]

    def recall(self, query: str, filters: dict = None, top_k: int = 5):
        """
        Retrieves vector-matching memory from sovereign memory engine.
        """
        try:
            return sovereign_memory.query(query=query, filters=filters or {}, top_k=top_k)
        except Exception as e:
            log.warning(f"[MEMORY_CORTEX] ⚠️ Sovereign recall failed: {e}")
            return []

    def peek_recent(self):
        """
        Returns most recent reflex memory event.
        """
        return self.recent_memory[-1] if self.recent_memory else None


# === Global Sovereign Memory Singleton ===
memory_cortex = MemoryCortex()