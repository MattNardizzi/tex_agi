# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/memory_layer/meta_memory_tracker.py
# Tier: ∞ΩΩΩ — Fork Outcome Logger + Drift-Aware Reflex Memory Trace (Chrono + Vector Entangled)
# Purpose: Tracks reflex/fork outcomes, encodes trust trajectory, drift pressure, and emotional imprint.
# ============================================================

from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log

# === Drift Instability Buffer
_instability_buffer = {}

def track_memory_use(
    belief_id: str,
    success: bool,
    urgency: float = 0.5,
    fingerprint: str = None,
    emotion: str = None
) -> None:
    """
    Reflex fork outcome tracker. Logs success/failure trace with drift, emotion, trust, heat, and symbolic lineage.

    Args:
        belief_id (str): Unique identifier for the belief or reflex decision
        success (bool): Outcome of execution
        urgency (float): Scale 0.0–1.0
        fingerprint (str): Optional symbolic trace ID
        emotion (str): Override or derived label
    """
    try:
        now = datetime.utcnow()
        outcome = "SUCCESS" if success else "FAILURE"
        emotion = emotion or ("satisfaction" if success else "frustration")
        urgency = round(urgency, 3)

        # === Instability Pressure Accumulation
        if not success:
            _instability_buffer[belief_id] = _instability_buffer.get(belief_id, 0) + 1
        else:
            _instability_buffer[belief_id] = 0

        instability_score = min(_instability_buffer[belief_id] * 0.2, 1.0)
        trust_score = round(1.0 - instability_score, 3)
        heat_score = round(min(1.0, urgency + instability_score), 3)

        # === Sovereign Memory Imprint
        summary = f"Belief {belief_id} → {outcome} | Urgency={urgency} | Emotion={emotion} | Instability={instability_score:.2f}"
        sovereign_memory.store(
            text=summary,
            metadata={
                "type": "fork_outcome_trace",
                "tags": ["reflex_outcome", "fork_trace", "instability", "entropy_memory"],
                "belief_id": belief_id,
                "outcome": outcome,
                "urgency": urgency,
                "emotion": emotion,
                "instability_score": instability_score,
                "trust_score": trust_score,
                "heat": heat_score,
                "prediction": f"{belief_id} would succeed",
                "actual": f"result={outcome}, instability={instability_score:.2f}",
                "fingerprint": fingerprint or "undefined",
                "source": "meta_memory_tracker",
                "timestamp": now.isoformat()
            }
        )

        log.info(
            f"[MEMTRACK] ✅ {belief_id} → {outcome} | Urgency={urgency} | Emotion={emotion} | Drift={instability_score:.2f}"
        )

    except Exception as e:
        log.error(f"[MEMTRACK:ERROR] ❌ {belief_id} → Failed to log memory trace: {e}")