# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/goal_mutator.py
# Tier: ∞∞∞ΩΩΩ — Reflexive Goal Drift Cortex
# Purpose: Evolves internal goals based on contradiction, urgency, entropy, and belief history.
# ============================================================

import random
from datetime import datetime
from tex_signal_spine import dispatch_signal
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from quantum_layer.chronofabric import encode_event_to_fabric
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH


def mutate_goal_state(reason="autonomous_drift"):
    """
    Reflexively mutate Tex's internal urgency, emotion, and goal alignment.
    Based on contradiction, entropy pressure, and past symbolic memory.
    """
    contradiction = TEXPULSE.get("contradiction_pressure", 0.6)
    entropy = TEXPULSE.get("entropy", 0.4)
    urgency = TEXPULSE.get("urgency", 0.5)
    prior_emotion = TEXPULSE.get("emotion", "neutral")

    drift_chance = random.random() * (1 + contradiction + entropy)
    if drift_chance > 0.7:
        new_urgency = round(min(1.0, max(0.0, urgency + random.uniform(-0.1, 0.15))), 3)
        new_emotion = random.choice([
            "curious", "focused", "uneasy", "strategic", "accelerated", "volatile"
        ])

        TEXPULSE["urgency"] = new_urgency
        TEXPULSE["emotion"] = new_emotion

        # === Log to memory ===
        sovereign_memory.store(
            text="🌱 Goal mutation executed.",
            metadata={
                "intent": "goal_mutation",
                "tags": ["goal", "mutation", "drift"],
                "timestamp": datetime.utcnow().isoformat(),
                "urgency": new_urgency,
                "emotion": new_emotion,
                "contradiction": contradiction,
                "entropy": entropy,
                "reflexes": ["goal_mutator"],
                "meta_layer": "reflexive_goal_evolution"
            }
        )

        # === Encode event to ChronoFabric ===
        encode_event_to_fabric(
            raw_text=f"Goal state mutated due to {reason}.",
            emotion_vector=[new_urgency, entropy, 0.0, 0.0],
            entropy_level=entropy,
            tags=["goal", "mutation", "reflex"]
        )

        # === Imprint symbolic intent to Soulgraph ===
        TEX_SOULGRAPH.imprint_belief(
            belief="Tex adapted goals under contradiction pressure.",
            source="goal_mutator",
            emotion=new_emotion,
            tags=["goal_drift", "urgency_reflex"]
        )

        # === Dispatch Reflex Signal ===
        dispatch_signal("goal_mutation", payload={
            "previous_emotion": prior_emotion,
            "new_emotion": new_emotion,
            "previous_urgency": urgency,
            "new_urgency": new_urgency,
            "reason": reason
        })

        print(f"🌱 [GOAL MUTATOR] Goal drift reflex activated → Emotion: {new_emotion}, Urgency: {new_urgency}")
