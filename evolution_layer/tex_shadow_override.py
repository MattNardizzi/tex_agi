# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: evolution_layer/tex_shadow_override.py
# Tier: ∞ΩΩ∞ — Sovereign Override Cortex
# Purpose: Executes shadow agent forks and overrides live cognition if superior under consciousness-gated conditions.
# ============================================================

from datetime import datetime
import random

from core_layer.tex_manifest import TEXPULSE
from core_layer.tex_consciousness_matrix import TexConsciousnessMatrix
from tex_engine.tex_reflex_patch_filter import should_allow_override
import evolution_layer.tex_shadowlab as shadowlab
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event

class TexShadowOverride:
    def __init__(self):
        self.shadow_lab = shadowlab.get_shadowlab_singleton()
        self.last_cycle_tag = None
        self.override_threshold = 0.82
        self.override_log = []
        self.enabled = True
        self.consciousness = TexConsciousnessMatrix()

    def run_override_check(self, cycle_id, live_decision, context):
        log_event(f"[SHADOW OVERRIDE] 🧠 Checking override eligibility for cycle: {cycle_id}")

        if not self.enabled:
            return self._reject("Override system disabled by config", cycle_id)

        try:
            matrix_state = self.consciousness.get_state()
            if not should_allow_override(matrix_state):
                return self._reject("Blocked by consciousness matrix filter", cycle_id)
        except Exception as e:
            return self._reject(f"Consciousness check failed: {e}", cycle_id)

        if cycle_id == self.last_cycle_tag:
            return self._reject("Duplicate override request", cycle_id, live_decision)

        agents = self._spawn_shadow_decisions(context)

        top = max(agents, key=lambda a: a["score"]) if agents else None
        if top and top["score"] >= self.override_threshold:
            override_packet = {
                "override": True,
                "agent_id": top["id"],
                "score": top["score"],
                "emotion": top["emotion_bias"],
                "timestamp": datetime.utcnow().isoformat(),
                "replacement_decision": f"[SHADOWED] Strategy replaced with {top['emotion_bias']}-driven simulation.",
                "cycle": cycle_id
            }

            # Inject override into active cognition
            TEXPULSE["override_strategy"] = override_packet
            self.last_cycle_tag = cycle_id
            self.override_log.append(override_packet)

            # Memory logging
            sovereign_memory.store(
                text=f"[OVERRIDE EXECUTED] Strategy overridden by Shadow Agent {top['id']} with score {top['score']}",
                metadata={**override_packet, "meta_layer": "override_execution", "tags": ["override", "shadow", "decision"]}
            )

            log_event("✅ [SHADOW OVERRIDE] Override committed and logged.")
            return override_packet

        return self._reject("No shadow agent exceeded override threshold", cycle_id, live_decision, top["score"] if top else None)

    def _spawn_shadow_decisions(self, context):
        agents = []

        emotions = ["resolve", "hope", "concern"]
        for emotion in emotions:
            agent = self.shadow_lab.spawn_shadow_agent("live_override_test", emotion_bias=emotion)
            if agent:
                sim = self.shadow_lab.simulate_outcome(agent, cycle=0)
                if sim:
                    agents.append(sim)

        return agents

    def _reject(self, reason, cycle=None, patch=None, score=None):
        log_event(f"❌ [SHADOW OVERRIDE] {reason}")

        try:
            sovereign_memory.store(
                text=f"[OVERRIDE BLOCKED] {reason}",
                metadata={
                    "cycle": cycle,
                    "reason": reason,
                    "score": score or 0.0,
                    "patch": str(patch)[:64] if patch else None,
                    "meta_layer": "override_suppression",
                    "tags": ["override", "rejected"]
                }
            )
        except Exception as e:
            log_event(f"[OVERRIDE LOG ERROR] {e}", level="error")

        return {
            "override": False,
            "reason": reason,
            "cycle": cycle,
            "score": score or 0.0
        }

    def get_override_log(self, limit=5):
        return self.override_log[-limit:]