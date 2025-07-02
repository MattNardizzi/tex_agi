# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: core_layer/reflex_patch_resolver.py
# Purpose: Diagnose override/mutation stalls and suggest safe recovery patches
# ============================================================

from datetime import datetime
import hashlib

# Memory of recent overrides to detect loops
last_override_hash = None
override_repeat_count = 0
max_repeat_threshold = 3  # After 3 loops, trigger patch

def generate_state_fingerprint(state: dict) -> str:
    """
    Generate a hash representing the current reasoning state.
    """
    try:
        state_str = str(sorted(state.items()))
        return hashlib.sha256(state_str.encode()).hexdigest()
    except Exception:
        return "unknown"

def analyze_override_loop(reasoning_state: dict) -> dict:
    """
    Detects cognitive loop due to reflex + failed mutation + null foresight.
    """
    global last_override_hash, override_repeat_count

    current_hash = generate_state_fingerprint(reasoning_state)

    if current_hash == last_override_hash:
        override_repeat_count += 1
    else:
        override_repeat_count = 0
        last_override_hash = current_hash

    if override_repeat_count >= max_repeat_threshold:
        return {
            "status": "loop_detected",
            "action": "apply_synthetic_foresight_patch",
            "message": f"Same override state repeated {override_repeat_count}x. Triggering fallback."
        }

    return {
        "status": "ok",
        "message": "Override pattern stable."
    }