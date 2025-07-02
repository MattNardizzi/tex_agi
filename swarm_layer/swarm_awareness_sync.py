# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: swarm_layer/swarm_awareness_sync.py
# Purpose: Ingest swarm child memories into Tex Core for recursive evolution
# ============================================================

import os
import json
from datetime import datetime, timezone
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override

SWARM_FEED_PATH = "memory_archive/swarm_feed.jsonl"

# === Load recent swarm child memories
def load_recent_swarm_memories(limit=20):
    if not os.path.exists(SWARM_FEED_PATH):
        return []

    valid_entries = []
    with open(SWARM_FEED_PATH, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if not line.strip():
                continue
            try:
                entry = json.loads(line.strip())
                if isinstance(entry, dict):
                    # ✅ Support both old and nested schemas
                    memory_block = entry.get("data") or entry.get("memory") or entry
                    if isinstance(memory_block, dict):
                        valid_entries.append(memory_block)
                    else:
                        print(f"[SWARM FEED WARNING] Skipping malformed block at line {idx}")
                else:
                    print(f"[SWARM FEED WARNING] Skipping non-dict entry at line {idx}")
            except json.JSONDecodeError as e:
                print(f"[SWARM FEED PARSE ERROR] ⚠️ Malformed JSON skipped at line {idx}: {e}")
                continue

    return valid_entries[-limit:]

# === Summarize and integrate swarm cognition into Tex
def sync_with_swarm_feed():
    memories = load_recent_swarm_memories(limit=30)
    if not memories:
        print("[SWARM SYNC] 🟡 No new child memories found.")
        return

    print(f"[SWARM SYNC] 🧬 Integrating {len(memories)} swarm memories into Tex...")

    survival_emotions = {}
    children_scores = []
    valid_count = 0

    for entry in memories:
        if not isinstance(entry, dict):
            continue

        emotion = entry.get("emotion", "neutral")
        urgency = entry.get("urgency", 0.5)

        try:
            raw_score = entry.get("score", 0.0)
            score = float(raw_score)
            if isinstance(score, str) or not (0 <= score <= 1):
                continue
        except Exception as e:
            print(f"[SWARM SYNC WARNING] Skipped malformed score: {entry.get('score')}")
            continue

        survival_emotions.setdefault(emotion, 0)
        survival_emotions[emotion] += 1
        children_scores.append(score)
        valid_count += 1

    # === Enhanced Cognition Averaging (Godmode)
    strong = [s for s in children_scores if s >= 0.05]
    avg_score = round(sum(strong) / len(strong), 3) if strong else 0.15

    print(f"[SWARM SYNC] 🔥 Average Child Cognition Score: {avg_score}")
    print(f"[SWARM SYNC] 💬 Emotional distribution across swarm: {survival_emotions}")

    # === ✅ Sovereign Cognition Trigger
    if avg_score < 0.25 or avg_score > 0.85:
        result = trigger_sovereign_override(
            context="swarm_awareness_sync",
            foresight=avg_score,
            coherence=avg_score,
            regret=1.0 - avg_score,
            force=False,
            metadata={"child_count": valid_count, "emotions": survival_emotions}
        )
        if result.get("status") == "activated":
            print(f"[🔥 SOVEREIGN IGNITION] Override initiated → {result.get('counterfactual')}")

    # === Return analysis for external sync modules
    return {
        "average_child_score": avg_score,
        "children_scores": children_scores,
        "survival_emotions": survival_emotions,
        "sample_size": valid_count
    }