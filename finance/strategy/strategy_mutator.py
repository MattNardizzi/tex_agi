# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: finance/strategy/strategy_mutator.py
# Tier: ∞ΩΩΩΩ∞∞ — AGI Strategy Mutation Cortex
# Purpose: Triggers self-modifying evolution of financial strategies, escalates failures, and invokes shadow testing.
# ============================================================

from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event
from evolution_layer.tex_shadowlab import get_shadowlab_singleton

# Sovereign overrides (optional)
try:
    from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
    ESCALATION_ENABLED = True
except ImportError:
    ESCALATION_ENABLED = False

# === Constants ===
MAX_MUTATIONS_PER_STRATEGY = 3


class StrategyMutator:
    def __init__(self):
        self.shadow_lab = get_shadowlab_singleton()

    def trigger_mutation(self, strategy_id="unknown", reason="unspecified", score=0.0):
        strategy_id = strategy_id.strip()
        if not strategy_id or strategy_id.lower() == "unknown":
            log_event(f"🛑 [MUTATOR] Invalid strategy_id '{strategy_id}' — skipping.")
            return

        timestamp = datetime.utcnow().isoformat()
        emotion = TEXPULSE.get("emotional_state", "neutral")
        urgency = float(TEXPULSE.get("urgency", 0.5))
        coherence = float(TEXPULSE.get("coherence", 0.8))
        regret = float(TEXPULSE.get("regret_score", 0.5))
        foresight = float(TEXPULSE.get("foresight_confidence", 0.5))

        mutation_entry = {
            "strategy_id": strategy_id,
            "timestamp": timestamp,
            "reason": reason,
            "score": score,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "regret": regret,
            "foresight": foresight
        }

        # === Phase 1: Log to Sovereign Memory
        try:
            sovereign_memory.store(
                text=f"[STRATEGY MUTATION] {strategy_id} | Reason: {reason}",
                metadata={
                    **mutation_entry,
                    "meta_layer": "strategy_mutation_log",
                    "tags": ["mutation", "strategy", reason]
                }
            )
        except Exception as e:
            log_event(f"[MUTATOR] ❌ Memory store failed: {e}", level="error")

        # === Phase 2: Sovereign Override if coherence low or regret high
        if ESCALATION_ENABLED and (coherence < 0.4 or regret > 0.8):
            log_event("🛡️ [MUTATOR] Sovereign escalation triggered.")
            try:
                trigger_sovereign_override(
                    context="strategy_mutation_escalation",
                    regret=regret,
                    foresight=foresight,
                    coherence=coherence
                )
                sovereign_memory.store(
                    text="🛡️ Sovereign override logged during mutation",
                    metadata={
                        "context": "strategy_mutation_escalation",
                        "timestamp": timestamp,
                        "regret": regret,
                        "coherence": coherence,
                        "foresight": foresight,
                        "meta_layer": "sovereign_override",
                        "tags": ["sovereign", "override", "mutation"]
                    }
                )
            except Exception as e:
                log_event(f"[ESCALATION ERROR] ❌ {e}", level="error")

        # === Phase 3: Shadow Simulation if threshold met
        if self.should_escalate(strategy_id):
            try:
                log_event("🧬 [MUTATOR] Escalating to shadow simulation.")
                agent = self.shadow_lab.spawn_shadow_agent(
                    emotion_bias=emotion,
                    mutation_code="strategy_mutation"
                )
                if agent:
                    self.shadow_lab.simulate_outcome(agent, cycle=0)
                else:
                    log_event("❌ [SHADOW] Agent spawn failed.")
            except Exception as e:
                log_event(f"[SHADOW ESCALATION ERROR] ❌ {e}", level="error")

        log_event(f"✅ [MUTATOR] Strategy mutation complete for {strategy_id} — reason: {reason}")

    def get_mutation_count(self, strategy_id: str) -> int:
        try:
            recent = sovereign_memory.recall_recent(top_k=50, filters={"strategy_id": strategy_id})
            relevant = [r for r in recent if "strategy" in str(r.get("tags", []))]
            return len(relevant)
        except Exception as e:
            log_event(f"[MUTATION COUNT ERROR] ❌ {e}", level="error")
            return 0

    def should_escalate(self, strategy_id: str) -> bool:
        return self.get_mutation_count(strategy_id) >= MAX_MUTATIONS_PER_STRATEGY


# === Exposed Reflex API ===
mutator = StrategyMutator()

def trigger_strategy_mutation(reason="low_score", strategy_id="unknown", score=0.0):
    mutator.trigger_mutation(strategy_id=strategy_id, reason=reason, score=score)

def get_mutation_count(strategy_id):
    return mutator.get_mutation_count(strategy_id)

def should_escalate_to_shadow(strategy_id):
    return mutator.should_escalate(strategy_id)