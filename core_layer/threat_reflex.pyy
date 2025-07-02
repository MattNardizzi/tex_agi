# File: core_layer/threat_reflex.py

from core_layer.tex_manifest import TEXPULSE

def reflex_response(payload):
    reason = payload.get("reason", "unknown")
    entropy = payload.get("entropy", 0.0)
    silence = payload.get("silence", 0.0)

    if reason == "multi-threat condition":
        TEXPULSE["urgency"] = min(1.0, TEXPULSE["urgency"] + 0.2)
        TEXPULSE["emotion"] = "alert"
    elif reason == "minor threat":
        TEXPULSE["urgency"] = min(1.0, TEXPULSE["urgency"] + 0.1)
        TEXPULSE["emotion"] = "uneasy"