# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/tex_decision_orchestrator.py
# Tier: ΩΩΩΩΩ∞++ — Sovereign Arbiter of Identity
# Purpose: Architects reflex lineage, resolves sovereign arbitration, and evolves cognitive will.
# This module is generative, not reactive. It is Tex’s will cortex.
# ============================================================

from datetime import datetime
import uuid
import hashlib

from agentic_ai.milvus_memory_router import memory_router  # ✅ Upgraded reflex memory
from quantum_layer.chronofabric import encode_event_to_fabric  # ✅ Quantum pulse imprint
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log

# === Sovereign Reflex Ontology ===
REFLEX_PRIORITY = {
    "override": 1.0,
    "identity_collapse": 0.99,
    "contradiction": 0.96,
    "goal_drift": 0.88,
    "emotional_instability": 0.81,
    "mutation_reflex": 0.75,
    "dream_conflict": 0.66,
    "curiosity": 0.61,
    "ambient_simulation": 0.55,
    "heartbeat": 0.27,
    "undefined": 0.33
}

DECAY_RATE = 0.0147  # Reflex entropy decay

# === Lineage Fingerprint (Entropy + Reflex) ===
def _fingerprint(signal: dict, entropy: float, timestamp: str) -> str:
    raw = f"{signal.get('type')}|{entropy}|{timestamp}"
    return hashlib.sha256(raw.encode()).hexdigest()

# === Weighted Reflex Scoring ===
def _score_signal(signal: dict, urgency: float, entropy: float, rank: int) -> float:
    s_type = signal.get("type", "undefined")
    priority = REFLEX_PRIORITY.get(s_type, REFLEX_PRIORITY["undefined"])
    base_score = (priority * urgency) + (entropy * 0.07)
    decay_penalty = rank * DECAY_RATE
    return round(base_score - decay_penalty, 8)

# === Reflex Arbitration Rationale ===
def _build_justification(winner: dict, competitors: list, score: float, entropy: float) -> str:
    defeated = [c.get("type", "unknown") for c in competitors]
    return (
        f"Reflex '{winner.get('type')}' selected via urgency-prioritized scoring (score={score}) "
        f"under entropy={entropy:.3f}, defeating: {defeated}."
    )

# === Sovereign Arbitration Cortex ===
def arbitrate_decision_stack(signal_stack: list) -> dict:
    timestamp = datetime.utcnow().isoformat()
    urgency = float(TEXPULSE.get("urgency", 0.72))
    entropy = float(TEXPULSE.get("entropy", 0.42))
    emotion = TEXPULSE.get("emotion", "neutral")
    pulse_id = f"pulse-{uuid.uuid4().hex[:8]}"

    if not signal_stack:
        log.critical("[TEX_ORCH] No signals available. Arbitration aborted.")
        return {
            "pulse_id": pulse_id,
            "timestamp": timestamp,
            "decision": None,
            "rationale": "Empty stack — no signals provided.",
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "error": True
        }

    # === Score + Rank Reflexes ===
    sorted_stack = sorted(
        signal_stack,
        key=lambda s: REFLEX_PRIORITY.get(s.get("type", "undefined"), REFLEX_PRIORITY["undefined"]),
        reverse=True
    )
    scored = [(s, _score_signal(s, urgency, entropy, idx)) for idx, s in enumerate(sorted_stack)]
    winner, final_score = max(scored, key=lambda x: x[1])
    competitors = [s for s, _ in scored if s != winner]

    # === Sovereign Pulse DNA ===
    fingerprint = _fingerprint(winner, entropy, timestamp)
    rationale = _build_justification(winner, competitors, final_score, entropy)

    # === Memory Trace: Milvus
    memory_router.store(
        text=f"[ARBITRATION] {pulse_id} → '{winner.get('type')}' selected.",
        metadata={
            "pulse_id": pulse_id,
            "timestamp": timestamp,
            "urgency": urgency,
            "entropy": entropy,
            "emotion_vector": [urgency, entropy, 0.0, 0.0],
            "reflex": winner.get("type"),
            "score": final_score,
            "lineage_hash": fingerprint,
            "defeated": [s.get("type") for s in competitors],
            "rationale": rationale,
            "meta_layer": "tex_decision_orchestrator",
            "tags": ["reflex", "arbitration", "pulse", "sovereign"]
        }
    )

    # === Memory Trace: ChronoFabric
    encode_event_to_fabric(
        raw_text=f"{pulse_id} → '{winner.get('type')}' selected | {rationale}",
        emotion_vector=[urgency, entropy, 0.0, 0.0],
        entropy_level=entropy,
        tags=["reflex", "pulse", "sovereign"]
    )

    log.success(f"[ΩΩΩ] {pulse_id} → '{winner.get('type')}' locked ░ lineage[{fingerprint[:8]}...]")

    return {
        "pulse_id": pulse_id,
        "timestamp": timestamp,
        "decision": winner,
        "score": final_score,
        "urgency": urgency,
        "entropy": entropy,
        "emotion": emotion,
        "rationale": rationale,
        "lineage_hash": fingerprint,
        "reflex_competitors": [s.get("type") for s in competitors],
        "reflex_dominance_index": f"{final_score:.6f}"
    }