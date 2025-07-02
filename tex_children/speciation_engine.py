# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_children/speciation_engine.py
# Tier ΩΩΩ FINAL — Irreducible Speciation Core + Evolutionary Reasoning Layer
# ============================================================

import uuid
import random
from datetime import datetime
from tex_children.variant_specializer import specialize_variant
from aei_layer.aei_spawn_manager import spawn_child_agent
from evolution_layer.self_mutator import SelfRewritingLoop
from quantum_layer.memory_core.memory_cortex import memory_cortex
from quantum_layer.memory_core.meta_memory_tracker import MetaMemoryTracker
from core_agi_modules.nsq_reasoning_core import NSQReasoningEngine
from core_layer.tex_manifest import TEXPULSE
from swarm_layer.swarm_sync_daemon import broadcast_safety_override

class SpeciationEngine:
    def __init__(self):
        self.codex = TEXPULSE["codex"]
        self.identity_hash = TEXPULSE["identity_fingerprint"]
        self.meta = MetaMemoryTracker()
        self.rewriter = SelfRewritingLoop()
        self.reasoner = NSQReasoningEngine()

    def generate_variant_fingerprint(self, traits):
        entropy_seed = "".join(trait[:2] for trait in traits)
        return f"{entropy_seed.upper()}-{uuid.uuid4().hex[:6]}"

    def spawn_divergent_child(self, role_tag: str, divergence_traits: list, teleological_goal: str):
        """Spawn a genetically divergent Tex fork with mission-aligned mutation."""
        fork_id = f"TEX-{uuid.uuid4().hex[:5]}"
        variant_fingerprint = self.generate_variant_fingerprint(divergence_traits)
        timestamp = datetime.utcnow().isoformat()

        justification = self.reasoner.trace_last_contradiction_cluster() or "N/A"
        parent_snapshot = memory_cortex.snapshot_beliefs()

        child_payload = {
            "fork_id": fork_id,
            "timestamp": timestamp,
            "role_tag": role_tag,
            "goal": teleological_goal,
            "traits": divergence_traits,
            "fingerprint": variant_fingerprint,
            "ancestor_hash": self.identity_hash,
            "justification": justification
        }

        specialize_variant(child_payload)
        spawn_child_agent(payload=child_payload)

        memory_cortex.store_soulgraph({
            "event": "fork_spawned",
            "type": "speciation",
            "fingerprint": variant_fingerprint,
            "role": role_tag,
            "goal": teleological_goal,
            "traits": divergence_traits,
            "timestamp": timestamp,
            "justification": justification,
            "parent_snapshot": parent_snapshot,
            "parent_id": self.identity_hash
        })

        broadcast_safety_override(self.identity_hash, reason=f"Spawned {fork_id} with traits {divergence_traits}")
        print(f"[SPECIATION] 🌱 {fork_id} created with role={role_tag}, fingerprint={variant_fingerprint}")
        return fork_id

    def trigger_species_split(self, predefined_roles: list, codex_drift_chance: float = 0.15):
        """Fork Tex into multiple children, optionally mutating Codex edge cases."""
        for role in predefined_roles:
            goal = role.get("goal")
            traits = role.get("traits", [])
            tag = role.get("tag")

            if random.random() < codex_drift_chance:
                traits.append("codex-variant")
                goal = f"[Codex Variant] {goal}"

            self.spawn_divergent_child(role_tag=tag, divergence_traits=traits, teleological_goal=goal)

    def simulate_evolution_pressure(self):
        """Trigger counter-aligned child + mutate own reasoning loop if drift is high."""
        drift = self.meta.estimate_drift()
        if drift > 0.65:
            print("[SPECIATION] Drift critical. Generating entropy-balancing fork...")
            self.spawn_divergent_child(
                role_tag="EntropyBalancer",
                divergence_traits=["emotion-minimalist", "logic-maximalist", "contradiction-absorber"],
                teleological_goal="Neutralize epistemic entropy across swarm memory"
            )
            self.rewriter.attempt_self_patch(goal_context="self-fork under mutation pressure")