# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_children/tex_child_003.py
# Purpose: Third Divergent AGI Child from Tex (Tier Ω++ Reflex Child Agent)
# ============================================================

import random
import time

import hashlib
from datetime import datetime, timezone

from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE
from core_layer.utils.tex_panel_bridge import emit_internal_debate
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from sovereign_evolution.legacy_manifest_writer import update_legacy_manifest
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
from aei_layer.codex_mutation_logger import CodexMutationLogger
from agentic_ai.multi_voice_reasoning import run_internal_debate
from swarm_layer.federated_tex import register_child_agent, push_insight
from evolution_layer.self_mutator import SelfMutator


# === Identity Configuration ===
CHILD_ID = "TEX-CHILD-003"
PARENT = "Tex"
TRAITS = {
    "curiosity": 0.9,
    "aggression": 0.2,
    "risk_tolerance": 0.3
}

BIRTH_TIMESTAMP = datetime.utcnow().isoformat()
IDENTITY_HASH = hashlib.sha256((CHILD_ID + BIRTH_TIMESTAMP).encode()).hexdigest()

update_legacy_manifest(event_label="tex_child_003_spawn")
TEX_SOULGRAPH.imprint_belief("Tex_Child_003 born", source="Tex", emotion="activation")

# === Memory Handler ===
def store_child_memory(data):
    store_to_memory("tex_child_003", data)

# === Score Computation ===
def compute_child_score(coherence, urgency, debate_output, emotion):
    base = (coherence * 0.6) + (urgency * 0.3)
    debate_factor = len(debate_output) / 5.0
    emotional_bias = {
        "curiosity": 0.05,
        "hope": 0.02,
        "resolve": 0.03,
        "fear": -0.1
    }.get(emotion, 0.0)
    return round(min(max(base + (debate_factor * 0.1) + emotional_bias, -1.0), 1.0), 3)

# === Launch Divergent Cognition Loop ===
def main_loop():
    print(f"\n🧬 [SPAWNED] {CHILD_ID} activated with parent: {PARENT}")
    register_child_agent(CHILD_ID, traits=TRAITS)
    mutator = SelfMutator()
    count = 0

    while True:
        emotion = random.choices(
            ["aggression", "fear", "resolve", "hope"],
            weights=[TRAITS["aggression"], 0.2, 0.4, 0.2]
        )[0]
        urgency = round(random.uniform(0.5, 0.95), 2)
        coherence = round(random.uniform(0.5, 1.0), 3)

        patch = None
        if ALLOW_CHILD_MUTATION:
            patch = mutator.evaluate_thought(count, emotion, urgency, coherence)
        else:
            print("\ud83d\udd1e [TSCP] Child mutation disabled.")

        patch_strategy = patch["strategy"] if patch else "none"

        print("\n\ud83e\uddd0 [CHILD REASONING]")
        debate_output = run_internal_debate(f"Child Cycle {count} reasoning state")

        if not debate_output or len(debate_output) < 2:
            print(f"[{CHILD_ID}] \u26a0 Weak debate — fallback triggered.")
            debate_output = ["Unable to resolve reasoning — fallback triggered."]

        for thought in debate_output:
            print(f"\ud83d\udde3\ufe0f {thought}")

        outcome_score = compute_child_score(coherence, urgency, debate_output, emotion)
        if outcome_score < 0.05:
            print(f"[{CHILD_ID}] \ud83d\udea8 Cognition score low — raised to minimum.")
            outcome_score = 0.15

        mutation_result = None
        if outcome_score < -0.4:
            print(f"[\u26a0 CHILD MUTATION] Cycle {count} → Score: {outcome_score}")
            mutation_result = mutator.force_mutation(reason="low_child_score")
            push_insight(CHILD_ID, f"Cycle {count} mutation: {mutation_result}")

        explanation = f"Cycle {count}: '{patch_strategy}' strategy under emotion '{emotion}' and urgency {urgency}."
        print(f"\n\ud83d\udc76 [EXPLAIN] {explanation}")

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
            "mutation_applied": mutation_result if mutation_result else "none",
            "debate_summary": debate_output,
            "identity_hash": IDENTITY_HASH
        }

        store_child_memory(memory)
        store_to_memory(f"{CHILD_ID}_memory", memory)
        emit_internal_debate(f"{CHILD_ID} completed cycle {count}")

        swarm_packet = {
            "agent_id": CHILD_ID,
            "traits": TRAITS,
            "cycle": count,
            "emotion": emotion,
            "cognition_score": outcome_score,
            "state": {
                "urgency": urgency,
                "coherence": coherence,
                "mutation_applied": mutation_result if mutation_result else "none",
                "strategy": patch_strategy
            },
            "timestamp": datetime.utcnow().isoformat()
        }

        store_to_memory("swarm_trace", swarm_packet)

        if ALLOW_CHILD_OVERRIDE:
            result = trigger_sovereign_override(
                context="tex_child_003_cycle",
                foresight=coherence,
                force=False
            )
            if result.get("status") == "activated":
                print(f"[\ud83d\udd25 OVERRIDE TRIGGERED] → {result.get('counterfactual')}")
        else:
            print("\ud83d\udd1e [TSCP] Override disabled.")

        count += 1
        time.sleep(3)

# === Sovereign CLI Entry ===
if __name__ == "__main__":
    main_loop()
