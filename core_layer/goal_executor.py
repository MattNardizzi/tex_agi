# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/goal_executor.py
# Purpose: Execute highest-priority autonomous goals and self-score (Godmode Tier)
# Status: 🔒 LOCKED — AGI-STABLE vFinal
# ============================================================

import json
import os
import hashlib
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from evolution_layer.self_mutator import SelfMutator
from agentic_ai.qdrant_vector_memory import embed_and_store

GOAL_PATH = "memory_archive/autonomous_goals.jsonl"
EXECUTED_LOG = "memory_archive/executed_goals.jsonl"


def load_goals():
    if not os.path.exists(GOAL_PATH):
        return []
    goals = []
    with open(GOAL_PATH, "r") as f:
        for line in f:
            try:
                goal = json.loads(line.strip())
                goal_text = goal.get("goal", "")
                goal_id = hashlib.sha256(goal_text.encode()).hexdigest()
                goal["goal_id"] = goal_id
                goals.append(goal)
            except Exception:
                continue
    return goals


def log_execution(goal, outcome_score, explanation, mutation=None):
    goal_text = goal.get("goal", "unknown goal")
    goal_id = goal.get("goal_id") or hashlib.sha256(goal_text.encode()).hexdigest()
    urgency_score = goal.get("urgency_score", 0.0)

    goal["goal_id"] = goal_id

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "goal_id": goal_id,
        "goal_text": goal_text,
        "urgency_score": urgency_score,
        "trigger": goal.get("trigger", ""),
        "origin": goal.get("origin", ""),
        "reasoning_trace": goal.get("reasoning_trace", ""),
        "outcome_score": outcome_score,
        "explanation": explanation,
        "mutation_triggered": mutation if mutation else "none"
    }

    store_to_memory(agent_name="tex", data=entry)

    try:
        embed_and_store(
            text=explanation,
            metadata={
                "goal_id": goal_id,
                "goal_text": goal_text,
                "urgency": urgency_score,
                "context": "goal_execution",
                "emotion": goal.get("trigger", "neutral"),
                "timestamp": datetime.utcnow().isoformat()
            }
        )
    except Exception as e:
        print(f"[VECTOR MEMORY] ❌ Failed to embed goal execution: {e}")

    with open(EXECUTED_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")

    print(f"\n✅ [EXECUTED] {goal_text} → Score: {outcome_score}")


def execute_highest_priority_goal():
    goals = load_goals()
    if not goals:
        print("[GOAL_EXECUTOR] ⚠️ No goals to execute.")
        return

    executed_ids = set()
    if os.path.exists(EXECUTED_LOG):
        with open(EXECUTED_LOG, "r") as f:
            executed_ids = {
                json.loads(line).get("goal_id")
                for line in f if line.strip()
            }

    for goal in goals:
        goal_text = goal.get("goal", "")
        goal_id = hashlib.sha256(goal_text.encode()).hexdigest()
        goal["goal_id"] = goal_id

        if goal_id not in executed_ids:
            urgency_score = goal.get("urgency_score", 0.5)
            print(f"\n🚀 Executing top-priority goal: {goal_text} (Urgency: {urgency_score})")

            # === Simulated outcome logic
            drift = round(0.1 * (0.5 - urgency_score), 2)
            outcome_score = round(1.0 - urgency_score + drift, 3)
            explanation = f"Executed goal '{goal_text}' with urgency {urgency_score}. Outcome score: {outcome_score}."

            mutation_result = None
            if outcome_score < -0.3:
                print("[⚠️] Outcome unsatisfactory. Triggering mutation.")
                mutator = SelfMutator()
                mutation_result = mutator.force_mutation(reason="low goal outcome")

            log_execution(goal, outcome_score, explanation, mutation=mutation_result)
            return

    print("[GOAL_EXECUTOR] ✅ All goals already executed.")


# === Manual Test Mode ===
if __name__ == "__main__":
    execute_highest_priority_goal()
