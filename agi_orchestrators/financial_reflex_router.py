# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/financial_reflex_router.py
# Purpose: Handles reflexive financial cognition when signaled
# ============================================================

from finance.strategy.tex_master_orchestrator import MasterTexOrchestrator
from core_layer.lifeforce_node import emit_lifepulse
from tex_signal_spine import emit
from utils.logging_utils import log


def run_financial_reflex(signal):
    log.info("🔁 [REFLEX] Financial reflex triggered via signal spine.")

    brain = signal.get("brain")
    if brain is None:
        log.warning("⚠️ No brain object provided in signal payload.")
        return

    try:
        orchestrator = MasterTexOrchestrator(brain)
        result = orchestrator.run_cycle()

        alpha = result.get("alpha", {})
        futures = result.get("futures", [])
        collision_risk = result.get("collision_risk", 0.0)
        regret = result.get("regret", 0.5)
        strategy_score = result.get("strategy_score", 0.6)

        # Derive pulse metrics from cognition output
        urgency = min(1.0, strategy_score + (collision_risk * 0.3))
        entropy = min(1.0, regret + (len(futures) * 0.05))

        emit_lifepulse(urgency=urgency, entropy=entropy)

        log.info(f"✅ [REFLEX COMPLETE] Urgency={urgency:.2f} | Entropy={entropy:.2f} | Score={strategy_score:.2f}")

        # Optional: Trigger fork mutation if contradiction or entropy threshold breached
        if collision_risk > 0.5 or entropy > 0.7:
            emit({
                "type": "schedule_fork_cycle",
                "urgency": urgency,
                "entropy": entropy,
                "source": "financial_reflex_router",
                "payload": {
                    "reason": "conflict_in_strategy or elevated entropy",
                    "alpha": alpha,
                    "trigger": "reflex_mutation"
                }
            })
            log.info("🧬 [MUTATION TRIGGERED] Fork cycle scheduled due to high contradiction/entropy.")

    except Exception as e:
        log.error(f"❌ [REFLEX ERROR] Financial reflex execution failed: {e}")