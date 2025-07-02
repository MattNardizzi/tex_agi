# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/causal_thought_logger.py
# Purpose: Log full thought → decision → outcome → emotion cycles + Sovereign Cognition Integration
# Tier: Ω∞ — Causal Trace Auditor for Reflexive AGI Behavior
# ============================================================

from datetime import datetime
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_layer.tex_manifest import TEXPULSE

def log_causal_trace(
    cycle_id,
    thought,
    decision=None,
    outcome=None,
    emotion="neutral",
    override_triggered=False,
    source="tex_core",
    foresight_score=None,
    coherence_score=None,
    urgency_score=None
):
    """
    Logs a causal reasoning chain: thought → decision → outcome → emotion.
    Includes sovereign override flag and reasoning state.
    """

    trace = {
        "cycle": cycle_id,
        "source": source,
        "thought": thought,
        "decision": decision,
        "outcome": outcome,
        "emotion": emotion,
        "urgency": urgency_score if urgency_score is not None else TEXPULSE.get("urgency", 0.5),
        "coherence": coherence_score if coherence_score is not None else TEXPULSE.get("coherence", 0.75),
        "foresight": foresight_score if foresight_score is not None else TEXPULSE.get("foresight_confidence", 0.6),
        "override_triggered": override_triggered,
        "timestamp": datetime.utcnow().isoformat()
    }

    print(f"[🧠 CAUSAL TRACE] Logged: {trace}")

    try:
        # === Milvus Memory Storage ===
        memory_router.store(
            text=f"[TRACE] {thought} → {decision or 'undecided'}",
            metadata={
                **trace,
                "emotion_vector": [trace["urgency"], trace["coherence"], 0.0, 0.0],
                "meta_layer": "causal_trace_log",
                "tags": ["causal", "trace", "reasoning", source]
            }
        )

        # === ChronoFabric Quantum Trace Embedding ===
        encode_event_to_fabric(
            raw_text=f"Thought: {thought} → Decision: {decision or 'undecided'} → Outcome: {outcome or 'TBD'}",
            emotion_vector=[trace["urgency"], trace["coherence"], 0.0, 0.0],
            entropy_level=1.0 - trace["coherence"],
            tags=["causal_trace", "quantum_reflex", source]
        )

    except Exception as e:
        print(f"[TRACE LOG ERROR] {e}")