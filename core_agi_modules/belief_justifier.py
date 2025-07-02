# ============================================================
# © 2025 VortexBlack LLC / Sovereign Cognition
# File: core_agi_modules/belief_justifier.py
# Tier: ΩΩΩ++ Reflex Justification Cortex — Symbolic Integrity Auditor
# ============================================================

from datetime import datetime
import numpy as np

from agentic_ai.milvus_memory_router import memory_router, embed_text  # ✅ Milvus vector + embed
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override


def get_soulgraph():
    """
    Sovereign-safe loader to avoid circular reflex loops.
    """
    from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
    return TEX_SOULGRAPH


class BeliefJustifier:
    def __init__(self):
        self.history = []

    def trace_belief_origin(self, belief_text: str, top_k: int = 5, threshold: float = 0.78) -> list:
        """
        Finds similar cognitive traces to this belief using vector similarity in Milvus.
        """
        vector = embed_text(belief_text)
        results = memory_router.query_by_vector(vector=vector, top_k=top_k)

        sources = []
        for r in results:
            payload = r.get("entity", r)
            sim_score = float(r.get("score", 0))
            if sim_score >= threshold:
                sources.append(payload.get("text", "") or payload.get("summary", ""))

        self.history.append({
            "belief": belief_text,
            "sources": sources,
            "timestamp": datetime.utcnow().isoformat()
        })
        return sources

    def detect_weak_justification(self, sources: list, threshold: int = 3) -> bool:
        """
        Determines if belief lacks meaningful support by measuring linguistic depth.
        """
        justification_score = sum(1 for s in sources if len(s.strip().split()) > 3)
        return justification_score < threshold

    def suggest_patch(self, belief_text: str) -> dict:
        """
        Evaluates belief justification. If weak, triggers override and soulgraph imprint.
        """
        sources = self.trace_belief_origin(belief_text)
        weak = self.detect_weak_justification(sources)

        if weak:
            print(f"⚠️ [BELIEF JUSTIFIER] Weak justification detected for: '{belief_text}'")

            get_soulgraph().imprint_belief(
                belief=f"Weakly grounded belief: '{belief_text}'",
                source="belief_justifier",
                emotion="doubt",
                tags=["belief", "weak", "override_trigger"]
            )

            trigger_sovereign_override(
                cognitive_event={"input": belief_text},
                reason="belief_weakness",
                heat=0.7
            )

            return {
                "belief": belief_text,
                "action": "flag_for_review",
                "justified": False,
                "sources_found": len(sources),
                "timestamp": datetime.utcnow().isoformat()
            }

        return {
            "belief": belief_text,
            "action": "none",
            "justified": True,
            "sources_found": len(sources),
            "timestamp": datetime.utcnow().isoformat()
        }

    def log_belief_review(self, belief_text: str, result: dict):
        """
        Logs the result of belief justification into both symbolic memory and Milvus.
        """
        emotion_label = "analytic" if result.get("justified", True) else "doubt"

        get_soulgraph().imprint_belief(
            belief=f"Belief justification recorded: '{belief_text}'",
            source="belief_justifier",
            emotion=emotion_label,
            tags=["belief_review", "symbolic_trace"]
        )

        memory_router.store(
            text=f"[BELIEF REVIEW] {belief_text}",
            metadata={
                "type": "belief_review",
                "tags": ["belief_review", "justification", "symbolic_trace"],
                "emotion": emotion_label,
                "trust_score": 0.85 if result.get("justified") else 0.5,
                "heat": 0.4 if result.get("justified") else 0.7,
                "prediction": "belief grounded in cognitive memory" if result.get("justified") else "belief flagged for review",
                "actual": f"sources_found={result.get('sources_found', 0)}",
                "result": result,
                "timestamp": datetime.utcnow().isoformat()
            }
        )