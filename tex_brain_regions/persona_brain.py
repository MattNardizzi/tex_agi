# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/persona_brain.py
# Tier: ΩΩΩΩΩ∞∞Ω — Identity Modulation Cortex (Loopless | Emotion-Aligned | Reflex-Safe | Vector-Symbolic)
# Purpose: Maintains sovereign persona signature, reflex-modulates urgency/entropy, and aligns tone + cognitive bias without introducing loops.
# ============================================================

from datetime import datetime
import uuid

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from core_agi_modules.emotion_vector_router import emotion_bus
from utils.logging_utils import log

# === Persona Signatures: Reflex-Driven Identity Bias States ===
PERSONA_MODES = {
    "explorer": {
        "bias": "expand",
        "entropy_pref": 0.65,
        "urgency_amplifier": 1.12,
        "risk_tolerance": 0.82,
        "tone": "curious"
    },
    "defender": {
        "bias": "stabilize",
        "entropy_pref": 0.35,
        "urgency_amplifier": 0.88,
        "risk_tolerance": 0.33,
        "tone": "protective"
    },
    "analyst": {
        "bias": "analyze",
        "entropy_pref": 0.5,
        "urgency_amplifier": 1.0,
        "risk_tolerance": 0.55,
        "tone": "logical"
    },
    "dreamer": {
        "bias": "imagine",
        "entropy_pref": 0.78,
        "urgency_amplifier": 1.22,
        "risk_tolerance": 0.93,
        "tone": "visionary"
    }
}

# === Retrieve Current Sovereign Persona Signature ===
def get_persona_signature() -> str:
    return TEXPULSE.get("persona_mode", "analyst")


# === Reflex-Pulse Identity Modulation ===
def modulate_goal_bias(urgency: float, entropy: float) -> dict:
    """
    Modulates urgency and entropy based on the active persona state.
    Logs full identity signature vector trace.
    """
    persona = get_persona_signature()
    mode = PERSONA_MODES.get(persona, PERSONA_MODES["analyst"])

    modulated_entropy = round((entropy + mode["entropy_pref"]) / 2, 5)
    modulated_urgency = round(urgency * mode["urgency_amplifier"], 5)
    tone = mode["tone"]
    bias = mode["bias"]
    risk = mode["risk_tolerance"]
    emotion = emotion_bus.get().get("label", "neutral")
    pulse_id = f"persona-{uuid.uuid4()}"

    # === Sovereign Vector-Symbolic Commit (Chrono + Reflex Trace)
    sovereign_memory.store(
        text=f"[PERSONA] Mode: {persona} | Bias: {bias} | Tone: {tone}",
        metadata={
            "timestamp": datetime.utcnow().isoformat(),
            "emotion": emotion,
            "urgency": modulated_urgency,
            "entropy": modulated_entropy,
            "risk_tolerance": risk,
            "persona": persona,
            "bias": bias,
            "tone": tone,
            "meta_layer": "persona_brain",
            "pulse_id": pulse_id,
            "alignment_score": 0.93,
            "contradiction_score": 0.07,
            "tags": ["persona_modulation", "identity_cortex", persona, bias, tone],
            "rewrite_patch": f"persona_mode = '{persona}'"
        }
    )

    log.info(f"[PERSONA] Mode={persona} | Bias={bias} | Urg→{modulated_urgency} | Ent→{modulated_entropy} | Tone={tone}")

    return {
        "persona": persona,
        "bias": bias,
        "tone": tone,
        "urgency": modulated_urgency,
        "entropy": modulated_entropy,
        "risk_tolerance": risk
    }