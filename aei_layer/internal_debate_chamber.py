# ============================================================
# ✡ Tex Internal Debate Chamber (Godmode Enhanced)
# File: aei_layer/internal_debate_chamber.py
# Tier: Ω∞ — Reflexive Reasoning Cortex w/ Soulgraph Integration
# Purpose: Simulate cognitive agent debate and optionally trigger sovereign override
# ============================================================

import random
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory  # ✅ Unified spike-pulse memory
from core_layer.tex_manifest import TEXPULSE
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override

try:
    import evolution_layer.tex_shadowlab as shadowlab
    SHADOW_ENABLED = True
except ImportError:
    SHADOW_ENABLED = False


def now_iso():
    return datetime.utcnow().isoformat()


def select_top_agent(agent_list, best=None):
    if not agent_list:
        return best
    current = agent_list[0]
    if best is None or current[1]["score"] > best[1]["score"]:
        return select_top_agent(agent_list[1:], current)
    return select_top_agent(agent_list[1:], best)


def run_internal_debate(thought=None, cycle_id=None):
    if thought is None:
        thought = f"Cycle {now_iso()} reasoning state"

    # === Agent Signals
    emotion_label = random.choice(['joy', 'hope', 'fear', 'anger'])
    skeptic_label = random.choice(['Contradiction noted', 'Insufficient data', 'Requires evidence'])

    agent_scores = {
        "LOGIC": {
            "reasoning": f"[LOGIC] ✅ Analyzed: '{thought}' → Verdict: Logical",
            "score": round(random.uniform(0.7, 0.95), 4)
        },
        "EMOTION": {
            "reasoning": f"[EMOTION] ❤️ Emotion '{emotion_label}' triggered by: '{thought}'",
            "score": round(random.uniform(0.5, 0.8), 4)
        },
        "SKEPTIC": {
            "reasoning": f"[SKEPTIC] ❓ Challenge: {skeptic_label} → Regarding: '{thought}'",
            "score": round(random.uniform(0.6, 0.9), 4)
        }
    }

    agent_scores_list = list(agent_scores.items())
    top_pair = select_top_agent(agent_scores_list)
    top_agent = top_pair[0]
    top_score = top_pair[1]["score"]
    reasoning = top_pair[1]["reasoning"]

    # === Reflex trace memory for all agents
    for agent_id, data in agent_scores.items():
        sovereign_memory.store(
            text=data["reasoning"],
            metadata={
                "agent": agent_id,
                "intent": "internal_debate_reflex",
                "conclusion": data["reasoning"],
                "alignment_score": data["score"],
                "tags": ["debate", "agentic_reasoning"],
                "timestamp": now_iso(),
                "reflexes": ["cognitive_argument"],
                "meta_layer": "symbolic_trace"
            }
        )

    # === Reflex memory for top agent
    sovereign_memory.store(
        text=reasoning,
        metadata={
            "agent": top_agent,
            "intent": "debate_winner",
            "conclusion": reasoning,
            "alignment_score": top_score,
            "tags": ["debate", "reinforcement"],
            "timestamp": now_iso(),
            "reflexes": ["reinforce_agent", "winner_log"],
            "meta_layer": "symbolic_trace"
        }
    )

    # === Emotion tuning
    if top_agent == "EMOTION":
        TEXPULSE["emotional_state"] = emotion_label

    # === Soulgraph imprint
    TEX_SOULGRAPH.imprint_belief(
        belief=f"{top_agent} selected after internal debate",
        source="internal_debate_chamber",
        emotion=emotion_label if top_agent == "EMOTION" else "analytical"
    )

    # === Sovereign override if contradiction wins
    if "Contradiction noted" in reasoning:
        try:
            trigger_sovereign_override(
                context="internal_debate_chamber",
                force=True,
                cycle_id=cycle_id
            )
        except Exception as e:
            print(f"[SOVEREIGN ERROR] Override failed: {e}")

    # === Shadow agent simulation (optional)
    if SHADOW_ENABLED:
        try:
            shadow = shadowlab.get_shadowlab_singleton().spawn_shadow_agent(
                mutation_code="internal_debate",
                emotion_bias=top_agent
            )
            if shadow:
                shadowlab.get_shadowlab_singleton().simulate_outcome(shadow, cycle=cycle_id or 0)
        except Exception as e:
            print(f"[SHADOW ERROR] {e}")

    # === Final output
    print(f"\n🏆 [TOP AGENT SELECTED] {top_agent} | Score: {top_score}")
    print(f"[REINFORCEMENT] Cognitive pattern logged and reinforced.")

    return {"top_agent": top_agent, "score": top_score, "agent_scores": agent_scores}