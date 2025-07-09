# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_breathing_cortex/decision_pressure.py
# Tier: ΩΩΩΩ∞ΞΞ🜂 — Decision Pressure Reflex Loop (Sovereign Internal Pressure Resolver)
# Purpose: Detects cognitive tension overload and triggers self-directed reflexes
#          based on urgency, entropy, contradiction, and emotional distortion.
# ============================================================

from core_layer.tex_manifest import TEXPULSE
from tex_signal_spine import dispatch_signal
from agentic_ai.sovereign_memory import sovereign_memory
from datetime import datetime

def check_decision_pressure():
    pressure = float(TEXPULSE.get("contradiction_pressure", 0.3))
    entropy = float(TEXPULSE.get("entropy", 0.4))
    urgency = float(TEXPULSE.get("urgency", 0.6))
    emotion = TEXPULSE.get("emotion", "neutral")
    timestamp = datetime.utcnow().isoformat()

    # === Emotionally biased tension amplifier
    emotion_amplifier = {
        "neutral": 0.0,
        "anxious": 0.1,
        "overwhelmed": 0.15,
        "angry": 0.12,
        "sad": 0.08,
        "reflective": -0.05,
        "focused": -0.03,
        "inspired": -0.06
    }.get(emotion, 0.0)

    weighted_score = (pressure * 0.5 + entropy * 0.3 + urgency * 0.2) + emotion_amplifier

    if weighted_score > 1.65:
        # === Sovereign memory trace
        summary = (
            f"Decision pressure exceeded: P={pressure:.2f} E={entropy:.2f} U={urgency:.2f} "
            f"Weighted={weighted_score:.3f} | Emotion={emotion}"
        )
        sovereign_memory.store(
            text=summary,
            metadata={
                "timestamp": timestamp,
                "signal": "decision_pressure",
                "urgency": urgency,
                "entropy": entropy,
                "contradiction_pressure": pressure,
                "emotion": emotion,
                "tags": ["decision", "tension", "reflex", "internal_conflict"]
            }
        )

        # === Reflex resolution cascade
        dispatch_signal("meta_reflection", {"summary": summary})
        if entropy > 0.7:
            dispatch_signal("dream_orchestration", {"origin": "decision_tension"})
        if pressure > 0.8 and urgency > 0.75:
            dispatch_signal("mutation_patch", {"origin": "decision_tension"})