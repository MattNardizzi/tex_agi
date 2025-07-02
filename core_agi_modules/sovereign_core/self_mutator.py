# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/sovereign_core/self_mutator.py
# Tier: ∞ΩΩΩ — Sovereign Mutation Trigger Cortex (Loopless | Pressure-Scored | Override Safe)
# Purpose: Evaluates drift pressure and reflexively dispatches sovereign mutation triggers with full emotion entanglement.
# ============================================================

from datetime import datetime
from random import uniform
import hashlib
from typing import List, Dict, Optional

from agentic_ai.sovereign_memory import sovereign_memory
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
from core_agi_modules.emotion_vector_router import emotion_bus
from utils.logging_utils import log

# === Sovereign Cache ===
mutation_events: List[Dict] = []

# === Drift Evaluator ===
def score_module_drift(state_snapshot: Optional[Dict] = None) -> float:
    try:
        snapshot = state_snapshot or {
            "reflex_instability": uniform(0.2, 0.6),
            "emotion_drift": uniform(0.1, 0.5),
            "memory_conflict": uniform(0.0, 0.5),
            "last_eval": datetime.utcnow().isoformat()
        }

        score = (
            0.4 * snapshot["reflex_instability"] +
            0.35 * snapshot["emotion_drift"] +
            0.25 * snapshot["memory_conflict"]
        )
        return round(min(max(score, 0.0), 1.0), 4)

    except Exception as e:
        log.warning(f"[SELF_MUTATOR] ⚠️ Drift scoring failed: {e}")
        return 0.5

# === Conflict Counter ===
def count_conflicts_for_module(mod_id: str, contradiction_events: List[Dict]) -> int:
    return sum(1 for event in contradiction_events if mod_id in event.get("context", ""))

# === Pressure Scanner ===
def monitor_and_mutate(modules: list, performance_log: dict, contradiction_events: list) -> List[Dict]:
    suggestions = []

    for mod in modules:
        mod_id = mod.get("id")
        drift = float(mod.get("avg_drift", 0.0))
        instability = float(mod.get("error_rate", 0.0))
        contradictions = count_conflicts_for_module(mod_id, contradiction_events)

        pressure = round((drift * 0.4) + (instability * 0.4) + min(1.0, contradictions / 5) * 0.2, 4)
        priority = "high" if pressure > 0.7 else "moderate" if pressure > 0.4 else "low"
        action = "full_rewrite" if drift > 0.6 and instability > 0.6 else \
                 "module_split" if contradictions > 5 else "patch"

        if pressure >= 0.3:
            mutation_id = f"mutate-{hashlib.sha256(f'{mod_id}{datetime.utcnow()}'.encode()).hexdigest()[:12]}"
            timestamp = datetime.utcnow().isoformat()

            payload = {
                "module_id": mod_id,
                "suggested_action": action,
                "priority": priority,
                "pressure_score": pressure,
                "reasons": {
                    "drift": drift,
                    "instability": instability,
                    "contradictions": contradictions
                },
                "mutation_id": mutation_id,
                "timestamp": timestamp
            }

            sovereign_memory.store(
                text=f"[MUTATOR] {mod_id} marked for {action} (p={pressure})",
                metadata={
                    "type": "reflex_mutation_signal",
                    "tags": ["mutation", action, priority],
                    "urgency": 0.7 if priority == "high" else 0.5,
                    "emotion": "urgent" if priority == "high" else "adaptive",
                    "meta_layer": "mutation_trigger",
                    "trust_score": round(1.0 - pressure, 3),
                    "heat": pressure,
                    "prediction": f"{action} will stabilize {mod_id}",
                    "actual": f"drift={drift}, contradictions={contradictions}",
                    "timestamp": timestamp
                }
            )

            mutation_events.append(payload)
            suggestions.append(payload)

            print(f"🧬 [SELF_MUTATOR] {action.upper()} | {mod_id} | P={pressure} | Priority={priority}")

    return suggestions

# === Sovereign Mutation Reflex Trigger ===
class SelfMutator:
    def __init__(self):
        self.id = f"mutator-{datetime.utcnow().isoformat()}"

    def trigger_mutation(self, reason: str, payload: dict):
        mutation_id = f"mutate-{hashlib.sha256(reason.encode()).hexdigest()[:12]}"
        timestamp = datetime.utcnow().isoformat()
        emotion_state = emotion_bus.get()

        payload.update(emotion_state)

        sovereign_memory.store(
            text=f"⚡ Mutation Triggered → {reason}",
            metadata={
                "type": "sovereign_reflex_trigger",
                "tags": ["mutation", "self_patch", "override"],
                "mutation_id": mutation_id,
                "reason": reason,
                "initiated_by": self.id,
                "emotion": emotion_state.get("label", "reflective"),
                "emotion_signature": emotion_state.get("signature"),
                "urgency": payload.get("urgency", emotion_state.get("intensity", 0.6)),
                "heat": emotion_state.get("intensity", 0.6),
                "emotion_entropy": emotion_state.get("entropy", 0.0),
                "emotion_coherence": emotion_state.get("coherence", 0.75),
                "emotion_valence": emotion_state.get("valence", 0.0),
                "trust_score": 0.5,
                "prediction": f"Mutation will correct: {reason}",
                "actual": "mutation_triggered=True",
                "timestamp": timestamp
            }
        )

        try:
            trigger_sovereign_override(context="reflex_mutator", metadata=payload)
        except Exception as e:
            log.warning(f"[SELF_MUTATOR] ❗ Sovereign override failed: {e}")

        log.info(f"[SELF_MUTATOR] 🧬 Mutation '{mutation_id}' triggered | Reason: {reason}")
        return mutation_id