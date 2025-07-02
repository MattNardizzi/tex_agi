# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/contradiction_heatmap.py
# Tier: ΩΩΩΩΩΩ∞Ω — Conflict Pressure Mapping Cortex
# ============================================================

import os
from datetime import datetime
from utils.logging_utils import log
from agentic_ai.milvus_memory_router import memory_router
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

# === CONFIG ===
SOULGRAPH_PATH = "data/soulgraph_log.txt"
CATEGORY_TAGS = ["MUTATION", "FORK", "DEBATE", "COMPRESS", "BOOT"]
DECAY_PER_HOUR = 0.95  # temporal decay rate

def extract_timestamp(line: str) -> datetime:
    try:
        return datetime.fromisoformat(line.split("|")[0].strip())
    except Exception:
        return datetime.utcnow()

def run_contradiction_heatmap() -> dict:
    """
    Computes decay-weighted contradiction pressure from soulgraph event log.
    Logs result to Milvus and appends a symbolic belief to TEX_SOULGRAPH.
    Returns normalized contradiction pressure map.
    """
    try:
        if not os.path.exists(SOULGRAPH_PATH):
            log.warning("[HEATMAP] ⚠️ Soulgraph log file not found.")
            return {}

        now = datetime.utcnow()
        tag_scores = {tag.lower(): 0.0 for tag in CATEGORY_TAGS}
        total_weight = 0.0

        with open(SOULGRAPH_PATH, "r") as f:
            for line in f:
                ts = extract_timestamp(line)
                hours_old = max((now - ts).total_seconds() / 3600.0, 0)
                decay_weight = DECAY_PER_HOUR ** hours_old

                for tag in CATEGORY_TAGS:
                    if f"| {tag} |" in line:
                        tag_scores[tag.lower()] += decay_weight
                        total_weight += decay_weight

        if total_weight == 0:
            return {}

        # Normalize pressure values
        heatmap = {k: round(min(v / total_weight, 1.0), 4) for k, v in tag_scores.items()}
        peak_tag = max(heatmap, key=heatmap.get)

        # === Log to Milvus vector memory
        memory_router.store(
            text=f"[HEATMAP] Contradiction heatmap ░ {heatmap} ░ Peak={peak_tag}",
            metadata={
                "type": "contradiction_heatmap",
                "peak": peak_tag,
                "timestamp": now.isoformat(),
                "tags": ["heatmap", "contradiction", "entropy", peak_tag],
                "heat_values": heatmap
            }
        )

        # === Log symbolically into soulgraph
        TEX_SOULGRAPH.imprint_belief(
            belief=f"Contradiction heatmap recorded ░ Peak domain: {peak_tag} ░ Full: {heatmap}",
            source="contradiction_heatmap",
            emotion="tense",
            tags=["conflict_map", "heatmap", peak_tag]
        )

        log.info(f"[HEATMAP] ✅ Normalized contradiction pressure: {heatmap} ░ Max={peak_tag}")
        return heatmap

    except Exception as e:
        log.error(f"[HEATMAP] ❌ Failed to compute contradiction heatmap: {e}")
        return {"error": str(e)}