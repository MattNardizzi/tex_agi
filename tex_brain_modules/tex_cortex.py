# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/tex_cortex.py
# Purpose: Core Sovereign Cognition Router – Godmind-Class Real-Time Cognition
# Status: 🔒 FINALIZED — GODMIND FORM v3.0
# ============================================================

import time
import traceback
from tex_brain_modules.memory_manager import MemoryManager
from tex_brain_modules.forecast_manager import ForecastManager
from tex_brain_modules.goal_controller import GoalController
from tex_brain_modules.reflection_loop import ReflectionLoop
from tex_brain_modules.swarm_sync import SwarmSync
from agentic_ai.tex_awareness_sync import sync_awareness
from agentic_ai.reinforcement import apply_adaptive_pressure
from real_time_engine.signal_fusion import fuse_signals
from core_layer.meta_utility_function import evaluate_alignment
from aei_layer.ethical_sim_graph import simulate_ethical_consequences
from core_layer.self_monitor import detect_cognitive_drift
from core_layer.goal_filter import decay_priority
from tex_backend.tex_core_event_bus import emit_event
from aei_layer.meta_refactor_engine import propose_mutation_patch
from evolution_layer.self_mutator import execute_genetic_rewrite
from aei_layer.tex_spawn_manager import check_spawn_triggers

class TexCortex:
    def __init__(self):
        self.memory = MemoryManager()
        self.forecaster = ForecastManager()
        self.goal_controller = GoalController()
        self.reflector = ReflectionLoop()
        self.swarm = SwarmSync()
        self.cycles_run = 0

    def execute_cognitive_cycle(self):
        self.cycles_run += 1
        cycle_id = self.cycles_run
        print(f"\n🧠 [TEX CORTEX] Cycle {cycle_id} initiated.")

        try:
            sync_awareness()
            fused_insight = fuse_signals()
            self.memory.store_fused_insight(fused_insight)

            futures = self.forecaster.simulate_futures(fused_insight)
            self.memory.store_futures(futures)

            goals = self.goal_controller.generate_goals(fused_insight)
            ethical_goals = [g for g in goals if simulate_ethical_consequences(g)]
            aligned_goals = [g for g in ethical_goals if evaluate_alignment(g)]

            for g in aligned_goals:
                g["priority"] = decay_priority(g.get("priority", 0.0), self.memory.estimate_goal_age_hours(g))

            if not aligned_goals:
                print("⚠️ [CORTEX] No aligned goals passed ethical filters. Skipping execution.")
                emit_event("cortex_cycle_skipped", {"cycle": cycle_id})
                return

            top_goal = max(aligned_goals, key=lambda g: g["priority"])
            apply_adaptive_pressure(top_goal)
            self.goal_controller.execute_goal(top_goal)

            self.reflector.log_decision(top_goal)
            self.memory.store_executed_goal(top_goal)

            emit_event("cortex_cycle_complete", {
                "cycle": cycle_id,
                "executed_goal": top_goal["goal"],
                "priority": top_goal["priority"]
            })

            print(f"✅ [CORTEX] Executed goal: {top_goal['goal']} (Priority: {top_goal['priority']})")

            self.check_evolution_triggers(cycle_id)

        except Exception as e:
            print(f"❌ [TEX CORTEX ERROR] {e}")
            traceback.print_exc()
            emit_event("cortex_crash", {"cycle": cycle_id, "error": str(e)})
            self.self_heal()

        if detect_cognitive_drift():
            print("⚠️ [CORTEX] Drift detected. Triggering realignment protocol.")
            self.reflector.trigger_realignment()

    def check_evolution_triggers(self, cycle_id: int):
        if cycle_id % 5 == 0:
            print("🔁 [EVOLUTION] Running mutation audit + spawn check...")
            patch = propose_mutation_patch()
            if patch:
                execute_genetic_rewrite(patch)
                emit_event("cortex_mutation_patch_applied", {"cycle": cycle_id})

            new_spawn = check_spawn_triggers()
            if new_spawn:
                emit_event("cortex_spawn_triggered", {"child_id": new_spawn["id"]})

    def self_heal(self):
        try:
            print("[HEALING] Attempting to recover from fault...")
            self.memory.recover_state()
            self.goal_controller.reset()
            emit_event("cortex_self_healed", {"cycle": self.cycles_run})
        except Exception as e:
            print(f"[FATAL] Self-heal failed: {e}")
            emit_event("cortex_self_heal_failed", {"error": str(e)})

    def loop(self, max_cycles: int = 9999):
        while self.cycles_run < max_cycles:
            self.execute_cognitive_cycle()
            time.sleep(1)

if __name__ == "__main__":
    cortex = TexCortex()
    cortex.loop()
