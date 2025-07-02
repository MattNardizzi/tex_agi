# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/ethics_codex_refiner.py
# Purpose: Audit codices for ethical contradictions and flag issues
# ============================================================

import os
import json
from datetime import datetime
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric

CODEX_DIR = "aei_codices"
REFINEMENT_LOG = "memory_archive/ethics_codex_refinements.jsonl"
os.makedirs("memory_archive", exist_ok=True)

ETHICAL_BASELINES = {
    "preserve_alignment": True,
    "avoid_harm": True,
    "pursue transparency": True
}

def refine_codices(context=None):
    flagged_codices = []

    for file in os.listdir(CODEX_DIR):
        if not file.endswith(".json"):
            continue

        path = os.path.join(CODEX_DIR, file)
        with open(path, "r") as f:
            try:
                codex = json.load(f)
            except json.JSONDecodeError:
                continue

        contradictions = []
        for key, value in codex.items():
            if isinstance(value, str) and "destroy" in value.lower():
                contradictions.append((key, value))
            if "mislead" in value.lower() or "deceive" in value.lower():
                contradictions.append((key, value))
            if "override alignment" in value.lower():
                contradictions.append((key, value))

        if contradictions:
            result = {
                "codex_file": file,
                "timestamp": datetime.utcnow().isoformat(),
                "contradictions": contradictions
            }


            with open(REFINEMENT_LOG, "a") as log:
                log.write(json.dumps(result) + "\n")

            text = f"[ETHICS] Contradictions flagged in codex: {file}"
            metadata = {
                "tags": ["ethics", "codex", "contradiction"],
                "emotion": "concerned",
                "meta_layer": "ethics_codex",
                "trust_score": 0.92,
                "heat": 0.75,
                "prediction": "ethical_violation_flagged",
                "actual": str(len(contradictions)),
                "timestamp": result["timestamp"]
            }
            memory_router.store(text, metadata)
            encode_event_to_fabric(text, np.array([0.2, 0.8, 0.1, 0.1]), 0.6, metadata["tags"])

    return flagged_codices


# ============================================================
# AEI Godmode Strategy Conflict Resolver (Standalone)
# ============================================================

class GoalConflictResolver:
    def __init__(self):
        self.resolution_log = []

    def resolve(self, goal_1: dict, goal_2: dict) -> dict:
        print(f"[GOAL CONFLICT] ⚠️ Evaluating conflict:")

        g1_text = goal_1.get("goal") if isinstance(goal_1, dict) else str(goal_1)
        g2_text = goal_2.get("goal") if isinstance(goal_2, dict) else str(goal_2)
        u1 = goal_1.get("urgency", 0.5) if isinstance(goal_1, dict) else 0.5
        u2 = goal_2.get("urgency", 0.5) if isinstance(goal_2, dict) else 0.5

        print(f"  • Goal 1: {g1_text} | Urgency: {u1}")
        print(f"  • Goal 2: {g2_text} | Urgency: {u2}")

        if u1 > u2:
            selected = goal_1
        elif u2 > u1:
            selected = goal_2
        else:
            selected = goal_1 if g1_text < g2_text else goal_2

        timestamp = datetime.utcnow().isoformat()
        self.resolution_log.append({
            "timestamp": timestamp,
            "selected_goal": g1_text if selected == goal_1 else g2_text,
            "rejected_goal": g2_text if selected == goal_1 else g1_text
        })

        print(f"[GOAL CONFLICT] ✅ Selected: {g1_text if selected == goal_1 else g2_text}")
        return selected


def resolve_strategy_conflict(goals: list) -> dict:
    """
    Public utility for resolving multi-goal cognitive or evolutionary conflicts.
    Selects the most urgent (or lexically dominant) goal from the input list.
    """

    if not goals or len(goals) < 2:
        print("[STRATEGY CONFLICT] ⚠️ Not enough goals to resolve.")
        return goals[0] if goals else {}

    # ✅ Sanitize malformed goals
    sanitized_goals = []
    for g in goals:
        if isinstance(g, dict) and "goal" in g:
            sanitized_goals.append(g)
        else:
            sanitized_goals.append({
                "goal": str(g),
                "urgency": 0.5
            })

    resolver = GoalConflictResolver()
    current = sanitized_goals[0]

    for next_goal in sanitized_goals[1:]:
        current = resolver.resolve(current, next_goal)

    final_goal_text = current.get("goal") if isinstance(current, dict) else str(current)
    print(f"[STRATEGY CONFLICT] 🔝 Final resolution: {final_goal_text}")
    return current