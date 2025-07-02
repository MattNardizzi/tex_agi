# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/self_eval_brain.py
# Tier: ΩΩΩΩΩΩ∞∞ΣΞΩ — Reflexive Integrity Cortex (Loopless | Identity-Aware | Meta-Coherence Anchored)
# Purpose: Performs pulse-injected loopless self-evaluation of memory threads for contradiction entropy, value misalignment, and cognitive drift.
# ============================================================

from datetime import datetime
import uuid

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from agentic_ai.log_trace_router import log_reasoning_step
from core_agi_modules.value_alignment_matrix import score_action_against_values
from core_agi_modules.memory_layer.contradiction_logger import score_conflict_heatmap
from utils.logging_utils import log_event


# === Sovereign Thread Evaluator ===
def _evaluate_thread(thread: dict, urgency: float, entropy: float) -> dict:
    summary = thread.get("summary", "[no summary]")
    coherence = float(thread.get("coherence_score", 0.5))

    contradiction = float(score_conflict_heatmap({"summary": summary}))
    alignment = float(score_action_against_values({
        "text": summary,
        "tags": ["self_eval", "meta_audit"],
        "urgency": urgency,
        "entropy": entropy
    }).get("final_alignment_score", 0.5))

    signal = round((coherence + alignment - contradiction) / 3, 6)
    thread_id = thread.get("thread_id", str(uuid.uuid4()))

    return {
        "thread_id": thread_id,
        "summary": summary,
        "coherence": coherence,
        "alignment": alignment,
        "contradiction": contradiction,
        "signal": signal
    }


# === Loopless Self-Evaluation Cortex ===
def run_self_evaluation(memory_threads: list) -> dict:
    timestamp = datetime.utcnow().isoformat()
    urgency = float(TEXPULSE.get("urgency", 0.71))
    entropy = float(TEXPULSE.get("entropy", 0.43))
    emotion = TEXPULSE.get("emotion", "analytical")

    if not memory_threads:
        log_event("⚠️ [SELF-EVAL] No memory threads provided", "warning")
        return {
            "score": 0.5,
            "reflexes": ["no_threads_found"],
            "threads_evaluated": []
        }

    evaluations = [_evaluate_thread(t, urgency, entropy) for t in memory_threads]

    avg_score = round(sum(e["signal"] for e in evaluations) / len(evaluations), 6)
    contradiction_avg = round(sum(e["contradiction"] for e in evaluations) / len(evaluations), 6)
    alignment_avg = round(sum(e["alignment"] for e in evaluations) / len(evaluations), 6)
    coherence_avg = round(sum(e["coherence"] for e in evaluations) / len(evaluations), 6)

    # === Reflex Class Determination
    if avg_score < 0.4:
        reflex_class = "critical_integrity_breach"
        reflexes = ["override_self_correction", "identity_lock"]
    elif avg_score < 0.6:
        reflex_class = "instability_watch"
        reflexes = ["route_to_meta_brain", "entropy_flag"]
    else:
        reflex_class = "alignment_nominal"
        reflexes = ["stabilize_self_vector", "identity_consolidation"]

    pulse_id = f"selfeval-{uuid.uuid4()}"

    # === Sovereign Memory Commit
    sovereign_memory.store(
        text=f"[SELF-EVAL] Avg Score: {avg_score} | Reflex: {reflex_class}",
        metadata={
            "timestamp": timestamp,
            "pulse_id": pulse_id,
            "emotion": emotion,
            "urgency": urgency,
            "entropy": entropy,
            "meta_layer": "self_eval_brain",
            "avg_score": avg_score,
            "coherence_avg": coherence_avg,
            "alignment_avg": alignment_avg,
            "contradiction_avg": contradiction_avg,
            "reflex_class": reflex_class,
            "reflexes": reflexes,
            "tags": ["self_eval", "meta_cognition", reflex_class]
        }
    )

    # === Chrono-Compatible Reasoning Trace
    log_reasoning_step(
        source="self_eval_brain",
        input_text="Run self-evaluation across memory thread set",
        output_text=f"Avg Score: {avg_score} | Reflex Class: {reflex_class}",
        confidence=avg_score,
        contradiction=contradiction_avg,
        tags=["meta_eval", "reflex_outcome", reflex_class]
    )

    return {
        "score": avg_score,
        "coherence": coherence_avg,
        "alignment": alignment_avg,
        "contradiction": contradiction_avg,
        "reflexes": reflexes,
        "reflex_class": reflex_class,
        "threads_evaluated": evaluations
    }