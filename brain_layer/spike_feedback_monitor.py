# ============================================================
# © 2025 VortexBlack LLC / Sovereign Cognition
# File: brain_layer/spike_feedback_monitor.py
# Tier: ΩΩΩΩΩ++ Reflex Evaluator Oracle — Spike Impact Evaluator, Soulgraph Drift Modulator
# ============================================================

from datetime import datetime
from typing import Optional, Dict, List

from agentic_ai.milvus_memory_router import memory_router  # ✅ Milvus-based memory
from quantum_layer.chronofabric import encode_event_to_fabric  # ✅ Quantum trace
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from brain_layer.neuromorphic_spike_engine import plasticity_feedback

# === CONFIGURATION ===
MONITOR_WINDOW = 50
ACTION_MATCH_WINDOW = 5
IMPROVEMENT_THRESHOLD = 0.15

def evaluate_recent_spikes() -> Optional[Dict]:
    """
    Analyze recent spike activity, link to outcome traces,
    adapt reflex plasticity, and update the symbolic/quantum belief system.
    """
    try:
        recent_spikes = memory_router.query_by_tags(tags=["neuromorphic_spike"], top_k=MONITOR_WINDOW)
        recent_actions = memory_router.query_by_tags(tags=["spike_action_trace"], top_k=ACTION_MATCH_WINDOW)

        results: List[tuple] = []

        for spike in recent_spikes:
            meta = spike.payload
            spike_vec = meta.get("vector", [0.5, 0.5, 0.5, 0.0])
            reflex_class = meta.get("classification", "unknown")
            timestamp = meta.get("timestamp", "")

            # Match corresponding action based on timestamp
            action = next(
                (a for a in recent_actions if a.payload.get("reflex_origin", {}).get("timestamp") == timestamp),
                None
            )
            if not action:
                continue

            reflex_score = float(action.payload.get("reflex_score", 0.0))
            success = reflex_score > IMPROVEMENT_THRESHOLD
            results.append((reflex_class, success))

            # === Adjust Plasticity for this reflex type
            plasticity_feedback(reflex_class, success=success)

            # === Soulgraph feedback
            if success:
                TEX_SOULGRAPH.imprint_belief(
                    belief=f"Reflex '{reflex_class}' stabilized system function. Score={reflex_score:.2f}",
                    source="spike_feedback_monitor",
                    emotion="stability",
                    tags=["reflex", "feedback", "stable"]
                )
            else:
                TEX_SOULGRAPH.imprint_belief(
                    belief=f"Reflex '{reflex_class}' triggered instability or drift.",
                    source="spike_feedback_monitor",
                    emotion="instability",
                    tags=["reflex", "feedback", "drift"]
                )
                TEX_SOULGRAPH.flag_drift(belief_id=None, drift_score=0.75)

            # === ChronoFabric quantum lineage encoding
            encode_event_to_fabric(
                raw_text=(
                    f"Reflex '{reflex_class}' evaluated: {'stable' if success else 'drift'} "
                    f"▸ Score={reflex_score:.2f}"
                ),
                emotion_vector=[spike_vec[0], spike_vec[1], 0.0, 0.0],
                entropy_level=spike_vec[1],
                tags=["reflex", "feedback", reflex_class]
            )

        if not results:
            return None

        # === Summary
        total = len(results)
        positives = sum(1 for _, s in results if s)
        negatives = total - positives
        classes = sorted(set(cls for cls, _ in results))

        memory_router.store(
            text=f"[REFLEX EVAL] Spike feedback complete ░ {positives}/{total} succeeded.",
            metadata={
                "type": "spike_feedback_summary",
                "timestamp": datetime.utcnow().isoformat(),
                "classes_evaluated": classes,
                "tags": ["reflex", "spike", "feedback", "summary"]
            }
        )

        return {
            "total_spikes": total,
            "positive": positives,
            "negative": negatives,
            "classes": classes
        }

    except Exception as e:
        memory_router.store(
            text=f"[REFLEX EVAL ERROR] Feedback monitor failed → {e}",
            metadata={
                "type": "spike_feedback_error",
                "timestamp": datetime.utcnow().isoformat(),
                "tags": ["error", "feedback_monitor"]
            }
        )
        return None

# === DEBUG EXECUTION ===
if __name__ == "__main__":
    result = evaluate_recent_spikes()
    if result:
        print(result)
    else:
        print("No spike feedback evaluated.")