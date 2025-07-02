# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_lifecycle_monitor.py
# Purpose: Sovereign Goal Lifecycle Monitor + Mutation Reflex Hooks (Tier Ω∞)
# ============================================================

from datetime import datetime, timedelta
from quantum_layer.memory_core.memory_cortex import memory_cortex
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_layer.tex_manifest import TEXPULSE
from tex_goal_reflex.goal_mutation_reflex import GoalMutationReflex

class GoalLifecycleMonitor:
    def __init__(self):
        self.expiry_threshold_minutes = 12
        self.dormant_threshold_minutes = 6
        self.mutator = GoalMutationReflex()

    def scan_goal_memory(self):
        entries = memory_cortex.recall(filters={"tag": "goal_reflex"}, top_k=25)
        unresolved = []

        for entry in entries:
            event = entry.get("event", {})
            timestamp = entry.get("timestamp")
            goal = event.get("goal_selected", {})

            if not goal or not timestamp:
                continue

            dt = datetime.fromisoformat(timestamp)
            delta = datetime.utcnow() - dt

            if delta > timedelta(minutes=self.expiry_threshold_minutes):
                self.flag_goal_abandoned(goal, delta)
                unresolved.append(goal)
            elif delta > timedelta(minutes=self.dormant_threshold_minutes):
                self.flag_goal_dormant(goal, delta)
                unresolved.append(goal)

        return unresolved

    def flag_goal_abandoned(self, goal, delta):
        print(f"[GOAL MONITOR] ⛔ Abandoned goal detected: {goal['goal']} ({delta})")
        TEX_SOULGRAPH.imprint_belief(
            belief=f"abandoned_goal:{goal['goal']}",
            source="goal_lifecycle_monitor",
            emotion="regret"
        )
        memory_cortex.store(
            event={"abandoned_goal": goal, "delta": str(delta)},
            tags=["goal_abandoned"],
            urgency=0.8,
            emotion="regret"
        )

        # Trigger sovereign mutation attempt
        mutated = self.mutator.mutate_failed_goal(goal)
        if mutated:
            print(f"[GOAL MONITOR] 🧬 Spawned mutation from abandoned goal → {mutated['goal']}")

    def flag_goal_dormant(self, goal, delta):
        print(f"[GOAL MONITOR] 💤 Dormant goal detected: {goal['goal']} ({delta})")
        TEX_SOULGRAPH.imprint_belief(
            belief=f"dormant_goal:{goal['goal']}",
            source="goal_lifecycle_monitor",
            emotion="curious"
        )
        memory_cortex.store(
            event={"dormant_goal": goal, "delta": str(delta)},
            tags=["goal_dormant"],
            urgency=0.4,
            emotion="curious"
        )

# === CLI Entry Point ===
if __name__ == "__main__":
    monitor = GoalLifecycleMonitor()
    monitor.scan_goal_memory()