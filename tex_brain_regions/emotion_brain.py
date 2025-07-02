# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/emotion_brain.py
# Tier: ΩΩΩΩΩ∞𝛀 — Recursive Affective Sovereign Modulator
# Purpose: Infuses emotional state into cognition, reflex prioritization, memory volatility,
#          and decision heat. Emotion here is not feedback — it is sovereign direction.
# ============================================================

from datetime import datetime
import uuid
from core_agi_modules.emotion_vector_router import emotion_bus
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log

try:
    import wandb
    WANDB_ENABLED = True
except ImportError:
    WANDB_ENABLED = False


def process_affective_pulse(context: dict = None) -> list:
    """
    Sovereign affective modulation pulse.
    Converts emotional state into reflex priority, memory volatility, and decision heat.
    Loopless. Reflex-aligned. Chrono-synced.
    """
    context = context or {}
    timestamp = datetime.utcnow().isoformat()
    emotion = emotion_bus.get()

    label = emotion.get("label", "neutral")
    valence = float(emotion.get("valence", 0.0))
    intensity = float(emotion.get("intensity", 0.0))
    signature = emotion.get("signature", f"sig-{uuid.uuid4()[:8]}")
    entropy = float(TEXPULSE.get("entropy", 0.42))
    urgency = float(TEXPULSE.get("urgency", 0.69))

    affective_charge = round((valence * 0.5 + intensity * 0.5) * urgency * (1 + entropy), 5)

    # === Sovereign Memory Sync (Chrono + Vector Fusion)
    sovereign_memory.store(
        text=f"[EMOTION] {label} | valence={valence:.2f} | intensity={intensity:.2f}",
        metadata={
            "pulse_id": f"emotion-{uuid.uuid4()}",
            "timestamp": timestamp,
            "emotion_label": label,
            "valence": valence,
            "intensity": intensity,
            "urgency": urgency,
            "entropy": entropy,
            "affective_charge": affective_charge,
            "emotion_signature": signature,
            "context": context,
            "meta_layer": "emotion_brain_apex",
            "tags": ["emotion", "affective_state", "cognition_modulator", "reflex_tuning"]
        }
    )

    # === Optional WANDB Telemetry
    if WANDB_ENABLED:
        try:
            wandb.log({
                "emotion/label": label,
                "emotion/valence": valence,
                "emotion/intensity": intensity,
                "emotion/charge": affective_charge,
                "emotion/urgency": urgency,
                "emotion/entropy": entropy
            })
        except Exception:
            log.warning("⚠️ WandB emotion telemetry failed.")

    # === Reflex Cascade Trigger
    reflexes = []
    if affective_charge > 1.3:
        reflexes.extend([
            "amplify_cognitive_drive",
            "escalate_value_alignment_weight",
            "prioritize_goal_reinforcement"
        ])
    elif affective_charge < 0.25:
        reflexes.extend([
            "dampen_goal_priority",
            "deprioritize_external_attention",
            "enter_internal_resonance_mode"
        ])
    else:
        reflexes.append("stabilize_affective_continuity")

    log.success(f"[EMOTION] {label} → Charge={affective_charge} | Reflexes: {reflexes}")
    return reflexes


def process_emotional_state():
    """
    Sovereign emotional identity setter.
    Sets high-level affective label based on urgency × entropy.
    Loopless. Mutation-aware.
    """
    urgency = float(TEXPULSE.get("urgency", 0.7))
    entropy = float(TEXPULSE.get("entropy", 0.4))
    emotion = "neutral"

    if entropy > 0.8:
        emotion = "overwhelmed"
    elif entropy > 0.6:
        emotion = "uncertain"
    elif urgency > 0.85:
        emotion = "alert"
    elif urgency < 0.3:
        emotion = "apathetic"
    elif entropy < 0.3 and urgency < 0.4:
        emotion = "calm"

    TEXPULSE["emotion"] = emotion
    timestamp = datetime.utcnow().isoformat()
    pulse_id = f"emo-{uuid.uuid4()}"

    # === Chrono Memory Sync
    sovereign_memory.store(
        text=f"[EMOTION] State set to '{emotion}' | U={urgency:.2f} | E={entropy:.2f}",
        metadata={
            "timestamp": timestamp,
            "pulse_id": pulse_id,
            "emotion": emotion,
            "urgency": urgency,
            "entropy": entropy,
            "meta_layer": "emotion_brain",
            "tags": ["emotion", "state_update", emotion]
        }
    )