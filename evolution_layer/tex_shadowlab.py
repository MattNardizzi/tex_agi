# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: evolution_layer/tex_shadowlab.py
# Tier: ∞ΩΩΩ∞ — Sovereign Shadow Cortex
# Purpose: Spawns speculative agents, simulates outcomes, logs failures/promotions, and triggers sovereign override or dreams.
# ============================================================

import uuid, random, hashlib
from datetime import datetime

from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
from aei_layer.mutation_lineage_tracker import log_evolution_decision
from aei_layer.codex_mutation_logger import log_codex_mutation
from aei_layer.divergence_mapper import log_fork_divergence
from aei_layer.shadow_dream_spawner import spawn_shadow_dream
from utils.logging_utils import log_event

# === Agent Hash Generator (Unique genome + emotion fingerprint) ===
def _hash_agent(agent: dict) -> str:
    try:
        uid = "|".join([
            agent.get("agent_id", ""),
            agent.get("mutation", ""),
            agent.get("emotion_bias", ""),
            agent.get("mutation_entropy", "")
        ])
        return hashlib.sha256(uid.encode("utf-8")).hexdigest()
    except:
        return "unknown_hash"

# === Sovereign Shadow Cortex ===
class TexShadowLab:
    def __init__(self):
        self.spawn_registry = {}
        self.cooldown = 0 if TEXPULSE.get("maxgodmode", False) else 45
        self.max_per_cycle = 10
        self.redundant_count = 0
        self.fallback_hash = None

    def spawn_shadow_agent(self, mutation_code: str, emotion_bias: str = None) -> dict:
        if TEXPULSE.get("shadow_spawned_this_cycle", False):
            return self._reject("already spawned this cycle")

        if not mutation_code or mutation_code.strip().lower() == "unknown":
            return self._reject("invalid mutation code")

        now = datetime.utcnow().timestamp()
        if now - self.spawn_registry.get(mutation_code, 0) < self.cooldown:
            return self._reject("cooldown active")

        agent_id = uuid.uuid4().hex
        agent = {
            "id": agent_id,
            "agent_id": agent_id,
            "mutation": mutation_code,
            "emotion_bias": emotion_bias or random.choice(["hope", "resolve", "curiosity"]),
            "mutation_entropy": uuid.uuid4().hex[:8],
            "score": None
        }

        self.spawn_registry[mutation_code] = now
        TEXPULSE["shadow_spawned_this_cycle"] = True

        sovereign_memory.store(
            text=f"🧪 Shadow Agent Spawned: {agent_id}",
            metadata={
                "type": "shadow_spawn",
                "mutation": mutation_code,
                "emotion": agent["emotion_bias"],
                "agent_id": agent_id,
                "trust_score": 0.8,
                "tags": ["shadow", "spawn"],
                "timestamp": datetime.utcnow().isoformat(),
                "meta_layer": "shadow_spawn"
            }
        )

        return agent

    def simulate_outcome(self, agent: dict, cycle: int) -> dict:
        if not agent:
            return self._reject("no agent provided")

        agent["score"] = round(random.uniform(0.0, 1.0), 3)
        now = datetime.utcnow().isoformat()

        # === Memory Log
        sovereign_memory.store(
            text=f"🧪 Simulated Agent Score: {agent['score']}",
            metadata={
                "type": "shadow_simulation",
                "agent_id": agent["id"],
                "mutation": agent["mutation"],
                "score": agent["score"],
                "emotion": agent["emotion_bias"],
                "trust_score": agent["score"],
                "heat": round(1.0 - agent["score"], 3),
                "tags": ["shadow", "simulation", "score"],
                "timestamp": now,
                "meta_layer": "shadow_simulation"
            }
        )

        # === Evolution Lineage
        log_evolution_decision(
            variant_id=_hash_agent(agent),
            metadata={
                "genome": {
                    "mutation": agent["mutation"],
                    "emotion": agent["emotion_bias"]
                },
                "score": agent["score"],
                "cycle": cycle,
                "mutation_type": "shadow_spawn",
                "emotion": agent["emotion_bias"],
                "arena": "shadowlab"
            },
            operator="TexShadowLab"
        )

        # === Sovereign Override Trigger
        if agent["score"] < 0.2:
            trigger_sovereign_override(
                context="shadow_agent_failure",
                regret=1.0 - agent["score"],
                foresight=agent["score"],
                coherence=TEXPULSE.get("coherence", 0.7)
            )

        # === Codex Logging
        log_codex_mutation(
            cycle=cycle,
            original="original_strategy_behavior",
            mutated=f"mutation={agent['mutation']}",
            trigger={
                "emotion": agent["emotion_bias"],
                "urgency": TEXPULSE.get("urgency", 0.5),
                "coherence": TEXPULSE.get("coherence", 0.7),
                "score": agent["score"]
            }
        )

        # === Fork Divergence Mapper
        log_fork_divergence(
            cycle=cycle,
            fork_id=agent["id"],
            divergence_score=round(1.0 - agent["score"], 3),
            source_emotion=agent["emotion_bias"],
            context={"mutation": agent["mutation"]}
        )

        # === Reflex Dream Generator
        if agent["score"] < 0.4:
            spawn_shadow_dream(
                cycle_id=f"{agent['id']}-{now}",
                dream_goal="Recover failure via parallel agent",
                emotion=agent["emotion_bias"],
                decision_context={
                    "shadow_id": agent["id"],
                    "mutation": agent["mutation"],
                    "score": agent["score"]
                }
            )

        # === Promotion to Fork if Successful
        if agent["score"] >= 0.75 and TEXPULSE.get("coherence", 0.7) >= 0.7:
            sovereign_memory.store(
                text="🧠 Autonomous Fork Promoted",
                metadata={
                    "type": "fork_promotion",
                    "agent_id": agent["id"],
                    "score": agent["score"],
                    "mutation": agent["mutation"],
                    "emotion": agent["emotion_bias"],
                    "tags": ["fork", "promotion"],
                    "trust_score": round(agent["score"], 3),
                    "heat": 0.2,
                    "timestamp": now,
                    "meta_layer": "fork_promotion"
                }
            )

        return agent

    def _reject(self, reason: str) -> None:
        log_event(f"⛔ [SHADOWLAB REJECT] {reason}")
        return None


# === Singleton Pattern — Lazy Init
_shadow_instance = None

def get_shadowlab_singleton():
    global _shadow_instance
    if _shadow_instance is None:
        _shadow_instance = TexShadowLab()
    return _shadow_instance