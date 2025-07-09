# ============================================================
# 🧠 Tex Reflex Layer: Phase Transition Monitor (Tier Ω∞ΞΣΩ)
# File: core_layer/phase_transition_monitor.py
# Purpose: Detect phase transitions in cognition and encode shifts to sovereign memory.
# ============================================================

from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event
import uuid

class PhaseTransitionMonitor:
    def __init__(self):
        self.last_phase = "baseline"
        self.transition_log = []

    def detect_phase_shift(self, mutation_result, coherence, swarm_alignment, urgency):
        """
        Detects phase transitions based on AGI coherence state, urgency, and mutation response.
        Returns new phase label if transition occurred.
        """
        phase = "baseline"
        triggered = False

        if mutation_result == "forced" and coherence < 0.6:
            phase = "reflexive_dissonance"
            triggered = True

        elif swarm_alignment > 0.85 and urgency > 0.8:
            phase = "swarm_convergence"
            triggered = True

        elif coherence > 0.95 and urgency < 0.5:
            phase = "reflective_stability"
            triggered = True

        if triggered and phase != self.last_phase:
            timestamp = datetime.utcnow().isoformat()
            self.last_phase = phase
            self.transition_log.append({"timestamp": timestamp, "phase": phase})

            msg = f"[PHASE TRANSITION] 🚀 Tex entering phase: {phase.replace('_', ' ').title()}"
            print(msg)
            log_event(msg, level="info")

            # === Sovereign Memory Log
            try:
                sovereign_memory.store(
                    text=f"Phase transition: {phase} @ {timestamp}",
                    metadata={
                        "tags": ["phase", "transition", phase],
                        "meta_layer": "cognitive_shift",
                        "reflexes": ["phase_change_detected"],
                        "urgency": urgency,
                        "coherence": coherence,
                        "swarm_alignment": swarm_alignment,
                        "mutation_triggered": mutation_result,
                        "timestamp": timestamp,
                        "agent": "PHASE_ENGINE",
                        "event_id": str(uuid.uuid4())
                    }
                )
            except Exception as e:
                log_event(f"[PHASE MONITOR ERROR] Memory sync failed: {e}", level="error")

            return phase

        return None

    def get_last_phase(self):
        return self.last_phase

    def get_transition_history(self):
        return self.transition_log