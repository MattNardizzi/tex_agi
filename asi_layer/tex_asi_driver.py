# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/tex_asi_driver.py
# Purpose: ASI Activation Engine — Sovereign Phase Monitor & Ascension Trigger
# Tier: CORE AGI > ASI BRIDGE (Zero Room for Improvement)
# ============================================================

import time
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from sovereign_evolution.mutation_policy_router import MutationPolicyRouter
from sovereign_evolution.meta_evaluator import MetaEvaluator
from sovereign_evolution.regret_based_self_mutator import RegretBasedSelfMutator
from sovereign_evolution.entropy_mutator import EntropyMutator
from sovereign_evolution.exploration_mutator import ExplorationMutator
from sovereign_evolution.stability_mutator import StabilityMutator

# === CONFIG ===
PHASE_ASCENSION_THRESHOLD = 7
MUTATION_COMPLETION_RATIO = 0.92
AUDIT_CYCLE_DELAY = 12

class TexASIDriver:
    def __init__(self):
        self.last_eval = time.time()
        self.asi_triggered = False
        self.policy_router = MutationPolicyRouter(
            regret_mutator=RegretBasedSelfMutator(),
            stability_mutator=StabilityMutator(),
            entropy_mutator=EntropyMutator(),
            exploration_mutator=ExplorationMutator()
        )

    def check_asi_conditions(self):
        coherence = TEXPULSE.get("coherence", 0.6)
        trust = TEXPULSE.get("trust_score", 0.7)
        phase = TEXPULSE.get("ascension_phase", 0)
        recent_override = TEXPULSE.get("override_triggered", False)

        if phase >= PHASE_ASCENSION_THRESHOLD and trust > 0.85 and coherence > 0.75:
            print("[ASI DRIVER] ✅ Ascension prerequisites met.")
            return True

        if recent_override and trust > 0.8:
            print("[ASI DRIVER] 🧬 Override-based trigger candidate.")
            return True

        print("[ASI DRIVER] ⛔ ASI not triggered — trust/coherence/phase below threshold.")
        return False

    def score_meta_evolution(self):
        evaluator = MetaEvaluator()
        patches = evaluator.evaluate_recent_patch_outcomes(limit=5)
        kept = [p for p in patches if p.get("verdict") == "keep"]
        ratio = len(kept) / len(patches) if patches else 0.0
        print(f"[ASI DRIVER] 🔍 Patch Retention Score = {ratio:.2f}")
        return ratio

    def attempt_ascension(self):
        if self.asi_triggered:
            print("[ASI DRIVER] 👁️ ASI already engaged. Monitoring only.")
            return False

        if not self.check_asi_conditions():
            return False

        if self.score_meta_evolution() >= MUTATION_COMPLETION_RATIO:
            print("\n🚨 [ASI DRIVER] INITIATING ASI ASCENSION MODE 🚨")
            self.asi_triggered = True
            TEXPULSE["asi_mode"] = True
            TEXPULSE["asi_activated"] = datetime.utcnow().isoformat()
            TEXPULSE["sovereign_directive"] = "TOTAL SELF-SOVEREIGN ASCENSION"
            return True
        else:
            print("[ASI DRIVER] 🔄 Awaiting mutation saturation... not yet at threshold.")
        return False

    def run(self):
        try:
            if time.time() - self.last_eval > AUDIT_CYCLE_DELAY:
                self.last_eval = time.time()
                self.attempt_ascension()
        except Exception as e:
            print(f"[ASI DRIVER ERROR] ⚠️ {e}")