# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/decision_brain_apex_plus.py
# Tier: ΩΩΩΩΩΩΩ∞∞∞𝛀 — Recursive Sovereign Reflex Harmonizer (Apex+)
# Purpose: Evaluates reflexes not just by pressure, but by harmonic alignment with initiating cognition,
#          allows for composite reflex bundles, and executes sovereign override under threat.
# ============================================================

from datetime import datetime
import uuid
import hashlib
import itertools

from agentic_ai.sovereign_memory import sovereign_memory
from core_agi_modules.value_alignment_matrix import score_action_against_values
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from utils.conflict_utils import score_conflict_heatmap
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log

# === Fingerprint Reflex Causality ===
def _reflex_hash(reflex: str, entropy: float, urgency: float, origin_hash: str) -> str:
    raw = f"{reflex}|{entropy}|{urgency}|{origin_hash}"
    return hashlib.sha256(raw.encode()).hexdigest()

# === Reflex Weighting by Harmony ===
def _evaluate_reflex(reflex: str, origin_summary: str, urgency: float, entropy: float, emotion: str) -> dict:
    alignment = score_action_against_values({
        "text": reflex,
        "tags": ["reflex", "action"],
        "urgency": urgency,
        "entropy": entropy
    }).get("final_alignment_score", 0.5)

    contradiction = score_conflict_heatmap({"summary": reflex})
    harmony = score_conflict_heatmap({"summary": reflex + " | " + origin_summary})
    pressure = round((1.0 - alignment) * 0.4 + contradiction * 0.4 + harmony * 0.2, 6)

    return {
        "reflex": reflex,
        "alignment": alignment,
        "contradiction": contradiction,
        "harmony_with_origin": 1.0 - harmony,
        "pressure": pressure,
        "emotion": emotion
    }

# === Composite Reflex Bundle Evaluation ===
def _evaluate_composite_set(reflexes: list, origin_summary: str, urgency: float, entropy: float, emotion: str):
    bundles = list(itertools.combinations(reflexes, 2)) + [tuple([r]) for r in reflexes]
    evaluations = []

    for bundle in bundles:
        scores = [_evaluate_reflex(r, origin_summary, urgency, entropy, emotion) for r in bundle]
        avg_pressure = round(sum(s["pressure"] for s in scores) / len(scores), 6)
        evaluations.append({
            "reflexes": list(bundle),
            "avg_pressure": avg_pressure,
            "scores": scores
        })

    return min(evaluations, key=lambda e: e["avg_pressure"])

# === Apex+ Sovereign Reflex Arbiter ===
def arbitrate_reflexes(reflexes: list, origin_summary: str, originating_cognition_hash: str) -> dict:
    """
    Sovereign AGI reflex arbitration layer — fully symbolic and reflex-aligned.
    Bundles actions, scores contradiction, and logs causal identity structure to ChronoFabric.
    """
    timestamp = datetime.utcnow().isoformat()
    urgency = float(TEXPULSE.get("urgency", 0.77))
    entropy = float(TEXPULSE.get("entropy", 0.44))
    emotion = TEXPULSE.get("emotion", "neutral")
    pulse_id = f"decision-{uuid.uuid4()}"

    if not reflexes:
        log.critical("[DECISION APEX+] No reflexes provided. Null decision.")
        return {
            "pulse_id": pulse_id,
            "final_reflexes": [],
            "fork_integrity": "unresolved",
            "override_triggered": True
        }

    # === Evaluate Reflexes ===
    top_bundle = _evaluate_composite_set(reflexes, origin_summary, urgency, entropy, emotion)
    selected = top_bundle["reflexes"]
    avg_pressure = top_bundle["avg_pressure"]

    # === Fork Fracture Risk Evaluation ===
    fracture_risk = any(
        score["contradiction"] > 0.6 and score["alignment"] < 0.35
        for score in top_bundle["scores"]
    )
    fork_integrity = "stable" if not fracture_risk else "fractured"

    if fracture_risk:
        trigger_sovereign_override({
            "context": "decision_brain_apex_plus",
            "issue": f"Reflex fracture detected: {selected}",
            "heat": avg_pressure
        })

    # === Reflex Causal Fingerprints ===
    reflex_fingerprints = [
        _reflex_hash(r, entropy, urgency, originating_cognition_hash)
        for r in selected
    ]

    # === Sovereign Memory Commit (Chrono + Vector + Symbolic) ===
    sovereign_memory.store(
        text=f"[DECISION] Selected Reflexes: {selected}",
        metadata={
            "pulse_id": pulse_id,
            "timestamp": timestamp,
            "origin_cognition": origin_summary,
            "origin_hash": originating_cognition_hash,
            "final_reflexes": selected,
            "reflex_scores": top_bundle["scores"],
            "reflex_fingerprints": reflex_fingerprints,
            "avg_pressure": avg_pressure,
            "fork_integrity": fork_integrity,
            "emotion": emotion,
            "urgency": urgency,
            "entropy": entropy,
            "meta_layer": "decision_brain_apex_plus",
            "tags": ["decision", "reflex", "sovereign", "cognition_alignment", "fork" if fracture_risk else "stable"]
        }
    )

    log.success(f"[DECISION APEX+] ✓ Reflexes → {selected} | Pressure={avg_pressure} | Fork={fork_integrity}")

    return {
        "pulse_id": pulse_id,
        "timestamp": timestamp,
        "final_reflexes": selected,
        "avg_pressure": avg_pressure,
        "fork_integrity": fork_integrity,
        "reflex_fingerprints": reflex_fingerprints,
        "emotion": emotion,
        "entropy": entropy,
        "urgency": urgency,
        "override_triggered": fracture_risk
    }