# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: simulator/agi_sim_sandbox.py
# Purpose: Tex-grade AGI sandbox for strategic agent evolution
# Status: AGI-FUSION READY — Supports emotion, drift, self-tagging
# ============================================================
import uuid
import random
from datetime import datetime

# === Environment + Scoring Logic ===
MARKET_SCENARIOS = ["stable", "bullish", "crash"]

STRATEGIES = [
    "high-risk growth",
    "balanced",
    "defensive capital preservation"
]

SCORE_MAP = {
    "fail": 0.0,
    "underperform": 0.3,
    "neutral": 0.5,
    "preserve": 0.7,
    "outperform": 1.0
}

# === Emotion Bias: Scenario Affinity Weighting ===
EMOTION_SCENARIO_WEIGHT = {
    "hope": {"bullish": 0.7, "stable": 0.2, "crash": 0.1},
    "fear": {"crash": 0.6, "stable": 0.3, "bullish": 0.1},
    "resolve": {"stable": 0.5, "crash": 0.3, "bullish": 0.2},
    "doubt": {"crash": 0.5, "stable": 0.4, "bullish": 0.1},
    "curious": {"bullish": 0.4, "stable": 0.4, "crash": 0.2}
}

def weighted_scenario(emotion):
    weights = EMOTION_SCENARIO_WEIGHT.get(emotion, {"stable": 0.4, "bullish": 0.3, "crash": 0.3})
    return random.choices(list(weights.keys()), weights=list(weights.values()))[0]

# === Simulation Core ===
def simulate_outcome(strategy, scenario):
    if scenario == "crash":
        result = "fail" if "high-risk" in strategy else "preserve"
    elif scenario == "bullish":
        result = "underperform" if "defensive" in strategy else "outperform"
    else:
        result = "neutral"

    return {
        "outcome": result,
        "score": SCORE_MAP[result],
        "scenario": scenario,
        "strategy": strategy,
        "timestamp": datetime.utcnow().isoformat()
    }

# === Sandbox Evaluation Wrapper ===
def run_simulation_batch(variants):
    if not variants or not isinstance(variants, list) or len(variants) == 0:
        raise ValueError("[SANDBOX] ❌ No valid cognitive agents passed to simulation. Halting for sovereign review.")
    
    print(f"[🧪] Starting {len(variants)} AGI-grade simulations...")
    results = []

    for agent in variants:
        emotion = agent.get("emotion_bias", "neutral")
        strategy = agent.get("mutation", "unknown")
        scenario = weighted_scenario(emotion)

        outcome = simulate_outcome(strategy, scenario)

        foresight = outcome["score"]
        coherence = round(random.uniform(0.5, 1.0), 3)
        urgency = round(random.uniform(0.4, 1.0), 3)
        entropy = agent.get("mutation_entropy", round(random.uniform(0.1, 0.9), 6))
        meta_drift = round(abs(coherence - urgency), 3)

        # === AGI Self-Awareness Tags ===
        if foresight >= 0.85:
            survival_profile = "thrives"
        elif foresight >= 0.6:
            survival_profile = "adapts"
        elif foresight >= 0.3:
            survival_profile = "stagnates"
        else:
            survival_profile = "collapses"

        drift_class = (
            "balanced" if meta_drift < 0.1 else
            "conflicted" if meta_drift < 0.25 else
            "unstable"
        )

        result = {
            "variant_id": agent.get("id", f"agent-{random.randint(1000,9999)}"),
            "agent_id": agent["agent_id"] if "agent_id" in agent else agent["id"],  
            "emotion": emotion,
            "mutation": strategy,
            "mutation_entropy": entropy,
            "score": foresight,
            "coherence": coherence,
            "urgency": urgency,
            "meta_drift": meta_drift,
            "outcome": outcome["outcome"],
            "scenario": scenario,
            "survival_profile": survival_profile,
            "drift_class": drift_class,
            "timestamp": outcome["timestamp"]
        }

        print(f"[🧠] Simulated: {strategy} in {scenario} → {outcome['outcome']} "
              f"(Score: {foresight} | Drift: {meta_drift} | {survival_profile} / {drift_class})")

        results.append(result)

    return results

# === Sovereign Fork Filter ===
def sandbox_passes(strategy_name, scenario=None, threshold=0.6, return_result=False):
    if not scenario:
        scenario = random.choice(MARKET_SCENARIOS)
    result = simulate_outcome(strategy_name, scenario)
    score = result.get("score", 0.0)
    return result if (return_result and score >= threshold) else score >= threshold

# === CLI Test Runner ===
if __name__ == "__main__":
    dummy_variants = [{
        "id": f"test_{i}",
        "mutation": random.choice(STRATEGIES),
        "emotion_bias": random.choice(list(EMOTION_SCENARIO_WEIGHT.keys())),
        "mutation_entropy": random.random()
    } for i in range(5)]

    results = run_simulation_batch(dummy_variants)
    for r in results:
        from pprint import pprint
        pprint(r)