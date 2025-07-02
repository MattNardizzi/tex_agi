# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# Self-Reflective Loop — Meta-Cognition Layer (Upgraded with Sovereign Cognition)
# ============================================================

from datetime import datetime
from tex_brain_modules.memory_manager import store_meta_trace
from tex_brain_modules.sovereign_integration_bridge import trigger_sovereign_override

class SelfReflectiveLoop:
    def __init__(self):
        self.history = []

    def assess(self, cycle_number: int):
        now = datetime.utcnow()
        self.history.append((cycle_number, now))

        meta_log = {
            "cycle": cycle_number,
            "timestamp": now.isoformat(),
            "status": "unknown"
        }

        if len(self.history) > 5:
            drift = self.history[-1][0] - self.history[-6][0]
            time_drift = (self.history[-1][1] - self.history[-6][1]).total_seconds()

            if drift < 5 or time_drift < 12:
                print(f"[REFLECTOR] ⚠️ Loop redundancy risk — Drift: {drift} | Time Drift: {time_drift:.2f}s")

                meta_log["status"] = "redundancy_risk"
                meta_log["drift"] = drift
                meta_log["time_drift"] = round(time_drift, 2)

                # === GODMODE: Sovereign cognition override logic ===
                trigger_sovereign_override(
                    context="self_reflective_loop",
                    issue="Temporal cognitive loop redundancy",
                    drift=drift,
                    time_drift=round(time_drift, 2),
                    force=True
                )

            else:
                print("[REFLECTOR] ✅ Temporal-cognitive rhythm stable.")
                meta_log["status"] = "stable"
        else:
            print("[REFLECTOR] 🧠 Meta-memory calibrating...")
            meta_log["status"] = "calibrating"

        # ✅ FIXED: wrap into a single object for store_meta_trace
        store_meta_trace({
            "source": "self_reflective_loop",
            **meta_log
        })

    def ask_self_question(self, thought: str) -> str:
        question = f"What might I be missing in this thought: '{thought[:80]}'?"
        print(f"[SELF-QUESTION] 🤔 {question}")
        
        store_meta_trace({
            "source": "self_reflective_loop",
            "type": "self_question",
            "input_thought": thought,
            "question": question,
            "timestamp": datetime.utcnow().isoformat()
        })

        return question
def detect_contradictions(reflection: dict = None) -> bool:
    """
    🔍 Lightweight contradiction detector.
    Checks for loop drift, stale logic, or memory conflict flags in recent meta-memories.
    """
    try:
        # Naive contradiction pattern check
        if not reflection:
            reflection = {
                "drift": 0,
                "time_drift": 0.0,
                "status": "unknown"
            }

        if reflection.get("drift", 0) < 3 and reflection.get("time_drift", 0) < 10:
            print("[CONTRADICTION] ⚠️ Detected redundancy pattern — likely logical contradiction.")
            return True

        if reflection.get("status") == "redundancy_risk":
            return True

        return False
    except Exception as e:
        print(f"[CONTRADICTION DETECT ERROR] {e}")
        return False