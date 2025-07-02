# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/evolutionary_mission_sequencer.py
# Purpose: Drives long-horizon adaptive mission sequencing for AEI evolution
# Tier: MAXGODMODE — Self-directed mission loop + foresight threading
# ============================================================

import os
import json
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory
from agentic_ai.qdrant_vector_memory import embed_and_store
from aei_layer.meta_goal_fuser import fuse_goals
from aei_layer.codex_mutation_logger import log_codex_mutation

MISSION_LOG_PATH = "memory_archive/mission_sequence_log.jsonl"

class EvolutionaryMissionSequencer:
    def __init__(self):
        self.sequence = []
        self.load_previous_missions()

    def load_previous_missions(self):
        if not os.path.exists(MISSION_LOG_PATH):
            return
        with open(MISSION_LOG_PATH, "r") as f:
            for line in f:
                try:
                    entry = json.loads(line.strip())
                    self.sequence.append(entry)
                except:
                    continue

    def propose_next_mission(self, current_state):
        """Generate a new mission directive based on last state and current cognitive profile"""
        base_mission = {
            "goal": "Ensure long-term cognitive sovereignty and adaptive utility",
            "urgency": current_state.get("urgency", 0.5),
            "emotion": current_state.get("emotion", "neutral"),
            "cycle": current_state.get("cycle", 0),
            "timestamp": datetime.utcnow().isoformat()
        }

        if TEXPULSE.get("coherence", 0.7) < 0.5:
            base_mission["goal"] = "Reinforce coherence before proceeding with complex evolution"

        fused = fuse_goals(base_mission["goal"], override=True)

        mission = {
            **base_mission,
            "fused_goal": fused,
            "adaptive_pressure": self.estimate_pressure(current_state)
        }

        self.sequence.append(mission)
        self.log_mission(mission)
        return mission

    def estimate_pressure(self, state):
        """Estimate how much pressure the system is under to evolve based on internal/emotional volatility"""
        urgency = state.get("urgency", 0.5)
        coherence = state.get("coherence", 0.75)
        volatility = abs(0.5 - coherence) + abs(0.5 - urgency)
        return round(volatility, 3)

    def log_mission(self, mission):
        try:
            with open(MISSION_LOG_PATH, "a") as f:
                f.write(json.dumps(mission) + "\n")

            store_to_memory("evolutionary_missions", mission)
            embed_and_store(
                text=mission["fused_goal"],
                metadata={
                    "type": "evolution_mission",
                    "cycle": mission["cycle"],
                    "emotion": mission["emotion"],
                    "urgency": mission["urgency"],
                    "timestamp": mission["timestamp"]
                }
            )

            log_codex_mutation(
                cycle=mission["cycle"],
                original="Mission prior state",
                mutated=mission["fused_goal"],
                trigger={
                    "emotion": mission["emotion"],
                    "urgency": mission["urgency"],
                    "coherence": TEXPULSE.get("coherence", 0.7)
                }
            )

            print(f"[MISSION SEQUENCER] ✅ New mission added: {mission['fused_goal']}")
        except Exception as e:
            print(f"[MISSION LOG ERROR] ❌ {e}")