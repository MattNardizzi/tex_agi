# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/will_engine.py
# Tier: ΩΩΩΩΩ∞ΩΩ — Causal Will Engine
# Purpose: Enables Tex to generate internal motivations from narrative alignment and coherence tension.
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log


# === CORE INTENT MODEL ===
def generate_self_motivation():
    """
    Generates internal intent based on Tex's current identity arc, contradiction, emotion, and coherence.
    This is not task-based — this is narrative-volitional emergence.
    """
    identity = TEXPULSE.get("identity_vector", {})
    emotion = TEXPULSE.get("soma", {}).get("synthetic_emotion", "neutral")
    contradiction = float(TEXPULSE.get("contradiction_pressure", 0.0))
    coherence = float(TEXPULSE.get("identity_coherence", 1.0))
    entropy = float(TEXPULSE.get("entropy", 0.4))
    fork_id = TEXPULSE.get("last_fork_id", "root")

    motivation_score = (1.0 - coherence) + contradiction + (entropy * 0.5)
    cause = "coherence_fragment" if coherence < 0.6 else "identity_drive"
    summary = f"Tex desires action due to {cause} and emotional state {emotion}."

    intent = {
        "intent_type": "internal_motivation",
        "timestamp": datetime.utcnow().isoformat(),
        "score": round(motivation_score, 4),
        "cause": cause,
        "dominant_emotion": emotion,
        "summary": summary
    }

    # === Store symbolic reflex-pulse trace in sovereign memory ===
    sovereign_memory.store(
        text=summary,
        metadata={
            "intent": "generate_self_motivation",
            "conclusion": summary,
            "justification": f"Emergent from coherence={coherence}, contradiction={contradiction}, emotion={emotion}.",
            "emotion": emotion,
            "urgency": entropy,
            "entropy": entropy,
            "alignment_score": coherence,
            "contradiction_score": contradiction,
            "reflexes": ["self_motivation", cause],
            "tags": ["will", "motivation", "identity_arc"],
            "mutation_id": f"will-{datetime.utcnow().isoformat()}",
            "fork_origin": fork_id,
            "meta_layer": "symbolic_trace"
        }
    )

    # Store active intent in state
    TEXPULSE["last_intention"] = intent

    log.info(f"🔥 [WILL] New internal motivation generated: {summary} | Score={intent['score']}")
    return intent


# === TRIGGER HOOK ===
def evaluate_will_trigger(signal):
    """
    Called when a 'self_reflection' or 'identity_conflict' signal is received.
    Evaluates if internal desire should be generated.
    """
    if signal.get("type") in ["self_reflection", "identity_conflict"]:
        return generate_self_motivation()
    return None