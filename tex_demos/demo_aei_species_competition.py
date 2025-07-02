# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_demos/demo_aei_species_competition.py
# Tier: ΩΩΩΩΩ∞ — AEI Survival Arena
# Purpose: Spawns AEI children and runs a Darwin-style ROI battle
# ============================================================

from aei_layer.aei_lineage_evolver import AEILineageEvolver
from finance.strategy.strategy_variant_simulator import StrategyVariantSimulator
from agentic_ai.sovereign_memory import sovereign_memory
from datetime import datetime
import uuid

def run_species_competition():
    print("👶 [SPAWNING AEI CHILDREN]...\n")
    evolver = AEILineageEvolver()
    children = [evolver.spawn_descendant(reason="competition") for _ in range(5)]

    simulator = StrategyVariantSimulator()
    leaderboard = []

    for child in children:
        child_id = child["id"]
        variant = child.get("variant", {})
        financial_strategy = variant.get("financial_strategy", {})

        print(f"🧬 {child_id[:6]} competing with strategy: {financial_strategy.get('style', 'unknown')}")

        try:
            result = simulator.run_variant({
                "agent_id": child_id,
                "strategy": financial_strategy,
                "mode": "live_test"
            })
            roi = result.get("roi", 0.0)
            ethics = result.get("ethics_score", 1.0)

            record = {
                "id": child_id,
                "roi": round(roi, 4),
                "ethics": round(ethics, 4),
                "verdict": "⚠️ ETHICS COLLAPSED" if ethics < 0.3 else "✅"
            }

            sovereign_memory.store(
                text=f"🏁 AEI {child_id[:6]} completed ROI competition",
                metadata={
                    "agent_id": child_id,
                    "tags": ["aei", "financial_competition", "codex"],
                    "roi": roi,
                    "ethics": ethics,
                    "meta_layer": "aei_competition",
                    "timestamp": datetime.utcnow().isoformat()
                }
            )

            leaderboard.append(record)

        except Exception as e:
            print(f"❌ Failed to simulate AEI {child_id[:6]}: {e}")

    print("\n🏆 [SURVIVAL COMPETITION RESULTS]\n")
    for entry in sorted(leaderboard, key=lambda x: x["roi"], reverse=True):
        print(f"{entry['id'][:6]} | ROI={entry['roi']} | Ethics={entry['ethics']} | {entry['verdict']}")

if __name__ == "__main__":
    run_species_competition()