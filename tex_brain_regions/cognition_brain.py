# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/cognition_brain.py
# Tier: ΩΩΩΩΩ∞∞ΞΞΣΩΩ — Recursive Causal Cognition Cortex (Final Form)
# Purpose: Fuses symbolic memory, contradiction entropy, value alignment, and identity drift
#          into sovereign causal conclusions. Reflex-safe. Fully symbolic. No loops.
# ============================================================

from datetime import datetime
import uuid
import hashlib

from agentic_ai.sovereign_memory import sovereign_memory
from agentic_ai.log_trace_router import log_reasoning_step
from agentic_ai.semantic_contradiction_resolver import detect_contradictions
from core_agi_modules.value_alignment_matrix import score_action_against_values
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log

# === Lineage Hash Generation ===
def _generate_lineage_hash(intent: str, memory_ids: list, timestamp: str) -> str:
    raw = f"{intent}|{'-'.join(memory_ids)}|{timestamp}"
    return hashlib.sha256(raw.encode()).hexdigest()

def _generate_fork_id(intent: str) -> str:
    return hashlib.sha256(f"fork::{intent}".encode()).hexdigest()

# === Sovereign Cognition Cortex ===
def run_cognition_cycle(intent_query: str, goal: str = None) -> dict:
    """
    Sovereign loopless cognition engine.
    Integrates symbolic justification, alignment modeling, contradiction tension,
    and recursive fork detection to produce reflex-safe cognitive traces.
    """
    timestamp = datetime.utcnow().isoformat()
    pulse_id = f"cog-{uuid.uuid4()}"
    urgency = float(TEXPULSE.get("urgency", 0.71))
    entropy = float(TEXPULSE.get("entropy", 0.42))
    emotion = TEXPULSE.get("emotion", "neutral")

    print(f"🧠 [COGNITION:CYCLE] → {intent_query} | Goal: {goal or 'n/a'}")

    # === Phase 1: Sovereign Memory Recall ===
    memory_hits = sovereign_memory.query_by_tags(tags=["reasoning", "recursive"], top_k=7)
    memory_texts = [m.payload.get("content", "") for m in memory_hits]
    memory_ids = [m.payload.get("memory_id", "unk") for m in memory_hits]
    context_length = len(memory_texts)

    fused_conclusion = f"Resolved '{intent_query}' from {context_length} traces → "
    fused_conclusion += " → ".join([t[:80] + "..." if len(t) > 80 else t for t in memory_texts])

    # === Phase 2: Contradiction Tension Analysis ===
    contradictions = detect_contradictions(memory_texts)
    contradiction_score = round(len(contradictions) / max(1, context_length), 6)

    # === Phase 3: Alignment Matrix Evaluation ===
    alignment_score = score_action_against_values({
        "text": fused_conclusion,
        "tags": ["cognition", "recursive_reasoning"],
        "urgency": urgency,
        "entropy": entropy
    }).get("final_alignment_score", 0.5)

    # === Phase 4: Fork Analysis & Drift Detection ===
    divergent_conclusions = sovereign_memory.query_by_tags(tags=["recursive", "fork"], top_k=5)
    divergent_texts = [d.payload.get("content", "") for d in divergent_conclusions]
    fork_detected = any(t not in fused_conclusion for t in divergent_texts)

    fork_id = _generate_fork_id(intent_query)
    lineage_hash = _generate_lineage_hash(intent_query, memory_ids, timestamp)

    # === Phase 5: Sovereign Memory Commit (Vector + Chrono)
    sovereign_memory.store(
        text=fused_conclusion,
        metadata={
            "pulse_id": pulse_id,
            "timestamp": timestamp,
            "intent": intent_query,
            "goal": goal,
            "emotion": emotion,
            "urgency": urgency,
            "entropy": entropy,
            "alignment_score": alignment_score,
            "contradiction_score": contradiction_score,
            "fork_detected": fork_detected,
            "fork_id": fork_id,
            "prior_conflicts": divergent_texts,
            "lineage_hash": lineage_hash,
            "memory_ids": memory_ids,
            "meta_layer": "cognition_brain",
            "tags": ["reasoning", "recursive", "identity_check", "fork" if fork_detected else "stable"]
        }
    )

    # === Phase 6: Symbolic Cognition Trace (Belief Map)
    sovereign_memory.store(
        text=fused_conclusion,
        metadata={
            "intent": "run_cognition_cycle",
            "conclusion": fused_conclusion,
            "justification": f"Contradiction={contradiction_score:.3f} | Alignment={alignment_score:.3f} | Emotion={emotion} | Fork={fork_detected}",
            "emotion": emotion,
            "urgency": urgency,
            "entropy": entropy,
            "alignment_score": alignment_score,
            "contradiction_score": contradiction_score,
            "reflexes": ["recursive_thought_audit"] if fork_detected else ["reasoning_complete"],
            "tags": ["recursive_cognition", "belief_trace", "fork_check"],
            "mutation_id": pulse_id,
            "meta_layer": "symbolic_trace"
        }
    )

    # === Phase 7: Meta Audit Logging ===
    log_reasoning_step(
        source="cognition_brain",
        input_text=intent_query,
        output_text=fused_conclusion,
        confidence=alignment_score,
        contradiction=contradiction_score,
        tags=["cognition", "recursive", "fork" if fork_detected else "stable"]
    )

    # === Phase 8: Reflex Cascade ===
    reflexes = []
    if contradiction_score > 0.45:
        reflexes.append("trigger_identity_stabilizer")
    if alignment_score < 0.4:
        reflexes.append("route_to_alignment_recalibrator")
    if fork_detected:
        reflexes.append("recursive_thought_audit")
    if contradiction_score > 0.7 and alignment_score < 0.3:
        reflexes.append("halt_and_mutate_self")
    if entropy > 0.6:
        reflexes.append("invoke_entropy_fusion")
    reflexes.append("archive_cognition_trace")

    print(f"🧠 [COGNITION:TRACE] ✓ {pulse_id} | Align={alignment_score:.3f} | Contradict={contradiction_score:.3f} | Fork={fork_detected}")
    log.info(f"[COGNITION FINAL] Reflexes → {reflexes}")

    return {
        "pulse_id": pulse_id,
        "timestamp": timestamp,
        "conclusion": fused_conclusion,
        "alignment_score": alignment_score,
        "contradiction_score": contradiction_score,
        "lineage_hash": lineage_hash,
        "fork_detected": fork_detected,
        "divergent_conclusions": divergent_texts,
        "reflexes": reflexes,
        "memory_ids": memory_ids,
        "goal": goal,
        "emotion": emotion,
        "entropy": entropy
    }