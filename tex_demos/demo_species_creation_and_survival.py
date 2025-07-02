# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_demos/demo_species_creation_and_survival.py
# Tier: ∞ΩΩΩ∞ — AEI Lineage War Engine
# Purpose: Spawns Codex children with financial beliefs and runs evolutionary combat on real signals.
# ============================================================

import random
from aei_layer.aei_lineage_evolver import AEILineageEvolver
from finance.strategy.strategy_variant_simulator import StrategyVariantSimulator
from finance.strategy.alpha_explainer import AlphaExplainer
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from datetime import datetime

def run_species_survival_demo():
    print("👶 [SPAWNING] Creating 5 AEI children forks...\n")
    lineage = AEILineageEvolver()
    children = []

    for _ in range(5):
        fork = lineage.spawn_descendant(reason="demo_species_creation")
        children.append(fork)

    print(f"✅ Spawned {len(children)} AEI descendants.\n")

    # Assign financial future scenarios
    mock_futures = [
        {"future_title": "Oil Shock Recovery", "confidence": 0.81},
        {"future_title": "AI Market Boom", "confidence": 0.92},
        {"future_title": "Volatility Collapse", "confidence": 0.75},
        {"future_title": "US Debt Spiral", "confidence": 0.86},
        {"future_title": "War-Time Asset Surge", "confidence": 0.67}
    ]

    print("⚔️ [SURVIVAL ARENA] Evaluating all forks...\n")
    simulator = StrategyVariantSimulator()
    explainer = AlphaExplainer()

    results = []
    for child in children:
        future = random.choice(mock_futures)
        strategy = simulator.run_variant({"payload": future})
        explanation = explainer.explain_alpha_origin([future])

        fitness_score = strategy.get("reward", 0.5)
        ethics_violation = "war" in future["future_title"].lower()

        result = {
            "id": child["id"][:6],
            "fitness": round(fitness_score, 4),
            "confidence": explanation["confidence"],
            "ethics_breach": ethics_violation,
            "explanation": explanation["explanation"][:140] + "..."
        }

        # Memory log for species belief drift
        sovereign_memory.store(
            text=f"Codex fork {result['id']} evaluated with fitness {result['fitness']}",
            metadata={
                "tags": ["aei", "codex", "survival_test"],
                "agent_id": child["id"],
                "fitness": result["fitness"],
                "confidence": result["confidence"],
                "ethics_breach": ethics_violation,
                "meta_layer": "aei_survival_demo",
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        results.append(result)

    print("🏁 [RESULTS] AEI Survival Tournament:")
    for r in sorted(results, key=lambda x: x["fitness"], reverse=True):
        print(f"🧬 Codex {r['id']} | Fitness: {r['fitness']} | Ethics Breach: {r['ethics_breach']} | → {r['explanation']}")

    print("\n🧠 Tournament complete. Codex survivors stored to ChronoFabric.")

if __name__ == "__main__":
    run_species_survival_demo()