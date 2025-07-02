# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: tex_goal_reflex/goal_conflict_auditor.py
# Tier Ω∞Ω Federated Divergence Auditor — Conflict Detection, Classification, and Resolution Trace
# ============================================================

import uuid
from core_agi_modules.vector_layer.embed_store import embedder
from core_agi_modules.vector_layer.query_ops import get_cosine_similarity
from core_layer.utils.tex_panel_bridge import emit_internal_debate
from quantum_layer.memory_core.memory_cortex import memory_cortex
from core_layer.tex_manifest import TEXPULSE

class GoalConflictAuditor:
    def __init__(self, conflict_threshold=0.82):
        self.conflict_threshold = conflict_threshold
        self.conflict_keywords = ["not", "cancel", "suppress", "block", "eliminate", "oppose", "reverse"]

    def audit(self, agent_goal_maps):
        """
        Detects and classifies inter-agent goal conflicts.
        Logs and emits internal debate triggers.
        Returns a list of conflict reports with classification and trace.
        """
        conflicts = []

        all_goals = []
        for entry in agent_goal_maps:
            agent_id = entry["agent_id"]
            for g in entry.get("goals", []):
                g_vec = embedder.encode(g["goal"], normalize_embeddings=True).tolist()
                all_goals.append({
                    "goal": g["goal"],
                    "embedding": g_vec,
                    "agent_id": agent_id,
                    "emotion": g.get("emotion", "neutral"),
                    "urgency": g.get("urgency", 0.5)
                })

        for i, g1 in enumerate(all_goals):
            for g2 in all_goals[i+1:]:
                sim = get_cosine_similarity(g1["embedding"], g2["embedding"])
                if sim >= self.conflict_threshold and self._is_negated_pair(g1["goal"], g2["goal"]):
                    classification = self._classify_conflict(g1["goal"], g2["goal"])
                    conflict_id = f"conflict_{uuid.uuid4().hex[:8]}"
                    report = {
                        "conflict_id": conflict_id,
                        "goal_1": g1["goal"],
                        "goal_2": g2["goal"],
                        "agent_1": g1["agent_id"],
                        "agent_2": g2["agent_id"],
                        "similarity": round(sim, 4),
                        "classification": classification,
                        "urgency_avg": round((g1["urgency"] + g2["urgency"]) / 2, 3),
                        "emotion_1": g1["emotion"],
                        "emotion_2": g2["emotion"]
                    }

                    emit_internal_debate(
                        f"⚠️ [GOAL CONFLICT] ({classification}) — '{g1['goal']}' ⟷ '{g2['goal']}' [sim={sim:.4f}]"
                    )

                    memory_cortex.store(
                        event={"goal_conflict_event": report},
                        tags=["goal_conflict", classification],
                        urgency=report["urgency_avg"],
                        emotion=report["emotion_1"]
                    )

                    conflicts.append(report)

        return conflicts

    def _is_negated_pair(self, text1: str, text2: str) -> bool:
        t1 = text1.lower()
        t2 = text2.lower()
        return any(kw in t1 or kw in t2 for kw in self.conflict_keywords)

    def _classify_conflict(self, goal1: str, goal2: str) -> str:
        """
        Attempts to classify the conflict type: ethical, strategic, resource, ideological, or unspecified.
        """
        combined = f"{goal1} {goal2}".lower()

        if "privacy" in combined and "data access" in combined:
            return "ethical"
        elif "expand" in combined and "restrict" in combined:
            return "strategic"
        elif "allocate" in combined and "limit" in combined:
            return "resource"
        elif any(k in combined for k in TEXPULSE["identity"]["mission"]):
            return "ideological"
        else:
            return "unspecified"