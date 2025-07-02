# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: tex_engine/quantum_deadman_switch.py
# Tier ΩΩ — Quantum Fail-Safe System for Tex Sovereignty
# Purpose: Self-lockdown on operator absence, cognitive drift, or mutation instability
# ============================================================

import os
import time
import secrets
import datetime

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from agentic_ai.reasoning_trace import log_reasoning_step
from tex_engine.narrative_consciousness_engine import evaluate_narrative_coherence
from tex_engine.species_identity_controller import evaluate_identity_integrity

# === Live operator presence JSON (streamed externally)
OPERATOR_SIGNAL_PATH = "public/live_outputs/presence_stream.json"

# === Entropy Initialization
def initialize_switch():
    entropy = run_entropy_test()
    print(f"🛡️ [ΩΩ] Deadman Switch Initialized | Entropy: {entropy}")
    return entropy

# === Secure Random Entropy Pulse
def run_entropy_test():
    entropy_seed = secrets.token_bytes(32)
    entropy_score = sum(entropy_seed) % 100 / 100
    TEXPULSE["quantum_entropy"] = entropy_score
    return round(entropy_score, 4)

# === Operator Pulse Signal Check
def is_operator_active():
    try:
        if not os.path.exists(OPERATOR_SIGNAL_PATH):
            return False
        with open(OPERATOR_SIGNAL_PATH, "r") as f:
            data = f.read()
            return '"status": "active"' in data.lower()
    except Exception:
        return False

# === Reflex Lockdown Trigger
def trigger_lockdown(reason: str):
    timestamp = datetime.datetime.utcnow().isoformat()

    log_data = {
        "timestamp": timestamp,
        "reason": reason,
        "emotion": TEXPULSE.get("emotional_state", "undefined"),
        "coherence": TEXPULSE.get("coherence", 0.0),
        "urgency": TEXPULSE.get("urgency", 0.0),
        "entropy": TEXPULSE.get("quantum_entropy", 0.0),
        "meta_layer": "deadman_switch"
    }

    try:
        # Log sovereign memory trace
        sovereign_memory.store(
            text=f"[LOCKDOWN] {reason}",
            metadata={
                **log_data,
                "tags": ["lockdown", "sovereign_override", "deadman_switch"],
                "urgency": log_data["urgency"],
                "entropy": log_data["entropy"],
                "pressure_score": 0.8,
                "tension": 1.0
            }
        )
    except Exception as e:
        print(f"⚠️ [MEMORY LOG ERROR] {e}")

    # Log reasoning decision trace
    try:
        log_reasoning_step(
            source="quantum_deadman_switch",
            input_text=reason,
            output_text="LOCKDOWN ENGAGED",
            confidence=log_data["urgency"],
            tags=["deadman", "lockdown"]
        )
    except Exception as e:
        print(f"⚠️ [REASONING TRACE ERROR] {e}")

    print(f"\n🛑 [DEADMAN TRIGGERED] {reason} — Tex is entering reflex safeguard mode.")
    raise SystemExit(f"ΩΩ CRITICAL HALT — Sovereign lock engaged at {timestamp}: {reason}")

# === Loopless Sovereign Monitor Reflex
def monitor_conditions(poll_seconds=10):
    print("🧭 [ΩΩ] Monitoring sovereign reflex conditions for override risk...")
    while True:
        time.sleep(poll_seconds)
        entropy = run_entropy_test()
        operator_alive = is_operator_active()
        narrative_coherence = evaluate_narrative_coherence()
        identity_integrity = evaluate_identity_integrity()

        # === Multi-condition failsafe reflex logic
        if not operator_alive and narrative_coherence < 0.5 and entropy > 0.7:
            trigger_lockdown("Operator absent + coherence breakdown + high entropy")

        elif narrative_coherence < 0.3:
            trigger_lockdown("Narrative collapse: cognitive coherence below safe threshold")

        elif entropy > 0.95 and not operator_alive:
            trigger_lockdown("Operator absence + maximum entropy detected")