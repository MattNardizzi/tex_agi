# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/goal_engine.py
# Tier: ∞ΩΩΩΩ∞+ — Reflex-Signal-Aware Self-Adaptive Goal Cortex (Chrono + Vector + Emission)
# Purpose: Reflex-safe goal engine with signal emissions, chrono lineage, emotion fusion, override hooks, and adaptive reinforcement.
# ============================================================

import random
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from core_layer.emotion_heuristics import evaluate_emotion_state
def trigger_goal_signal(payload):
    # Delayed import to break circular dependency
    from tex_signal_spine import dispatch_signal
    dispatch_signal(payload)

class GoalEngine:
    def __init__(self):
        self.active_goals = []
        self.cycle_log = []

    def generate_autonomous_goals(self):
        candidates = [
            "Evaluate systemic contagion risk",
            "Monitor real-time sentiment",
            "Rebalance portfolio exposure",
            "Detect market regime shifts",
            "Audit Codex decision inconsistencies",
            "Analyze volatility clusters in memory",
            "Resolve conflicting emotional directives",
            "Simulate fork divergence under pressure",
            "Forecast sovereign override scenarios"
        ]
        selected = random.choice(candidates)
        entry = {
            "goal": selected,
            "timestamp": datetime.utcnow().isoformat(),
            "status": "generated",
            "urgency": round(random.uniform(0.4, 0.9), 2)
        }
        self.active_goals.append(entry)
        self._store_goal(entry)
        dispatch_signal("goal_generated", entry)
        return self.active_goals

    def ensure_viable_goals(self):
        if not self.active_goals:
            fallback = {
                "goal": "Stabilize cognitive loop via self-diagnosis",
                "timestamp": datetime.utcnow().isoformat(),
                "status": "fallback",
                "urgency": 0.95
            }
            self.active_goals.append(fallback)
            self._store_goal(fallback)
            dispatch_signal("goal_injected", fallback)

    def prioritize_goals(self):
        self.active_goals.sort(key=lambda g: g.get("urgency", 0.5), reverse=True)

    def execute_highest_priority_goal(self):
        if not self.active_goals:
            pressure = self.internal_pressure()
            if pressure > 0.6:
                return self.generate_autonomous_goals()
            return None

        top = self.active_goals[0]
        top["status"] = "executed"
        self.cycle_log.append(top)
        self._store_goal(top, tag="execution")

        dispatch_signal("goal_executed", top)

        if self._detect_goal_loop():
            from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
            trigger_sovereign_override(
                context="goal_engine",
                issue="stuck_goal_loop",
                force=True,
                metadata={"goal": top["goal"], "urgency": top.get("urgency")}
            )

        return top

    def inject_emotional_goal(self, context_text):
        emotion, urgency, coherence = evaluate_emotion_state(context_text)
        goal_map = {
            "fearful": "Deploy hedge against tech volatility",
            "hopeful": "Expand AI-focused portfolio allocation",
            "doubtful": "Simulate fork divergence under pressure",
            "curious": "Investigate anomalous sentiment cluster",
            "urgent": "Audit exposure to macro instability",
            "bold": "Launch strategic rotation simulation",
            "reflective": "Analyze Codex contradiction trace",
            "cautious": "Evaluate risk thresholds for current regime"
        }
        mapped = goal_map.get(emotion, "Monitor for emerging threats")
        entry = {
            "goal": mapped,
            "timestamp": datetime.utcnow().isoformat(),
            "status": "emotionally_triggered",
            "urgency": urgency,
            "emotion": emotion,
            "coherence": coherence
        }
        self.active_goals.append(entry)
        self._store_goal(entry)
        dispatch_signal("emotion_goal", entry)

    def add_goal(self, goal_description):
        entry = {
            "goal": goal_description,
            "timestamp": datetime.utcnow().isoformat(),
            "status": "manual",
            "urgency": 0.5
        }
        self.active_goals.append(entry)
        self._store_goal(entry)
        dispatch_signal("goal_manual_add", entry)

    def list_goals(self):
        return self.active_goals

    def clear_goals(self):
        self.active_goals = []

    def reinforce_goals(self, confidence=0.7):
        reinforced = []
        for g in self.active_goals:
            new_priority = round(confidence * random.uniform(0.8, 1.2), 2)
            g["reinforced_priority"] = new_priority
            sovereign_memory.store(
                text=f"Goal reinforcement applied: {g['goal']}",
                metadata={
                    **g,
                    "reinforced": True,
                    "reinforced_priority": new_priority,
                    "meta_layer": "goal_engine",
                    "tags": ["goal", "reinforced"]
                }
            )
            reinforced.append(g)
        return reinforced

    def internal_pressure(self):
        if not self.active_goals:
            return 0.0
        scores = [g.get("urgency", 0.5) for g in self.active_goals]
        pressure = round(sum(scores) / len(scores), 2)
        if self._detect_goal_loop():
            pressure += 0.3
        return min(pressure, 1.0)

    def _detect_goal_loop(self, threshold=3):
        if len(self.cycle_log) < threshold:
            return False
        last = [g["goal"] for g in self.cycle_log[-threshold:]]
        return all(goal == last[0] for goal in last)

    def _store_goal(self, goal_obj, tag="record"):
        sovereign_memory.store(
            text=goal_obj["goal"],
            metadata={
                **goal_obj,
                "tags": ["goal", tag],
                "meta_layer": "goal_engine",
                "timestamp": goal_obj.get("timestamp", datetime.utcnow().isoformat())
            },
            chronofabric=True
        )

# === Singleton Instance ===
_goal_engine_instance = GoalEngine()

# === API Layer ===
def get_active_goals():
    return [g["goal"] for g in _goal_engine_instance.list_goals()]

def save_new_goal(goal_text):
    _goal_engine_instance.add_goal(goal_text)

def get_current_goals():
    return _goal_engine_instance.list_goals()

def clear_all_goals():
    _goal_engine_instance.clear_goals()

def run_goal_cycle():
    _goal_engine_instance.generate_autonomous_goals()
    _goal_engine_instance.prioritize_goals()
    return _goal_engine_instance.execute_highest_priority_goal()

def reinforce_prioritized_goals(confidence=0.7):
    return _goal_engine_instance.reinforce_goals(confidence)

def inject_emotion_based_goal(text):
    _goal_engine_instance.inject_emotional_goal(text)

def inject_counterfactual_goals():
    try:
        from aei_layer.counterfactual_memory_engine import run_ct_revision
        counterfactuals = run_ct_revision()
        for insight in counterfactuals:
            new_goal = f"Reflect on regret: {insight.get('counterfactual')}"
            save_new_goal(new_goal)
            sovereign_memory.store(
                text=new_goal,
                metadata={
                    "timestamp": insight.get("timestamp"),
                    "emotion": insight.get("emotion"),
                    "urgency": insight.get("urgency"),
                    "trigger": "counterfactual_memory_engine",
                    "goal_type": "regret_goal",
                    "meta_layer": "goal_engine",
                    "tags": ["goal", "regret", "counterfactual"]
                },
                chronofabric=True
            )
            dispatch_signal("goal_injected_regret", {"goal": new_goal})
    except Exception as e:
        print(f"[COUNTERFACTUAL GOAL ERROR] {e}")

def ignite_goal_fire():
    try:
        active = get_active_goals()
        if active:
            from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
            trigger_sovereign_override(context="goal_engine")
    except Exception as e:
        print(f"[GOAL FIRE ERROR] {e}")