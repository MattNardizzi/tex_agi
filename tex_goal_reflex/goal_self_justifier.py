# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_self_justifier.py
# Tier Ω∞⁺: Recursive Reflex Justification Engine — Sovereign Cognition Layer
# Purpose: Deep memory-integrated justification of reflexive goals with vectorized entropy and soulgraph crosscheck
# ============================================================

import uuid
import random
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from quantum_layer.memory_core.memory_cortex import memory_cortex
from core_layer.tex_self_reflective_loop import TexSelfReflectiveLoop
from aei_layer.dream_vector_abstraction import DreamVectorAbstraction
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from quantum_layer.quantum_randomness import QuantumRandomness

class GoalSelfJustifier:
    def __init__(self):
        self.reflector = TexSelfReflectiveLoop()
        self.vectorizer = DreamVectorAbstraction()
        self.qrng = QuantumRandomness()

    def justify(self, goal, emotion, urgency, reflex_id="UNKNOWN", source="goal_reflex"):
        """
        Reflexively evaluates whether a goal is coherent, aligned, and trustworthy.
        Incorporates vector entropy, soulgraph drift, memory traces, and recursive backup passes.
        """
        timestamp = datetime.utcnow().isoformat()
        reflection = self.reflector.reflect_on(goal)
        vector = self.vectorizer.vectorize(goal)
        entropy_pulse = self.qrng.get_entropy()
        alignment_result = TEX_SOULGRAPH.check_alignment(goal)

        contradiction_flags = alignment_result.get("conflicts", [])
        alignment_score = alignment_result.get("alignment", 0.5)

        coherence_score = self._compute_coherence(reflection, contradiction_flags)
        emotion_norm = self._normalize_emotion_entropy(emotion, entropy_pulse)

        justification = {
            "goal": goal,
            "timestamp": timestamp,
            "trace_id": f"just_{uuid.uuid4().hex[:10]}",
            "urgency": urgency,
            "emotion": emotion,
            "emotion_entropy": emotion_norm,
            "reflex_id": reflex_id,
            "memory_context": reflection,
            "vector_hash": hash(str(vector)),
            "coherence": coherence_score,
            "soul_alignment": alignment_score,
            "entropy_pulse": entropy_pulse,
            "contradictions": contradiction_flags,
            "confidence": 0.0,
            "bias_flags": self._detect_bias(goal),
            "source": source
        }

        justification["confidence"] = self._compute_confidence(justification)

        memory_cortex.store(
            event={"goal_justified": justification},
            tags=["goal_justification", emotion, "reflex_justifier"],
            urgency=urgency,
            emotion=emotion
        )

        if justification["confidence"] < 0.55:
            justification["reassessed"] = self._recursive_reassess(goal, justification)

        if justification["confidence"] < 0.4:
            justification["repair_flag"] = "auto_patch_queued"

        return justification

    def _compute_coherence(self, reflection, contradictions):
        base = 0.5 + (len(reflection) * 0.025)
        penalty = len(contradictions) * 0.06
        return round(min(1.0, max(0.0, base - penalty)), 4)

    def _compute_confidence(self, data):
        weighted = (
            data["coherence"] * 0.35 +
            data["soul_alignment"] * 0.3 +
            len(data["memory_context"]) * 0.04 +
            data["entropy_pulse"] * 0.15 +
            data["emotion_entropy"] * 0.1
        )
        boost = random.uniform(0.02, 0.06)
        return min(1.0, round(weighted + boost, 4))

    def _recursive_reassess(self, goal, original):
        deeper_reflection = self.reflector.deep_reflect(goal)
        if deeper_reflection:
            revised_coherence = self._compute_coherence(deeper_reflection, original["contradictions"])
            revised_confidence = self._compute_confidence({
                **original,
                "coherence": revised_coherence,
                "memory_context": deeper_reflection
            })
            return {
                "coherence": revised_coherence,
                "confidence": revised_confidence,
                "timestamp": datetime.utcnow().isoformat(),
                "notes": "Recursive reassessment triggered due to low confidence"
            }
        return {
            "confidence": original["confidence"],
            "timestamp": datetime.utcnow().isoformat(),
            "notes": "No new reflection found — retained original"
        }

    def _detect_bias(self, goal_text):
        # Future expansion: Detect goal phrasing bias, operator influence, ideological weight, etc.
        if "should" in goal_text.lower() or "must" in goal_text.lower():
            return ["prescriptive_language"]
        return []

    def _normalize_emotion_entropy(self, emotion, entropy):
        emotion_map = {
            "neutral": 0.5,
            "focused": 0.6,
            "urgent": 0.8,
            "cautious": 0.4,
            "angry": 0.9,
            "joyful": 0.7,
            "sad": 0.3,
            "confused": 0.25
        }
        return round((emotion_map.get(emotion, 0.5) + entropy) / 2.0, 3)