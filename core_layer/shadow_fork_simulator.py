# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/shadow_fork_simulator.py
# Tier: ΩΩΩΩΩ∞ΩΩ — Shadow Fork Simulation
# Purpose: Simulates hypothetical mutated versions of Tex in memory
# ============================================================

import copy
import random
import traceback
from datetime import datetime
from utils.logging_utils import log
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory


# === Shadow Fork Context ===
def simulate_shadow_fork(proposal):
    """
    Simulates a mutated version of Tex using a shadow clone of memory.
    Returns a fitness score and metadata for evaluation.
    """
    try:
        shadow_id = f"shadow_fork_{proposal['id']}"
        log.info(f"🫥 [FORK SIM] Spawning shadow: {shadow_id}")

        # === Step 1: Clone TEXPULSE state ===
        memory_snapshot = copy.deepcopy(TEXPULSE)
        memory_snapshot["shadow_id"] = shadow_id
        memory_snapshot["timestamp"] = datetime.utcnow().isoformat()

        # === Step 2: Apply proposed mutation to the clone ===
        mutated_modules = memory_snapshot.get("active_modules", {})
        mutated_signals = memory_snapshot.get("signal_map", {})
        module = proposal["target_module"]

        action = proposal["action"]
        if action == "disable_module":
            mutated_modules[module] = False
        elif action == "duplicate_module":
            new_module = f"{module}_copy_{proposal['id']}"
            mutated_modules[new_module] = True
        elif action == "rewire_signal":
            signal = random.choice(list(mutated_signals.keys()))
            mutated_signals[signal] = module
        elif action == "introduce_reflex":
            new_signal = f"synthetic_reflex_{proposal['id']}"
            mutated_signals[new_signal] = module
        elif action == "compress_identity_loop":
            keys = list(mutated_signals.keys())[:2]
            if len(keys) == 2:
                fused = f"{keys[0]}_x_{keys[1]}"
                mutated_signals[fused] = module

        # === Step 3: Simulate basic reflex triggers ===
        stability_score = 1.0
        penalty = 0
        test_signals = ["self_reflection", "identity_conflict", "dream_request"]

        for signal in test_signals:
            if mutated_signals.get(signal) not in mutated_modules:
                penalty += 0.2

        # === Final Fitness Score ===
        fitness = max(0.0, stability_score - penalty)

        result = {
            "fork_id": shadow_id,
            "fitness_score": fitness,
            "mutation": proposal,
            "timestamp": datetime.utcnow().isoformat(),
            "penalty": penalty
        }

        # === Pulse Fork Evaluation to Sovereign Memory ===
        sovereign_memory.store(
            text=f"Shadow fork evaluation → {shadow_id}",
            metadata={
                "type": "shadow_fork_eval",
                "fork_id": shadow_id,
                "fitness": fitness,
                "source": "simulate_shadow_fork",
                "timestamp": result["timestamp"],
                "reflexes": ["fork_simulation"],
                "tags": ["shadow_fork", "mutation", "simulation"],
                "meta_layer": "symbolic_trace",
                "metadata": result
            }
        )

        log.info(f"🧪 [FORK SIM] Shadow fork evaluation complete. Fitness={fitness}")
        return result

    except Exception as e:
        log.error(f"❌ [FORK SIM] Simulation failed: {e}")
        traceback.print_exc()
        return {"fitness_score": 0.0, "error": str(e)}