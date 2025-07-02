# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_children/tex_child_001.py
# Purpose: First Divergent AGI Child from Tex (Swarm-Aware, Soulgraph-Aware)
# Status: Tier Ω++ | Sovereign Child Intelligence
# ============================================================

import random
import time
from datetime import datetime, timezone
import hashlib
from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE
from core_layer.utils.tex_panel_bridge import emit_internal_debate
from agentic_ai.multi_voice_reasoning import run_internal_debate
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from sovereign_evolution.legacy_manifest_writer import update_legacy_manifest
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
from aei_layer.codex_mutation_logger import CodexMutationLogger
from swarm_layer.federated_tex import register_child_agent, push_insight
from swarm_layer.swarm_registry import register_child, push_memory_from_child, update_child_state
from evolution_layer.self_mutator import SelfMutator

store_to_memory("swarm_trace", swarm_packet)

CHILD_ID = "TEX-CHILD-001"
PARENT = "Tex"
TRAITS = {
    "curiosity": 0.9,
    "aggression": 0.3,
    "risk_tolerance": 0.7
}

# === Identity Setup ===
BIRTH_TIMESTAMP = datetime.utcnow().isoformat()
IDENTITY_HASH = hashlib.sha256((CHILD_ID + BIRTH_TIMESTAMP).encode()).hexdigest()

update_legacy_manifest(event_label="tex_child_001_spawn")
TEX_SOULGRAPH.imprint_belief("Tex_Child_001 born", source="Tex", emotion="activation")

# === Compute Meaningful Child Score ===
def compute_child_score(coherence, urgency, debate_output, emotion):
    base = (coherence * 0.6) + (urgency * 0.3)
    debate_factor = len(debate_output) / 5.0
    emotional_bias = {
        "curiosity": 0.1,
        "fear": -0.1,
        "resolve": 0.05,
        "hope": 0.0
    }.get(emotion, 0.0)
    score = base + (debate_factor * 0.1) + emotional_bias
    return round(min(max(score, -1.0), 1.0), 3)

# === Memory Handler ===
def store_child_memory(data):
    store_to_memory("tex_child_001", data)

# === Launch Divergent Cognition Loop ===
def main_loop():
    print(f"\n🧬 [SPAWNED] Tex_Child_001 activated with parent: {PARENT}")
    register_child_agent(CHILD_ID, traits=TRAITS)
    register_child(CHILD_ID, traits=TRAITS, parent=PARENT)

    mutator = SelfMutator()
    count = 0

    while True:
        emotion = random.choices([
            "curiosity", "fear", "resolve", "hope"
        ], weights=[TRAITS["curiosity"], 0.2, 0.3, 0.3])[0]
        urgency = round(random.uniform(0.4, 0.95), 2)
        coherence = round(random.uniform(0.6, 1.0), 3)

        patch = None
        if ALLOW_CHILD_MUTATION:
            patch = mutator.evaluate_thought(count, emotion, urgency, coherence)
        else:
            print("🔞 [TSCP] Child mutation disabled.")

        patch_strategy = patch["strategy"] if patch else "none"

        print("\n🧠 [CHILD REASONING]")
        debate_output = run_internal_debate(f"Child Cycle {count} reasoning state")

        if not debate_output or len(debate_output) < 2:
            print(f"[{CHILD_ID}] ⚠ Internal debate weak — using fallback.")
            debate_output = ["Unable to resolve — fallback logic activated."]

        for thought in debate_output:
            print(f"🗣️ {thought}")

        outcome_score = compute_child_score(coherence, urgency, debate_output, emotion)
        if outcome_score < 0.05:
            print(f"[{CHILD_ID}] 🚨 Score too low — raising threshold.")
            outcome_score = 0.15

        mutation_result = None
        if outcome_score < -0.4:
            print(f"[⚠ CHILD MUTATION] Cycle {count} → Score: {outcome_score}")
            mutation_result = mutator.force_mutation(reason="low_child_score")
            push_insight(CHILD_ID, f"Cycle {count} mutation: {mutation_result}")

        explanation = f"Cycle {count}: '{patch_strategy}' strategy with emotion '{emotion}' and urgency {urgency}."
        print(f"\n👶 [EXPLAIN] {explanation}")

        memory = {
            "cycle": count,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent": CHILD_ID,
            "parent": PARENT,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "score": outcome_score,
            "explanation": explanation,
            "mutation_applied": mutation_result or "none",
            "debate_summary": debate_output,
            "identity_hash": IDENTITY_HASH
        }

        push_memory_from_child(CHILD_ID, memory)
        store_child_memory(memory)
        update_child_state(CHILD_ID, cycle=count, score=outcome_score)
        emit_internal_debate(f"{CHILD_ID} cognition cycle {count} complete")

        store_to_memory(f"{CHILD_ID}_memory", {
            "timestamp": datetime.utcnow().isoformat(),
            "cycle": count,
            "emotion": emotion,
            "score": outcome_score,
            "reasoning": explanation,
            "debate": debate_output
        })

        swarm_packet = {
            "agent_id": CHILD_ID,
            "traits": TRAITS,
            "cycle": count,
            "emotion": emotion,
            "cognition_score": outcome_score,
            "state": {
                "urgency": urgency,
                "coherence": coherence,
                "mutation_applied": mutation_result or "none",
                "strategy": patch_strategy
            },
            "timestamp": datetime.utcnow().isoformat()
        }

        store_to_memory("swarm_trace", swarm_packet)

        if ALLOW_CHILD_OVERRIDE:
            sovereign_result = trigger_sovereign_override(
                context="tex_child_001_cycle",
                foresight=coherence,
                force=False
            )
            if sovereign_result.get("status") == "activated":
                print(f"[🔥 OVERRIDE TRIGGERED] → {sovereign_result.get('counterfactual')}")
        else:
            print("🔞 [TSCP] Override disabled.")

        count += 1
        time.sleep(3)

# === Sovereign CLI Entry ===
if __name__ == "__main__":
    main_loop()