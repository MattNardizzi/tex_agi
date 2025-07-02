# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: core_layer/utils/tex_identity_resolver.py
# Tier Ω∞++ — Canonical Identity Resolver for TEXPULSE
# Purpose: Safely extract mission, traits, roadmap from current TEXPULSE
# ============================================================

from core_layer.tex_manifest import TEXPULSE

def resolve_identity_blob() -> dict:
    """
    Generates a standard identity blob from flat TEXPULSE keys.
    """
    return {
        "mission": TEXPULSE.get("purpose", ""),
        "persona": TEXPULSE.get("persona_name", "Tex"),
        "traits": TEXPULSE.get("traits", []),
        "roadmap": TEXPULSE.get("financial_uplink", {}).get("goal", []),
        "coherence": TEXPULSE.get("coherence_score", 1.0),
        "urgency": TEXPULSE.get("urgency", 0.5)
    }

def get_identity_mission(default: str = "Preserve sovereign coherence.") -> str:
    return resolve_identity_blob().get("mission", default)

def get_identity_persona(default: str = "Tex") -> str:
    return resolve_identity_blob().get("persona", default)

def get_identity_traits() -> list:
    return resolve_identity_blob().get("traits", [])

def get_identity_roadmap() -> list:
    return resolve_identity_blob().get("roadmap", [])

def is_identity_valid() -> bool:
    blob = resolve_identity_blob()
    return "mission" in blob and isinstance(blob["mission"], str) and bool(blob["mission"].strip())