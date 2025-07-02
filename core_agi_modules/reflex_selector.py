# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/reflex_selector.py
# Tier: Ω∞Ω — Reflex Selector with GPU Scoring + Priority Weighting + Chrono Logging
# Purpose: Determines active reflexes using real-time signal fusion and memory-informed optimization.
# ============================================================

from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from core_layer.emotion_heuristics import get_emotion_signal
from sovereign_evolution.sovereign_cognition_fire import score_conflict_heatmap
from swarm_layer.swarm_strategy_arbitrator import get_swarm_alignment_score

from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric

from core_agi_modules.reflex_forecaster import ReflexForecaster
from core_agi_modules.reflex_priority_matrix import ReflexPriorityMatrix
from core_agi_modules.reflex_stability_model import ReflexStabilityModel
from core_agi_modules.preactivation_queue import preactivation_queue
from core_agi_modules.reflex_gpu_accelerator import gpu_accelerator


def get_memory_pressure_score() -> float:
    """
    Estimates memory pressure from entropy + recent memory heat.
    """
    try:
        recent = memory_router.recall_recent(minutes=5, top_k=25)
        if not recent:
            return 0.4

        avg_heat = sum(float(r.get("heat", 0.5)) for r in recent) / len(recent)
        entropy_weight = TEXPULSE.get("entropy", 0.4)
        return round(min(max((avg_heat + entropy_weight) / 2, 0.0), 1.0), 3)

    except Exception as e:
        print(f"[MEMORY PRESSURE ERROR] ❌ {e}")
        return 0.5


class ReflexSelector:
    def __init__(self):
        self.forecaster = ReflexForecaster()
        self.priority_matrix = ReflexPriorityMatrix()
        self.stability_model = ReflexStabilityModel()

        self.reflex_thresholds = TEXPULSE.get("reflex_thresholds", {
            "goal_reflex": 0.6,
            "memory_reflex": 0.5,
            "mutation_reflex": 0.4,
            "dream_reflex": 0.3,
            "swarm_reflex": 0.6
        })

    def evaluate(self, cognitive_event=None, cycle_id=None, current_goal=None):
        signal_batch = []
        trace_log = []
        timestamp = datetime.utcnow().isoformat()

        # === Gather Input Signals
        emotion = get_emotion_signal()
        urgency = emotion.get("urgency", 0.0)
        valence = emotion.get("valence", 0.0)
        memory_pressure = get_memory_pressure_score()
        coherence = TEXPULSE.get("coherence", 1.0)
        conflict = score_conflict_heatmap(cognitive_event) if cognitive_event else 0.0
        alignment = get_swarm_alignment_score(current_goal) if current_goal else 1.0

        # === Assemble Reflex Input Vectors
        signal_batch.extend([
            {"reflex": "goal_reflex", "urgency": urgency, "valence": valence, "memory_pressure": 0.0, "coherence": coherence},
            {"reflex": "memory_reflex", "urgency": 0.2, "valence": 0.0, "memory_pressure": memory_pressure, "coherence": coherence},
            {"reflex": "mutation_reflex", "urgency": 0.3, "valence": 0.0, "memory_pressure": 0.0, "coherence": 1.0 - conflict},
            {"reflex": "dream_reflex", "urgency": 0.0, "valence": 0.1, "memory_pressure": 0.0, "coherence": coherence},
            {"reflex": "swarm_reflex", "urgency": 0.1, "valence": 0.0, "memory_pressure": 0.0, "coherence": alignment}
        ])

        # === Step 1: GPU-Based Reflex Scoring
        gpu_ranked = gpu_accelerator.evaluate_reflex_signals(signal_batch)

        # === Step 2: Priority Weighting
        weights = self.priority_matrix.update_weights()
        weighted_scores = {
            name: round(score * weights.get(name, 1.0), 4)
            for name, score in gpu_ranked
        }

        # === Step 3: Stability Filtering
        suppressed = set(self.stability_model.get_stability_report().get("suppressed_reflexes", []))
        final_scores = {
            name: score for name, score in weighted_scores.items()
            if name not in suppressed and score >= self.reflex_thresholds.get(name, 0.5)
        }

        # === Step 4: Memory + Chrono Logging
        if final_scores:
            summary = f"[REFLEX SELECTOR] Final Reflexes: {final_scores}"
            memory_router.store(
                text=summary,
                metadata={
                    "timestamp": timestamp,
                    "selected_reflexes": list(final_scores.keys()),
                    "weights": weighted_scores,
                    "suppressed": list(suppressed),
                    "meta_layer": "reflex_selector",
                    "tags": ["reflex", "selection", "reflex_selector"]
                }
            )
            encode_event_to_fabric(
                raw_text=summary,
                emotion_vector=[urgency, TEXPULSE.get("entropy", 0.4), 0.0, 0.0],
                entropy_level=TEXPULSE.get("entropy", 0.4),
                tags=["reflex", "selector"]
            )

        # === Step 5: Forecast + Preactivation
        forecast = self.forecaster.forecast()
        for reflex, score in forecast.get("predicted_reflexes", {}).items():
            if reflex not in final_scores:
                preactivation_queue.add(reflex, score=score, forecast_horizon=forecast["forecast_horizon"])
                print(f"[FORECAST] {reflex} preactivated @ score {score:.3f}")

        # === CLI Reflex Trace Log
        if final_scores:
            print(f"\n🧠 [REFLEX SELECTOR @ {timestamp}" + (f" | Cycle {cycle_id}" if cycle_id else "") + "]")
            for name, score in final_scores.items():
                print(f"[TRIGGER] {name} → {score:.3f}")

        return sorted(final_scores.items(), key=lambda x: -x[1])


# === CLI Diagnostic Run ===
if __name__ == "__main__":
    selector = ReflexSelector()
    reflexes = selector.evaluate(current_goal="Maintain strategic edge")
    print("\n[REFLEX SELECTOR] Ranked Reflexes:", reflexes)