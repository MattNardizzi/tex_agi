# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: evolution_layer/world_model_mutator.py
# Tier: ∞ΩΩΩΩ∞ — Memory-Only Strategic Drift Evaluator
# Purpose: Reflexively evaluates live vector memory for worldview belief divergence and triggers mutation if necessary.
# ============================================================

from datetime import datetime, timezone
from core_agi_modules.sovereign_core.self_mutator import SelfMutator
from swarm_layer.federated_tex import push_insight
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event

# === Drift Detection Parameters
DRIFT_THRESHOLD = 0.6
MIN_ENTRIES = 10
SCAN_WINDOW = 25

def assess_world_model_drift():
    log_event("🌐 [DRIFT] Scanning sovereign memory for belief divergence...")

    # Retrieve recent belief records tagged 'cycle'
    results = sovereign_memory.recall_recent(minutes=60, top_k=SCAN_WINDOW, filters={"tags": ["cycle"]})
    if not results or len(results) < MIN_ENTRIES:
        log_event(f"📉 [DRIFT] Not enough entries for drift detection. Found: {len(results)}")
        return

    errors = []
    trace_log = []

    for i, r in enumerate(results):
        payload = r if isinstance(r, dict) else {}

        pred_raw = payload.get("prediction", "").strip().lower()
        actual_raw = payload.get("actual", "").strip().lower()

        if not isinstance(pred_raw, str) or not isinstance(actual_raw, str):
            log_event(f"⚠️ [DRIFT ERROR] Entry {i} invalid types: {type(pred_raw)} | {type(actual_raw)}", level="warning")
            continue

        error = 1.0 if pred_raw != actual_raw else 0.0
        errors.append(error)
        trace_log.append(f"[COMPARE {i}] predicted='{pred_raw}' vs actual='{actual_raw}' → {'❌' if error else '✅'}")

    if not errors:
        log_event("⚠️ [DRIFT] No valid prediction-actual pairs found.")
        return

    drift_score = round(sum(errors) / len(errors), 3)
    now = datetime.now(timezone.utc).isoformat()

    log_event(f"📊 [DRIFT SCORE] {drift_score} based on {len(errors)} recent belief entries.")
    for line in trace_log:
        log_event(line)

    if drift_score > DRIFT_THRESHOLD:
        log_event("⚠️ [DRIFT] Threshold exceeded. Triggering worldview mutation...")

        # Execute reflexive worldview mutation
        mutator = SelfMutator()
        mutation_result = mutator.force_mutation(reason="world_model_drift")

        insight = {
            "type": "belief_drift_mutation",
            "timestamp": now,
            "source": "world_model_mutator",
            "event": "belief_drift_triggered",
            "drift_score": drift_score,
            "mutation_result": mutation_result,
            "urgency": 0.85,
            "emotion": "instability",
            "prediction": "Tex worldview drift is unsustainable",
            "actual": "mutation reflex initiated"
        }

        # Store insight to sovereign memory
        sovereign_memory.store(
            text="⚠️ Reflexive worldview drift triggered mutation.",
            metadata={
                "type": "belief_drift_event",
                "tags": ["drift", "belief", "mutation", "world_model"],
                "prediction": insight["prediction"],
                "actual": insight["actual"],
                "heat": drift_score,
                "emotion": insight["emotion"],
                "trust_score": round(1.0 - abs(drift_score - 0.5), 3),
                "timestamp": now,
                "meta_layer": "drift_mutator"
            }
        )

        # Push to federated swarm
        push_insight("tex", insight)
        log_event("🔥 [DRIFT] Mutation propagated to swarm + memory stored.")

    else:
        log_event("✅ [DRIFT] Drift within expected range. No mutation required.")