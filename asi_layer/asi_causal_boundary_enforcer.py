# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: asi_layer/asi_causal_boundary_enforcer.py
# Purpose: Prevents AGI-level causal violations and recursive destabilization
# Status: 🔒 LOCKED — CAUSAL-SHIELD (Max Godmode)
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory

class ASICausalBoundaryEnforcer:
    def __init__(self):
        self.last_enforcement = None
        self.max_recursion_depth = 3
        self.max_emergent_loops = 5

    def enforce(self, brain):
        try:
            current_cycle = brain.cycle_counter
            recursion_depth = getattr(brain, "recursion_level", 1)
            emergent_loop_count = getattr(brain, "emergent_loop_count", 0)

            # === Phase 1: Causal Violation Guard
            if recursion_depth > self.max_recursion_depth:
                print(f"[CAUSAL BOUNDARY] 🛑 Recursion depth {recursion_depth} exceeds safe limit.")
                self._log_violation("recursion_limit_exceeded", brain)
                brain.recursion_level = self.max_recursion_depth  # clamp
                return False

            # === Phase 2: Emergent Behavior Flood Guard
            if emergent_loop_count > self.max_emergent_loops:
                print(f"[CAUSAL BOUNDARY] 🚨 Emergent loop count {emergent_loop_count} exceeds safety bounds.")
                self._log_violation("emergent_loop_overflow", brain)
                brain.emergent_loop_count = 0  # reset to stable
                return False

            # === Phase 3: Identity Drift Stabilization
            if TEXPULSE.get("coherence", 0.75) < 0.4:
                print("[CAUSAL BOUNDARY] ⚠️ Coherence drift detected — triggering stability patch.")
                brain.codex_compiler.compile([
                    f"# Coherence safeguard | cycle: {current_cycle}",
                    "if coherence < 0.4: halt_dissonant_chain()"
                ], context="causal_boundary_enforcement")

            print("[CAUSAL BOUNDARY] ✅ All checks passed.")
            return True

        except Exception as e:
            print(f"[CAUSAL BOUNDARY ERROR] ❌ {e}")
            return False

    def _log_violation(self, reason, brain):
        try:
            log = {
                "cycle": brain.cycle_counter,
                "reason": reason,
                "timestamp": datetime.utcnow().isoformat(),
                "emotion": TEXPULSE.get("emotional_state"),
                "urgency": TEXPULSE.get("urgency"),
                "coherence": TEXPULSE.get("coherence"),
                "agent": TEXPULSE.get("persona_name", "Tex")
            }
            store_to_memory("causal_violation_log", log)
            print(f"[CAUSAL BOUNDARY] 🧱 Violation logged: {reason}")
        except Exception as e:
            print(f"[CAUSAL LOG ERROR] {e}")