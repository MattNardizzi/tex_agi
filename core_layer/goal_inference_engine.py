# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_inference_engine.py
# Purpose: Tier Ω∞ Reflex — Goal Justification via Emotion, Urgency, Forecast, and Memory Trace
# ============================================================

import uuid
import datetime
import hashlib
import re

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory


class GoalInferenceEngine:
    def __init__(self):
        self.inference_log = []

    def infer_reason(self, goal_text: str, emotion: str, urgency: float, prediction_score: float, memory_reference: str = None) -> dict:
        """
        Reflex: Generates a self-justifying rationale for goal selection and modulation.
        Integrates emotion, urgency modulation, belief alignment, memory reference anchors.
        """
        timestamp = datetime.datetime.utcnow().isoformat()
        reason_id = str(uuid.uuid4())

        # === Pulse modulation ===
        modulation = self._modulate_urgency(emotion)
        modulated_urgency = round(min(1.0, urgency + modulation), 3)

        # === Rationale synthesis ===
        rationale_parts = [
            f"Reflex trigger: {emotion}",
            f"Urgency (mod): {modulated_urgency}",
            f"Forecast confidence: {round(prediction_score, 3)}"
        ]

        if memory_reference:
            rationale_parts.append(f"Memory anchor: {memory_reference[:64]}...")

        source_type = "Market mode" if TEXPULSE.get("financial_uplink", {}).get("active") else "Cognitive mode"
        rationale = f"{source_type} | " + " | ".join(rationale_parts)
        trace_id = self._generate_trace_id(goal_text, rationale)

        reason = {
            "id": reason_id,
            "goal": goal_text,
            "reason": rationale,
            "timestamp": timestamp,
            "emotion": emotion,
            "urgency": modulated_urgency,
            "forecast_score": prediction_score,
            "memory_reference": memory_reference or "",
            "intent_tags": self._extract_tags(goal_text),
            "trace_id": trace_id
        }

        # === Loopless pulse into sovereign memory ===
        sovereign_memory.store(
            text=goal_text,
            metadata={
                "agent": "TEX",
                "intent": "goal_justification",
                "conclusion": goal_text,
                "alignment_score": prediction_score,
                "justification": rationale,
                "emotion": emotion,
                "urgency": modulated_urgency,
                "entropy": 1.0 - prediction_score,
                "reflexes": ["goal_alignment", "reason_inference"],
                "tags": reason["intent_tags"],
                "trust_score": 0.85,
                "mutation_id": trace_id,
                "parent_id": memory_reference,
                "rewrite_patch": None,
                "meta_layer": "symbolic_trace"
            }
        )

        self.inference_log.append(reason)
        return reason

    def _modulate_urgency(self, emotion: str) -> float:
        weights = {
            "urgent": 0.18, "anxious": 0.15, "resolute": 0.12, "fearful": 0.25,
            "curious": 0.06, "bold": 0.08, "optimistic": -0.04, "neutral": 0.0
        }
        return weights.get(emotion.lower(), 0.0)

    def _generate_trace_id(self, goal: str, rationale: str) -> str:
        return hashlib.sha256(f"{goal}::{rationale}".encode()).hexdigest()[:12]

    def _extract_tags(self, text: str) -> list:
        words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())
        stopwords = {"from", "this", "that", "which", "their", "have", "with", "been", "about", "tex", "must"}
        return list(set([w for w in words if w not in stopwords]))[:6]


# === CLI Reflex Test ===
if __name__ == "__main__":
    engine = GoalInferenceEngine()
    output = engine.infer_reason(
        goal_text="Tex must realign volatility strategy to outperform hedge consensus",
        emotion="resolute",
        urgency=0.75,
        prediction_score=0.86,
        memory_reference="Q2 misalignment between predicted and actual variance index"
    )
    print(output)