# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/mutation_decision_engine.py
# Tier: ΩΩΩ-MUTATE — Reflex-Aligned Sovereign Mutation Arbiter (Loopless | Max-Power)
# Purpose: Selects highest-value mutation via entropy, urgency, integrity decay, and emotion-aligned arbitration.
# ============================================================

from typing import List, Dict
from datetime import datetime
import hashlib

from agentic_ai.milvus_memory_router import memory_router
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_layer.tex_manifest import TEXPULSE
from core_agi_modules.emotion_vector_router import emotion_bus


class MutationDecisionEngine:
    def __init__(self):
        self.weights = {
            "entropy": 1.35,
            "urgency": 1.15,
            "integrity": -1.0,
            "volatility": 0.85,
            "contradictions": 0.95
        }

    def score_mutation(self, mutation: Dict, emotional_state: Dict) -> float:
        """
        Weighted arbitration score based on mutation signal and current emotion bus.
        """
        score = 0.0
        rationale = {}

        for key, weight in self.weights.items():
            value = float(mutation.get(key, 0.0))
            product = value * weight
            rationale[key] = {"value": value, "weight": weight, "product": round(product, 4)}
            score += product

        if mutation.get("emotion") == emotional_state.get("label"):
            score += 0.2
            rationale["emotion_alignment_bonus"] = 0.2

        mutation["scoring_rationale"] = rationale
        return round(score, 4)

    def choose(self, candidates: List[Dict]) -> Dict:
        """
        Selects best mutation candidate based on arbitration score.
        """
        if not candidates:
            return {}

        emotion = emotion_bus.get()
        scored = [
            {**mutation, "arbitration_score": self.score_mutation(mutation, emotion)}
            for mutation in candidates
        ]

        best = max(scored, key=lambda m: m["arbitration_score"], default={})
        self.log_mutation(best)
        return best

    def log_mutation(self, decision: Dict):
        """
        Logs mutation arbitration into Milvus + Soulgraph with rationale and symbolic trace.
        """
        emotion = emotion_bus.get()
        fingerprint = f"{decision.get('module_id')}|{decision.get('arbitration_score')}|{emotion.get('signature', 'unk')}"
        decision_id = hashlib.sha256(fingerprint.encode()).hexdigest()[:12]

        summary = f"[MUTATION DECISION] Module: {decision.get('module_id')} | Score={decision.get('arbitration_score')}"

        memory_router.store(
            text=summary,
            metadata={
                "type": "sovereign_mutation_arbitration",
                "tags": ["mutation", "arbitration", "reflex", "symbolic"],
                "timestamp": datetime.utcnow().isoformat(),
                "emotion": emotion.get("label", "neutral"),
                "urgency": emotion.get("intensity", TEXPULSE.get("urgency", 0.65)),
                "entropy": emotion.get("entropy", TEXPULSE.get("entropy", 0.45)),
                "integrity": decision.get("integrity", 1.0),
                "volatility": decision.get("volatility", 0.3),
                "contradictions": decision.get("contradictions", 0.2),
                "decision_id": decision_id,
                "arbitration_score": decision.get("arbitration_score", 0.0),
                "rationale": decision.get("scoring_rationale", {})
            }
        )

        TEX_SOULGRAPH.imprint_belief(
            belief=f"Mutation selected for module '{decision.get('module_id')}' with score {decision.get('arbitration_score')}",
            emotion=emotion.get("label", "neutral"),
            source="mutation_decision_engine",
            tags=["mutation", "arbitration", decision_id]
        )


# === Manual Execution Harness ===
if __name__ == "__main__":
    sample_pool = [
        {
            "module_id":