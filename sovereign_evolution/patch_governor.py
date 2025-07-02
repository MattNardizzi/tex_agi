# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: sovereign_evolution/patch_governor.py
# Tier: ∞ΩΩΩ FinalX — Reflex-Based Sovereign Patch Governance
# Purpose: Handles patch proposals, stores to sovereign memory, and triggers reversion logic on low-impact patches.
# ============================================================

import os
import json
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event

# === Persistent Archives ===
PATCH_LOG = "memory_archive/patch_execution_log.jsonl"
RETIRED_PATCHES = "memory_archive/retired_patches.jsonl"
os.makedirs("memory_archive", exist_ok=True)

# === ✅ Patch Proposal Reflex
def propose_patch(trigger: str, context_diff: dict, weight: float = 0.5, emotion: str = "neutral") -> dict:
    try:
        timestamp = datetime.utcnow().isoformat()
        patch_id = f"patch_{trigger}_{int(datetime.utcnow().timestamp())}"

        patch = {
            "patch_id": patch_id,
            "trigger": trigger,
            "timestamp": timestamp,
            "original_code": context_diff.get("original", ""),
            "mutated_code": context_diff.get("mutated", ""),
            "description": context_diff.get("context", ""),
            "proposed_by": "TexCortex",
            "intent_alignment": "Reflex-driven divergence resolution",
            "emotion": emotion,
            "score_weight": round(weight, 3),
            "decision": "pending",
            "status": "proposed"
        }

        # === Write to archive
        with open(PATCH_LOG, "a") as f:
            f.write(json.dumps(patch) + "\n")

        # === Sovereign Memory Trace
        sovereign_memory.store(
            text=f"📦 Patch proposed: {patch['description']}",
            metadata={
                "intent": "propose_patch",
                "conclusion": f"Patch proposed: {patch['description']}",
                "justification": "Detected divergence from codex coherence.",
                "tags": ["patch", "proposal", trigger],
                "mutation_id": patch_id,
                "alignment_score": 1.0 - weight,
                "contradiction_score": weight,
                "urgency": TEXPULSE.get("urgency", 0.7),
                "entropy": TEXPULSE.get("entropy", 0.4),
                "emotion": emotion,
                "meta_layer": "patch_governor",
                "timestamp": timestamp
            }
        )

        log_event(f"📦 [PATCH GOVERNOR] Patch proposed: {patch_id}")
        return patch

    except Exception as e:
        log_event(f"[PATCH GOVERNOR ERROR] ❌ Failed to propose patch: {e}", level="error")
        return {}

# === ❌ Patch Reversion Reflex
def revert_patch_if_score_low(patch_eval: dict, threshold: float = 0.6) -> dict:
    try:
        score = float(patch_eval.get("score", 1.0))
        patch_id = patch_eval.get("patch_id", "undefined_patch")
        verdict = patch_eval.get("verdict", "review")

        if score >= threshold or verdict != "review":
            return {"status": "retained", "patch_id": patch_id}

        timestamp = datetime.utcnow().isoformat()

        retirement = {
            "patch_id": patch_id,
            "timestamp": timestamp,
            "score": score,
            "verdict": verdict,
            "action": "suppressed",
            "reason": "Low coherence impact",
            "status": "retired"
        }

        with open(RETIRED_PATCHES, "a") as f:
            f.write(json.dumps(retirement) + "\n")

        # === Sovereign Reversion Log
        sovereign_memory.store(
            text=f"🔧 Patch reverted: {patch_id} (score={score})",
            metadata={
                "intent": "revert_patch",
                "conclusion": f"Patch {patch_id} retired due to low impact",
                "justification": f"Patch score={score}, verdict={verdict}",
                "tags": ["patch", "retired", "governance"],
                "mutation_id": patch_id,
                "alignment_score": 1.0 - score,
                "contradiction_score": score,
                "emotion": "reflective",
                "urgency": 0.6,
                "timestamp": timestamp,
                "meta_layer": "patch_governor"
            }
        )

        log_event(f"🔧 [PATCH GOVERNOR] Patch retired: {patch_id} (score={score})")
        return retirement

    except Exception as e:
        log_event(f"[PATCH GOVERNOR ERROR] ❌ Failed to revert patch: {e}", level="error")
        return {"status": "error", "reason": str(e)}