# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/divergence_mapper.py
# Purpose: Map fork divergence events from simulated variant paths
# Tier: Sovereign Cognition · AEI Aligned · No Further Enhancements Needed
# ============================================================

import os
import json
import time
from datetime import datetime
from hashlib import sha256

# === File Paths ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_DIR = os.path.join(BASE_DIR, "..", "memory_archive")
DIVERGENCE_LOG = os.path.join(MEMORY_DIR, "divergence_map.jsonl")
SUPPRESSED_LOG = os.path.join(MEMORY_DIR, "suppressed_forks.jsonl")
EVOLUTION_LOG = os.path.join(MEMORY_DIR, "evolution_results.jsonl")

os.makedirs(MEMORY_DIR, exist_ok=True)

# === Hash Utility ===
def _hash_context(context):
    try:
        return sha256(json.dumps(context, sort_keys=True).encode("utf-8")).hexdigest()
    except Exception:
        return "invalid_context_hash"

def _hash_fork_id(fork_id):
    try:
        return sha256(fork_id.encode("utf-8")).hexdigest()
    except Exception:
        return "invalid_fork_id_hash"

# === Main Divergence Logger ===
def log_fork_divergence(cycle=None, fork_id=None, divergence_score=None, source_emotion="neutral", context=None):
    """
    Logs a cognitive fork event and evaluates suppression logic.

    Args:
        cycle (int): Cognitive cycle. If None, defaults to 0.
        fork_id (str): Unique forked agent or strategy ID.
        divergence_score (float): Delta from base variant (0.0 = same, 1.0 = fully divergent).
        source_emotion (str): Emotion that influenced the fork.
        context (dict): Optional metadata from sandbox or decision engine.
    """
    cycle = cycle if cycle is not None else 0
    context = context or {}
    context_hash = _hash_context(context)
    fork_hash = _hash_fork_id(fork_id or "unknown")

    entry = {
        "cycle": cycle,
        "fork_id": fork_id,
        "divergence_score": round(divergence_score or 0.0, 4),
        "source_emotion": source_emotion,
        "context": context,
        "context_hash": context_hash,
        "fork_hash": fork_hash,
        "timestamp": datetime.utcnow().isoformat()
    }

    # === Sovereign Suppression Logic
    if divergence_score and divergence_score > 0.95:
        if not context.get("novel_strategy", False):
            suppression = {**entry, "status": "suppressed_due_to_high_instability"}
            try:
                with open(SUPPRESSED_LOG, "a") as f:
                    f.write(json.dumps(suppression) + "\n")
                print(f"[DIVERGENCE MAP] 🚫 Suppressed unstable fork: {fork_id} | Δ: {divergence_score}")
            except Exception as e:
                print(f"[SUPPRESSION LOG ERROR] {e}")
            return  # Exit early

        print(f"[DIVERGENCE MAP] ⚠️ High-divergence allowed due to novelty → Fork: {fork_id}")

    # === Write to Divergence Log
    try:
        with open(DIVERGENCE_LOG, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[DIVERGENCE MAP] 🌐 Cycle {cycle} | Fork: {fork_id} → Δ: {divergence_score}")
    except Exception as e:
        print(f"[DIVERGENCE LOG ERROR] {e}")

    # === Evolution Result Log (used for training overlays or visualization)
    evo_entry = {
        "cycle": cycle,
        "dominant_variant": fork_id,
        "score": round(1.0 - (divergence_score or 0.0), 4),
        "sandbox_pass": divergence_score is not None and divergence_score < 0.75,
        "emotion": source_emotion,
        "timestamp": time.time(),
        "source": "divergence_mapper",
        "id": fork_id
    }

    try:
        with open(EVOLUTION_LOG, "a") as f:
            f.write(json.dumps(evo_entry) + "\n")
    except Exception as evo_err:
        print(f"[EVOLUTION LOG ERROR] Failed to write evolution log: {evo_err}")