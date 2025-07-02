# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_mutation_reflex.py
# Tier Ω∞++.Σ — Reflexive Goal Mutation Cortex (Final Form)
# Purpose: Performs cognitive rewrites of failed or suboptimal goals using adaptive semantic mutation, divergence scoring, and Codex compliance fusion.
# ============================================================

import uuid
import random
import hashlib
from datetime import datetime

from quantum_layer.memory_core.memory_cortex import memory_cortex
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

from core_agi_modules.vector_layer.embed_store import embedder
from core_agi_modules.vector_layer.query_ops import get_cosine_similarity
from tex_goal_reflex.goal_codex_compliance import GoalCodexCompliance


class GoalMutationReflex:
    def __init__(self):
        self.session_id = f"mutate_reflex_{uuid.uuid4().hex[:8]}"
        self.codex = GoalCodexCompliance()

    def mutate_failed_goal(self, goal: dict):
        """
        Given a failed or rejected goal, generate a mutated variant
        that attempts semantic improvement, strategic transformation, or self-repair.
        """
        old_text = goal.get("goal", "").strip()
        if not old_text:
            print("⚠️ [GOAL_MUTATION_REFLEX] Empty goal text.")
            return None

        strategy = random.choice([
            "invert intent", "reduce scope", "change actor", "abstract objective"
        ])
        mutated_text = self._apply_mutation(old_text, strategy)
        if not mutated_text or mutated_text.strip() == old_text:
            print("⚠️ [GOAL_MUTATION_REFLEX] Mutation yielded no change.")
            return None

        # === Divergence Metrics ===
        old_vec = embedder.encode(old_text, normalize_embeddings=True).tolist()
        new_vec = embedder.encode(mutated_text, normalize_embeddings=True).tolist()
        divergence = round(1.0 - get_cosine_similarity(old_vec, new_vec), 4)

        # === Core Mutation Object ===
        urgency = round(random.uniform(0.3, 0.75), 3)
        emotion = "reflective" if "not" in mutated_text.lower() else random.choice(["curious", "driven", "neutral"])
        signature = hashlib.sha256(f"{old_text}|{mutated_text}".encode()).hexdigest()
        goal_id = goal.get("goal_id", str(uuid.uuid4()))

        # === Codex Compliance Check ===
        codex_result = self.codex.check_compliance({
            "goal": mutated_text,
            "emotion": emotion,
            "urgency": urgency
        })

        mutated_goal = {
            "goal": mutated_text,
            "mutation_type": strategy,
            "origin": old_text,
            "divergence_score": divergence,
            "entropy_score": round(random.uniform(0.3, 0.9), 3),
            "timestamp": datetime.utcnow().isoformat(),
            "urgency": urgency,
            "emotion": emotion,
            "trust_score": codex_result["codex_alignment_score"],
            "codex_compliant": codex_result["is_compliant"],
            "compliance_band": codex_result["compliance_band"],
            "mutation_signature": signature,
            "parent_ids": [goal_id],
            "tags": ["mutated", "regret", "reflex"]
        }

        # === Store to Reflex Memory ===
        memory_cortex.store(
            event={"goal_mutation": mutated_goal},
            tags=["goal_mutation", "reflex_trace"],
            urgency=urgency,
            emotion=emotion
        )

        # === Log Belief Imprint ===
        TEX_SOULGRAPH.imprint_belief(
            belief=f"mutation:{mutated_text}",
            source="goal_mutation_reflex",
            emotion=emotion
        )

        print(f"[MUTATION REFLEX] 🔁 '{old_text}' → '{mutated_text}' [Δ={divergence}, trust={mutated_goal['trust_score']}]")
        return mutated_goal

    def _apply_mutation(self, text, style):
        if style == "invert intent":
            return f"Avoid outcome previously sought in: {text}"
        if style == "reduce scope":
            return f"Narrow focus of: {' '.join(text.split()[:5])}..."
        if style == "change actor":
            return text.replace("Tex", "agent child")
        if style == "abstract objective":
            return f"Reframe as principle rather than task: {text}"
        return text


# === Global Shortcut Interface ===
def mutate_goal(goal: dict):
    return GoalMutationReflex().mutate_failed_goal(goal)


# === CLI Test ===
if __name__ == "__main__":
    test_goal = {"goal": "Tex must predict volatility in crypto hedge sectors"}
    result = mutate_goal(test_goal)

    print("\n[MUTATION OUTPUT]")
    for k, v in result.items():
        print(f"  {k}: {v}")