# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_agenda_tracker.py
# Tier Ω∞ Sovereign Cognition Subsystem
# Purpose: Tracks macro, meso, and micro goals, their transitions, emotional overlays, and progress logs
# ============================================================

from datetime import datetime
import uuid
from statistics import mean

from quantum_layer.memory_core.memory_cortex import memory_cortex

class GoalAgendaTracker:
    def __init__(self):
        self.current_agenda = {
            "macro": None,
            "meso": [],
            "micro": []
        }
        self.history = []

    def update_agenda(self, new_goal, level="meso", parent_id=None):
        """
        Inserts a goal into the agenda at the specified level.
        Supports parent linkage, urgency decay, and full reflex logging.
        """
        assert level in ["macro", "meso", "micro"], "Invalid goal level."
        goal_id = f"agenda_{uuid.uuid4().hex[:8]}"
        timestamp = datetime.utcnow().isoformat()

        record = {
            "goal_id": goal_id,
            "goal": new_goal["goal"],
            "level": level,
            "timestamp": timestamp,
            "emotion": new_goal.get("emotion", "neutral"),
            "urgency": new_goal.get("urgency", 0.5),
            "status": "active",
            "origin_trace": new_goal.get("trace_id"),
            "parent_id": parent_id
        }

        if level == "macro":
            self.current_agenda["macro"] = record
        else:
            self.current_agenda[level].append(record)

        self.history.append(record)

        memory_cortex.store(
            event={"agenda_transition": record},
            tags=["goal_agenda", level],
            urgency=record["urgency"],
            emotion=record["emotion"]
        )

        return goal_id

    def complete_goal(self, goal_id, outcome="completed"):
        for level in ["macro", "meso", "micro"]:
            if level == "macro" and self.current_agenda["macro"] and self.current_agenda["macro"]["goal_id"] == goal_id:
                self.current_agenda["macro"]["status"] = outcome
                self._log_completion(self.current_agenda["macro"], outcome)
                return True
            for goal in self.current_agenda[level]:
                if goal["goal_id"] == goal_id:
                    goal["status"] = outcome
                    self._log_completion(goal, outcome)
                    return True
        return False

    def _log_completion(self, goal, outcome):
        memory_cortex.store(
            event={"agenda_resolution": goal, "outcome": outcome},
            tags=["goal_agenda", outcome],
            urgency=goal.get("urgency", 0.5),
            emotion=goal.get("emotion", "neutral")
        )

    def get_active_agenda(self):
        return self.current_agenda

    def get_full_history(self):
        return self.history

    def get_goals_by_emotion(self, emotion):
        return [g for g in self.history if g["emotion"] == emotion]

    def get_goals_by_status(self, status):
        return [g for g in self.history if g.get("status") == status]

    def get_urgent_goals(self, min_urgency=0.7):
        return [g for g in self.history if g.get("urgency", 0) >= min_urgency]

    def get_emotional_drift(self, level="meso"):
        tier = self.current_agenda.get(level, [])
        emotions = [g.get("emotion", "neutral") for g in tier if g.get("status") == "active"]
        return {
            "level": level,
            "active_count": len(emotions),
            "dominant_emotion": max(set(emotions), key=emotions.count) if emotions else "neutral"
        }