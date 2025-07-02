# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/goal_filter.py
# Purpose: Tex-Class AGI Goal Filter — Priority-Preserving, Tag-Diverse, Time-Decaying
# ============================================================

import os
import json
from typing import List, Dict
from datetime import datetime
from sentence_transformers import SentenceTransformer, util
from core_layer.memory_engine import store_to_memory

# === Config ===
GOAL_FILE = "memory_archive/autonomous_goals.jsonl"
SIM_THRESHOLD = 0.81
GOAL_EXPIRY_HOURS = 24
MODEL = SentenceTransformer("all-MiniLM-L6-v2")

# === Load & Save ===

def load_goals() -> List[Dict]:
    if not os.path.exists(GOAL_FILE):
        return []
    with open(GOAL_FILE, "r") as f:
        return [json.loads(line) for line in f if line.strip()]

def save_goals(goals: List[Dict]) -> None:
    os.makedirs(os.path.dirname(GOAL_FILE), exist_ok=True)
    with open(GOAL_FILE, "w") as f:
        for g in goals:
            f.write(json.dumps(g) + "\n")

# === Utility ===

def decay_priority(original: float, age_hours: float) -> float:
    decay_factor = 0.95 ** age_hours
    return round(original * decay_factor, 3)

def parse_iso_timestamp(ts_raw: str) -> datetime:
    if not isinstance(ts_raw, str):
        raise ValueError("Timestamp is not a string.")
    return datetime.fromisoformat(ts_raw)

# === Main Filtering Logic ===

def filter_goals(goals: List[Dict]) -> List[Dict]:
    if not goals:
        print("[GOAL FILTER] ⚠️ Input goal list is empty.")
        return []

    now = datetime.utcnow()  # Offset-naive to match parsed timestamps
    kept = []
    seen = set()
    dropped_due_to_expiry = 0
    dropped_due_to_similarity = 0

    valid_goals = [g for g in goals if isinstance(g, dict) and "goal" in g]
    texts = [g["goal"] for g in valid_goals]

    if not texts:
        print("[GOAL FILTER] ❌ No valid goal text found in input.")
        return []

    embeddings = MODEL.encode(texts, convert_to_tensor=True)
    if embeddings.device.type != "cpu":
        embeddings = embeddings.cpu()
    sim_matrix = util.pytorch_cos_sim(embeddings, embeddings).numpy()

    for i, g1 in enumerate(valid_goals):
        if i in seen:
            continue

        try:
            ts = parse_iso_timestamp(g1.get("timestamp", ""))
            age_hours = (now - ts).total_seconds() / 3600
            if age_hours > GOAL_EXPIRY_HOURS:
                dropped_due_to_expiry += 1
                continue
            g1["decayed_priority"] = decay_priority(g1.get("priority", 0.0), age_hours)
        except Exception as e:
            print(f"[FILTER WARNING] Timestamp error: {e}")
            continue

        similar_indices = [j for j, sim in enumerate(sim_matrix[i]) if j != i and sim >= SIM_THRESHOLD]
        top_candidate = g1
        top_index = i

        for j in similar_indices:
            g2 = valid_goals[j]
            if j in seen:
                continue
            try:
                ts_j = parse_iso_timestamp(g2.get("timestamp", ""))
                age_j = (now - ts_j).total_seconds() / 3600
                decayed_j = decay_priority(g2.get("priority", 0.0), age_j)
                g2["decayed_priority"] = decayed_j
                if decayed_j > top_candidate["decayed_priority"]:
                    top_candidate = g2
                    top_index = j
            except:
                continue

        kept.append(top_candidate)
        seen.add(top_index)
        seen.update(similar_indices)
        dropped_due_to_similarity += len(similar_indices)

    save_goals(kept)
    print(f"[GOAL FILTER] ✅ {len(kept)} goals retained | 🗑️ {dropped_due_to_expiry} expired | 🤖 {dropped_due_to_similarity} redundant")

    store_to_memory("goal_filter_summary", {
        "retained": len(kept),
        "expired": dropped_due_to_expiry,
        "redundant": dropped_due_to_similarity,
        "timestamp": now.isoformat()
    })

    return kept