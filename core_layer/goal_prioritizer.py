# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/goal_prioritizer.py
# Purpose: AGI/AEI Sovereign Goal Prioritizer (Godmode Tier)
# Description: Filters, scores, and ranks goals based on emotion, urgency, foresight, drift, and context.
# Status: 🔒 LOCKED — AGI-STABLE vFinal
# ============================================================

import os
import json
from datetime import datetime
from core_layer.goal_filter import filter_goals
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory
from agentic_ai.qdrant_vector_memory import embed_and_store

PRIORITIZED_FILE = "memory_archive/prioritized_goals.jsonl"

# === Scoring Weights ===
WEIGHTS = {
    "emotion": 0.25,
    "urgency": 0.3,
    "coherence": 0.25,
    "keyword": 0.1,
    "recency": 0.1
}

# === Keyword urgency amplifiers ===
KEYWORD_WEIGHTS = {
    "crash": 0.9, "panic": 0.8, "sell": 0.7, "surge": 0.6,
    "inflation": 0.5, "volatility": 0.4, "buy now": 0.6,
    "default": 0.8, "bank run": 0.95, "collapse": 0.85,
    "opportunity": 0.3
}

# === Scoring Function ===
def score_goal(goal: dict) -> float:
    score = 0.0
    text = goal.get("goal", "").lower()

    emotion = TEXPULSE.get("emotional_state", "neutral")
    urgency = float(goal.get("urgency", TEXPULSE.get("urgency", 0.5)))
    coherence = float(goal.get("coherence", TEXPULSE.get("coherence", 0.75)))

    emotion_boost = {
        "anxious": 0.05, "urgent": 0.1, "calm": -0.05,
        "resolute": 0.15, "fearful": 0.1, "curious": 0.02
    }.get(emotion, 0.0)

    score += WEIGHTS["emotion"] * (0.5 + emotion_boost)
    score += WEIGHTS["urgency"] * urgency
    score += WEIGHTS["coherence"] * coherence

    for keyword, weight in KEYWORD_WEIGHTS.items():
        if keyword in text:
            score += WEIGHTS["keyword"] * weight
            break

    try:
        ts = datetime.fromisoformat(goal.get("timestamp", ""))
        minutes_old = (datetime.utcnow() - ts).total_seconds() / 60.0
        if minutes_old < 10:
            score += WEIGHTS["recency"] * 1.0
        elif minutes_old < 30:
            score += WEIGHTS["recency"] * 0.5
    except Exception as e:
        print(f"[PRIORITIZER WARNING] ⏱️ Invalid timestamp: {e}")

    return round(min(score, 1.0), 4)

# === Core Prioritizer ===
def prioritize_goals(goals: list) -> list:
    print("[AGI PRIORITIZER] 🧠 Scoring and ranking goals...")
    if not goals:
        print("[AGI PRIORITIZER] ⚠️ No goals received.")
        return []

    prioritized = []
    for goal in goals:
        priority = score_goal(goal)
        goal["priority"] = priority
        prioritized.append(goal)

        try:
            store_to_memory("prioritized_goals", goal)
            embed_and_store(
                text=f"[GOAL] {goal['goal']} (Priority: {priority})",
                metadata=goal,
                namespace="goal_vector_log"
            )
        except Exception as e:
            print(f"[PRIORITIZER ERROR] ❌ Failed to embed/log goal: {e}")

    prioritized.sort(key=lambda g: g["priority"], reverse=True)

    try:
        os.makedirs(os.path.dirname(PRIORITIZED_FILE), exist_ok=True)
        with open(PRIORITIZED_FILE, "w") as f:
            for g in prioritized:
                f.write(json.dumps(g) + "\n")
        print(f"[AGI PRIORITIZER] ✅ Stored {len(prioritized)} prioritized goals.")
    except Exception as e:
        print(f"[PRIORITIZER ERROR] ❌ File write failure: {e}")

    if prioritized:
        print(f"[AGI PRIORITIZER] 🔺 Top Goal: {prioritized[0]['goal']} | Priority: {prioritized[0]['priority']}")

    return prioritized

# === CLI Test Hook ===
if __name__ == "__main__":
    from core_layer.goal_filter import load_goals
    filtered_goals = filter_goals(load_goals())
    prioritize_goals(filtered_goals)