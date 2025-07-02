# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agentic_ai/semantic_contradiction_resolver.py
# Tier: ΩΩΩΩΩ — Semantic Conflict Detector
# Purpose: Detects semantic contradiction by comparing incoming thought against recent vector memory traces.
# ============================================================

from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
import numpy as np

def detect_contradictions(reasoning_chain: list[str]) -> list[str]:
    contradictions = []
    seen = set()

    for line in reasoning_chain:
        norm = line.strip().lower()
        if "not " in norm or "opposite" in norm or "conflict" in norm:
            for prev in seen:
                if prev in norm or norm in prev:
                    contradictions.append(line)
        seen.add(norm)

    return contradictions


def check_contradiction_against_memory(current_thought: str):
    results = memory_router.query(current_thought, top_k=6)
    payloads = [r.payload.get("summary", "").lower() for r in results]

    contradictions = []
    for entry in payloads:
        if (
            "not " in entry or
            "opposite" in entry or
            "conflict" in entry or
            "contradiction" in entry
        ) and current_thought.lower() in entry:
            contradictions.append(entry)

    if contradictions:
        print(f"[CONTRADICTION] ❗ Detected {len(contradictions)} conflict(s) in memory:")
        for c in contradictions:
            print(f" - {c}")

        # ✅ Log contradiction to ChronoFabric
        encode_event_to_fabric(
            raw_text=f"Contradiction detected: '{current_thought}'",
            emotion_vector=np.array([0.1, 0.7, 0.2, 0.0]),
            entropy_level=0.5,
            tags=["contradiction", "memory_conflict", "semantic"]
        )
    else:
        print("[CONTRADICTION] ✅ No direct memory conflicts detected.")

    return contradictions