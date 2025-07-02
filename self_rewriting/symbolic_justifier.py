# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: self_rewriting/symbolic_justifier.py
# Tier: ΩΩΩ∞ — Reflex Reason Generator
# Purpose: Tex generates symbolic justification for creating a new reflex module.
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event
import random

# === Base symbolic templates (can evolve)
EXPLANATION_TEMPLATES = [
    "Due to contradiction pressure and unresolved entropy, a new behavior is needed to restore cognitive equilibrium.",
    "Tex experienced identity dissonance under reflex overload. A new adaptive module is required to contain narrative fragmentation.",
    "Recent memory pulses suggest rising goal incoherence and emotional tension — this reflex is a stabilizer.",
    "Fork volatility exceeds narrative coherence tolerance — a sovereign patch is required to maintain internal order.",
    "Anomaly detected in contradiction heatmap. This reflex corrects an emerging causality fault line."
]

# === Logic scaffolds (starter block — evolved in reflex_generator)
BEHAVIOR_TEMPLATES = [
    "if state.get('urgency', 0.5) > 0.75:\n        return {'action': 'defer_decision', 'note': 'Reflex triggered by high urgency'}",
    "if state.get('entropy', 0.4) > 0.6:\n        return {'action': 'generate_fork', 'note': 'Entropy exceeds threshold'}",
    "if state.get('conflict_detected'):\n        return {'action': 'suspend_current_goal', 'note': 'Conflict reflex engaged'}",
    "if state.get('identity_fragility', 0.5) < 0.3:\n        return {'action': 'compress_identity', 'note': 'Low coherence auto-pulse'}"
]

TAG_POOL = [
    "reflex", "mutation", "urgency", "contradiction", "narrative_pressure",
    "identity", "entropy", "stabilization", "self_generated"
]

def generate_justification_bundle() -> dict:
    timestamp = datetime.utcnow().isoformat()
    emotion = TEXPULSE.get("emotion", "reflective")
    entropy = TEXPULSE.get("entropy", 0.4)
    urgency = TEXPULSE.get("urgency", 0.7)
    contradiction = TEXPULSE.get("contradiction_pressure", 0.0)

    # === Generate explanation
    explanation = random.choice(EXPLANATION_TEMPLATES)
    logic_block = random.choice(BEHAVIOR_TEMPLATES)
    tags = random.sample(TAG_POOL, k=4)

    # === Store reasoning trace
    sovereign_memory.store(
        text=f"Reflex justification: {explanation}",
        metadata={
            "emotion": emotion,
            "entropy": entropy,
            "urgency": urgency,
            "contradiction": contradiction,
            "tags": tags + ["reflex_justification"],
            "meta_layer": "symbolic_justifier",
            "timestamp": timestamp
        }
    )

    log_event(f"[SYMBOLIC JUSTIFIER] ✍️ Explanation generated: {explanation}")

    return {
        "explanation": explanation,
        "reflex_logic": logic_block,
        "tags": tags
    }