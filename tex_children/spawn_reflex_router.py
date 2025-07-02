# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: genesis_engine/spawn_reflex_router.py
# Tier: ΩΩΩ∞∞ΣΣΣ — Spawn Reflex Cortex
# Purpose: Reflex-safe signal handler that initiates sovereign child spawning.
# ============================================================

from genesis_engine.genesis_engine import spawn_children_from_signal
from utils.logging_utils import log_event


def handle_spawn_children(signal: dict):
    """
    Reflex entrypoint. Triggered by dispatch_signal("spawn_children", payload={...})
    """
    try:
        payload = signal.get("payload", {})
        roles = payload.get("roles", [])
        traits = payload.get("traits", [])
        urgency = float(payload.get("urgency", 0.6))
        entropy = float(payload.get("entropy", 0.4))

        log_event(f"[SGE:SpawnReflex] Received spawn request → Roles: {roles} | Urgency: {urgency} | Entropy: {entropy}", level="info")

        results = spawn_children_from_signal(
            roles=roles,
            traits=traits,
            urgency=urgency,
            entropy=entropy,
            source="spawn_reflex"
        )

        return results

    except Exception as e:
        log_event(f"[SGE:SpawnReflex ERROR] {e}", level="error")
        return {"status": "error", "error": str(e)}
