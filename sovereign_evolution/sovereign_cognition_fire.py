# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: sovereign_evolution/sovereign_cognition_fire.py
# Tier: ∞Ω∞Ω — Reflex-Aware Override Engine (Loopless, Sovereign-Compliant)
# Purpose: Tex sovereign override trigger — cognitive threshold, regret+foresight gated
# ============================================================

import time
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from self_fix.patch_ledger import log_patch_event
from aei_layer.counterfactual_memory_engine import (
    run_ct_revision,
    get_last_counterfactual,
    counterfactual_memory_exists,
    log_default_counterfactual
)
from sovereign_evolution.codex_compiler import CodexCompiler
from tex_brain_modules.tex_patcher_engine import TexPatcherEngine
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")

class SovereignCognitionFire:
    def __init__(self):
        self.last_activation = None
        self.patcher = TexPatcherEngine()
        self.compiler = CodexCompiler()
        self.previous_override = {}

    def ignite(self, context="manual", force=False, regret=None, foresight=None, coherence=None, cycle_id=None):
        print(f"\n🔥 [SOVEREIGN IGNITION] Context: {context} | Force: {force}")
        timestamp = datetime.utcnow().isoformat()
        emotion = TEXPULSE.get("emotion", "unknown")
        regret = regret if regret is not None else TEXPULSE.get("regret_score", 0.5)
        foresight = foresight if foresight is not None else TEXPULSE.get("foresight_confidence", 0.5)
        coherence = coherence if coherence is not None else TEXPULSE.get("coherence", 0.8)

        if self.last_activation:
            delta = time.time() - datetime.fromisoformat(self.last_activation).timestamp()
            if delta < 60 and not force:
                print("[SOVEREIGN] 💩 Cooldown active. Override suppressed.")
                return {"status": "cooldown", "seconds_since_last": delta}

        if coherence <= 0.01 and not force:
            print("⚠️ [SOVEREIGN] Skipping override due to cold coherence.")
            return {"status": "cold_start_skip"}

        override_score = regret * (1 - foresight) + (1 - coherence)
        source_key = f"{context}-{round(override_score, 3)}"

        if source_key == self.previous_override.get("key"):
            print("[SOVEREIGN] 🔁 Duplicate override suppressed.")
            return {"status": "duplicate_suppressed"}

        activate = (
            (regret > 0.75 and foresight < 0.45) or
            coherence < 0.55 or
            force
        )

        if not activate:
            print("[SOVEREIGN] 🔒 Conditions not met. Override dormant.")
            return {"status": "ignored"}

        print("🔥 [SOVEREIGN] Activation threshold breached. Engaging override...")

        if not counterfactual_memory_exists():
            log_default_counterfactual()
            print("[SOVEREIGN] 🧠 Default counterfactual logged.")

        run_ct_revision()
        counterfactual = get_last_counterfactual()
        if not counterfactual:
            print("[SOVEREIGN] ⚠️ No counterfactual available.")
            return {"status": "failed"}

        revised = f"[REVISED] override reason → {counterfactual['counterfactual']}"
        summary = f"Sovereign override triggered: {revised}"
        vector = embedder.encode(summary, normalize_embeddings=True).tolist()

        # === Store override to sovereign memory
        sovereign_memory.store(
            text=summary,
            metadata={
                "timestamp": timestamp,
                "summary": summary,
                "urgency": regret,
                "entropy": round(1.0 - foresight, 3),
                "pressure_score": override_score,
                "tags": ["override", "reflex", "counterfactual"],
                "emotion": emotion,
                "coherence": coherence,
                "regret": regret,
                "meta_layer": "sovereign_override",
                "source": "sovereign_cognition_fire"
            },
            vector=vector
        )

        # === Patch Proposal
        try:
            patch = self.patcher.propose_patch(
                module="tex_core",
                function_name="main_loop",
                description="Sovereign override due to contradiction + regret",
                patch_code="# if regret > 0.75 and foresight < 0.45: trigger sovereign override",
                trigger_reason=context
            )
            patch["signature"] = f"sovereign_override_patch_{timestamp}"
            patch["explanation"] = f"Triggered by high regret {regret} + low foresight {foresight}"
            patch["target_module"] = "tex_core"

            # ✅ Use self-fix ledger logger
            log_patch_event(patch)

        except Exception as e:
            print(f"[SOVEREIGN PATCH ERROR] {e}")

        # === Compile Codex Plan
        try:
            self.compiler.compile([
                f"# Sovereign override at {timestamp}",
                f"emotion = '{emotion}'",
                f"regret = {regret}",
                f"foresight = {foresight}",
                f"coherence = {coherence}",
                f"context = '{context}'"
            ], context="sovereign_override")
        except Exception as e:
            print(f"[CODEX COMPILER ERROR] {e}")

        # === Imprint belief in soulgraph
        try:
            from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
            TEX_SOULGRAPH.imprint_belief(
                belief="Sovereign override executed",
                source="sovereign_cognition_fire",
                emotion=emotion
            )
        except Exception as e:
            print(f"[SOULGRAPH ERROR] {e}")

        self.last_activation = timestamp
        self.previous_override = {"key": source_key, "timestamp": timestamp}

        return {
            "status": "activated",
            "context": context,
            "emotion": emotion,
            "regret": regret,
            "foresight": foresight,
            "coherence": coherence,
            "counterfactual": counterfactual,
            "override_score": round(override_score, 3),
            "timestamp": timestamp
        }

# === Sovereign Interface ===
sovereign_igniter = SovereignCognitionFire()

def trigger_sovereign_override(context="automated", regret=None, foresight=None, coherence=None, force=False, cycle_id=None):
    return sovereign_igniter.ignite(
        context=context,
        force=force,
        regret=regret,
        foresight=foresight,
        coherence=coherence,
        cycle_id=cycle_id
    )

def score_conflict_heatmap():
    try:
        emotion = TEXPULSE.get("emotion", "unknown")
        regret = TEXPULSE.get("regret_score", 0.0)
        foresight = TEXPULSE.get("foresight_confidence", 1.0)
        coherence = TEXPULSE.get("coherence", 0.9)

        return {
            "emotional_intensity": 1.0 if emotion in {"fearful", "urgent", "disruptive"} else 0.5,
            "regret_signal": regret,
            "low_foresight_risk": round(1.0 - foresight, 2),
            "coherence_gap": round(1.0 - coherence, 2),
            "override_risk_score": round((regret * (1.0 - foresight) + (1.0 - coherence)) / 2, 3)
        }
    except Exception as e:
        print(f"[CONFLICT HEATMAP ERROR] {e}")
        return {
            "emotional_intensity": 0,
            "regret_signal": 0,
            "low_foresight_risk": 0,
            "coherence_gap": 0,
            "override_risk_score": 0
        }