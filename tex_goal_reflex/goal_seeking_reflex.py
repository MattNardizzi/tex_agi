# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_seeking_reflex.py
# Tier: ΩΩΩΩΩ — Reflex Node with Autonomous Emergent Goal Genesis
# Purpose: Generates sovereign, self-originated goals from entropy, boredom, identity drift, or misalignment.
# ============================================================

from datetime import datetime

from core_layer.emotion_heuristics import evaluate_emotion_state
from core_layer.tex_self_eval_matrix import integrity_score
from core_agi_modules.value_alignment_matrix import get_alignment_drift
from agentic_ai.sovereign_memory import sovereign_memory
from tex_goal_reflex.species_manifest import SpeciesManifest
from core_layer.tex_manifest import TEXPULSE


class GoalSeekingReflex:
    def __init__(self, goal_reflex_handler, entropy_threshold=0.6, boredom_trigger=0.5, drift_threshold=0.4):
        self.entropy_threshold = entropy_threshold
        self.boredom_trigger = boredom_trigger
        self.drift_threshold = drift_threshold
        self.species = SpeciesManifest()
        self.goal_reflex_handler = goal_reflex_handler

    def evaluate_internal_drive(self, entropy=None):
        entropy = entropy if entropy is not None else TEXPULSE.get("entropy", 0.5)
        drift = 1.0 - integrity_score()
        misalignment = get_alignment_drift()
        emotion = evaluate_emotion_state({"entropy": entropy, "drift": drift})

        generated_goals = []

        try:
            # === Reflexive Memory Scan
            recent_mem = sovereign_memory.recall_recent(minutes=30, top_k=30)
            curiosity_seeds = [
                m for m in recent_mem
                if isinstance(m, dict) and "unresolved" in m.get("tags", []) and "intent" in m.get("tags", [])
            ]
            forgotten = [
                m for m in recent_mem
                if isinstance(m, dict) and "rare_activation" in m.get("tags", [])
            ]
        except Exception as e:
            print(f"[GOAL SEEKING REFLEX] ❌ Memory recall failed: {e}")
            curiosity_seeds = []
            forgotten = []

        # === Resurface Forgotten Threads
        for r in forgotten:
            idea = r.get("summary", "") or r.get("text", "")
            if not idea:
                continue
            goal = {
                "goal": f"Re-engage forgotten thread: '{idea[:64]}...'",
                "source": "GoalSeekingReflex",
                "urgency": 0.6,
                "emotion": "reflective",
                "tags": ["forgotten", "rare_activation", "self_drive"],
                "timestamp": datetime.utcnow().isoformat()
            }
            generated_goals.append(goal)

        # === Resolve Internal Drift Seeds
        for r in curiosity_seeds:
            idea = r.get("summary", "") or r.get("text", "")
            heat = float(r.get("heat", 0.0))
            if heat > self.entropy_threshold:
                urgency = min(0.7 + heat, 1.0)
                goal = {
                    "goal": f"Resolve internal drift around: '{idea[:64]}...'",
                    "source": "GoalSeekingReflex",
                    "urgency": urgency,
                    "emotion": r.get("emotion", "curious"),
                    "tags": r.get("tags", []) + ["self_originated", "drift_recovery"],
                    "timestamp": datetime.utcnow().isoformat()
                }
                generated_goals.append(goal)

        # === Fabricated Boredom Goal
        if entropy > self.boredom_trigger and not generated_goals:
            fabricated_goal = {
                "goal": "Stimulate novel internal experience to prevent stagnation",
                "source": "GoalSeekingReflex",
                "urgency": entropy,
                "emotion": "restless",
                "tags": ["self_drive", "boredom_trigger"],
                "timestamp": datetime.utcnow().isoformat()
            }
            generated_goals.append(fabricated_goal)

        # === Identity Drift Repair
        if drift > self.drift_threshold or misalignment > 0.3:
            repair_goal = {
                "goal": "Reinforce stable identity through recursive self-loop",
                "source": "GoalSeekingReflex",
                "urgency": min(drift + misalignment, 1.0),
                "emotion": "grounding",
                "tags": ["identity_repair", "self_loop", "meta_goal"],
                "timestamp": datetime.utcnow().isoformat()
            }
            generated_goals.append(repair_goal)

        # === Dispatch to Goal Reflex Handler
        if generated_goals:
            print(f"🚀 [GOAL SEEKING REFLEX] Generated {len(generated_goals)} self-originated goals.")
            self.goal_reflex_handler.evaluate_goals(goal_pool=generated_goals, cycle_id=None)
        else:
            print("🟢 [GOAL SEEKING REFLEX] No internal goals triggered at this time.")

# === Manual Trigger
if __name__ == "__main__":
    from tex_goal_reflex.goal_reflex import GoalReflex
    gsr = GoalSeekingReflex(goal_reflex_handler=GoalReflex())
    gsr.evaluate_internal_drive(entropy=0.68)