# ============================================================
# © 2025 VortexBlack LLC / Sovereign Cognition
# File: core_agi_modules/belief_justifier.py
# Tier: ΩΩΩ++ Reflex Justification Cortex — Symbolic Integrity Auditor
# Purpose: Evaluates, scores, and flags beliefs for justification strength
# ============================================================

from datetime import datetime
import numpy as np

from agentic_ai.milvus_memory_router import memory_router, embed_text
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from core_layer.tex_manifest import TEXPULSE

def get_soulgraph():
    from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
    return TEX_SOULGRAPH


class BeliefJustifier:
    def __init__(self):
        self.history = []

    def trace_belief_origin(self, belief_text: str, top_k: int = 5, threshold: float = 0.78) -> list:
        """
        Finds similar cognitive traces using vector similarity in Milvus.
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

    def evaluate_justification_strength(self, belief_text: str, sources: list) -> float:
        """
        Computes a justification strength score based on:
        - # of valid supporting sources
        - semantic signal boost
        - urgency and entropy modulation
        """
        urgency = float(TEXPULSE.get("urgency", 0.7))
        entropy = float(TEXPULSE.get("entropy", 0.4))

        source_depth_score = sum(1 for s in sources if len(s.strip().split()) > 3)
        source_factor = min(source_depth_score / 5.0, 1.0)

        relevant_terms = [
            "inflation", "fed", "BlackRock", "earnings", "GDP", "AI",
            "merger", "interest rates", "volatility", "ECB", "layoffs"
        ]
        semantic_boost = 0.05 if any(term.lower() in belief_text.lower() for term in relevant_terms) else 0.0
        urgency_boost = urgency * (0.1 + entropy * 0.1)

        strength = round(min(1.0, source_factor + semantic_boost + urgency_boost), 6)
        return strength

    def suggest_patch(self, belief_text: str) -> dict:
        """
        Suggests justification metadata and reflex triggers for a belief.
        """
        urgency = float(TEXPULSE.get("urgency", 0.7))
        entropy = float(TEXPULSE.get("entropy", 0.4))

        sources = self.trace_belief_origin(belief_text)
        justification_strength = self.evaluate_justification_strength(belief_text, sources)

        justified = justification_strength >= (0.5 - entropy * 0.2)
        reflexes = []

        if not justified:
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
                heat=0.6 + urgency * 0.3
            )

            reflexes = ["flag_for_review", "route_to_self_reflection"]

        return {
            "belief": belief_text,
            "justified": justified,
            "justification_strength": justification_strength,
            "sources_found": len(sources),
            "timestamp": datetime.utcnow().isoformat(),
            "reflexes": reflexes,
            "semantic_triggered": any(term.lower() in belief_text.lower() for term in [
                "inflation", "fed", "BlackRock", "AI", "GDP", "volatility", "interest rates"
            ]),
            "urgency": urgency,
            "entropy": entropy
        }

    def log_belief_review(self, belief_text: str, result: dict):
        """
        Logs belief justification status into both soulgraph and vector memory.
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
    def detect_weak_justification(self, sources: list) -> bool:
        """
        Lightweight heuristic to determine if belief justification is weak.
        """
        return len(sources) < 2 or all(len(s.strip()) < 30 for s in sources)