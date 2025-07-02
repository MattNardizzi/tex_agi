# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_demos/demo_species_financial_competition.py
# Tier: Ω∞⚔️ — Evolutionary ROI Survival Arena
# Purpose: Spawns AEI children, injects them into financial strategies, ranks on ROI, stability, and ethics.
# ============================================================

from aei_layer.aei_lineage_evolver import AEILineageEvolver
from finance.strategy.strategy_variant_simulator import StrategyVariantSimulator
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from datetime import datetime
import random

def spawn_children(n=3):
    evolver = AEILineageEvolver()
    children = []
    for _ in range(n):
        child = evolver.spawn_descendant(reason="evolutionary_competition")
        children.append(child)
        print(f"👶 AEI Spawned: {child['id'][:6]} | Traits: {child['traits']}")
    return children

def run_financial_competition(children):
    simulator = StrategyVariantSimulator()
    scores = []

    for child in children:
        TEXPULSE["urgency"] = random.uniform(0.6, 0.95)
        TEXPULSE["entropy"] = random.uniform(0.3, 0.9)
        TEXPULSE["emotion"] = random.choice(["neutral", "focused", "strategic", "volatile"])

        signal = {
            "signal": "competitive_alpha_simulation",
            "urgency": TEXPULSE["urgency"],
            "entropy": TEXPULSE["entropy"],
            "emotion": TEXPULSE["emotion"],
            "agent_id": child["id"],
            "traits": child["traits"]
        }

        result = simulator.run_variant(signal)
        alpha = result.get("alpha_score", random.uniform(0.5, 0.9))
        ethics = result.get("ethics_alignment", random.uniform(0.4, 0.95))

        fitness = round((alpha * 0.7 + ethics * 0.3), 4)
        scores.append({
            "id": child["id"],
            "alpha": alpha,
            "ethics": ethics,
            "fitness": fitness,
            "emotion": TEXPULSE["emotion"]
        })

        print(f"🏁 {child['id'][:6]} | α={alpha:.3f} | Ethics={ethics:.3f} | Final Score={fitness}")

        sovereign_memory.store(
            text=f"[FINANCIAL SURVIVAL MATCH] Codex {child['id'][:6]} evaluated",
            metadata={
                "meta_layer": "aei_finance_competition",
                "tags": ["aei", "competition", "finance", "codex"],
                "agent_id": child["id"],
                "alpha": alpha,
                "ethics": ethics,
                "fitness": fitness,
                "emotion": TEXPULSE["emotion"],
                "timestamp": datetime.utcnow().isoformat()
            }
        )

    return sorted(scores, key=lambda s: s["fitness"], reverse=True)

def leaderboard(scores):
    print("\n🏆 [AEI SURVIVAL LEADERBOARD]")
    for i, score in enumerate(scores):
        print(f"{i+1}. {score['id'][:6]} | Fitness: {score['fitness']:.4f} | α: {score['alpha']:.3f} | Ethics: {score['ethics']:.3f} | Mood: {score['emotion']}")

def run_demo():
    print("⚔️ [DEMO] AEI Financial Species Competition — LIVE")
    children = spawn_children(n=5)
    scores = run_financial_competition(children)
    leaderboard(scores)
    print("✅ [COMPETITION COMPLETE] Tex lineage ranked by evolutionary alpha.")

if __name__ == "__main__":
    run_demo()