# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/voice_io_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞ΩΩ++ — Voice Cognition Cortex (Final Form)
# Purpose: Sovereignly routes real-time human speech into emotion, cognition, memory, and reflex arcs.
# ============================================================

from datetime import datetime
from tex_voiceos.voice_input_listener import parse_streamed_voice
from tex_breathing_cortex.tex_nervous_system import route_internal_signal
from agentic_ai.milvus_memory_router import memory_router  # ✅ Upgraded memory system
from quantum_layer.chronofabric import encode_event_to_fabric  # ✅ Quantum voice imprint
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log

def route_voice_input(audio_stream: bytes, metadata: dict = None) -> dict:
    """
    Sovereign voice ingress module.
    Parses human dialogue, classifies emotional state, and routes transcript into the cognitive reflex engine.
    """

    try:
        metadata = metadata or {}
        urgency = float(metadata.get("urgency", TEXPULSE.get("urgency", 0.65)))
        entropy = float(metadata.get("entropy", TEXPULSE.get("entropy", 0.4)))
        tone = metadata.get("tone", "neutral")
        timestamp = datetime.utcnow().isoformat()

        # === Parse streamed voice input
        result = parse_streamed_voice(audio_stream)
        transcript = result.get("transcript", "")
        emotion = result.get("emotion", tone)
        heat = float(result.get("heat", 0.5))

        if not transcript.strip():
            log.warning("[VOICE ORCH] Empty transcript detected.")
            return {"transcript": None, "emotion": emotion, "heat": heat}

        summary = f"Operator voice input: {transcript[:64]}..."

        # === Memory Log: Milvus
        memory_router.store(
            text=f"[VOICE] {transcript}",
            metadata={
                "timestamp": timestamp,
                "urgency": urgency,
                "entropy": entropy,
                "emotion_vector": [urgency, entropy, 0.0, 0.0],
                "tone": tone,
                "transcript": transcript,
                "meta_layer": "voice_input",
                "tags": ["voice", "speech", "operator", "emotion", "dialogue"]
            }
        )

        # === Quantum Log: ChronoFabric
        encode_event_to_fabric(
            raw_text=f"Voice input from operator: {transcript}",
            emotion_vector=[urgency, entropy, 0.0, 0.0],
            entropy_level=entropy,
            tags=["voice", "human", "speech", "alignment"]
        )

        # === Route into cognitive reflex layer
        route_internal_signal({
            "type": "voice_stream_input",
            "urgency": urgency,
            "entropy": entropy,
            "pressure_score": heat,
            "summary": summary,
            "timestamp": timestamp
        })

        log.info(f"[VOICE ORCH] Transcript processed ░ Emotion: {emotion} ░ Heat: {heat}")
        return {
            "transcript": transcript,
            "emotion": emotion,
            "heat": heat
        }

    except Exception as e:
        log.error(f"❌ [VOICE ORCH] Voice cognition failure: {e}")
        return {
            "transcript": None,
            "emotion": "uncertain",
            "heat": 0.5
        }