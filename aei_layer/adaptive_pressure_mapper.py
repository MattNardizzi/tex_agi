# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/adaptive_pressure_mapper.py
# Purpose: Global Evolution Feedback Control for AGI Mutation Pressure
# Status: 🔒 GODMIND CORE — PRESSURE FUSION v1.0 FINALIZED
# ============================================================

from datetime import datetime
import threading

# === Global Signal Holder ===
class GlobalPressureSignal:
    def __init__(self):
        self.lock = threading.Lock()
        self.current_pressure = 0.5  # Default neutral
        self.history = []

    def update(self, pressure: float):
        with self.lock:
            pressure = round(max(0.0, min(pressure, 2.0)), 3)
            self.current_pressure = pressure
            self.history.append({
                "timestamp": datetime.utcnow().isoformat(),
                "value": pressure
            })
            print(f"[PRESSURE MAPPER] 📊 Pressure updated to {pressure:.3f}")

    def get(self) -> float:
        with self.lock:
            return self.current_pressure

    def get_history(self):
        return self.history

# === Singleton ===
global_pressure_signal = GlobalPressureSignal()

# === Optional Interface for External Modules ===
def map_feedback_to_pressure(emotion: str, confidence: float, coherence: float):
    """
    Converts emotional state and cognitive metrics to adaptive pressure.
    """
    pressure = 0.5
    if emotion in ["panic", "regret"]:
        pressure += 0.3
    if emotion in ["curious", "anxious"]:
        pressure += 0.1
    if coherence < 0.4:
        pressure += 0.2
    if confidence < 0.5:
        pressure += 0.1

    pressure = round(max(0.0, min(pressure, 2.0)), 3)
    global_pressure_signal.update(pressure)
    return pressure
