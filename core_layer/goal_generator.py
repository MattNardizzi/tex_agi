# ===========================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/goal_generator.py
# Purpose: Autonomous emotional+reasoning-driven goal generation (VORTEX PRIME MODE)
# Status: 🔒 LOCKED - GODMODE vFinal
# ===========================================================

import os
import json
from datetime import datetime
from sentence_transformers import SentenceTransformer
from agentic_ai.milvus_memory_router import memory_router

# === Config ===
QDRANT_COLLECTION = "tex_reasoning_memory"
GOAL_OUTPUT = "memory_archive/autonomous_goals.jsonl"
MEMORY_LOG = "memory_archive/evaluation_history.json"
GOAL_SEED_SOURCE = "InternalMemory"

# === Live Systems ===
embedder = SentenceTransformer("all-MiniLM-L6-v2")


# === Static Trigger Themes ===
STATIC_TRIGGERS = {
    "crash": "Reinforce crash-resistance strategy",
    "panic": "Stabilize sentiment and reduce volatility",
    "bullish": "Expand into momentum sectors",
    "inflation": "Rebalance fixed income exposure",
    "interest rates": "Hedge against rate shock scenarios",
    "AI": "Investigate AGI acceleration signals",
    "regret": "Audit past decisions for correction",
    "contradiction": "Resolve conflicting internal logic",
    "fork": "Simulate timeline divergence and response",
    "sovereign": "Recalibrate self-override readiness"
}

# === Urgency Mapping ===
def assign_urgency(goal_text, source, emotion="neutral", urgency_raw=0.5):
    base = urgency_raw
    if "panic" in goal_text.lower() or "crash" in goal_text.lower():
        base += 0.3
    if emotion in ["fear", "anger"]:
        base += 0.2
    if emotion == "joy":
        base -= 0.1
    if source == "InternalMemory":
        base += 0.05
    return round(min(max(base, 0.0), 1.0), 2)

# === Qdrant Vector Query ===
def query_vector_memory_for_goals(query_text="adaptive strategy", top_k=12):
    try:
        results = memory_router.query(query_text, top_k=top_k)
        return results
    except Exception as e:
        print(f"[❌ VECTOR SEARCH ERROR] {e}")
        return []



# === Reasoning Trace Goal Generator ===
def generate_goals_from_reasoning_traces():
    results = query_vector_memory_for_goals()
    goals = []

    for match in results:
        reasoning = match.get("summary", "").lower()
        timestamp = match.get("timestamp", datetime.utcnow().isoformat())

        matched_static = False
        for trigger, goal_text in STATIC_TRIGGERS.items():
            if trigger in reasoning:
                urgency = assign_urgency(goal_text, "VectorMemory", "neutral", 0.7)
                goals.append({
                    "goal": goal_text,
                    "trigger": trigger,
                    "origin": timestamp,
                    "urgency_score": urgency,
                    "reasoning_trace": reasoning[:300],
                    "timestamp": datetime.utcnow().isoformat()
                })
                matched_static = True
                break

        if not matched_static:
            dynamic_goal = f"Investigate reasoning: '{reasoning[:80]}...'"
            urgency = assign_urgency(dynamic_goal, "InternalMemory", "curiosity", 0.5)
            goals.append({
                "goal": dynamic_goal,
                "trigger": "emergent",
                "origin": timestamp,
                "urgency_score": urgency,
                "reasoning_trace": reasoning[:300],
                "timestamp": datetime.utcnow().isoformat()
            })

    return goals

# === Evaluation History Goal Seeding ===
def generate_goals_from_memory_seeds():
    if not os.path.exists(MEMORY_LOG):
        return []

    with open(MEMORY_LOG, "r") as f:
        try:
            memory = json.load(f)
        except json.JSONDecodeError:
            return []

    goals = []
    for item in memory:
        if item.get("type") == "goal_seed":
            urgency = assign_urgency(item.get("goal", "Exploratory expansion"), "ExternalSeed", "neutral", 0.6)
            goals.append({
                "goal": item.get("goal", "Exploratory expansion"),
                "origin": item.get("source", GOAL_SEED_SOURCE),
                "urgency_score": urgency,
                "reasoning_trace": item.get("headline", "N/A")[:300],
                "timestamp": item.get("timestamp", datetime.utcnow().isoformat())
            })

    return goals

# === Master Generator ===
def generate_autonomous_goals():
    print("[🧠] Generating autonomous goals...")
    vector_goals = generate_goals_from_reasoning_traces()
    seed_goals = generate_goals_from_memory_seeds()
    combined = vector_goals + seed_goals

    # Fallback seed injection if nothing was generated
    if not combined:
        print("[🟡] No goals generated. Injecting fallback sentinel.")
        fallback_goal = {
            "goal": "Stabilize reasoning engine through fallback strategy",
            "trigger": "fallback",
            "origin": "EmergencySeed",
            "urgency_score": 0.65,
            "reasoning_trace": "Self-healing fallback triggered by null cognitive state.",
            "timestamp": datetime.utcnow().isoformat()
        }
        combined.append(fallback_goal)

    # Deduplication and normalization
    seen = set()
    unique_goals = []
    for goal in combined:
        key = goal["goal"]
        if key not in seen and "cycle" not in key.lower():
            goal["urgency"] = goal.get("urgency_score", 0.5)
            unique_goals.append(goal)
            seen.add(key)

    prioritized = sorted(unique_goals, key=lambda g: g["urgency"], reverse=True)
    os.makedirs("memory_archive", exist_ok=True)

    with open(GOAL_OUTPUT, "a") as f:
        for g in prioritized:
            f.write(json.dumps(g) + "\n")

    print(f"[🎯] Generated {len(prioritized)} autonomous goal(s):")
    for g in prioritized:
        print(f"  → {g['goal']} (Urgency: {g['urgency']})")

    return prioritized

# === CLI Hook ===
if __name__ == "__main__":
    generate_autonomous_goals()
    try:
        from core_layer.goal_prioritizer import prioritize_goals
        from core_layer.goal_filter import load_goals
        filtered = filter_goals(load_goals())
        prioritize_goals(filtered)
    except Exception as e:
        print(f"[ERROR] Failed to prioritize goals: {e}")