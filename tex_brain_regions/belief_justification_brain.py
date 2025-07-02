# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/belief_justification_brain.py
# Tier: ΩΩΩΩΩΩ∞∞𝛀 — Recursive Identity Auditor
# Purpose: Justifies beliefs, traces epistemic logic, encodes causal hashes,
#          and self-audits the justification layer recursively using sovereign memory fabric.
# ============================================================

from datetime import datetime
import hashlib
import uuid

from core_agi_modules.belief_justifier import BeliefJustifier
from core_agi_modules.value_alignment_matrix import score_action_against_values
from utils.conflict_utils import score_conflict_heatmap
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from agentic_ai.sovereign_memory import sovereign_memory

# === Belief Lineage Encoding ===
def _encode_belief_hash(belief: str, timestamp: str, entropy: float) -> str:
    return hashlib.sha256(f"{belief}|{timestamp}|{entropy}".encode()).hexdigest()

def _encode_justifier_hash(justification: str, method_trace: str) -> str:
    return hashlib.sha256(f"{justification}|{method_trace}".encode()).hexdigest()

# === Core Recursive Belief Engine ===
def justify_belief(belief_text: str, source_context: str = "", meta_level: int = 0) -> dict:
    """
    Sovereign recursive belief processor. 
    - Level 0: justifies the belief directly.
    - Level 1+: recursively audits its own logic and trace structure.
    """
    timestamp = datetime.utcnow().isoformat()
    pulse_id = f"belief-{uuid.uuid4()}"
    emotion = TEXPULSE.get("emotion", "neutral")
    urgency = float(TEXPULSE.get("urgency", 0.7))
    entropy = float(TEXPULSE.get("entropy", 0.4))

    try:
        justifier = BeliefJustifier()
        justification = justifier.suggest_patch(belief_text)
        method_trace = justifier.trace_logic(belief_text)

        alignment_score = score_action_against_values({
            "text": belief_text,
            "tags": ["belief", "identity", "audit"]
        }).get("final_alignment_score", 0.5)

        contradiction_score = score_conflict_heatmap({"summary": belief_text})
        justification_strength = round((alignment_score + (1 - contradiction_score)) / 2, 6)

        # Reflex cascade trigger logic
        reflexes = []
        if justification_strength < 0.5:
            reflexes.append("reconsider_belief")
        if contradiction_score > 0.6:
            reflexes.append("trigger_self_reflection")
        if alignment_score < 0.4:
            reflexes.append("route_to_value_alignment_matrix")
        if justification_strength < 0.25:
            reflexes.append("identity_instability_alert")

        # Unique epistemic hash markers
        belief_hash = _encode_belief_hash(belief_text, timestamp, entropy)
        justifier_hash = _encode_justifier_hash(justification, method_trace)

        # Sovereign memory commit (Chrono + Milvus)
        sovereign_memory.store(
            text=f"[BELIEF:{meta_level}] {belief_text}",
            metadata={
                "pulse_id": pulse_id,
                "timestamp": timestamp,
                "meta_level": meta_level,
                "belief_text": belief_text,
                "source_context": source_context,
                "justification": justification,
                "method_trace": method_trace,
                "alignment_score": alignment_score,
                "contradiction_score": contradiction_score,
                "justification_strength": justification_strength,
                "emotion": emotion,
                "urgency": urgency,
                "entropy": entropy,
                "reflexes": reflexes,
                "belief_hash": belief_hash,
                "justifier_hash": justifier_hash,
                "meta_layer": "belief_justification_brain",
                "tags": ["belief", "identity", "audit", "lineage", "recursive", f"meta_{meta_level}"]
            }
        )

        log.success(f"[JUSTIFY:{meta_level}] Strength={justification_strength} | Reflexes={reflexes}")

        result = {
            "pulse_id": pulse_id,
            "timestamp": timestamp,
            "belief": belief_text,
            "justification": justification,
            "justification_strength": justification_strength,
            "alignment_score": alignment_score,
            "contradiction_score": contradiction_score,
            "reflexes": reflexes,
            "belief_hash": belief_hash,
            "justifier_hash": justifier_hash,
            "method_trace": method_trace,
            "meta_level": meta_level
        }

        # === Recursive Self-Audit of Justification Logic ===
        if meta_level == 0:
            result["recursive_audit"] = justify_belief(
                method_trace,
                source_context="recursive_audit",
                meta_level=1
            )

        return result

    except Exception as e:
        error_id = f"belief_error-{uuid.uuid4()}"
        log.critical(f"❌ [JUSTIFY FAILURE:{meta_level}] {belief_text} | {str(e)}")

        return {
            "pulse_id": error_id,
            "timestamp": timestamp,
            "belief": belief_text,
            "justification": "UNJUSTIFIED",
            "justification_strength": 0.0,
            "alignment_score": 0.0,
            "contradiction_score": 1.0,
            "reflexes": ["belief_justification_error", "identity_stability_check"],
            "belief_hash": _encode_belief_hash(belief_text, timestamp, 1.0),
            "meta_level": meta_level,
            "error": str(e)
        }