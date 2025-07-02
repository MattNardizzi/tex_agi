# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: quantum_layer/memory_core/memory_self_eval.py
# Tier ΩΩΩΩΩΩΩΩ — Recursive Belief Contradiction & Drift Engine
# Purpose: Detects belief contradictions, drift, and cognitive incoherence in long-term memory
# ============================================================

from quantum_layer.memory_core.long_term_memory_bridge import LongTermMemoryBridge
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from utils.logging_utils import log
from datetime import datetime
from sentence_transformers import SentenceTransformer, util
import numpy as np

class MemorySelfEvaluator:
    def __init__(self):
        self.ltm = LongTermMemoryBridge()
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.conflict_threshold = 0.35
        self.module_tag = "memory_self_eval"

    def check_for_conflicts(self, top_k=40, tag_filter="belief"):
        """
        Scan LTM for contradictory beliefs based on low semantic similarity and opposing emotional signatures.
        Returns a contradiction report with metadata.
        """
        log.info(f"[{self.module_tag}] 🔍 Initiating belief contradiction scan...")

        try:
            entries = self.ltm.search_by_tag(tag_filter, top_k=top_k)
            if not entries or "result" not in entries:
                log.warning(f"[{self.module_tag}] ❌ No belief-tagged memories retrieved.")
                return []

            items = entries["result"]
            texts = [m["payload"].get("text", "") for m in items]
            metas = [m["payload"] for m in items]

            embeddings = self.model.encode(texts, convert_to_tensor=True)
            sim_matrix = util.pytorch_cos_sim(embeddings, embeddings).cpu().numpy()

            contradictions = []
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    score = sim_matrix[i][j]
                    if score < self.conflict_threshold:
                        contradiction = {
                            "belief_1": texts[i],
                            "belief_2": texts[j],
                            "similarity_score": float(score),
                            "belief_id_1": metas[i].get("belief_id", "unknown"),
                            "belief_id_2": metas[j].get("belief_id", "unknown"),
                            "origin_1": metas[i].get("origin_id"),
                            "origin_2": metas[j].get("origin_id"),
                            "goal_1": metas[i].get("goal"),
                            "goal_2": metas[j].get("goal"),
                            "emotion_1": metas[i].get("emotion"),
                            "emotion_2": metas[j].get("emotion"),
                            "urgency_1": metas[i].get("urgency", 0.5),
                            "urgency_2": metas[j].get("urgency", 0.5),
                            "timestamp": datetime.utcnow().isoformat()
                        }
                        contradictions.append(contradiction)

            if contradictions:
                log.warning(f"[{self.module_tag}] ⚠️ {len(contradictions)} belief contradictions detected.")

                TEX_SOULGRAPH.imprint_belief(
                    belief="Contradiction detected across memory beliefs.",
                    source=self.module_tag,
                    emotion="conflict",
                    tags=["memory", "integrity", "drift"]
                )
            else:
                log.info(f"[{self.module_tag}] ✅ No contradictions found.")

            return contradictions

        except Exception as e:
            log.error(f"[{self.module_tag}] ❌ Self-eval error: {e}")
            return []

# === Singleton Access
_self_eval = MemorySelfEvaluator()

def check_for_memory_drift():
    return _self_eval.check_for_conflicts()