# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/tex_decision_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞ΩΩ++ — Reflex Arbitration Cortex (Loopless | Recursive | Final Form)
# Purpose: Sovereign arbitration engine for pulse-based decision selection among competing reflex signals.
# ============================================================

from datetime import datetime
import uuid
import hashlib

from agentic_ai.milvus_memory_router import memory_router  # ✅ Upgraded to Milvus vector memory
from quantum_layer.chronofabric import encode_event_to_fabric  # ✅ Quantum lineage encoding
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log

# === Tunable Reflex Priority Weights ===
REFLEX_PRIORITY = {
    "override": 1.0,
    "identity_collapse": 0.97,
    "contradiction": 0.92,
    "goal_drift": 0.85,
    "emotional_instability": 0.78,
    "mutation_reflex": 0.7,
    "dream_conflict": 0.6,
    "curiosity": 0.55,
    "ambient_simulation": 0.5,
    "heartbeat": 0.25,
    "undefined": 0.3
}

# === Reflex Signal Scoring Function ===
def _score_signal(signal: dict, urgency: float, entropy: float) -> float:
    s_type = signal.get("type", "undefined")
    priority = REFLEX_PRIORITY.get(s_type, REFLEX_PRIORITY["undefined"])
    return round((priority * urgency) + (entropy * 0.1), 6)

# === Reflex Fingerprinting ===
def _generate_lineage_fingerprint(signal: dict, entropy: float, timestamp: str) -> str:
    raw = f"{signal.get('type')}|{signal.get('source', 'none')}|{entropy}|{timestamp}"
    return hashlib.sha256(raw.encode()).hexdigest()

# === Arbitration Function ===
def arbitrate_decision_stack(signal_stack: list) -> dict:
    timestamp = datetime.utcnow().isoformat()
    urgency = float(TEXPULSE.get("urgency", 0.72))
    entropy = float(TEXPULSE.get("entropy", 0.45))
    emotion = TEXPULSE.get("emotion", "neutral")
    pulse_id = f"pulse-{uuid.uuid4().hex[:8]}"

    if not signal_stack:
        log.warning("[DECISION ORCH] No signals provided for arbitration.")
        return {
            "pulse_id": pulse_id,
            "decision": None,
            "reason": "empty stack",
            "score": 0.0,
            "entropy": entropy,
            "urgency": urgency,
            "emotion": emotion
        }

    # === Loopless Score Ranking ===
    scored = [(sig, _score_signal(sig, urgency, entropy)) for sig in signal_stack]
    top_signal, top_score = max(scored, key=lambda x: x[1])

    # === Lineage Hash ===
    fingerprint = _generate_lineage_fingerprint(top_signal, entropy, timestamp)

    # === Sovereign Memory Trace: Milvus
    memory_router.store(
        text=f"[DECISION] {pulse_id} → Reflex selected: '{top_signal.get('type')}'",
        metadata={
            "timestamp": timestamp,
            "urgency": urgency,
            "entropy": entropy,
            "emotion_vector": [urgency, entropy, 0.0, 0.0],
            "signal_type": top_signal.get("type"),
            "source": top_signal.get("source", "unspecified"),
            "score": top_score,
            "lineage_hash": fingerprint,
            "pulse_id": pulse_id,
            "meta_layer": "reflex_arbitration",
            "tags": ["reflex", "arbitration", "pulse", "decision", "sovereign"]
        }
    )

    # === Quantum Memory Trace: ChronoFabric
    encode_event_to_fabric(
        raw_text=f"Reflex arbitration: '{top_signal.get('type')}' selected with score {top_score}",
        emotion_vector=[urgency, entropy, 0.0, 0.0],
        entropy_level=entropy,
        tags=["reflex", "arbitration", "quantum", "pulse"]
    )

    log.success(f"[ΩΩΩ] {pulse_id} → '{top_signal.get('type')}' locked ░ score={top_score:.6f} ░ lineage[{fingerprint[:8]}...]")

    return {
        "pulse_id": pulse_id,
        "timestamp": timestamp,
        "decision": top_signal,
        "score": top_score,
        "urgency": urgency,
        "entropy": entropy,
        "emotion": emotion,
        "lineage_hash": fingerprint
    }