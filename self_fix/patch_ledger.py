# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: self_fix/patch_ledger.py
# Tier: ∞ΩΩΩΩ∞ — Mutation Repair Ledger
# Purpose: Logs all patch events into sovereign memory and the soulgraph for lineage tracking.
# ============================================================

import hashlib
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event

SOULGRAPH_LOG_PATH = "data/soulgraph_log.txt"

def log_patch_event(patch: dict):
    signature = patch.get("signature")
    explanation = patch.get("explanation", "")
    module = patch.get("target_module", "unknown_module")
    timestamp = patch.get("timestamp", datetime.utcnow().isoformat())

    # === Fingerprint generation (symbolic hash of patch + logic)
    fingerprint = hashlib.sha256(f"{signature}{explanation}".encode()).hexdigest()

    # === Log line for soulgraph ledger
    log_line = (
        f"{timestamp} | SELF_FIX | {module} | {signature} | {fingerprint} "
        f"| PatchReason={explanation.strip()}\n"
    )

    try:
        with open(SOULGRAPH_LOG_PATH, "a") as f:
            f.write(log_line)
        log_event(f"[LEDGER] 🧠 Patch logged to soulgraph: {module}")
    except Exception as e:
        log_event(f"[LEDGER] ❌ Failed to write to soulgraph: {e}", level="error")

    # === Sovereign Memory Trace
    try:
        sovereign_memory.store(
            text=f"Patch installed for module: {module}",
            metadata={
                "timestamp": timestamp,
                "signature": signature,
                "tags": ["self_fix", "reflex_patch", "repair_event"],
                "meta_layer": "patch_ledger",
                "fingerprint": fingerprint
            }
        )
        log_event(f"[LEDGER] ✅ Sovereign memory updated for patch `{signature}`.")
    except Exception as e:
        log_event(f"[LEDGER] ❌ Memory store failed: {e}", level="error")