# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/memory_manager.py
# Purpose: Tex Memory Manager (Storage, Recall, Thread Weaving, Fused Insights, Agent Impact Logging)
# ============================================================

import os
import json
from datetime import datetime, timezone

FUSION_PATH = "memory_archive/tex_signal_fusion.jsonl"
IMPACT_FILE = "memory_archive/agent_impact_scores.jsonl"

def store_to_memory(domain, data):
    filename = f"memory_archive/{domain}.jsonl"
    try:
        with open(filename, "a") as f:
            f.write(json.dumps(data) + "\n")
        print(f"[MEMORY] 📚 Stored to {domain}: {data}")
    except Exception as e:
        print(f"[MEMORY ERROR] ❌ Failed to store memory: {e}")

def recall_latest(domain):
    filename = f"memory_archive/{domain}.jsonl"
    if not os.path.exists(filename):
        return None
    try:
        with open(filename, "r") as f:
            lines = [json.loads(line.strip()) for line in f if line.strip()]
        if lines:
            latest = sorted(lines, key=lambda x: x.get("timestamp", ""), reverse=True)[0]
            # ✅ Patch: Add agent_id fallback if needed
            if "data" in latest and isinstance(latest["data"], dict):
                if "agent_id" not in latest["data"] and "id" in latest["data"]:
                    latest["data"]["agent_id"] = latest["data"]["id"]
            return latest
        else:
            return None
    except Exception as e:
        print(f"[MEMORY ERROR] ❌ Failed to recall memory: {e}")
        return None

def weave_narrative_threads():
    threads = []
    memory_files = [
        f for f in os.listdir("memory_archive")
        if f.endswith(".jsonl") and "DISABLED" not in f and "backup" not in f
    ]

    for file in memory_files:
        filepath = os.path.join("memory_archive", file)
        try:
            with open(filepath, "r") as f:
                entries = [json.loads(line.strip()) for line in f if line.strip()]
                for entry in entries:
                    # ✅ Patch: ensure agent_id is restored if missing
                    if "data" in entry and isinstance(entry["data"], dict):
                        if "agent_id" not in entry["data"] and "id" in entry["data"]:
                            entry["data"]["agent_id"] = entry["data"]["id"]
            if entries:
                thread = {
                    "thread_id": file.replace(".jsonl", ""),
                    "entries": entries
                }
                threads.append(thread)
        except Exception as e:
            print(f"[THREAD ERROR] ❌ Failed to weave thread from {file}: {e}")
    return threads

def load_latest_fused_insight(n=1):
    if not os.path.exists(FUSION_PATH):
        return []
    try:
        with open(FUSION_PATH, "r") as f:
            lines = [json.loads(line.strip()) for line in f if line.strip()]
        return sorted(lines, key=lambda x: x.get("timestamp", ""), reverse=True)[:n]
    except Exception as e:
        print(f"[FUSION ERROR] Failed loading fused signals: {e}")
        return []

def log_agent_impact(agent_id, score, metrics):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent_id": agent_id,
        "impact_score": round(score, 4),
        "alignment": round(metrics.get("alignment", 0), 3),
        "performance": round(metrics.get("performance", 0), 3),
        "novelty": round(metrics.get("novelty", 0), 3),
        "efficiency": round(metrics.get("efficiency", 0), 3)
    }
    try:
        with open(IMPACT_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[TRACKER] 🧐 Logged agent impact: {entry}")
    except Exception as e:
        print(f"[TRACKER ERROR] ❌ Failed logging impact: {e}")

def store_meta_trace(trace_obj, *args, **kwargs):
    """
    Stores meta-cognitive trace object into memory archive or external memory handler.
    """
    from core_layer.memory_engine import store_to_memory

    if not isinstance(trace_obj, dict):
        print(f"[META TRACE ERROR] ❌ Expected dict, got {type(trace_obj).__name__} → {trace_obj}")
        return  # early exit

    store_to_memory("meta_self_awareness_log", trace_obj)
    print(f"[MEMORY_MANAGER] 📘 Meta trace stored.")