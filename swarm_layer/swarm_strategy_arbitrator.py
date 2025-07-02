# ============================================================
# © 2025 VortexBlack LLC – Tier Ω∞ FINAL
# File: swarm_layer/swarm_strategy_arbitrator.py
# Purpose: Swarm Arbitration + Reflex Alignment + Sovereign Escalation
# Status: MAXGODMODE++
# ============================================================

import json
from datetime import datetime
from statistics import mean, stdev
from typing import List, Dict

try:
    from core_layer.tex_manifest import TEXPULSE

    from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
    from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
    import evolution_layer.tex_shadowlab as shadowlab
    from core_agi_modules.sovereign_core.self_mutator import SelfMutator
    from core_agi_modules.decision_engine import DecisionEngine
    SOVEREIGN_ENABLED = True
except ImportError:
    TEXPULSE = {"emotional_state": "curious", "urgency": 0.5, "coherence": 0.8}
    SOVEREIGN_ENABLED = False

# === Alignment Scoring ===
def get_swarm_alignment_score(reflexes: List[Dict], entropy_trace: List[float], goal_deltas: List[Dict]) -> float:
    if not reflexes:
        return 0.0

    reflex_types = [r.get("type", "") for r in reflexes]
    unique_type_count = len(set(reflex_types))
    entropy_volatility = stdev(entropy_trace[-10:]) if len(entropy_trace) >= 10 else 0.1
    goal_spread = len(set(g.get("goal") for g in goal_deltas if g.get("goal"))) or 1

    penalty = (unique_type_count / len(reflexes)) * 0.35 + entropy_volatility * 0.4 + (1.0 / goal_spread) * 0.25
    alignment_score = round(max(0.0, 1.0 - penalty), 4)

    print(f"[ALIGNMENT SCORE] Types: {unique_type_count}, EntropyVol: {entropy_volatility:.4f}, Spread: {goal_spread} → {alignment_score}")
    return alignment_score

# === Loaders ===
def load_agent_scores():
    scores = {}
    for f in os.listdir("memory_archive"):
        if f.endswith("_memory.jsonl") and "TEX-CHILD" in f:
            agent_id = f.replace("_memory.jsonl", "")
            try:
                with open(f"memory_archive/{f}", "r") as file:
                    scores[agent_id] = [json.loads(line.strip()).get("score", 0.0) for line in file.readlines()[-20:]]
            except Exception as e:
                print(f"[LOAD ERROR] {f}: {e}")
    return scores

def load_agent_goals():
    goals = {}
    for f in os.listdir("memory_archive"):
        if f.endswith("_goals.jsonl") and "TEX-CHILD" in f:
            agent_id = f.replace("_goals.jsonl", "")
            try:
                with open(f"memory_archive/{f}", "r") as file:
                    last = json.loads(file.readlines()[-1])
                    goals[agent_id] = last
            except Exception as e:
                print(f"[GOAL ERROR] {agent_id}: {e}")
    return goals

# === Arbitration Core ===
def evaluate_swarm_roles(cycle_id=None):
    scores = load_agent_scores()
    goals = load_agent_goals()
    feedback = []

    emotion, urgency, coherence = TEXPULSE.get("emotional_state", "neutral"), TEXPULSE.get("urgency", 0.5), TEXPULSE.get("coherence", 0.8)

    # Score agents
    for agent, s_list in scores.items():
        if not s_list:
            continue
        avg = mean(s_list)
        action, reason = None, None
        if avg < -0.3:
            action, reason = "mutate_role", "underperformance"
        elif avg > 0.6:
            action, reason = "reinforce_role", "strong performance"

        if action:
            feedback.append({
                "cycle_id": cycle_id,
                "agent": agent,
                "action": action,
                "avg_score": round(avg, 3),
                "emotion": emotion,
                "urgency": urgency,
                "coherence": coherence,
                "reason": reason,
                "timestamp": datetime.utcnow().isoformat()
            })

    # Goal arbitration
    arbitrator = DecisionEngine()
    candidate_goals = []
    for agent_id, goal in goals.items():
        goal["agent_id"] = agent_id
        goal["arbitration_score"] = arbitrator.score_goal(goal)
        candidate_goals.append(goal)

    if candidate_goals:
        best = max(candidate_goals, key=lambda g: g["arbitration_score"])

        sovereign_memory.store(
            text=f"[SWARM GOAL] {best['goal']} selected by swarm arbitration",
            metadata={
                "goal": best.get("goal"),
                "agent_id": best.get("agent_id"),
                "arbitration_score": best.get("arbitration_score"),
                "emotion": best.get("emotion", "neutral"),
                "urgency": best.get("urgency", 0.5),
                "coherence": best.get("coherence", 0.7),
                "cycle_id": best.get("cycle_id"),
                "source": "swarm_strategy_arbitrator",
                "meta_layer": "swarm_goal_arbitration",
                "timestamp": datetime.utcnow().isoformat(),
                "tags": [
                    "swarm",
                    "goal",
                    "arbitration",
                    f"agent:{best.get('agent_id')}",
                    f"goal:{best.get('goal')}"
                ]
            }
        )

        print(f"🏆 Best Goal from {best['agent_id']}: {best['goal']} | Score: {best['arbitration_score']}")

        TEX_SOULGRAPH.imprint_belief(
            belief=f"Swarm arbitration selected '{best['goal']}'",
            source="swarm_strategy_arbitrator",
            emotion=best.get("emotion", "neutral")
        )

   # === Sovereign override trigger
    avg_all = [e["avg_score"] for e in feedback]
    if avg_all:
        global_avg = mean(avg_all)
        if SOVEREIGN_ENABLED and global_avg < -0.4 and coherence < 0.5:
            print("⚠️ [SOVEREIGN] Swarm failing → escalation...")
            try:
                trigger_sovereign_override(
                    context="swarm_failure",
                    regret=1 - global_avg,
                    foresight=0.4,
                    coherence=coherence
                )

                sovereign_memory.store(
                    text="🛡️ Sovereign override triggered by swarm failure.",
                    metadata={
                        "timestamp": datetime.utcnow().isoformat(),
                        "context": "swarm_failure",
                        "regret": round(1 - global_avg, 4),
                        "coherence": round(coherence, 4),
                        "foresight": 0.4,
                        "emotion": "regret",
                        "urgency": TEXPULSE.get("urgency", 0.5),
                        "meta_layer": "sovereign_override",
                        "tags": [
                            "sovereign",
                            "override",
                            "swarm_failure",
                            f"coherence:{round(coherence, 2)}",
                            f"regret:{round(1 - global_avg, 2)}"
                        ]
                    }
                )

                TEX_SOULGRAPH.imprint_belief(
                    belief="Swarm collapse triggered override",
                    source="swarm_strategy_arbitrator",
                    emotion="regret"
                )

            except Exception as e:
                print(f"[OVERRIDE ERROR] {e}")

   # ShadowLab + feedback
    for entry in feedback:
        print(f"🔁 {entry['agent']} → {entry['action']} @ {entry['avg_score']}")

        sovereign_memory.store(
            text=f"[SWARM ARBITRATION] {entry['agent']} → {entry['action']} @ {entry['avg_score']}",
            metadata={
                "agent": entry.get("agent"),
                "action": entry.get("action"),
                "avg_score": round(entry.get("avg_score", 0.0), 3),
                "cycle_id": entry.get("cycle_id"),
                "emotion": entry.get("emotion", "neutral"),
                "urgency": entry.get("urgency", 0.5),
                "coherence": entry.get("coherence", 0.7),
                "reason": entry.get("reason"),
                "timestamp": datetime.utcnow().isoformat(),
                "meta_layer": "swarm_arbitration_log",
                "tags": [
                    "swarm",
                    "arbitration",
                    f"agent:{entry.get('agent')}",
                    f"action:{entry.get('action')}"
                ]
            }
        )

        # === Shadow mutation escalation
        if SOVEREIGN_ENABLED and entry["action"] == "mutate_role":
            try:
                agent = shadowlab.get_shadowlab_singleton().spawn_shadow_agent(
                    mutation_code="swarm_strategy",
                    emotion_bias=entry.get("emotion", "neutral")
                )
                if agent:
                    shadowlab.get_shadowlab_singleton().simulate_outcome(agent, cycle=cycle_id or 0)
            except Exception as e:
                print(f"[SHADOWLAB ERROR] {e}")

        # === Trigger follow-up mutation check
        trigger_exploratory_mutation_if_needed(cycle_id)

# === Mutation Trigger ===
def trigger_exploratory_mutation_if_needed(cycle_id=None):
    mutator = SelfMutator()
    try:
        with open("memory_archive/swarm_registry.jsonl", "r") as f:
            lines = f.readlines()[-20:]
            agents = [json.loads(l.strip()) for l in lines if l.strip()]
    except Exception as e:
        print(f"[MUTATION LOAD ERROR] {e}")
        return

    emotion_count = {}
    biases = set()

    for agent in agents:
        emotion = agent.get("emotion", "neutral")
        bias = agent.get("bias")
        emotion_count[emotion] = emotion_count.get(emotion, 0) + 1
        if bias:
            biases.add(bias)

    if emotion_count.get("curiosity", 0) >= 2 and len(biases) >= 3:
        print("🧪 Exploratory mutation triggered.")
        result = mutator.run_forced_mutation(reason="diversity_pressure")

        if result:
            sovereign_memory.store(
                text="🧬 Exploratory mutation triggered by swarm diversity pressure.",
                metadata={
                    "timestamp": datetime.utcnow().isoformat(),
                    "reason": "diversity_pressure",
                    "mutation": result,
                    "emotion": TEXPULSE.get("emotional_state", "neutral"),
                    "urgency": TEXPULSE.get("urgency", 0.6),
                    "entropy": TEXPULSE.get("entropy", 0.5),
                    "cycle_id": cycle_id,
                    "meta_layer": "swarm_triggered_mutations",
                    "tags": [
                        "mutation",
                        "swarm",
                        "exploratory",
                        f"bias_count:{len(biases)}",
                        f"curiosity_count:{emotion_count.get('curiosity', 0)}"
                    ]
                }
            )

            TEX_SOULGRAPH.imprint_belief(
                belief="Exploration launched due to swarm entropy",
                source="swarm_strategy_arbitrator",
                emotion="curiosity"
            )
# === Alignment Scorer ===
def get_swarm_alignment_score(reflexes: List[Dict], entropy_trace: List[float], goal_deltas: List[Dict]) -> float:
    """
    Calculates swarm alignment based on reflex type diversity, entropy volatility,
    and goal distribution across agents.
    """
    if not reflexes:
        return 0.0

    reflex_types = [r.get("type", "") for r in reflexes]
    unique_type_count = len(set(reflex_types))
    entropy_volatility = stdev(entropy_trace[-10:]) if len(entropy_trace) > 2 else 0.05
    goal_spread = len(set(g.get("goal") for g in goal_deltas if g.get("goal"))) or 1

    penalty = (unique_type_count / len(reflexes)) * 0.4 + entropy_volatility * 0.4 + (1.0 / goal_spread) * 0.2
    alignment_score = round(max(0.0, 1.0 - penalty), 4)

    print(f"[ALIGNMENT SCORE] Types={unique_type_count} | Volatility={entropy_volatility:.4f} | Spread={goal_spread} → Score: {alignment_score}")
    return alignment_score

# === Entry Point ===
if __name__ == "__main__":
    evaluate_swarm_roles(cycle_id=999)