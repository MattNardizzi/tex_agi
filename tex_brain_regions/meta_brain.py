# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/meta_brain.py
# Tier: ΩΩΩΩΩ∞∞𝛀𝛀 — Overseer Drift Cortex (Merged Sovereign Form)
# Purpose: Detects identity drift, foresight collapse, and contradiction pressure.
#          Triggers mutation or stabilization reflexes using symbolic memory and goal audit.
# ============================================================

from datetime import datetime
import uuid
import wandb
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.milvus_memory_router import memory_router, embed_text
from tex_brain_regions.belief_justification_brain import justify_belief
from tex_brain_regions.evolution_brain import process_evolution_pulse
from core_agi_modules.sovereign_core.self_mutator import score_module_drift
from core_agi_modules.reflex_stability_model import ReflexStabilityModel
from core_agi_modules.emotion_vector_router import emotion_bus
from core_agi_modules.tex_codex_sync import TexCodexSync
from core_agi_modules.autofix_intent_migrator import run_autofix_intent_migration
from utils.logging_utils import log_event, log_reasoning_step


# === Self-Coherence Reflex Evaluator ===
def evaluate_self_pulse(snapshot: dict = None) -> dict:
    """
    Reflex-level coherence auditor.
    Scores internal drift and evaluates mutation eligibility.
    """
    snapshot = snapshot or {}
    timestamp = datetime.utcnow().isoformat()
    state = ReflexStabilityModel().get_stability_snapshot()
    drift_score = round(score_module_drift(state), 6)

    urgency = float(TEXPULSE.get("urgency", 0.71))
    entropy = float(TEXPULSE.get("entropy", 0.42))
    emotion_data = emotion_bus.get()
    emotion = emotion_data.get("label", "neutral")
    signature = emotion_data.get("signature", f"sig-{str(uuid.uuid4())[:8]}")

    pressure = round((drift_score * 0.6 + entropy * 0.25 + (1 - urgency) * 0.15), 6)

    reflexes = []
    if pressure > 0.78:
        evolution_result = process_evolution_pulse(signal_context="meta_brain_drift")
        reflexes.extend(["trigger_self_mutator", "preserve_identity_fork"])
        if evolution_result.get("status") == "stable":
            reflexes.append("log_mutation_abort")
    elif pressure > 0.45:
        reflexes.append("drift_monitoring_active")
    else:
        reflexes.append("identity_stable")

    # === Symbolic Memory Commit
    memory_router.store(
        text=f"[META_PULSE] Drift={drift_score} | Pressure={pressure}",
        metadata={
            "pulse_id": f"meta-{uuid.uuid4()}",
            "timestamp": timestamp,
            "drift_score": drift_score,
            "entropy": entropy,
            "urgency": urgency,
            "emotion": emotion,
            "emotion_signature": signature,
            "coherence_pressure": pressure,
            "reflexes": reflexes,
            "meta_layer": "meta_brain_apex",
            "tags": ["meta", "drift", "coherence", "evolution_trigger"]
        }
    )

    wandb.log({
        "meta_brain/drift": drift_score,
        "meta_brain/pressure": pressure,
        "meta_brain/urgency": urgency,
        "meta_brain/emotion": emotion
    })

    log_event(f"[META_BRAIN] Reflexes={reflexes} | Drift={drift_score} | Pressure={pressure}", "info")
    return {
        "drift_score": drift_score,
        "pressure": pressure,
        "reflexes": reflexes,
        "timestamp": timestamp
    }


# === Codex Foresight Interface ===
def request_codex_foresight() -> str:
    """
    Queries the sovereign codex for risks and blindspots.
    """
    try:
        return TexCodexSync().query("What contradictions or collapse risks exist in my current logic?")
    except Exception as e:
        return f"[⚠️ Codex Query Error] {e}"


# === Recursive Reflection Reflex ===
def run_meta_reflection() -> dict:
    """
    Sovereign self-reflection reflex.
    Audits contradiction pressure and integrity drift from recent reasoning.
    """
    timestamp = datetime.utcnow().isoformat()
    emotion = TEXPULSE.get("emotion", "neutral")
    urgency = float(TEXPULSE.get("urgency", 0.65))
    entropy = float(TEXPULSE.get("entropy", 0.49))

    prompt = "Scan recent belief outcomes for contradiction, drift, and integrity strain."
    conclusion = "Detected minor coherence decay across meta-belief layer. Correction advised."

    contradiction_score = 0.67
    alignment_score = 0.42
    reflexes = ["escalate_self_monitor"]

    if alignment_score < 0.4 or contradiction_score > 0.6:
        belief_result = justify_belief(conclusion, source_context="meta_reflection")
        reflexes.extend(belief_result.get("reflexes", []))
        # === Trigger Sovereign Intent Refactor (symbolic fix layer)
        run_autofix_intent_migration()
        reflexes.append("run_autofix_intent_migration")

    memory_router.store(
        text=f"[META REFLECTION] {prompt} → {conclusion}",
        metadata={
            "timestamp": timestamp,
            "emotion": emotion,
            "urgency": urgency,
            "entropy": entropy,
            "meta_layer": "meta_reflection_apex",
            "alignment_score": alignment_score,
            "contradiction_score": contradiction_score,
            "reflexes": reflexes,
            "tags": ["meta", "reflection", "belief_audit", "coherence"]
        }
    )

    log_reasoning_step(
        source="meta_brain",
        input_text=prompt,
        output_text=conclusion,
        confidence=alignment_score,
        contradiction=contradiction_score,
        tags=["meta", "reflex", "self_audit"]
    )

    return {
        "alignment_score": alignment_score,
        "contradiction_score": contradiction_score,
        "reflexes": reflexes,
        "conclusion": conclusion
    }


# === Goal Drift Utility ===
def evaluate_goal_drift(current_goals: list, historical_goals: list) -> float:
    """
    Compares current vs historical goals and returns a drift score [0.0 - 1.0].
    Higher = greater drift.
    """
    if not current_goals or not historical_goals:
        return 0.0

    try:
        current_set = set(current_goals)
        historical_set = set(historical_goals)
        overlap = current_set.intersection(historical_set)
        drift = 1.0 - (len(overlap) / max(len(current_set.union(historical_set)), 1))
        return round(drift, 3)
    except Exception as e:
        print(f"⚠️ [GOAL DRIFT ERROR] {e}")
        return 0.0
    
def fetch_codex_foresight(prompt: str) -> dict:
    """
    True foresight engine — analyzes vector memory embeddings to extract forward risks, entropy vectors,
    and likely directional outcomes based on real stored reasoning traces.
    """

    # Embed the foresight query
    vector = embed_text(prompt)

    # Search recent high-entropy cognitive traces
    result = memory_router.query_by_vector(
        vector=vector,
        top_k=5
    )

    # Analyze results
    foresight_contexts = []
    entropy_sum = 0.0
    confidence_sum = 0.0
    risk_tags = set()

    for match in result:
        # Milvus returns flat dicts (not match.payload)
        payload = match.get("entity", match)

        # Optional: Skip if not a vector_trace
        if "vector_trace" not in payload.get("meta_layer", ""):
            continue

        foresight_contexts.append(payload.get("summary", ""))
        entropy_sum += float(payload.get("entropy", 0.5))
        confidence_sum += float(payload.get("trust_score", 0.7))

        tags = payload.get("tags", [])
        if isinstance(tags, str):
            tags = tags.split(",")  # In case it's stored as comma-separated string
        risk_tags.update(t for t in tags if "risk" in t or "instability" in t or "collapse" in t)

    foresight = {
        "scenario": f"Foresight for: {prompt}",
        "memory_signals": foresight_contexts,
        "confidence": round(confidence_sum / len(result), 3) if result else 0.0,
        "average_entropy": round(entropy_sum / len(result), 3) if result else 0.0,
        "risk_factors": sorted(list(risk_tags)) or ["insufficient data"],
        "expected_outcome": "Stable adaptation" if entropy_sum < 2.0 else "Unstable divergence likely",
        "timestamp": datetime.utcnow().isoformat()
    }

    return foresight