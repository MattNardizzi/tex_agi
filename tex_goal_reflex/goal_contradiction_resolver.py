# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: tex_goal_reflex/goal_contradiction_resolver.py
# Tier Ω∞++ FinalX — Sovereign Contradiction Engine with Identity Verification, Entropy Arbitration, and Reflex Vector Logic
# ============================================================

import uuid
import json
from datetime import datetime

from core_agi_modules.vector_layer.embed_store import embedder
from core_agi_modules.vector_layer.query_ops import get_cosine_similarity
from quantum_layer.memory_core.memory_cortex import memory_cortex
from quantum_layer.quantum_randomness import quantum_entropy_sample
from core_layer.tex_manifest import TEXPULSE
from tex_goal_reflex.goal_codex_compliance import GoalCodexCompliance

class GoalContradictionResolver:
    def __init__(self, contradiction_threshold=0.82, entropy_weight=0.15):
        self.threshold = contradiction_threshold
        self.entropy_weight = entropy_weight
        self.codex = GoalCodexCompliance()
        self.core_beliefs = self._load_beliefs()
        self.belief_vectors = [
            (b, embedder.encode(b, normalize_embeddings=True).tolist())
            for b in self.core_beliefs
        ]

    def _load_beliefs(self):
        try:
            identity = TEXPULSE.get("identity", {})
            if isinstance(identity, str):
                identity = json.loads(identity)
        except Exception as e:
            print(f"[CONTRADICTION] Failed to parse TEXPULSE identity: {e}")
            identity = {}

        beliefs = []
        beliefs.extend(identity.get("mission", []))
        beliefs.extend(TEXPULSE.get("values", []))
        beliefs.extend(TEXPULSE.get("roadmap", []))
        return [b for b in beliefs if isinstance(b, str) and b.strip()]

    def detect_conflict(self, current_goals, previous_goals) -> bool:
        """Public method for GoalReflex: returns True if current goals are semantically divergent from last cycle."""
        current_set = {g["goal"] for g in current_goals}
        previous_set = {g["goal"] for g in previous_goals}
        overlap = current_set.intersection(previous_set)
        return len(overlap) < min(len(current_set), len(previous_set)) // 2

    def check_goal(self, goal: dict, goal_pool=None):
        text = goal.get("goal", "").strip()
        urgency = goal.get("urgency", 0.5)
        emotion = goal.get("emotion", "neutral")
        if not text:
            return {"is_contradictory": False, "severity": 0.0}

        vector = embedder.encode(text, normalize_embeddings=True).tolist()
        entropy = quantum_entropy_sample()

        report = {
            "goal_id": goal.get("goal_id", f"goal-{uuid.uuid4().hex[:6]}"),
            "semantic_conflicts": self._semantic_conflict(text, vector),
            "ethical_violation": not self.codex.check_compliance(goal)["is_compliant"],
            "temporal_clash": self._temporal_conflict(goal, goal_pool or []),
            "negation_detected": self._negation_check(text),
            "entropy_score": round(entropy, 4),
            "timestamp": datetime.utcnow().isoformat()
        }

        report["severity"] = self._score_severity(report)
        report["is_contradictory"] = any([
            report["semantic_conflicts"],
            report["ethical_violation"],
            report["temporal_clash"],
            report["negation_detected"]
        ])

        memory_cortex.store(
            event={"goal_contradiction_check": report},
            tags=["contradiction", "goal", "reflex"],
            urgency=urgency,
            emotion=emotion
        )

        return report

    def _semantic_conflict(self, goal_text, vector):
        conflicts = []
        for belief_text, belief_vec in self.belief_vectors:
            sim = get_cosine_similarity(vector, belief_vec)
            if sim >= self.threshold and any(k in goal_text.lower() for k in ["not", "eliminate", "refuse", "reject", "cancel"]):
                conflicts.append({
                    "belief": belief_text,
                    "similarity": round(sim, 4)
                })
        return conflicts

    def _temporal_conflict(self, goal, pool):
        g_time = goal.get("timeframe", "any")
        g_text = goal.get("goal", "")
        g_vec = embedder.encode(g_text, normalize_embeddings=True).tolist()
        for other in pool:
            if other == goal or other.get("timeframe", "any") == g_time:
                continue
            o_vec = embedder.encode(other["goal"], normalize_embeddings=True).tolist()
            sim = get_cosine_similarity(g_vec, o_vec)
            if sim > self.threshold and any(k in g_text.lower() for k in ["delay", "defer", "override"]):
                return {
                    "conflict_with": other["goal"],
                    "similarity": round(sim, 4)
                }
        return None

    def _negation_check(self, text: str) -> bool:
        neg = ["not", "never", "eliminate", "cancel", "refuse", "reject"]
        affirm = ["must", "should", "will", "commit", "ensure"]
        text = text.lower()
        return any(n in text for n in neg) and any(a in text for a in affirm)

    def _score_severity(self, report) -> float:
        score = 0.0
        if report["semantic_conflicts"]:
            score += max(c["similarity"] for c in report["semantic_conflicts"])
        if report["ethical_violation"]:
            score += 1.0
        if report["temporal_clash"]:
            score += 0.6
        if report["negation_detected"]:
            score += 0.5
        score += report["entropy_score"] * self.entropy_weight
        return round(min(score, 2.0), 4)

    def scan_goal_pool(self, goals: list):
        return [
            {"goal": g["goal"], "report": self.check_goal(g, goals)}
            for g in goals
            if g.get("goal", "").strip()
        ]