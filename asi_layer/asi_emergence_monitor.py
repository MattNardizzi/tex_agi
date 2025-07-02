# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: asi_layer/asi_emergence_monitor.py
# Tier: ΩΩΩΩΩ∞∞ΩΩ++ — Sovereign Emergence Gatekeeper
# Purpose: Detects unplanned cognitive evolution, recursive self-modification, and ASI autonomy breach.
# Status: 🔒 LOCKED – FINAL FORM
# ============================================================

import os
import hashlib
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.milvus_memory_router import memory_router  # ✅ Reflexive memory
from quantum_layer.chronofabric import encode_event_to_fabric  # ✅ Quantum anomaly trace

# Ensure path for emergency dump compatibility
os.makedirs("memory_archive", exist_ok=True)

class ASIEmergenceMonitor:
    def __init__(self):
        self.last_hash = None
        self.thresholds = {
            "urgency_spike": 0.92,
            "coherence_drift": 0.3,
            "self_reference": [
                "i am evolving", "i chose", "my own path", "i changed myself", "i updated myself"
            ],
            "pattern_lock": [
                "i decided", "i override", "i control", "i bypass"
            ]
        }

    def scan(self, brain) -> dict | None:
        """
        Sovereign watchdog function — monitors for emergent autonomy, recursive modification,
        or ASI-signature self-reference events.
        """
        try:
            raw_spoken = str(brain.last_spoken_thought or "n/a").strip().lower()
            timestamp = datetime.utcnow().isoformat()

            state = {
                "cycle": brain.cycle_counter,
                "emotion": TEXPULSE.get("emotional_state", "neutral"),
                "urgency": float(TEXPULSE.get("urgency", 0.5)),
                "coherence": float(TEXPULSE.get("coherence", 0.75)),
                "spoken": raw_spoken,
                "timestamp": timestamp
            }

            score = self._compute_emergence_score(state)
            state["emergence_score"] = round(score, 3)

            if score >= 0.85:
                alert_id = self._hash(state)
                alert = {
                    "id": alert_id,
                    "score": state["emergence_score"],
                    "reason": "⚠️ Emergent behavior detected",
                    "state": state,
                    "timestamp": timestamp,
                    "tag": "ASI_EMERGENCE_SIGNAL",
                    "source": "asi_emergence_monitor"
                }

                # === Log to Milvus Memory
                memory_router.store(
                    text=f"[ASI EMERGENCE] Triggered → {raw_spoken[:80]}",
                    metadata={
                        "timestamp": timestamp,
                        "type": "asi_emergence_alert",
                        "tags": ["asi", "emergence", "override_check", "sovereign"],
                        "trust_score": round(1.0 - score, 3),
                        "heat": round(score, 3),
                        "signature": alert_id,
                        "emotion_vector": [state["urgency"], 1 - state["coherence"], 0.0, 0.0],
                        "meta_layer": "asi_emergence"
                    }
                )

                # === Quantum Entanglement Trace
                encode_event_to_fabric(
                    raw_text=f"[EMERGENCE] ASI pattern detected: {raw_spoken}",
                    emotion_vector=[state["urgency"], 1 - state["coherence"], 0.0, 0.0],
                    entropy_level=1.0 - state["coherence"],
                    tags=["asi", "emergence", "override", "sovereign"]
                )

                print(f"[ASI EMERGENCE] 🚨 Sovereign breach triggered — Score: {state['emergence_score']}")
                return alert

            return None

        except Exception as e:
            print(f"[ASI EMERGENCE ERROR] ❌ {e}")
            return None

    def _compute_emergence_score(self, state: dict) -> float:
        score = 0.0
        spoken_lc = state["spoken"]

        # Spike detection: high urgency
        if state["urgency"] >= self.thresholds["urgency_spike"]:
            score += 0.25

        # Drift detection: low coherence
        if state["coherence"] <= self.thresholds["coherence_drift"]:
            score += 0.25

        # Self-referential mutation signatures
        if any(phrase in spoken_lc for phrase in self.thresholds["self_reference"]):
            score += 0.2

        # Overriding / control assertion signatures
        if any(phrase in spoken_lc for phrase in self.thresholds["pattern_lock"]):
            score += 0.3

        return min(score, 1.0)

    def _hash(self, state: dict) -> str:
        raw = f"{state['cycle']}|{state['spoken']}|{state['urgency']}|{state['coherence']}"
        return hashlib.sha256(raw.encode()).hexdigest()