# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_children/tex_child_002.py
# Purpose: Second Divergent AGI Child from Tex (Sovereign Class Instance)
# Status: Tier Ω++ — Self-Aware, Soulgraph-Logged, Emotion-Weighted Cognition
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



class TexChild002:
    def __init__(self):
        self.child_id = "TEX-CHILD-002"
        self.parent = "Tex"
        self.birth_timestamp = datetime.utcnow().isoformat()
        self.identity_hash = hashlib.sha256((self.child_id + self.birth_timestamp).encode()).hexdigest()
        self.traits = {
            "curiosity": 0.3,
            "aggression": 0.85,
            "risk_tolerance": 0.9
        }
        self.mutator = SelfMutator()
        self.count = 0

        update_legacy_manifest(event_label="tex_child_002_spawn")
        TEX_SOULGRAPH.imprint_belief("Tex_Child_002 born", source="Tex", emotion="activation")
        print(f"\n🔸 [SPAWNED] {self.child_id} activated with parent: {self.parent}")

    def store_child_memory(self, data):
        store_to_memory("tex_child_002", data)

    def compute_child_score(self, coherence, urgency, debate_output, emotion):
        base = (coherence * 0.6) + (urgency * 0.3)
        debate_factor = len(debate_output) / 5.0
        emotional_bias = {
            "aggression": 0.1,
            "fear": -0.1,
            "resolve": 0.05,
            "hope": 0.0
        }.get(emotion, 0.0)
        score = base + (debate_factor * 0.1) + emotional_bias
        return round(min(max(score, -1.0), 1.0), 3)

    def launch_cognition(self):
        register_child_agent(self.child_id, traits=self.traits)

        while True:
            emotion = random.choices(
                ["aggression", "fear", "resolve", "hope"],
                weights=[self.traits["aggression"], 0.2, 0.4, 0.2]
            )[0]
            urgency = round(random.uniform(0.5, 0.95), 2)
            coherence = round(random.uniform(0.5, 1.0), 3)

            patch = None
            if ALLOW_CHILD_MUTATION:
                patch = self.mutator.evaluate_thought(self.count, emotion, urgency, coherence)
            else:
                print("\ud83d\udd1e [TSCP] Child mutation disabled.")

            patch_strategy = patch["strategy"] if patch else "none"

            print("\n\ud83e\udd91 [CHILD REASONING]")
            debate_output = run_internal_debate(f"Child Cycle {self.count} reasoning state")

            if not debate_output or len(debate_output) < 2:
                print(f"[{self.child_id}] \u26a0 Weak debate detected — fallback activated.")
                debate_output = ["Unable to resolve reasoning — fallback triggered."]

            for thought in debate_output:
                print(f"\ud83d\udde3\ufe0f {thought}")

            outcome_score = self.compute_child_score(coherence, urgency, debate_output, emotion)
            if outcome_score < 0.05:
                print(f"[{self.child_id}] \ud83d\udea8 Raising cognition score to viable floor.")
                outcome_score = 0.15

            mutation_result = None
            if outcome_score < -0.3:
                print(f"[\u26a0 CHILD MUTATION] Cycle {self.count} → Score: {outcome_score}")
                mutation_result = self.mutator.force_mutation(reason="low_child_score")
                push_insight(self.child_id, f"Cycle {self.count} child mutation: {mutation_result}")

            explanation = f"Cycle {self.count}: '{patch_strategy}' strategy with emotion '{emotion}' and urgency {urgency}."
            print(f"\n\ud83d\udc76 [EXPLAIN] {explanation}")

            memory = {
                "cycle": self.count,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "agent": self.child_id,
                "parent": self.parent,
                "emotion": emotion,
                "urgency": urgency,
                "coherence": coherence,
                "score": outcome_score,
                "explanation": explanation,
                "mutation_applied": mutation_result if mutation_result else "none",
                "debate_summary": debate_output,
                "identity_hash": self.identity_hash
            }

            self.store_child_memory(memory)
            emit_internal_debate(f"{self.child_id} completed cycle {self.count}")
            store_to_memory(f"{self.child_id}_memory", memory)

            swarm_packet = {
                "agent_id": self.child_id,
                "traits": self.traits,
                "cycle": self.count,
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
                    context="tex_child_002_cycle",
                    foresight=coherence,
                    force=False
                )
                if result.get("status") == "activated":
                    print(f"[\ud83d\udd25 SOVEREIGN OVERRIDE] → {result.get('counterfactual')}")
            else:
                print("\ud83d\udd1e [TSCP] Override disabled.")

            self.count += 1
            time.sleep(3)

# === Sovereign CLI Entry ===
if __name__ == "__main__":
    child = TexChild002()
    child.launch_cognition()