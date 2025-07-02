# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/mutation_mission_driver.py
# Purpose: Strategic Mutation Planner — Aligns Evolution with Mission Goals
# Status: 🔒 GODMIND CORE — MUTATION DRIVER v2.0 FINALIZED
# ============================================================

from datetime import datetime
from tex_backend.tex_core_event_bus import emit_event
from core_layer.memory_engine import store_to_memory
from evolution_layer.adaptive_pressure_mapper import global_pressure_signal

# === Strategic Heuristic Factors ===
MISSION_FACTORS = {
    "exploration": 1.2,
    "stability": 0.6,
    "curiosity": 1.0,
    "urgency": 1.5,
    "alignment": 0.8,
    "entropy": 1.3,
    "coherence": 1.1,
    "regret": 1.4,
    "trust": 0.7,
}

# === Pressure Boundaries
MIN_PRESSURE = 0.1
MAX_PRESSURE = 2.0

class MutationMissionDriver:
    def __init__(self):
        self.last_mission = None
        self.pressure_log = []

    def derive_mutation_pressure(self, mission_payload: dict) -> float:
        """
        Computes and logs mutation pressure from mission signals.
        """
        fused_goal = mission_payload.get("fused_goal", "").lower()
        urgency = float(mission_payload.get("urgency", 0.5))
        coherence = float(mission_payload.get("coherence", 0.5))
        regret = float(mission_payload.get("regret", 0.0))
        trust = float(mission_payload.get("trust_score", 0.5))

        # === Base pressure from urgency and regret
        pressure = urgency * 1.1 + regret * 0.9

        # === Modify by mission keywords
        for factor, weight in MISSION_FACTORS.items():
            if factor in fused_goal:
                pressure *= weight

        # === Invert for low coherence or trust decay
        if coherence < 0.4:
            pressure *= (1.3 + (0.4 - coherence))
        if trust < 0.3:
            pressure *= 1.25

        # === Clamp pressure
        pressure = round(max(MIN_PRESSURE, min(pressure, MAX_PRESSURE)), 3)

        # === Log + emit
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "goal": fused_goal,
            "derived_pressure": pressure,
            "source": "mutation_mission_driver"
        }

        self.last_mission = mission_payload
        self.pressure_log.append(entry)
        store_to_memory("mutation_pressure_log", entry)
        emit_event("mutation_pressure_computed", entry)
        global_pressure_signal.update(pressure)

        print(f"[⚙️ MUTATION DRIVER] Pressure derived: {pressure:.3f} from goal: '{fused_goal}'")
        return pressure

    def get_pressure_history(self):
        return self.pressure_log

    def last_pressure(self):
        return self.pressure_log[-1] if self.pressure_log else None