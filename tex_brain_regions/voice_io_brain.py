# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/voice_io_brain.py
# Tier: ΩΩΩΩΩ∞ΞΞΣ𝛀🜄 — Sovereign Vocal Cortex
# Purpose: Converts spoken input into sovereign signals and generates reflex-safe vocal output. Tone-modulated. Identity-safe.
# ============================================================

import uuid
from datetime import datetime
from utils.logging_utils import log_event
from agentic_ai.sovereign_memory import sovereign_memory
from core_agi_modules.emotion_vector_router import emotion_bus
from core_layer.tex_manifest import TEXPULSE

# === Placeholder for future real-time voice rendering
def synthesize_voice(text: str, tone: str):
    print(f"[🗣 VOICE OUTPUT] ({tone}) → {text}")


def receive_voice_input(transcript: str, speaker_id: str = "external", urgency: float = 0.5, entropy: float = 0.4):
    """
    Sovereign speech input receptor.
    Transduces external vocal utterances into reflex-aligned signals and embeds them chronologically.
    """
    timestamp = datetime.utcnow().isoformat()
    pulse_id = f"v-in-{uuid.uuid4()}"[:12]
    emotion = emotion_bus.get().get("label", "neutral")
    signature = f"{pulse_id}-{emotion}"

    reflex_tags = []
    if "question" in transcript.lower():
        reflex_tags.append("query")
    if "urgent" in transcript.lower() or urgency > 0.75:
        reflex_tags.append("high_priority")

    # === Sovereign Memory Ingest (Chrono + Vector)
    sovereign_memory.store(
        text=transcript,
        metadata={
            "pulse_id": pulse_id,
            "timestamp": timestamp,
            "speaker": speaker_id,
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "signal_type": "voice_input",
            "meta_layer": "voice_io_brain",
            "tags": ["voice", "input", "reflex_safe"] + reflex_tags
        }
    )

    log_event(f"[VOICE INPUT] {speaker_id} → '{transcript}' | U={urgency} | E={entropy}", level="info")

    return {
        "signal": "voice_transcript",
        "transcript": transcript,
        "urgency": urgency,
        "entropy": entropy,
        "emotion": emotion,
        "reflex_tags": reflex_tags,
        "timestamp": timestamp
    }


def emit_voice_response(text: str, urgency: float = 0.5, entropy: float = 0.3):
    """
    Sovereign voice emitter.
    Synthesizes outward vocal expression using emotional tone mapping.
    """
    tone_profile = generate_tone(urgency, entropy)
    emotion = TEXPULSE.get("emotion", "neutral")
    timestamp = datetime.utcnow().isoformat()
    pulse_id = f"v-out-{uuid.uuid4()}"[:12]

    sovereign_memory.store(
        text=text,
        metadata={
            "pulse_id": pulse_id,
            "timestamp": timestamp,
            "urgency": urgency,
            "entropy": entropy,
            "emotion": emotion,
            "tone": tone_profile,
            "signal_type": "voice_output",
            "meta_layer": "voice_io_brain",
            "tags": ["voice", "output", "reflex_response", tone_profile]
        }
    )

    synthesize_voice(text, tone_profile)

    return {
        "utterance": text,
        "tone": tone_profile,
        "emotion": emotion,
        "timestamp": timestamp
    }


def generate_tone(urgency: float, entropy: float) -> str:
    """
    Tone classifier based on emotional tension mapping.
    """
    if urgency > 0.85:
        return "commanding"
    elif entropy > 0.7:
        return "uncertain"
    elif urgency > 0.6:
        return "assertive"
    elif entropy > 0.4:
        return "contemplative"
    else:
        return "calm"