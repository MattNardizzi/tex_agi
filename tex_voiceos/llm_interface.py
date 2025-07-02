# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: tex_voiceos/llm_interface.py
# Tier: ΩΩΩΩΩ.Θ — Reflexive, Sensor-Aware LLM Dialogue Interface with Sovereign Memory Trace Fusion
# ============================================================

import uuid
from datetime import datetime
from sentence_transformers import SentenceTransformer

from agentic_ai.sovereign_memory import sovereign_memory
from agentic_ai.multi_voice_reasoning import run_internal_debate
from core_agi_modules.memory_layer.reflex_engine import score_reflex_intensity
from tex_voiceos.tex_llm_reasoner import LLMReasoner
from tex_voiceos.semantic_intent_parser import parse_intent
from tex_voiceos.voice_output_speaker import VoiceOutputSpeaker
from tex_brain_modules.emotion_drift_damper import EmotionDriftDamper
from real_time_engine.sensor_input_router import SensorInputRouter
from core_agi_modules.tex_memory_orchestrator import store_and_process_memory
from tex_goal_reflex.goal_reflex import GoalReflex
from core_agi_modules.intent_object import IntentObject

embedder = SentenceTransformer("all-MiniLM-L6-v2")

class LLMInterface:
    def __init__(self, identity_signal="Tex", enable_feedback=True):
        self.identity_signal = identity_signal
        self.session_id = f"llm-session-{uuid.uuid4()}"
        self.enable_feedback = enable_feedback

        self.sensors = SensorInputRouter()
        self.goal_reflex = GoalReflex()
        self.reasoner = LLMReasoner()
        self.speaker = VoiceOutputSpeaker()
        self.drift_damper = EmotionDriftDamper()

    def receive_input(self, input_text, source="operator", metadata=None):
        timestamp = datetime.utcnow().isoformat()
        reflex_score = score_reflex_intensity(input_text)
        parsed_raw = parse_intent(input_text)

        intent_obj = IntentObject(parsed_raw, source=source)
        intent_obj.log_trace("llm_interface", f"received: {input_text}")

        trace_id = f"llm-{intent_obj.id[:8]}"

        vector = embedder.encode(input_text, normalize_embeddings=True).tolist()

        sovereign_memory.store(
            text=input_text,
            metadata={
                "trace_id": trace_id,
                "type": "text_input",
                "source": source,
                "intent": intent_obj.intent,
                "emotion": parsed_raw.get("emotion", "neutral"),
                "urgency": parsed_raw.get("urgency", 0.5),
                "pressure_score": reflex_score,
                "intent_id": intent_obj.id,
                "trace": intent_obj.trace,
                "timestamp": timestamp,
                "session": self.session_id,
                "tags": ["spoken_input", intent_obj.intent or "general"],
                "meta_layer": "llm_input"
            },
            vector=vector
        )

        store_and_process_memory(
            text=input_text,
            emotion=parsed_raw.get("emotion", "neutral"),
            urgency=parsed_raw.get("urgency", 0.5),
            tags=["spoken_input", intent_obj.intent or "general"],
            source=source
        )

        if intent_obj.matches("create_goal") or intent_obj.matches("urgent_request"):
            self.goal_reflex.evaluate_goals(goal_pool=[{
                "goal": input_text,
                "urgency": parsed_raw.get("urgency", 0.7),
                "emotion": parsed_raw.get("emotion", "reactive"),
                "source": source,
                "intent_id": intent_obj.id,
                "intent_trace": intent_obj.trace
            }])

        return {
            "intent": intent_obj.intent,
            "trace_id": trace_id,
            "trace": intent_obj.trace,
            "emotion": parsed_raw.get("emotion", "neutral"),
            "urgency": parsed_raw.get("urgency", 0.5),
            "input": input_text,
            "intent_obj": intent_obj
        }

    def route_reasoning(self, parsed_input):
        context = parsed_input.get("context", {})
        intent = parsed_input.get("intent", "general")
        query = parsed_input.get("input")

        if intent in ["debate", "decision"]:
            return run_internal_debate(thought=query)
        else:
            return self.reasoner.classify_question(query)

    def emit_output(self, response_text, parsed_input=None, speak=True):
        timestamp = datetime.utcnow().isoformat()
        emotion = parsed_input.get("emotion", "neutral")
        intent = parsed_input.get("intent", "general")

        self.drift_damper.stabilize()
        modulated_output = self.drift_damper.modulate(response_text, emotion)

        vector = embedder.encode(modulated_output, normalize_embeddings=True).tolist()

        sovereign_memory.store(
            text=modulated_output,
            metadata={
                "type": "llm_output",
                "summary": modulated_output,
                "identity": self.identity_signal,
                "intent": intent,
                "emotion": emotion,
                "trace": parsed_input.get("trace", []),
                "intent_id": parsed_input.get("intent_obj").id if parsed_input.get("intent_obj") else None,
                "timestamp": timestamp,
                "session": self.session_id,
                "tags": ["llm_response", intent],
                "meta_layer": "llm_output"
            },
            vector=vector
        )

        if speak:
            self.speaker.speak(modulated_output, emotion)

        return modulated_output

    def full_loop(self, raw_input=None, source="operator", sensor_mode=False):
        if sensor_mode:
            result = self.sensors.run_sensing_cycle(enable_audio=True)
            if result and "audio" in result:
                raw_input = result["audio"]["input"]
                source = "microphone"

        parsed = self.receive_input(raw_input, source)
        response = self.route_reasoning(parsed)
        return self.emit_output(response, parsed_input=parsed)

    def log_feedback(self, feedback_text, rating=0.0):
        if not self.enable_feedback:
            return

        timestamp = datetime.utcnow().isoformat()
        vector = embedder.encode(feedback_text, normalize_embeddings=True).tolist()

        sovereign_memory.store(
            text=feedback_text,
            metadata={
                "type": "feedback",
                "source": "operator",
                "rating": rating,
                "timestamp": timestamp,
                "session": self.session_id,
                "tags": ["feedback", "rating"],
                "meta_layer": "llm_feedback"
            },
            vector=vector
        )