# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/swarm_reflex.py
# Tier Ω∞+ Distributed Cognition Reflex Engine (Final Sovereign Upgrade)
# ============================================================

from datetime import datetime
import uuid

from swarm_layer.federated_tex import federated_swarm
from swarm_layer.swarm_strategy_arbitrator import get_swarm_alignment_score
from aei_layer.internal_debate_chamber import run_internal_debate
from core_layer.utils.tex_panel_bridge import emit_internal_debate
from quantum_layer.memory_core.memory_cortex import memory_cortex
from core_layer.tex_manifest import TEXPULSE

# 🧠 Recursion protection
SWARM_REFLEX_ACTIVE = False

class SwarmReflex:
    def __init__(self):
        self.last_consensus = None

    def run(self, cycle_id: int, current_goal: str = None):
        global SWARM_REFLEX_ACTIVE
        if SWARM_REFLEX_ACTIVE:
            print("[⚠️ SWARM REFLEX] Reflex already active — skipping redundant invocation.")
            return self._result(cycle_id, reflex_id="swarm_skipped", triggered=False, alignment=None, consensus=None)

        SWARM_REFLEX_ACTIVE = True
        reflex_id = f"swarm_{uuid.uuid4().hex[:6]}"
        print(f"\n✨ [SWARM REFLEX] Evaluating swarm alignment @ Cycle {cycle_id} | ID: {reflex_id}")

        try:
            consensus = federated_swarm.reach_consensus()
            if not consensus:
                print("[SWARM REFLEX] ❌ No swarm consensus reached.")
                return self._result(cycle_id, reflex_id, False, None, None)

            self.last_consensus = consensus

            if current_goal:
                alignment = get_swarm_alignment_score(current_goal)
                print(f"[SWARM REFLEX] 🧭 Alignment score for goal: '{current_goal}' → {alignment:.2f}")

                if alignment < 0.4:
                    emit_internal_debate("⚠️ Swarm misalignment detected — initiating override debate.")
                    run_internal_debate(thought=f"Swarm coherence breach @ Cycle {cycle_id}")

                    # Sovereign signal adjustments
                    TEXPULSE["urgency"] = min(1.0, TEXPULSE["urgency"] + 0.02)
                    TEXPULSE["sovereignty"]["coherence_score"] = max(
                        0.0, TEXPULSE["sovereignty"].get("coherence_score", 0.7) - 0.01
                    )

                    memory_cortex.store(
                        event={
                            "swarm_reflex_triggered": True,
                            "reflex_id": reflex_id,
                            "goal": current_goal,
                            "alignment_score": alignment
                        },
                        tags=["swarm_misalignment", "reflex"],
                        urgency=TEXPULSE["urgency"],
                        emotion="doubt"
                    )

                    return self._result(cycle_id, reflex_id, True, alignment, consensus)
                else:
                    print("[SWARM REFLEX] ✅ Alignment sufficient. No override needed.")
                    memory_cortex.store(
                        event={
                            "swarm_alignment_confirmed": True,
                            "reflex_id": reflex_id,
                            "goal": current_goal,
                            "alignment_score": alignment
                        },
                        tags=["swarm_alignment", "reflex"],
                        urgency=0.4,
                        emotion="trust"
                    )
                    return self._result(cycle_id, reflex_id, False, alignment, consensus)
            else:
                print("[SWARM REFLEX] ⚠️ No goal provided — skipping alignment scoring.")
                return self._result(cycle_id, reflex_id, False, None, consensus)

        except Exception as e:
            print(f"[SWARM REFLEX ERROR] ❌ {e}")
            return self._result(cycle_id, reflex_id, False, None, None, error=str(e))
        finally:
            SWARM_REFLEX_ACTIVE = False

    def _result(self, cycle_id, reflex_id, triggered, alignment, consensus, error=None):
        return {
            "cycle_id": cycle_id,
            "reflex_id": reflex_id,
            "timestamp": datetime.utcnow().isoformat(),
            "reflex_triggered": triggered,
            "alignment": alignment,
            "consensus": consensus,
            "error": error
        }

# === CLI TEST ===
if __name__ == "__main__":
    reflex = SwarmReflex()
    result = reflex.run(cycle_id=999, current_goal="Maintain strategic edge in volatile conditions")
    print(f"\n🧬 [SWARM REFLEX OUTPUT]\n{result}")