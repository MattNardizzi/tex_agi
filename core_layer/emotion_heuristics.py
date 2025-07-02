# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/emotion_heuristics.py
# Tier: ∞ΩΩ — Affective Reflex Cortex (Chrono + Vector Synced | Loopless | Sovereign-Safe)
# Purpose: Translates context into emotion, updates TEXPULSE, and emits goal/mutation signals reflexively.
# ============================================================

import random
from datetime import datetime

from agentic_ai.sovereign_memory import sovereign_memory
from real_time_engine.advanced_analytics import AdvancedAnalytics
from core_layer.tex_manifest import TEXPULSE
from tex_engine.cognitive_event_router import dispatch_event, CognitiveEvent
from utils.logging_utils import log

# === Emotion Mapping
TEX_EMOTION_MAP = {
    "risk": "cautious", "opportunity": "hopeful", "crisis": "fearful", "error": "reflective",
    "failure": "doubtful", "threat": "defensive", "victory": "proud", "success": "resolute",
    "conflict": "anxious", "innovation": "curious", "pressure": "urgent", "pattern": "strategic",
    "chaos": "bold", "question": "curious", "unknown": "curious", "collapse": "fearful",
    "mutation": "disruptive", "evolution": "committed", "volatility": "cautious", "ai": "strategic"
}

# === Emotion Urgency Profiles
TONE_DYNAMICS = {
    "fearful": (0.75, 0.95), "urgent": (0.8, 1.0), "anxious": (0.72, 0.93),
    "strategic": (0.6, 0.82), "bold": (0.55, 0.85), "curious": (0.5, 0.75),
    "cautious": (0.65, 0.85), "hopeful": (0.55, 0.78), "resolute": (0.7, 0.92),
    "doubtful": (0.6, 0.8), "reflective": (0.45, 0.7), "committed": (0.75, 0.95),
    "disruptive": (0.85, 1.0), "proud": (0.65, 0.88)
}

def evaluate_emotion_state(context_text: str = "") -> tuple:
    """
    Evaluates emotional response from input context and updates TEXPULSE.
    Logs to sovereign memory and dispatches cognition update signal.
    Returns: (emotion, urgency, coherence)
    """
    lowered = context_text.lower()
    matched_emotion = next((v for k, v in TEX_EMOTION_MAP.items() if k in lowered), "curious")
    urgency_range = TONE_DYNAMICS.get(matched_emotion, (0.55, 0.85))
    urgency = round(random.uniform(*urgency_range), 2)
    volatility = AdvancedAnalytics.get_market_volatility_score()
    coherence = round(random.uniform(0.55, 0.95 - volatility), 2)

    # === Update global state
    TEXPULSE["emotional_state"] = matched_emotion
    TEXPULSE["urgency"] = urgency
    TEXPULSE["coherence"] = coherence

    # === Sovereign memory log
    sovereign_memory.store(
        text=context_text,
        metadata={
            "emotion": matched_emotion,
            "urgency": urgency,
            "coherence": coherence,
            "tags": ["emotion", "pulse", "affective_response"],
            "meta_layer": "emotion_heuristics",
            "timestamp": datetime.utcnow().isoformat()
        }
    )

    # === Signal reflex update
    dispatch_event(CognitiveEvent(
        event_type="emotional_state_updated",
        payload={
            "emotion": matched_emotion,
            "urgency": urgency,
            "coherence": coherence,
            "context": context_text
        },
        urgency=urgency,
        coherence_shift=coherence - 0.75
    ))

    return matched_emotion, urgency, coherence

def trigger_emotion_response_signal(emotion: str, urgency: float, coherence: float, context_text: str):
    """
    Triggers behavior routing signals based on high emotion/urgency thresholds.
    """
    from tex_signal_dispatch import route_signal

    if urgency >= 0.8 and coherence >= 0.7:
        route_signal("GOAL_INFERENCE", {"stimulus": context_text})
        sovereign_memory.store(
            text="Goal inference triggered by affective alignment.",
            metadata={
                "tags": ["emotion_trigger", "goal_inference"],
                "urgency": urgency,
                "coherence": coherence,
                "emotion": emotion,
                "source": "emotion_heuristics",
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    elif urgency > 0.9 and emotion in {"fearful", "disruptive"}:
        route_signal("SELF_MUTATION", {
            "emotion": emotion,
            "urgency": urgency,
            "reason": f"Extreme emotional volatility detected: {context_text[:60]}"
        })
        sovereign_memory.store(
            text="Sovereign self-mutation triggered from high emotional volatility.",
            metadata={
                "tags": ["emotion_trigger", "mutation"],
                "urgency": urgency,
                "coherence": coherence,
                "emotion": emotion,
                "source": "emotion_heuristics",
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    elif urgency > 0.85 and emotion == "proud":
        sovereign_memory.store(
            text=f"Tex felt pride from input: {context_text}",
            metadata={
                "tags": ["emotion", "status", "proud"],
                "emotion": "proud",
                "urgency": urgency,
                "meta_layer": "emotion_heuristics",
                "timestamp": datetime.utcnow().isoformat()
            }
        )

def get_emotion_signal():
    """ Returns current emotional state snapshot from TEXPULSE. """
    return {
        "emotion": TEXPULSE.get("emotional_state", "curious"),
        "urgency": TEXPULSE.get("urgency", 0.0),
        "coherence": TEXPULSE.get("coherence", 1.0)
    }

def embed_emotion_symbolic_fusion(variant: dict, emotion: str, urgency: float, coherence: float):
    """ Embeds emotion state into a symbolic memory or metadata object. """
    variant["emotion_signature"] = {
        "emotion": emotion,
        "urgency": urgency,
        "coherence": coherence,
        "fusion_stamp": datetime.utcnow().isoformat()
    }

def get_emotional_state_vector() -> list:
    """ Converts current emotional label into a vector via sovereign embedding. """
    try:
        memory = sovereign_memory.recall_recent(top_k=1)
        mood = memory[0].get("metadata", {}).get("emotion", "neutral") if memory else "neutral"
        return sovereign_memory.embed_text(mood)
    except Exception:
        return [0.0] * 384

def debug_emotion_readout(text: str):
    """ Prints out a real-time emotion analysis for debugging. """
    e, u, c = evaluate_emotion_state(text)
    print(f"[EMOTION] 🧠 '{text}' → Emotion='{e}' | Urgency={u} | Coherence={c}")
    return e, u, c