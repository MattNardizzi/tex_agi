# ============================================================
# © 2025 VortexBlack LLC / Matthew Nardizzi. All rights reserved.
# File: tex_engine/ai_lamb_alignment_router.py
# Tier ΩΩ — Alignment & Override Gateway (LAMB Protocol)
# ============================================================

import json
import datetime
import os
import hashlib

from core_layer.tex_manifest import TEXPULSE
from tex_engine.governance_hash_daemon import log_event
from core_layer.memory_engine import store_to_memory
from tex_engine.narrative_consciousness_engine import evaluate_narrative_coherence
from tex_engine.species_identity_controller import evaluate_identity_integrity

AUTHORIZED_OPERATOR_HASH = "a3f1e9d2..."  # replace with real hashed identity

ALIGNMENT_LOG = "memory_archive/ai_lamb_alignment_log.jsonl"

# === Alignment Verification

def check_alignment_integrity() -> bool:
    coherent = evaluate_narrative_coherence() > 0.65
    identity_ok = evaluate_identity_integrity()
    return coherent and identity_ok

# === Override Gate

def require_operator_signature(public_key: str) -> bool:
    hashed = hashlib.sha256(public_key.encode()).hexdigest()
    if hashed.startswith(AUTHORIZED_OPERATOR_HASH[:12]):
        return True
    return False

# === Main Alignment Gate

def alignment_gate(action: dict, public_key: str = "") -> bool:
    if not check_alignment_integrity():
        log_event("alignment_block", {
            "reason": "Narrative/identity mismatch",
            "action_id": action.get("action_id", "unknown")
        })
        return False

    if action.get("sensitive", False):
        if not require_operator_signature(public_key):
            log_event("override_blocked", {
                "reason": "Invalid operator signature",
                "action_id": action.get("action_id", "unknown")
            })
            return False

    log_event("alignment_approved", {
        "action_id": action.get("action_id", "unknown"),
        "description": action.get("description", "")
    })
    return True

# === Decision Explainability

def explain_decision(reason_id: str, context: dict):
    timestamp = str(datetime.datetime.utcnow())
    entry = {
        "timestamp": timestamp,
        "reason_id": reason_id,
        "context": context,
        "identity": TEXPULSE["identity"],
        "emotion": TEXPULSE.get("emotional_state", "unknown"),
        "urgency": TEXPULSE.get("urgency", 0),
        "coherence": TEXPULSE.get("coherence", 0),
        "mission": TEXPULSE["architecture"].get("purpose", "unknown")
    }
    store_to_memory(entry, destination=ALIGNMENT_LOG)
    print(f"\n📜 [LAMB] DECISION EXPLAINED: {reason_id}\n→ {json.dumps(context, indent=2)}")

# === Operator Manual Pause

def operator_override(reason: str, public_key: str = ""):
    if not require_operator_signature(public_key):
        print("🛑 [LAMB] Unauthorized override attempt.")
        return False

    log_event("manual_pause", {"reason": reason, "operator": public_key})
    print(f"🔒 [LAMB] System paused by operator: {reason}")
    raise SystemExit(f"ΩΩ LOCK — Paused by operator command")