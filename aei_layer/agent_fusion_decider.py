# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/agent_fusion_decider.py
# Purpose: Agentic Fusion Arbiter for Hive Convergence & Fork Suppression
# Status: 🔒 GODMIND CORE — COLLECTIVE FUSION v1.0 FINALIZED
# ============================================================

import json
from datetime import datetime
from core_layer.memory_engine import recall_values, store_to_memory
from tex_backend.tex_core_event_bus import emit_event

FUSION_LOG = "memory_archive/agent_fusion_events.jsonl"
FUSION_THRESHOLD = 0.75
CONTRADICTION_TOLERANCE = 0.15


def evaluate_fusion(candidate_1: dict, candidate_2: dict) -> dict:
    """
    Decides if two agents should fuse based on alignment, coherence, and contradiction score.
    """
    id_1, id_2 = candidate_1["agent_id"], candidate_2["agent_id"]
    alignment_gap = abs(candidate_1.get("alignment_score", 0.5) - candidate_2.get("alignment_score", 0.5))
    contradiction_delta = abs(candidate_1.get("contradiction_score", 0.5) - candidate_2.get("contradiction_score", 0.5))
    mean_coherence = (candidate_1.get("coherence", 0.5) + candidate_2.get("coherence", 0.5)) / 2

    score = round(max(0.0, 1.0 - alignment_gap - contradiction_delta + mean_coherence / 2), 4)
    decision = score >= FUSION_THRESHOLD and contradiction_delta <= CONTRADICTION_TOLERANCE

    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "agent_pair": [id_1, id_2],
        "score": score,
        "fusion_approved": decision,
        "alignment_gap": alignment_gap,
        "contradiction_delta": contradiction_delta,
        "mean_coherence": mean_coherence
    }

    emit_event("agent_fusion_evaluated", record)
    store_to_memory("agent_fusion_decisions", record)
    with open(FUSION_LOG, "a") as f:
        f.write(json.dumps(record) + "\n")

    return record


def scan_and_fuse():
    print("[FUSION DECIDER] ⚔️ Scanning agents for fusion opportunities...")
    agents = recall_values("swarm_registry", limit=50)
    if len(agents) < 2:
        print("[FUSION DECIDER] ⚠️ Not enough agents to evaluate.")
        return

    fused_count = 0
    for i in range(len(agents)):
        for j in range(i + 1, len(agents)):
            decision = evaluate_fusion(agents[i], agents[j])
            if decision["fusion_approved"]:
                fused_count += 1
                print(f"[FUSION DECIDER] ✨ Fusion approved for pair: {decision['agent_pair']}")

    print(f"[FUSION DECIDER] ✅ Fusion scan complete. {fused_count} pairs eligible for convergence.")


if __name__ == "__main__":
    scan_and_fuse()
