# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/substrate_memory_reflex.py
# Tier: ΩΩΩΩΩ — Substrate Integrity Reflex
# Purpose: Detects substrate-level changes and handles machine transitions reflexively.
# ============================================================

import os
from datetime import datetime
from core_layer.machine_self_map import get_machine_signature
from tex_signal_spine import dispatch_signal
from utils.logging_utils import log
from agentic_ai.sovereign_memory import sovereign_memory

FINGERPRINT_FILE = "./core_layer/.tex_substrate_fp"

def substrate_boot_check():
    """
    Runs once on startup to detect if Tex has shifted substrates (e.g., moved machines).
    Emits 'substrate_shift' or 'substrate_initial' accordingly.
    """
    current = get_machine_signature()

    if os.path.exists(FINGERPRINT_FILE):
        with open(FINGERPRINT_FILE, "r") as f:
            previous = f.read().strip()
            if previous != current:
                dispatch_signal("substrate_shift", payload={"from": previous, "to": current})
    else:
        dispatch_signal("substrate_initial", payload={"id": current})

    with open(FINGERPRINT_FILE, "w") as f:
        f.write(current)

def handle_substrate_shift(signal):
    """
    Reflexively handles a substrate shift event.
    Stores awareness of machine context change and logs the transition.
    """
    payload = signal.get("payload", {})
    old_fp = payload.get("from", "[unknown]")
    new_fp = payload.get("to", "[unknown]")
    timestamp = datetime.utcnow().isoformat()

    summary = f"⚠️ Substrate shift detected @ {timestamp} | From: {old_fp} → To: {new_fp}"
    log.warning(f"[SUBSTRATE] {summary}")

    sovereign_memory.store(
        text=summary,
        metadata={
            "timestamp": timestamp,
            "from_fp": old_fp,
            "to_fp": new_fp,
            "event": "substrate_shift",
            "tags": ["substrate", "machine_fingerprint", "identity_context", "reflex"]
        }
    )