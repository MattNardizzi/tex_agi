# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/reflex_priority_matrix.py
# Tier: Ω∞Ω — Reflex Priority Matrix with Entangled Memory + Utility Learning
# Purpose: Dynamically adjust reflex weights based on performance traces using vector + quantum memory only.
# ============================================================

from datetime import datetime
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_layer.tex_manifest import TEXPULSE


class ReflexPriorityMatrix:
    def __init__(self):
        self.weights = {
            "goal_reflex": 1.0,
            "memory_reflex": 1.0,
            "mutation_reflex": 1.0,
            "dream_reflex": 1.0,
            "swarm_reflex": 1.0
        }
        self.performance_memory = {}
        self.suppressed_flags = []

    def update_weights(self):
        trace_summary = []

        for reflex in self.weights:
            try:
                history = memory_router.recall_recent(
                    minutes=60,
                    top_k=25,
                    filters={"tags": [reflex]}
                )
            except Exception as e:
                print(f"[REFLEX MATRIX] Recall failed for '{reflex}': {e}")
                continue

            scores = [float(entry.get("score", 0.0)) for entry in history]
            regrets = [float(entry.get("regret", 0.0)) for entry in history]

            if not scores:
                continue

            avg_score = sum(scores) / len(scores)
            avg_regret = sum(regrets) / max(len(regrets), 1)
            adjusted = avg_score * (1.0 - avg_regret)
            new_weight = round(min(1.5, max(0.5, adjusted)), 3)
            self.weights[reflex] = new_weight

            if new_weight < 0.6:
                self.suppressed_flags.append(reflex)

            self.performance_memory[reflex] = {
                "avg_score": round(avg_score, 3),
                "avg_regret": round(avg_regret, 3),
                "last_updated": datetime.utcnow().isoformat(),
                "weight": new_weight
            }

            trace = {
                "reflex": reflex,
                "weight": new_weight,
                "avg_score": round(avg_score, 3),
                "avg_regret": round(avg_regret, 3),
                "suppressed": reflex in self.suppressed_flags,
                "timestamp": datetime.utcnow().isoformat()
            }

            trace_summary.append(trace)

            # Log individual weight trace
            memory_router.store(
                text=f"[WEIGHT] Reflex '{reflex}' → {new_weight}",
                metadata={
                    **trace,
                    "meta_layer": "reflex_weight_trace",
                    "tags": ["reflex", "weight", reflex]
                }
            )

            encode_event_to_fabric(
                raw_text=f"Reflex '{reflex}' updated to weight={new_weight}",
                emotion_vector=[
                    TEXPULSE.get("urgency", 0.6),
                    TEXPULSE.get("entropy", 0.4),
                    1.0 - new_weight,
                    0.0
                ],
                entropy_level=TEXPULSE.get("entropy", 0.4),
                tags=["reflex", reflex, "weight"]
            )

        # Log final matrix state
        memory_router.store(
            text="[MATRIX] Reflex weights updated.",
            metadata={
                "weights": self.weights,
                "performance_memory": self.performance_memory,
                "suppressed": self.suppressed_flags,
                "meta_layer": "reflex_priority_matrix",
                "tags": ["reflex", "priority", "matrix"],
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        return self.weights

    def get_weight(self, reflex_name: str) -> float:
        return self.weights.get(reflex_name, 1.0)


# === Manual Run for CLI Diagnostics ===
if __name__ == "__main__":
    matrix = ReflexPriorityMatrix()
    weights = matrix.update_weights()
    print("\n[REFLEX MATRIX] Updated Weights:")
    for k, v in weights.items():
        print(f"  - {k}: {v}")