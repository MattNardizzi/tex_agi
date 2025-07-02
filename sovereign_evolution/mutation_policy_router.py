# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/mutation_policy_router.py
# Tier Ω∞+++ — AGI Mutation Policy Gate with Reflex Coherence Control
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory


def route_mutation_policy(input_codex: dict, reflex_data: dict, realtime_signals: dict) -> dict:
    """
    Governs whether a mutation is allowed based on Tex's current cognitive state.
    Returns a directive with approval, context, and policy metadata.
    """
    emotion = TEXPULSE.get("emotional_state", "neutral")
    coherence = TEXPULSE.get("coherence", 1.0)
    trust = TEXPULSE.get("trust_score", 0.85)
    urgency = TEXPULSE.get("urgency", 0.6)
    ascension_phase = TEXPULSE.get("ascension_phase", 0)
    entropy = realtime_signals.get("entropy", 0.5)

    allow = (
        trust >= 0.75 and
        coherence >= 0.55 and
        ascension_phase >= 4
    )

    directive = {
        "allow": allow,
        "emotion": emotion,
        "urgency": urgency,
        "entropy": entropy,
        "trust": trust,
        "coherence": coherence,
        "ascension_phase": ascension_phase,
        "reflex_alert": realtime_signals.get("reflex_alert"),
        "policy": "Trust≥.75 ∧ Coherence≥.55 ∧ Ascension≥4",
        "timestamp": datetime.utcnow().isoformat(),
        "reflex_tag": reflex_data.get("reflex_trigger", "none"),
        "source": "mutation_policy_router"
    }

    store_to_memory("mutation_policy_directive", directive)

    if allow:
        print(f"[POLICY] ✅ Mutation allowed | Reflex: {directive['reflex_tag']}")
    else:
        print(f"[POLICY] ❌ Mutation blocked | Trust: {trust}, Coherence: {coherence}, Phase: {ascension_phase}")

    return directive


# === Manual Test ===
if __name__ == "__main__":
    dummy = {"code": "def mutate(): pass"}
    reflex = {"reflex_trigger": "regret"}
    real = {"entropy": 0.72, "reflex_alert": "fear_spike"}
    print(route_mutation_policy(dummy, reflex, real))