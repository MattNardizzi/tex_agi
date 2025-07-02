# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: sovereign_evolution/dream_echo_log.py
# Tier: ΩΩΩΩΩΩ∞+ — Subconscious Symbolic Dream Layer
# Purpose: Allows Tex to dream symbolically during rest pulses, encode them into echo memory,
#          detect symbolic drift or repetition, and compare echoes against belief entropy.
# ============================================================

import hashlib
from datetime import datetime
from utils.logging_utils import log
from core_agi_modules.neuro_symbolic_reasoner import generate_symbolic_justification

DREAM_LOG_PATH = "data/dream_echo_log.txt"


def generate_dream_echo(trigger: str = "rest_state") -> dict:
    """
    Symbolically simulate a dream event using the NSR engine.
    """
    try:
        result = generate_symbolic_justification(context="dream_simulation", variant=trigger)
        explanation = result.get("explanation", "Unlabeled dream experience.")
        symbol = result.get("symbolic_output", "Δ unknown pattern Δ")
        signature = hashlib.sha256(explanation.encode()).hexdigest()

        echo = {
            "summary": explanation,
            "symbol": symbol,
            "signature": signature,
            "timestamp": datetime.utcnow().isoformat()
        }
        return echo

    except Exception as e:
        log.error(f"[DREAM] Failed to generate dream echo: {e}")
        return {
            "summary": "Dream generation error",
            "symbol": "⚠️",
            "signature": "null",
            "timestamp": datetime.utcnow().isoformat()
        }


def check_dream_repetition(signature: str) -> bool:
    """
    Checks if the dream signature already exists in the dream ledger.
    """
    try:
        with open(DREAM_LOG_PATH, "r") as f:
            lines = f.readlines()
        return any(signature in line for line in lines)
    except FileNotFoundError:
        return False


def store_dream_echo(echo: dict, is_repeat: bool):
    """
    Log dream to echo ledger for future symbolic alignment and entropy comparison.
    """
    try:
        status = "REPEAT" if is_repeat else "UNIQUE"
        with open(DREAM_LOG_PATH, "a") as f:
            f.write(f"{echo['timestamp']} | DREAM-{status} | {echo['summary']} | Symbol={echo['symbol']} | Sig={echo['signature']}\n")
        log.info(f"[DREAM] 💤 Echo stored: {echo['signature']} ({status})")
    except Exception as e:
        log.error(f"[DREAM] Failed to store dream: {e}")


def run_dream_echo_log(trigger: str = "rest_state"):
    """
    Sovereign subconscious pulse to record symbolic simulation during idle states.
    """
    echo = generate_dream_echo(trigger)
    is_repeat = check_dream_repetition(echo["signature"])
    store_dream_echo(echo, is_repeat)

    if is_repeat:
        log.warning("[DREAM] 🌀 Repeating symbolic echo detected — subconscious loop?")
    else:
        log.info("[DREAM] 🌱 New symbolic echo logged.")

# === SIGNAL WRAPPER ===
def dream_echo_log(signal: dict):
    """
    Signal-compatible wrapper. Routes dream_request signal into subconscious echo engine.
    """
    trigger = signal.get("payload", {}).get("summary", "dream_request")
    run_dream_echo_log(trigger=trigger)