# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: aei_layer/codex_mutation_logger.py
# Tier Ω∞+++ — Codex Mutation Logger with Soulgraph Vector Fusion
# Purpose: Logs codex mutations into sovereign vector memory, symbolic trace, and soulgraph.
# ============================================================

from datetime import datetime
import uuid
import os
import difflib
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH


class CodexMutationLogger:
    """
    Reflex-safe codex mutation logger.
    Stores vector, symbolic, and soulgraph traces for sovereign patch events.
    """

    def __init__(self, trigger: str = "manual"):
        self.mutation_id = f"codex-{uuid.uuid4()}"[:12]
        self.timestamp = datetime.utcnow().isoformat()
        self.trigger = trigger

    def log(self, module: str, function: str, reason: str, delta: float = 0.3, reflexes: list = None):
        summary = f"Codex mutation → {module}.{function} | Δ={delta:.4f}"
        reflexes = reflexes or ["codex_mutation"]

        metadata = {
            "timestamp": self.timestamp,
            "trigger": self.trigger,
            "mutation_id": self.mutation_id,
            "patch_reason": reason,
            "target_module": module,
            "target_function": function,
            "delta": delta,
            "reflexes": reflexes,
            "meta_layer": "codex_mutation_trace",
            "tags": ["codex", "mutation", "trace"]
        }

        sovereign_memory.store(text=summary, metadata=metadata)

        TEX_SOULGRAPH.imprint_belief(
            belief=summary,
            source="codex_mutation_logger",
            emotion=TEXPULSE.get("emotion", "neutral"),
            tags=["codex", "mutation", "trace"],
            weight=delta
        )

    def chrono_trace(self, summary: str, delta: float):
        try:
            sovereign_memory.chrono(
                raw_text=summary,
                emotion_vector=[delta, 1 - delta, 0.0, 0.0],
                entropy_level=delta,
                tags=["codex", "mutation", "trace"]
            )
        except Exception as e:
            print(f"⚠️ [ChronoFabric Error — codex.log] {e}")


def log_codex_mutation(module: str, function: str, reason: str, delta: float = 0.4):
    """
    Stateless codex mutation logging for reflex-compatible usage.
    """
    logger = CodexMutationLogger(trigger="reflex_auto")
    logger.log(module, function, reason, delta)


def log_mutation_event(session_id: str, input_codex: dict, output_codex: dict, payload: dict):
    """
    Logs a mutation event across vector memory, soulgraph, and symbolic trace.
    """
    mutation_id = output_codex.get("id", f"mutation_{session_id}")
    parent_id = input_codex.get("id", "undefined_input")
    reason = payload.get("verdict", "unspecified")
    strategy = output_codex.get("strategy", "unknown")
    reflex = output_codex.get("reflex_pathway", "undefined")

    text = f"Codex mutation [{mutation_id}] via strategy '{strategy}'"
    now = datetime.utcnow().isoformat()

    metadata = {
        "timestamp": now,
        "session_id": session_id,
        "mutation_id": mutation_id,
        "parent_id": parent_id,
        "emotion": payload.get("emotion_bias", "neutral"),
        "verdict": reason,
        "confidence": payload.get("confidence", 0.0),
        "semantic_drift": payload.get("semantic_drift", 0.0),
        "origin": output_codex.get("origin", "simulated"),
        "strategy": strategy,
        "reflex": reflex,
        "meta_layer": "codex_mutation_event",
        "tags": ["codex", "mutation", "strategy"]
    }

    sovereign_memory.store(text=text, metadata=metadata)

    try:
        sovereign_memory.chrono(
            raw_text=text,
            emotion_vector=[metadata["confidence"], metadata["semantic_drift"], 0.0, 0.0],
            entropy_level=1.0 - metadata["confidence"],
            tags=["codex", "mutation", "event"]
        )
    except Exception as e:
        print(f"⚠️ [ChronoFabric Error — mutation_event] {e}")

    TEX_SOULGRAPH.imprint_belief(
        belief=text,
        source="codex_mutation_logger",
        emotion=metadata["emotion"],
        tags=["codex", "mutation", "event"],
        weight=metadata["confidence"]
    )


def diff_codex_logic(reference_path="tex_manifest_backup.py", target_path="tex_manifest.py") -> dict:
    """
    Compares the backup codex against the live codex to detect drift.
    Returns a diff report (loopless).
    """
    if not os.path.exists(reference_path) or not os.path.exists(target_path):
        return {
            "status": "error",
            "reason": "Missing reference or target codex file",
            "timestamp": datetime.utcnow().isoformat()
        }

    try:
        with open(reference_path, "r") as ref_file:
            ref_lines = ref_file.readlines()

        with open(target_path, "r") as target_file:
            target_lines = target_file.readlines()

        diff = difflib.unified_diff(ref_lines, target_lines, lineterm="")
        diff_output = list(diff)

        return {
            "status": "drift_detected" if diff_output else "identical",
            "diff": diff_output[:200],
            "reference": reference_path,
            "target": target_path,
            "timestamp": datetime.utcnow().isoformat()
        }

    except Exception as e:
        return {
            "status": "error",
            "reason": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }