# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: self_rewriting/soulgraph_logger.py
# Tier: ΩΩ∞∞ΩΩΩ — Reflex Lineage Writer
# Purpose: Logs new reflex mutations into the soulgraph lineage system for recursive identity traceability.
# ============================================================

import hashlib
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event

SOULGRAPH_LOG_PATH = "data/soulgraph_log.txt"

def log_reflex_to_soulgraph(reflex_metadata: dict, alignment_score: float):
    signature = reflex_metadata.get("signature")
    explanation = reflex_metadata.get("explanation", "")
    timestamp = datetime.utcnow().isoformat()

    # === Generate reflex fingerprint (hash of signature + justification)
    fingerprint = hashlib.sha256(f"{signature}{explanation}".encode()).hexdigest()

    # === Log line for soulgraph ledger
    log_line = (
        f"{timestamp} | MUTATION | {signature} | {fingerprint} "
        f"| Alignment={alignment_score:.3f} | {explanation.strip()}\n"
    )

    # === Write to soulgraph log
    try:
        with open(SOULGRAPH_LOG_PATH, "a") as f:
            f.write(log_line)
        log_event(f"[SOULGRAPH] ✍️ Reflex `{signature}` logged to soulgraph.")
    except Exception as e:
        log_event(f"[SOULGRAPH] ❌ Failed to write to soulgraph log: {e}", level="error")

    # === Store in sovereign memory
    try:
        sovereign_memory.store(
            text=f"Reflex installed: {signature}",
            metadata={
                "timestamp": timestamp,
                "fingerprint": fingerprint,
                "alignment_score": alignment_score,
                "tags": ["mutation", "soulgraph", "reflex_lineage"],
                "meta_layer": "soulgraph_logger"
            }
        )
    except Exception as e:
        log_event(f"[SOULGRAPH] ❌ Failed to store in sovereign memory: {e}", level="error")