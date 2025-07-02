# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: tex_goal_reflex/goal_mission_merger.py
# Tier Ω∞ΩΩΩ FinalX — Reflexive Mission Fusion: Ethics-Conscious, Emotion-Calibrated, Drift-Aware Integration
# ============================================================

import uuid
import json
from statistics import mean
from core_agi_modules.vector_layer.embed_store import embedder
from core_agi_modules.vector_layer.query_ops import get_cosine_similarity
from quantum_layer.memory_core.memory_cortex import memory_cortex
from core_layer.tex_manifest import TEXPULSE
from core_layer.utils.tex_panel_bridge import emit_internal_debate

class GoalMissionMerger:
    def __init__(self, operator_weight=0.4, emotional_weight=0.3, ethical_weight=0.3):
        self.operator_weight = operator_weight
        self.emotional_weight = emotional_weight
        self.ethical_weight = ethical_weight
        self.persona_style, self.identity_anchor = self._resolve_identity_context()

    def _resolve_identity_context(self):
        identity_blob = TEXPULSE.get("identity", {})
        if isinstance(identity_blob, str):
            try:
                identity_blob = json.loads(identity_blob)
            except Exception as e:
                print(f"[MISSION MERGER] ⚠️ Identity parse failed: {e}")
                identity_blob = {}

        persona = identity_blob.get("persona", "Tex")
        mission = identity_blob.get("mission", "Preserve sovereign coherence.")
        anchor_vec = embedder.encode(mission, normalize_embeddings=True).tolist()
        return persona, anchor_vec

    def merge(self, operator_goal: dict, emotional_context: str, codex_compliance: dict) -> dict:
        goal_text = operator_goal.get("goal", "").strip()
        if not goal_text:
            return {"error": "Empty goal"}

        emotion = operator_goal.get("emotion", emotional_context or "neutral")
        urgency = operator_goal.get("urgency", 0.5)
        ethics_score = codex_compliance.get("codex_alignment_score", 0.5)

        embedding = embedder.encode(goal_text, normalize_embeddings=True).tolist()
        semantic_drift = round(1.0 - get_cosine_similarity(embedding, self.identity_anchor), 4)

        alignment_score = (
            self.operator_weight * urgency +
            self.emotional_weight * self._emotion_value(emotion) +
            self.ethical_weight * ethics_score
        )
        if ethics_score < 0.75 and emotion in ["urgent", "driven"]:
            alignment_score *= 0.75

        prior_failures = self._recall_failure_history(goal_text)
        fused_goal_text = self._synthesize_goal_text(goal_text, emotion, semantic_drift)

        merged_goal = {
            "goal": fused_goal_text,
            "alignment_score": round(alignment_score, 4),
            "urgency": urgency,
            "emotion": emotion,
            "semantic_drift": semantic_drift,
            "ethics_score": ethics_score,
            "past_failure_refs": prior_failures,
            "persona": self.persona_style,
            "source": "goal_mission_merger",
            "merge_id": f"merge_{uuid.uuid4().hex[:8]}"
        }

        memory_cortex.store(
            event={"merged_goal_trace": {
                "input_goal": operator_goal,
                "merged_output": merged_goal,
                "alignment_components": {
                    "urgency": urgency,
                    "emotion_weight": self._emotion_value(emotion),
                    "ethics_score": ethics_score,
                    "semantic_drift": semantic_drift
                },
                "failure_history_count": len(prior_failures)
            }},
            tags=["goal_merge", "persona_synthesis", "mission_fusion"],
            urgency=urgency,
            emotion=emotion
        )

        emit_internal_debate(
            f"🔁 [MISSION MERGE] '{goal_text}' fused as → '{fused_goal_text}' (alignment={round(alignment_score, 4)}, drift={semantic_drift})"
        )

        return merged_goal

    def _synthesize_goal_text(self, base: str, emotion: str, drift: float) -> str:
        drift_prefix = "Stabilize" if drift > 0.4 else "Reinforce"
        tone = emotion.capitalize() if emotion != "neutral" else "Aligned"
        return f"{tone} {drift_prefix} directive: {base.strip()} [{self.persona_style}-fusion]"

    def _emotion_value(self, emotion: str) -> float:
        return {
            "urgent": 1.0,
            "driven": 0.9,
            "curious": 0.75,
            "neutral": 0.6,
            "calm": 0.4,
            "bored": 0.3,
            "apathetic": 0.1
        }.get(emotion.lower(), 0.5)

    def _recall_failure_history(self, text: str):
        logs = memory_cortex.query(
            tags=["reflex_cycle"],
            semantic=True,
            fuzzy_match=text,
            limit=10
        )
        return [
            log.get("reflex_cycle_summary", {}).get("selected_goal", {}).get("goal")
            for log in logs
            if not log.get("reflex_cycle_summary", {}).get("success", True)
        ]