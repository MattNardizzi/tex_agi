# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agentic_ai/log_trace_router.py
# Tier: ΩΩΩΩΩ — Loop-Safe Reasoning Trace Logger
# Purpose: Logs cognition traces into vector + identity memory without invoking reflex loops.
# ============================================================

from datetime import datetime
import numpy as np

from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from core_agi_modules.intent_object import IntentObject
from tex_engine.cognitive_event_router import dispatch_event, CognitiveEvent
from core_agi_modules.belief_justifier import BeliefJustifier
from tex_children.spawn_memory_query_tool import get_recent_fork_scores
from utils.logging_utils import log

justifier = BeliefJustifier()

def log_reasoning_step(
    source: str,
    input_text: str,
    output_text: str,
    confidence: float = 0.85,
    agent: str = "TexCore",
    tags: list = None
):
    """
    Logs a reasoning step into vector and identity memory without invoking reflexes or overrides.
    Safe for use in cognition orchestrators and meta-level diagnostics.
    """
    timestamp = datetime.utcnow().isoformat()
    tags = tags or []

    try:
        intent = IntentObject(input_text, source=source)
        intent.log_trace("reasoning_trace", "reasoning step executed")

        justification = justifier.suggest_patch(output_text)
        forks = get_recent_fork_scores(top_k=8)
        avg_fork_alignment = round(sum(forks) / len(forks), 3) if forks else 0.5

        # === Vector Memory (Milvus)
        text = output_text
        metadata = {
            "tags": ["reasoning", "trace"] + tags,
            "emotion": "analytical",
            "timestamp": timestamp,
            "source": source,
            "agent": agent,
            "intent_id": intent.id,
            "prediction": input_text,
            "actual": output_text,
            "justification": justification or "none",
            "fork_alignment": avg_fork_alignment,
            "trust_score": confidence,
            "meta_layer": "reasoning_trace",
        }
        memory_router.store(text, metadata)

        # === Identity Memory (ChronoFabric)
        encode_event_to_fabric(
            text,
            np.array([0.3, 0.6, 0.1, 0.1]),
            entropy_level=0.4,
            tags=metadata["tags"]
        )

        # === Cognitive Event Dispatch
        dispatch_event(CognitiveEvent("REASONING_LOGGED", {
            "agent": agent,
            "source": source,
            "confidence": confidence,
            "output": output_text,
            "tags": tags,
            "timestamp": timestamp
        }))

        log.info(f"[TRACE] Reasoning step stored → {output_text[:64]}")

    except Exception as e:
        log.error(f"[log_trace_router] ❌ Error during trace logging: {e}")