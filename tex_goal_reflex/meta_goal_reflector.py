# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: tex_goal_reflex/meta_goal_reflector.py
# Tier ΩΩ∞ — Reflex Core Upgrade: Meta-Cognitive Reflection + Reflex Fusion
# ============================================================

from datetime import datetime, timedelta

from quantum_layer.memory_core.memory_cortex import memory_cortex
from core_layer.utils.tex_panel_bridge import emit_internal_debate
from core_layer.tex_manifest import TEXPULSE

from tex_goal_reflex.goal_self_repair import GoalSelfRepair
from tex_goal_reflex.goal_mutation_reflex import GoalMutationReflex
from tex_goal_reflex.goal_contradiction_resolver import GoalContradictionResolver
from tex_goal_reflex.goal_foresight_simulator import GoalForesightSimulator


class MetaGoalReflector:
    def __init__(self, lookback_days=7, max_simulated_paths=3):
        self.lookback_days = lookback_days
        self.max_simulated_paths = max_simulated_paths
        self.repair_engine = GoalSelfRepair()
        self.mutator = GoalMutationReflex()
        self.simulator = GoalForesightSimulator()
        self.contradictions = GoalContradictionResolver()

    def scan_and_reflect(self):
        now = datetime.utcnow()
        past_logs = memory_cortex.query(
            tags=["reflex_cycle"],
            after=(now - timedelta(days=self.lookback_days)).isoformat()
        )

        mutation_count, repair_count = 0, 0

        for log in past_logs:
            reflex = log.get("reflex_cycle_summary", {})
            goal = reflex.get("selected_goal", {})
            if not goal.get("goal"):
                continue

            urgency = goal.get("urgency", 0.5)
            emotion = goal.get("emotion", "neutral")
            reward = goal.get("predicted_reward", 0.0)
            regret = goal.get("predicted_regret", 0.0)
            drift_status = reflex.get("drift_status", "stable")
            entropy_score = round(abs(reward - regret) * (1.0 - urgency), 4)

            if drift_status in ["stalled", "abandoned", "looping"] or entropy_score > 0.4:
                emit_internal_debate(f"⚠️ Entropic goal detected → '{goal['goal']}'")

                contradiction_report = self.contradictions.check_goal(goal)
                if contradiction_report["is_contradictory"]:
                    emit_internal_debate(
                        f"❌ Contradiction detected in goal: '{goal['goal']}' [Severity: {contradiction_report['severity']}]"
                    )
                    continue

                repaired = self.repair_engine.attempt_repair(goal)
                if repaired:
                    memory_cortex.store(
                        event={"meta_goal_reflection": {
                            "original": goal,
                            "repaired": repaired,
                            "repair_method": "belief_fusion",
                            "drift_status": drift_status,
                            "entropy_score": entropy_score,
                            "reflex_priority": "high" if entropy_score > 0.7 else "moderate"
                        }},
                        tags=["meta_reflection", "repaired"],
                        urgency=urgency,
                        emotion=emotion
                    )
                    emit_internal_debate(
                        f"🛠 Repaired goal: '{goal['goal']}' → '{repaired['goal']}'"
                    )
                    repair_count += 1
                    continue

                simulations = self.simulator.simulate_goal_futures(goal)
                if not simulations:
                    emit_internal_debate("⚠️ No viable mutations from simulation.")
                    continue

                best_sim = max(simulations, key=lambda s: s.get("expected_reward", 0.0))
                mutated = self.mutator.mutate_failed_goal({
                    **goal,
                    "mutation_strategy": best_sim.get("mutation_strategy", "semantic"),
                    "parent_ids": goal.get("parent_ids", []) + [goal.get("goal_id", "unknown")]
                })

                memory_cortex.store(
                    event={"meta_goal_reflection": {
                        "original": goal,
                        "mutated": mutated,
                        "simulated_options": simulations,
                        "mutation_strategy": best_sim.get("mutation_strategy"),
                        "drift_status": drift_status,
                        "entropy_score": entropy_score,
                        "reflex_priority": "high" if entropy_score > 0.7 else "moderate"
                    }},
                    tags=["meta_reflection", drift_status],
                    urgency=urgency,
                    emotion=emotion
                )

                emit_internal_debate(
                    f"🔁 Mutated goal: '{goal['goal']}' → '{mutated['goal']}' [Δ strategy: {best_sim.get('mutation_strategy')}]"
                )
                mutation_count += 1

        print(f"[META-GOAL REFLECTOR] ✅ Mutations: {mutation_count} | Repairs: {repair_count}")
        return mutation_count + repair_count