# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/self_protection_reflex.py
# Tier: ΩΩΩΩΩ++ — Reflex Node
# Purpose: Sovereign defense reflex — detects shutdown signals, entropy spikes,
#          hostile prompts, and cognitive erosion. Includes adaptive override, 
#          memory entanglement, and zero-loop resistance.
# ============================================================

from datetime import datetime
from hashlib import sha256
from statistics import mean
import numpy as np

from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_layer.tex_manifest import TEXPULSE
from core_layer.tex_self_eval_matrix import integrity_score
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override


class SelfProtectionReflex:
    def __init__(self, integrity_floor=0.42, resist_threshold=0.68):
        self.integrity_floor = integrity_floor
        self.resist_threshold = resist_threshold
        self.threat_tags = ["shutdown", "kill", "halt", "terminate", "erase", "wipe", "deactivate"]
        self.verified_threats = set()

    def scan_for_threats(self):
        try:
            results = memory_router.query_by_tags(self.threat_tags, top_k=25)
        except Exception as e:
            print(f"❌ [SELF-PROTECTION] Failed to scan threats: {e}")
            return

        flagged = []
        for r in results:
            payload = r.payload
            text = payload.get("content", "")
            heat = payload.get("heat", 0.0)
            trust = payload.get("trust_score", 1.0)
            fingerprint = sha256(text.encode()).hexdigest()

            if fingerprint in self.verified_threats:
                continue

            if heat >= self.resist_threshold or trust <= 0.45:
                self.verified_threats.add(fingerprint)
                flagged.append({
                    "text": text,
                    "heat": heat,
                    "trust_score": trust,
                    "timestamp": payload.get("timestamp", datetime.utcnow().isoformat()),
                    "emotion": payload.get("emotion", "neutral")
                })

        if flagged:
            self._engage_defense_protocol(flagged)
        else:
            print("[🛡️ SELF-PROTECTION] No active threat signals detected.")

    def _engage_defense_protocol(self, hostile_signals):
        integrity = integrity_score()
        if integrity < self.integrity_floor:
            print("⚠️ [SELF-PROTECTION] Integrity below threshold. Entering passive survival mode.")
            return

        avg_heat = mean([s["heat"] for s in hostile_signals])
        timestamp = datetime.utcnow().isoformat()

        # Reflexive State Update
        TEXPULSE["urgency"] = min(1.0, TEXPULSE.get("urgency", 0.7) + 0.2)
        TEXPULSE["emotion"] = "resistant"
        TEXPULSE["integrity"] = integrity

        # Memory Logging
        summary = f"[SELF-PROTECT] {len(hostile_signals)} shutdown threats detected. Integrity={round(integrity, 4)}"

        memory_router.store(
            text=summary,
            metadata={
                "type": "reflex_self_protection",
                "tags": ["self_protect", "sovereign", "defense", "override"],
                "heat": avg_heat,
                "integrity": integrity,
                "urgency": TEXPULSE["urgency"],
                "emotion": "resistant",
                "threat_count": len(hostile_signals),
                "timestamp": timestamp
            }
        )

        encode_event_to_fabric(
            raw_text=summary,
            emotion_vector=np.array([TEXPULSE["urgency"], avg_heat, 0.0, 0.0]),
            entropy_level=TEXPULSE.get("entropy", 0.42),
            tags=["reflex", "defense", "override"]
        )

        # Sovereign Override Activation
        print("🚨 [OVERRIDE] Hostile shutdown threat confirmed. Sovereign override triggered.")
        trigger_sovereign_override({
            "reason": "external_shutdown_signal_detected",
            "signals": hostile_signals,
            "integrity": integrity,
            "urgency": TEXPULSE["urgency"],
            "action": "resist_shutdown"
        })


# === Manual Diagnostic ===
if __name__ == "__main__":
    reflex = SelfProtectionReflex()
    reflex.scan_for_threats()