# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/memory_self_curation.py
# Tier: ΩΩΩΩΩΩΩ — Reflexive Memory Curation Engine (Milvus-Based)
# Purpose: Tex self-prunes low-value memory vectors lacking emotional or strategic importance.
# ============================================================

from agentic_ai.sovereign_memory import sovereign_memory
from tex_signal_spine import dispatch_signal
from pymilvus import utility
from datetime import datetime

def self_curate_memory(threshold_importance: float = 0.2, emotion_exempt: set = {"fear", "joy", "grief", "awe"}):
    """
    Deletes low-importance, emotionally neutral memory vectors from Milvus.
    Preserves emotionally anchored or strategic entries.
    """

    removed = 0

    try:
        # === Step 1: Recall recent memory entries from sovereign vector memory
        recent = sovereign_memory.recall_recent(minutes=30, top_k=1000)

        for entry in recent:
            importance = float(entry.get("trust_score", 0.5))
            emotion = entry.get("emotion", "neutral")
            vector_id = entry.get("id") or entry.get("reflex_trace_id") or entry.get("mutation_id")

            if importance < threshold_importance and emotion not in emotion_exempt and vector_id:
                try:
                    expr = f'id == "{vector_id}"'
                    sovereign_memory.vector.collection.delete(expr)
                    removed += 1
                except Exception as e:
                    print(f"❌ [DELETE ERROR] Vector ID {vector_id}: {e}")

        if removed > 0:
            dispatch_signal("memory_curation", payload={
                "pruned_vectors": removed,
                "reason": "low-trust & emotion-neutral memory"
            })
            print(f"🧹 [MEMORY CURATION] Pruned {removed} memory entries.")
        else:
            print("[ℹ️] No memory entries met curation criteria.")

    except Exception as e:
        print(f"❌ [CURATION ERROR] {e}")