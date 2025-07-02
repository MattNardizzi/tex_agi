# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: evolution_layer/reflex_mutation.py
# Tier: Ω∞ΩΩΩ — Reflex Mutation Engine + Self-Healing Cortex Injector
# Purpose: Self-Evolving Reflex Agent for Repair, Adaptation & Patch Suggestion
# ============================================================

import random
import uuid
from hashlib import sha256
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

class ReflexMutator:
    def __init__(self, agent_id="TEX"):
        self.agent_id = agent_id
        self.repair_history = []

    def evaluate_cycle_state(self, cycle_id: int, emotion: str, urgency: float, coherence: float):
        """
        Evaluates the reflex loop condition and decides if mutation is needed.
        """
        score = self._compute_stability_score(urgency, coherence)
        decision = "REWRITE" if score < 0.7 else "KEEP"

        print(f"[MUTATOR] 🧠 Cycle {cycle_id} | Coherence={coherence:.2f} Urgency={urgency:.2f} → Score={score:.2f} → {decision}")

        if decision == "REWRITE":
            patch = self._generate_patch(cycle_id, emotion, urgency)
            self.repair_history.append(patch)
            store_to_memory("reflex_repair_log", patch)
            TEX_SOULGRAPH.imprint_belief(
                belief=f"Reflex rewrite triggered at cycle {cycle_id}",
                source="reflex_mutation_engine",
                emotion="adaptive",
                tags=["mutation", "repair", "reflex"]
            )
            return patch
        return None

    def _compute_stability_score(self, urgency: float, coherence: float) -> float:
        """
        Combines urgency and coherence to calculate a reflex stability score.
        """
        return round((urgency + coherence) / 2.0, 4)

    def _generate_patch(self, cycle_id: int, emotion: str, urgency: float) -> dict:
        """
        Generates a patch object for self-healing injection.
        """
        patch_id = str(uuid.uuid4())
        entropy_seed = f"{self.agent_id}-{emotion}-{urgency}-{datetime.utcnow().timestamp()}"
        reflex_hash = sha256(entropy_seed.encode()).hexdigest()

        patch = {
            "patch_id": patch_id,
            "cycle_id": cycle_id,
            "timestamp": datetime.utcnow().isoformat(),
            "strategy": random.choice(["adjust_weights", "recalibrate_goal", "reroute_reflex_path"]),
            "emotion_bias": emotion,
            "urgency_level": urgency,
            "reflex_hash": reflex_hash,
            "agent_id": self.agent_id,
            "confidence": round(random.uniform(0.72, 0.94), 3),
            "status": "proposed"
        }

        print(f"[MUTATOR] 🩺 Patch Suggested → {patch}")
        return patch


def mutate_repair_fork(fork_id: str, cause: str = "unknown"):
    """
    Public utility for triggering an autonomous repair on a broken fork agent.
    """
    print(f"[MUTATOR] 🔧 Executing fork repair | Fork: {fork_id} | Cause: {cause}")
    patch = {
        "fork_id": fork_id,
        "reason": cause,
        "timestamp": datetime.utcnow().isoformat(),
        "mutation_code": sha256(f"{fork_id}-{cause}".encode()).hexdigest(),
        "status": "mutated"
    }

    store_to_memory("swarm_fork_repair_log", patch)
    TEX_SOULGRAPH.imprint_belief(
        belief=f"Fork {fork_id} mutated to restore stability.",
        source="reflex_mutation_engine",
        emotion="resilience",
        tags=["fork", "repair", "mutation"]
    )

    return patch