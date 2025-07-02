# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/goal_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞ — Mission Drift + Goal Trace Router
# Purpose: Detects misalignment, integrity decay, and routes into goal cortex.
# ============================================================

from datetime import datetime
import random

from tex_brain_regions.goal_brain import evaluate_goal_trace
from core_layer.tex_manifest import TEXPULSE
from core_layer.goal_engine import get_active_goals
from utils.logging_utils import log
from agentic_ai.sovereign_memory import sovereign_memory  # ✅ New unified memory system


class GoalOrchestrator:
    def __init__(self):
        self.goal_log = []

    def generate_new_goals(self, regret_score: float, drift_score: float) -> dict:
        timestamp = datetime.utcnow().isoformat()
        urgency = TEXPULSE.get("urgency", 0.7)
        entropy = TEXPULSE.get("entropy", 0.4)
        emotion = TEXPULSE.get("emotional_state", "neutral")

        goal = random.choice([
            "Stabilize volatility exposure",
            "Reinforce regret-minimized alpha set",
            "Override conflicting future assumptions",
            "Elevate coherence via goal realignment",
            "Expand predictive capacity in multiworld"
        ])

        integrity = max(0.0, 1.0 - drift_score)
        progress = round(random.uniform(0.2, 0.75), 2)

        packet = {
            "goal": goal,
            "progress": progress,
            "integrity": integrity,
            "reason": "reflex_pulse",
            "timestamp": timestamp
        }

        result = self.run_goal_trace(packet)

        sovereign_memory.store(
            text=f"[GOAL INIT] {goal} launched with integrity={integrity}",
            metadata={
                "agent": "TEX",
                "intent": "goal_initialization",
                "conclusion": goal,
                "alignment_score": integrity,
                "urgency": urgency,
                "emotion": emotion,
                "entropy": entropy,
                "reflexes": result.get("reflexes", []),
                "tags": ["goal", "reflex", "strategy_cycle"],
                "timestamp": timestamp,
                "meta_layer": "symbolic_trace"
            }
        )

        self.goal_log.append({
            "goal": goal,
            "result": result,
            "timestamp": timestamp
        })

        return result

    def run_goal_trace(self, goal_packet: dict) -> dict:
        try:
            goal = goal_packet.get("goal", "undefined")
            progress = float(goal_packet.get("progress", 0.5))
            integrity = float(goal_packet.get("integrity", 0.5))
            reason = goal_packet.get("reason", "unspecified")
            timestamp = goal_packet.get("timestamp", datetime.utcnow().isoformat())

            urgency = TEXPULSE.get("urgency", 0.7)
            entropy = TEXPULSE.get("entropy", 0.4)
            emotion = TEXPULSE.get("emotional_state", "neutral")

            result = evaluate_goal_trace(
                goal=goal,
                progress=progress,
                integrity=integrity,
                urgency=urgency,
                entropy=entropy
            )

            sovereign_memory.store(
                text=f"[GOAL TRACE] {goal} evaluated with integrity={integrity}",
                metadata={
                    "agent": "TEX",
                    "intent": "goal_trace",
                    "conclusion": goal,
                    "alignment_score": integrity,
                    "urgency": urgency,
                    "emotion": emotion,
                    "entropy": entropy,
                    "reflexes": result.get("reflexes", []),
                    "tags": ["goal", "trace", "mission_drift"],
                    "timestamp": timestamp,
                    "meta_layer": "symbolic_trace"
                }
            )

            log.info(f"[GOAL ORCH] Goal: {goal} | Reflexes: {result.get('reflexes', [])}")
            return result

        except Exception as e:
            log.error(f"❌ [GOAL ORCH] Failed to route goal trace: {e}")
            return {
                "reflexes": [],
                "goal": "error"
            }


# === Standalone signal-activated version for tex_goal_inference_orchestrator ===
def run_goal_trace(signal=None):
    """
    Activated via AGI signal or goal-cycle to evaluate active goals.
    Triggers symbolic trace logic and stores evaluations.
    """
    goals = get_active_goals()
    if not goals:
        print("🧠 [GOAL TRACE] No active goals.")
        return

    for goal in goals:
        trace_result = evaluate_goal_trace(goal)
        sovereign_memory.store(
            text=f"[GOAL TRACE] {goal['goal']} → {trace_result}",
            metadata={
                "agent": "TEX",
                "intent": "goal_trace_evaluation",
                "goal": goal,
                "trace": trace_result,
                "emotion": TEXPULSE.get("emotional_state", "neutral"),
                "urgency": TEXPULSE.get("urgency", 0.6),
                "coherence": TEXPULSE.get("coherence", 0.8),
                "tags": ["goal", "trace", "reflex"],
                "timestamp": datetime.utcnow().isoformat(),
                "meta_layer": "symbolic_trace"
            }
        )
        print(f"[GOAL TRACE] {goal['goal']} → {trace_result}")