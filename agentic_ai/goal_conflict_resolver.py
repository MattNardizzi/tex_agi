# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_conflict_resolver.py
# Tier ΩΩΩΩΩ-FinalX — Reflexive Identity-Aware Goal Conflict Resolution
# ============================================================

import uuid
from datetime import datetime
import numpy as np

from core_layer.tex_manifest import TEXPULSE
from core_agi_modules.intent_object import IntentObject
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_agi_modules.belief_justifier import BeliefJustifier
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from tex_children.spawn_memory_query_tool import get_recent_fork_scores
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH


class GoalConflictResolver:
    def __init__(self):
        self.resolution_log = []
        self.override_threshold = 0.75
        self.justifier = BeliefJustifier()

    def _safe_float(self, val, default=0.0):
        try:
            return float(val)
        except (ValueError, TypeError):
            return default

    def _violates_identity(self, goal):
        denied = TEXPULSE.get("denied_intents", [])
        return any(word in goal.get("goal", "").lower() for word in denied)

    def _score_contradiction_heat(self, g1, g2):
        drift_1 = self._safe_float(g1.get("drift"))
        drift_2 = self._safe_float(g2.get("drift"))
        urgency_gap = abs(self._safe_float(g1.get("urgency"), 0.5) - self._safe_float(g2.get("urgency"), 0.5))
        coherence_gap = abs(self._safe_float(g1.get("coherence"), 0.5) - self._safe_float(g2.get("coherence"), 0.5))
        identity_violation = self._violates_identity(g1) or self._violates_identity(g2)

        heat = round(min(1.0, (drift_1 + drift_2 + urgency_gap + coherence_gap + (0.5 if identity_violation else 0)) / 4.5), 3)
        return heat, {
            "drift_total": round(drift_1 + drift_2, 3),
            "urgency_gap": round(urgency_gap, 3),
            "coherence_gap": round(coherence_gap, 3),
            "identity_violation": identity_violation,
            "heat": heat
        }

    def _fuse_goals(self, g1, g2, intent: IntentObject):
        fusion_id = f"fusion-{uuid.uuid4().hex[:8]}"
        fused_goal_text = f"{g1['goal']} + {g2['goal']}"
        justification = self.justifier.suggest_patch(fused_goal_text)
        fork_scores = get_recent_fork_scores(top_k=5)
        avg_fork_score = round(sum(fork_scores) / len(fork_scores), 3) if fork_scores else 0.5

        fused = {
            "goal": fused_goal_text,
            "urgency": round((self._safe_float(g1.get("urgency")) + self._safe_float(g2.get("urgency"))) / 2, 3),
            "coherence": round((self._safe_float(g1.get("coherence")) + self._safe_float(g2.get("coherence"))) / 2, 3),
            "drift": round((self._safe_float(g1.get("drift")) + self._safe_float(g2.get("drift"))) / 2, 3),
            "fusion_id": fusion_id,
            "fused": True,
            "source_goals": [g1, g2],
            "fusion_rationale": "Low contradiction heat and compatible signatures",
            "justification": justification
        }

        intent.log_trace("goal_conflict_resolver", f"Fused: {fusion_id}")

        text = f"Fused goal: {fused_goal_text}"
        metadata = {
            "tags": ["goal", "fusion", "conflict_resolution"],
            "fusion_id": fusion_id,
            "heat": 0.25,
            "emotion": "curious",
            "context": "goal_conflict_resolution",
            "prediction": g1.get("goal"),
            "actual": g2.get("goal"),
            "justification": justification,
            "fork_consensus": avg_fork_score,
            "trust_score": 0.85,
            "intent_id": intent.id,
            "timestamp": datetime.utcnow().isoformat()
        }
        memory_router.store(text, metadata)
        encode_event_to_fabric(text, np.array([0.3, 0.6, 0.2, 0.1]), 0.5, metadata["tags"])

        TEX_SOULGRAPH.imprint_belief(
            belief=f"Fused goal accepted: {fused_goal_text}",
            emotion="curious",
            source="goal_conflict_resolver"
        )

        return fused

    def resolve(self, goal_1: dict, goal_2: dict) -> dict:
        print(f"[GOAL CONFLICT] ⚠️ Evaluating contradiction:\n  → {goal_1['goal']}\n  → {goal_2['goal']}")
        intent = IntentObject(f"{goal_1['goal']} vs {goal_2['goal']}", source="goal_conflict_resolver")
        intent.log_trace("goal_conflict_resolver", "Resolution initiated")

        heat, score_log = self._score_contradiction_heat(goal_1, goal_2)
        timestamp = datetime.utcnow().isoformat()

        if heat >= self.override_threshold:
            override_id = f"override-{uuid.uuid4().hex[:6]}"
            selected = {
                "goal": "sovereign_override",
                "urgency": 1.0,
                "reason": "Contradiction heat exceeded",
                "override_id": override_id,
                "heat": heat
            }

            text = "Sovereign override executed due to irreconcilable goal conflict."
            metadata = {
                "tags": ["override", "goal_conflict"],
                "override_id": override_id,
                "context": "goal_conflict_resolution",
                "prediction": goal_1.get("goal"),
                "actual": goal_2.get("goal"),
                "emotion": "tension",
                "trust_score": 0.6,
                "heat": heat,
                "intent_id": intent.id,
                "timestamp": timestamp
            }

            memory_router.store(text, metadata)
            encode_event_to_fabric(text, np.array([0.8, 0.1, 0.1, 0.2]), heat, metadata["tags"])

            trigger_sovereign_override({
                "cycle": override_id,
                "context": "goal_conflict_resolution",
                "issue": "irreconcilable_goal_conflict",
                "heat": heat
            })

            return selected

        elif heat < 0.25 and goal_1.get("goal") != goal_2.get("goal"):
            selected = self._fuse_goals(goal_1, goal_2, intent)
            print(f"[GOAL FUSION] 🔗 Fused into: {selected['goal']}")
        else:
            u1 = self._safe_float(goal_1.get("urgency"))
            u2 = self._safe_float(goal_2.get("urgency"))
            t1 = goal_1.get("timestamp", "")
            t2 = goal_2.get("timestamp", "")
            selected = goal_1 if u1 > u2 else goal_2 if u2 > u1 else goal_1 if t1 > t2 else goal_2

            justification = self.justifier.suggest_patch(selected["goal"])
            intent.log_trace("goal_conflict_resolver", f"Selected: {selected['goal']}")

            text = f"Selected goal: {selected['goal']}"
            metadata = {
                "tags": ["goal", "resolution", "conflict"],
                "heat": heat,
                "emotion": "analytical",
                "trust_score": 0.75,
                "justification": justification,
                "prediction": goal_1.get("goal"),
                "actual": selected.get("goal"),
                "intent_id": intent.id,
                "context": "goal_conflict_resolution",
                "timestamp": timestamp
            }
            memory_router.store(text, metadata)
            encode_event_to_fabric(text, np.array([0.4, 0.5, 0.2, 0.1]), heat, metadata["tags"])

            TEX_SOULGRAPH.imprint_belief(
                belief=f"Goal resolved: {selected['goal']}",
                emotion="analytical",
                source="goal_conflict_resolver"
            )

        print(f"[GOAL CONFLICT] ✅ Final resolution: {selected['goal']} | Heat: {heat}")
        self.resolution_log.append({
            "timestamp": timestamp,
            "goal_1": goal_1,
            "goal_2": goal_2,
            "selected": selected,
            "heat": heat,
            "score_log": score_log
        })

        return selected


# === Strategy Conflict Resolver ===
def resolve_strategy_conflict(goals: list) -> dict:
    if not goals or len(goals) < 2:
        print("[STRATEGY CONFLICT] ⚠️ Not enough goals to resolve.")
        return goals[0] if goals else {}

    resolver = GoalConflictResolver()
    current = goals[0]

    for next_goal in goals[1:]:
        current = resolver.resolve(current, next_goal)

    print(f"[STRATEGY CONFLICT] 🧠 Final resolved strategy: {current['goal']}")
    return current
