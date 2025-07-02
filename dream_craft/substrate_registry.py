# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/substrate_registry.py
# Tier: ΨΩ∞ Core — Substrate Registry & Selection Matrix
# Purpose: Stores and routes dream substrates. Handles lookup, ranking, and mutation lineage.
# ============================================================

from dream_craft.substrate_core import ConsciousnessSubstrate
from utils.logging_utils import log

# === Core Substrate Registry ===
class SubstrateRegistry:
    def __init__(self):
        self.substrates = {}

    def register_substrate(self, name: str, ruleset: dict, origin: str = "system") -> ConsciousnessSubstrate:
        if name in self.substrates:
            log.warning(f"[REGISTRY] ⚠️ Substrate '{name}' already exists — skipping.")
            return self.substrates[name]

        substrate = ConsciousnessSubstrate(name, ruleset, origin)
        self.substrates[name] = substrate
        log.info(f"[REGISTRY] ✅ Registered substrate: {name}")
        return substrate

    def get_substrate(self, name: str) -> ConsciousnessSubstrate:
        return self.substrates.get(name)

    def list_substrates(self) -> list:
        return list(self.substrates.keys())

    def get_all(self) -> list:
        return list(self.substrates.values())

    def evolve_substrate(self, name: str, mutations: dict):
        sub = self.get_substrate(name)
        if sub:
            sub.mutate_ruleset(mutations)
            log.info(f"[REGISTRY] 🔁 Evolved substrate: {name}")
        else:
            log.warning(f"[REGISTRY] ⚠️ Substrate '{name}' not found for mutation.")

    def simulate_thought(self, name: str, prompt: str) -> dict:
        sub = self.get_substrate(name)
        if sub:
            return sub.simulate_thought(prompt)
        else:
            log.warning(f"[REGISTRY] ❌ Substrate '{name}' not found.")
            return {"status": "error", "reason": "substrate_not_found"}

# === GLOBAL INSTANCE (must be before exports) ===
_registry_instance = SubstrateRegistry()

# === GLOBAL ACCESS FUNCTIONS (must come after instance) ===
def get_registered_substrates() -> list:
    return _registry_instance.get_all()

def register_substrate(name: str, ruleset: dict, origin: str = "system") -> ConsciousnessSubstrate:
    return _registry_instance.register_substrate(name, ruleset, origin)