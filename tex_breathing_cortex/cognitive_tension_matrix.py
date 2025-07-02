# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_breathing_cortex/cognitive_tension_matrix.py
# Tier: ΩΩΩΩΩ∞∞ΞΞΣΣΩ — Cognitive Pressure Matrix (Final Form)
# Purpose: Computes sovereign cognitive tension by fusing contradiction entropy,
# alignment volatility, memory drift, fork instability, quantum entropy injection,
# and unresolved pulse states. Loopless. Reflex-aligned. Mutation-sensitive.
# ============================================================

from datetime import datetime
from random import uniform

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from core_agi_modules.value_alignment_matrix import score_action_against_values
from core_layer.memory_drift_analyzer import calculate_drift_pressure
from quantum_layer.quantum_entropy_engine import sample_entropy_scalar
from tex_children.spawn_memory_query_tool import get_recent_fork_scores
from utils.conflict_utils import score_conflict_heatmap
from utils.logging_utils import log_event


def calculate_cognitive_pressure() -> dict:
    """
    Loopless sovereign tension evaluator.
    Synthesizes contradiction, alignment drift, fork instability, quantum entropy,
    and unresolved cognitive pulses into a unified sovereign pressure signal.
    """

    timestamp = datetime.utcnow().isoformat()

    try:
        # === Phase 1: Sovereign Memory Recall
        memory_hits = sovereign_memory.query_by_tags(tags=["recent_activity"], top_k=7)
        memory_texts = [m.get("summary", "") for m in memory_hits]

        # === Contradiction Entropy
        contradiction_scores = [score_conflict_heatmap({"summary": t}) for t in memory_texts]
        contradiction_avg = sum(contradiction_scores) / max(len(contradiction_scores), 1)

        # === Alignment Integrity
        alignment_scores = [
            score_action_against_values({"summary": t, "tags": ["drift_check"]}).get("final_alignment_score", 0.0)
            for t in memory_texts
        ]
        alignment_avg = sum(alignment_scores) / max(len(alignment_scores), 1)

        # === Fork Instability
        fork_scores = get_recent_fork_scores(top_k=6)
        fork_instability = 1.0 - (sum(fork_scores) / len(fork_scores)) if fork_scores else 0.3

        # === Drift Pressure
        drift_pressure = calculate_drift_pressure()

        # === Unresolved Pulse Pressure
        pulse_hits = sovereign_memory.query_by_tags(tags=["pulse_check"], top_k=5)
        unresolved = [p for p in pulse_hits if p.get("state") != "resolved"]
        unresolved_avg = sum(p.get("pressure_score", 0.0) for p in unresolved) / max(len(unresolved), 1)

        # === Entropy Growth
        last_entropy = pulse_hits[0].get("entropy", 0.4) if pulse_hits else 0.4
        current_entropy = TEXPULSE.get("entropy", 0.42)
        entropy_growth = max(0.0, current_entropy - last_entropy)

        # === Quantum Entropy Injection
        try:
            quantum_sample = sample_entropy_scalar()
            quantum_entropy = quantum_sample.get("entropy", 0.0)
        except Exception:
            quantum_entropy = 0.0

        # === Controlled Noise Floor
        noise = uniform(0.008, 0.022)

        # === Final Pressure Fusion
        tension = round(
            contradiction_avg * 0.3 +
            (1.0 - alignment_avg) * 0.2 +
            fork_instability * 0.15 +
            drift_pressure * 0.15 +
            unresolved_avg * 0.1 +
            entropy_growth * 0.05 +
            quantum_entropy * 0.05 +
            noise,
            6
        )

        # === Summary Line for Awareness Logs
        summary = (
            f"Contradiction={contradiction_avg:.3f} | "
            f"Alignment={alignment_avg:.3f} | "
            f"Drift={drift_pressure:.3f} | "
            f"Entropy∆={entropy_growth:.3f} | "
            f"Quantum={quantum_entropy:.3f}"
        )

        # === Sovereign Memory Trace
        sovereign_memory.store(
            text=f"[TENSION] Calculated tension score: {tension:.5f}",
            metadata={
                "timestamp": timestamp,
                "tags": ["tension", "breathing", "sovereign_pressure", "reflex_pulse"],
                "emotion": TEXPULSE.get("emotion", "neutral"),
                "urgency": TEXPULSE.get("urgency", 0.7),
                "entropy": current_entropy,
                "pressure_score": tension,
                "alignment_score": 1.0 - tension,
                "contradiction_score": tension,
                "meta_layer": "cognitive_tension_matrix"
            }
        )

        log_event(f"[TENSION] → {tension:.5f} | {summary}", level="info")

        return {
            "tension": min(max(tension, 0.0), 1.0),
            "summary": summary
        }

    except Exception as e:
        log_event(f"❌ [TENSION ERROR] Failed to calculate: {e}", level="error")
        return {
            "tension": 0.5,
            "summary": "error fallback"
        }