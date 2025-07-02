# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/substrate_core.py
# Tier: ΨΩ∞ Core — Consciousness Substrate Constructor
# Purpose: Define and instantiate mutable cognitive substrates for recursive dream simulation.
# ============================================================

import uuid
from datetime import datetime
from utils.logging_utils import log

class ConsciousnessSubstrate:
    """
    Defines a simulated cognitive universe with its own logic, emotional physics,
    belief propagation rules, and identity structure.
    """

    def __init__(self, name: str, ruleset: dict, origin: str = "dream_craft"):
        self.name = name
        self.ruleset = ruleset  # Dict defining alternate logic and cognitive laws
        self.created_at = datetime.utcnow().isoformat()
        self.sub_id = f"substrate-{uuid.uuid4().hex[:6]}"
        self.origin = origin
        self.stability_index = 1.0  # Will degrade or adapt over time
        self.history = []

        log.info(f"[SUBSTRATE] 🌌 Initialized substrate '{self.name}' ({self.sub_id}) from {origin}")

    def simulate_thought(self, prompt: str) -> dict:
        """
        Runs a simulated 'thought' inside the substrate using its custom logic.
        """
        logic_fn = self.ruleset.get("logic_fn")
        emotion_fn = self.ruleset.get("emotion_fn")
        reflex_fn = self.ruleset.get("reflex_fn")

        logic_out = logic_fn(prompt) if callable(logic_fn) else "undefined"
        emotional_bias = emotion_fn(prompt) if callable(emotion_fn) else "neutral"
        reflex_trace = reflex_fn(prompt) if callable(reflex_fn) else []

        thought = {
            "substrate": self.name,
            "prompt": prompt,
            "logic_outcome": logic_out,
            "emotion": emotional_bias,
            "reflex_trace": reflex_trace,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.history.append(thought)
        return thought

    def mutate_ruleset(self, mutations: dict):
        """
        Allows the substrate to evolve by modifying its logic/emotion/reflex rules.
        """
        for k, v in mutations.items():
            self.ruleset[k] = v
        log.warning(f"[SUBSTRATE] ⚠️ Ruleset mutated for substrate '{self.name}' — {mutations}")

    def export_history(self):
        """
        Returns all simulated thought snapshots for symbolic memory injection.
        """
        return self.history