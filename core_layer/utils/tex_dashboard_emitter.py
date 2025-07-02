from datetime import datetime
from core_layer.utils.tex_state import tex_state

def emit_dashboard_state(orchestrator, foresight):
    print("🚨 EMITTER CALLED")
    print("[EMITTER] foresight:", foresight)

    try:
        sovereign_data = {
            "godmindActive": True,
            "overrideTriggered": foresight.get("override_triggered", False),
            "trustScore": foresight.get("confidence", 0.0),
            "forkSuppressed": foresight.get("fork_suppressed", False),
            "anchorTether": foresight.get("anchor_tether", "unknown"),
            "lastSpawnedPersona": getattr(orchestrator, "last_persona", "AeonDelta"),
            "ghostForks": getattr(orchestrator, "ghost_forks", ["variant_x1"]),
            "sovereignSignal": foresight.get("sovereign_signal", "Awaiting..."),
            "timestamp": datetime.utcnow().isoformat()
        }

        print("[EMITTER] Writing to tex_state...")
        print("[EMITTER] tex_state ID:", id(tex_state))
        tex_state.update_state("sovereign_cognition", sovereign_data)

    except Exception as e:
        print("❌ [EMITTER ERROR] Failed to emit dashboard state:", e)