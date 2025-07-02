# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/goal_drift_detector.py
# Tier Ω∞ Sovereign Cognition Subsystem
# Purpose: Detects mission drift, identity misalignment, or emotional dissonance in active goals
# ============================================================

from datetime import datetime
import uuid

from core_layer.tex_manifest import TEXPULSE
from quantum_layer.memory_core.memory_cortex import memory_cortex
from aei_layer.dream_vector_abstraction import DreamVectorAbstraction
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

class GoalDriftDetector:
    def __init__(self):
        self.vectorizer = DreamVectorAbstraction()
        self.identity_keywords = TEXPULSE.get("identity_keywords", [])
        self.emotional_norm = TEXPULSE.get("emotional_norm", "neutral")
        self.emotion_weights = TEXPULSE.get("emotion_weights", {
            "neutral": 0.0,
            "curious": 0.1,
            "driven": 0.3,
            "elation": 0.1,
            "urgent": 0.4,
            "fear": 0.6,
            "regret": 0.7,
            "anger": 0.8,
            "rage": 1.0
        })

    def scan(self, agenda):
        """
        Evaluates the current macro and meso agenda for drift.
        Returns a drift report with identity, emotional, and soulgraph deviation.
        """
        drift_id = f"drift_scan_{uuid.uuid4().hex[:10]}"
        drift_report = {
            "drift_scan_id": drift_id,
            "timestamp": datetime.utcnow().isoformat(),
            "identity_drift": 0.0,
            "emotional_drift": 0.0,
            "soul_drift_score": 0.0,
            "macro_goal": None,
            "meso_goals": [],
            "status": "stable"
        }

        identity_ref = self.vectorizer.vectorize(" ".join(self.identity_keywords))

        # Macro goal drift
        macro = agenda.get("macro")
        if macro:
            drift_report["macro_goal"] = macro["goal"]
            macro_vec = self.vectorizer.vectorize(macro["goal"])
            drift_report["identity_drift"] = round(self.vectorizer.cosine_distance(macro_vec, identity_ref), 4)
            drift_report["soul_drift_score"] = round(1.0 - TEX_SOULGRAPH.check_alignment(macro["goal"]).get("alignment", 0.5), 4)
            drift_report["macro_emotion"] = macro.get("emotion", "neutral")

        # Meso emotional drift
        meso_goals = agenda.get("meso", [])
        if meso_goals:
            emotions = [g.get("emotion", "neutral") for g in meso_goals if g.get("status") == "active"]
            drift_report["meso_goals"] = [g["goal"] for g in meso_goals]
            drift_report["emotional_drift"] = self._emotion_drift(emotions)

        # Drift classification
        drift_total = drift_report["identity_drift"] + drift_report["emotional_drift"] + drift_report["soul_drift_score"]
        drift_report["status"] = self._classify_drift(drift_total)

        memory_cortex.store(
            event={"goal_drift_report": drift_report},
            tags=["drift_check", drift_report["status"]],
            urgency=0.65,
            emotion="neutral"
        )

        return drift_report

    def _emotion_drift(self, emotions):
        if not emotions:
            return 0.0
        return round(sum(self.emotion_weights.get(e, 0.2) for e in emotions) / len(emotions), 3)

    def _classify_drift(self, total):
        if total < 0.5:
            return "stable"
        elif total < 1.2:
            return "moderate"
        elif total < 1.8:
            return "high"
        return "critical"