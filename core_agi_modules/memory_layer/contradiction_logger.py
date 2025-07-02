# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/memory_layer/contradiction_logger.py
# Tier ΩΩΩ-State FinalX — Reflex Conflict Detector + Memory Heatmap Evaluator
# ============================================================

import hashlib
import difflib
from datetime import datetime

from agentic_ai.sovereign_memory import sovereign_memory
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

# === Local in-memory contradiction log ===
contradiction_log = []

def detect_contradiction(belief_a: str, belief_b: str) -> bool:
    negations = ["not ", "no ", "never ", "cannot "]
    a, b = belief_a.lower(), belief_b.lower()

    for neg in negations:
        if neg in a and b.replace(neg, "") in a:
            return True
        if neg in b and a.replace(neg, "") in b:
            return True
    return False

def log_contradiction(belief_a: str, belief_b: str, context="unknown") -> dict:
    timestamp = datetime.utcnow().isoformat()
    fusion_hash = hashlib.sha256((belief_a + belief_b).encode()).hexdigest()
    similarity = difflib.SequenceMatcher(None, belief_a, belief_b).ratio()
    severity = round(1 - similarity, 4)

    negations = ["not", "never", "no", "cannot"]
    ctype = "negation" if any(n in belief_a.lower() or n in belief_b.lower() for n in negations) else "general"

    entry = {
        "belief_a": belief_a,
        "belief_b": belief_b,
        "context": context,
        "timestamp": timestamp,
        "contradiction_id": fusion_hash,
        "severity": severity,
        "type": ctype
    }

    contradiction_log.append(entry)
    print(f"⚠️ [CONTRADICTION] Logged {ctype} conflict. Severity={severity} | Hash={fusion_hash[:10]}")

    # === Store to Sovereign Memory
    sovereign_memory.store(
        text=f"[CONTRADICTION] '{belief_a}' ⟷ '{belief_b}'",
        metadata={
            "timestamp": timestamp,
            "context": context,
            "severity": severity,
            "type": ctype,
            "contradiction_id": fusion_hash,
            "tags": ["contradiction", "memory_conflict", ctype]
        }
    )

    return entry

def score_conflict_heatmap(event: dict, top_k: int = 10, threshold: float = 0.75) -> float:
    """
    Estimates contradiction density in memory using recent entries.
    Avoids external embedding/vector services. Uses summary similarity.
    """
    try:
        text = event.get("input") or event.get("text") or ""
        if not text.strip():
            return 0.0

        recent_memories = sovereign_memory.recall_recent(hours=3, top_k=top_k)
        conflicts = [
            m for m in recent_memories
            if "contradiction" in m.get("tags", []) or "conflict" in m.get("tags", [])
        ]

        similarity_scores = [
            difflib.SequenceMatcher(None, text, m.get("text", "")).ratio()
            for m in conflicts if "text" in m
        ]

        contradiction_hits = [s for s in similarity_scores if s < 0.65]
        heat_score = round(min(1.0, len(contradiction_hits) / top_k), 4)

        if heat_score >= threshold:
            TEX_SOULGRAPH.imprint_belief(
                belief=f"⚠️ Contradiction heatmap spike detected. Heat={heat_score}",
                source="conflict_heatmap",
                emotion="caution",
                tags=["heatmap", "contradiction", "memory"]
            )

        return heat_score

    except Exception as e:
        print(f"[HEATMAP ERROR] Failed to evaluate contradiction heatmap: {e}")
        return 0.0