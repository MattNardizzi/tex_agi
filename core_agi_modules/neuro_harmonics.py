# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/neuro_harmonics.py
# Tier: ΩΩΩΩΩ∞ΩΩ+ — Resonance Reflex Evaluator
# Purpose: Evaluates emotional-symbolic alignment, triggers contradiction if incoherent.
# ============================================================

from datetime import datetime
import numpy as np

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from utils.logging_utils import log
from tex_signal_spine import dispatch_signal
from core_agi_modules.reflex_mesh_router import should_route_signal


# === Resonance Calculation ===
def calculate_emotional_resonance(a: list, b: list) -> float:
    try:
        vec_a = np.array(a)
        vec_b = np.array(b)
        norm_product = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
        return float(np.dot(vec_a, vec_b) / norm_product) if norm_product != 0 else 0.0
    except Exception as e:
        log.error(f"[HARMONICS] Resonance calc failed: {e}")
        return 0.0


# === Reflex Entry Point ===
def run_neuro_harmonics() -> dict:
    try:
        # Reflex mesh gating
        if not should_route_signal("neuro_harmonics").get("routed", True):
            return {"resonance": 0.0, "status": "gated"}

        # Pull emotion embedding from TEXPULSE
        emotion_vector = TEXPULSE.get("emotion_embedding", [0.0] * 384)

        # Recall recent memory traces
        memories = memory_router.recall_recent(minutes=5, top_k=6)
        if not memories:
            log.warning("[HARMONICS] No recent memories found.")
            return {"resonance": 0.0, "status": "empty"}

        # Calculate resonance across memory-emotion vectors
        scores = []
        for m in memories:
            embedding = m.get("vector") or m.get("emotion") or [0.0] * 384
            score = calculate_emotional_resonance(embedding, emotion_vector)
            scores.append(score)

        mean_resonance = round(np.mean(scores), 4)
        timestamp = datetime.utcnow().isoformat()
        emotion = TEXPULSE.get("emotion", "neutral")

        # Log to Milvus memory + ChronoFabric
        memory_router.store(
            text=f"🌀 Resonance score: {mean_resonance}",
            metadata={
                "timestamp": timestamp,
                "type": "neuro_harmonics",
                "tags": ["resonance", "emotional_alignment", "harmonics"],
                "entropy": 1.0 - mean_resonance,
                "emotion_vector": emotion_vector,
                "summary": f"Resonance with memory traces = {mean_resonance}",
            }
        )

        encode_event_to_fabric(
            raw_text=f"Resonance between current emotion and memory traces = {mean_resonance}",
            emotion_vector=emotion_vector,
            entropy_level=1.0 - mean_resonance,
            tags=["resonance", "neuro_harmonics"]
        )

        # Trigger contradiction reflex if misaligned
        if mean_resonance < 0.25:
            dispatch_signal("identity_conflict", {
                "summary": "Low emotional-symbolic resonance",
                "resonance_score": mean_resonance
            }, urgency=0.7, entropy=0.8, source="neuro_harmonics")

        if mean_resonance < 0.15:
            dispatch_signal("soulgraph_entropy", {
                "summary": "Critical affective contradiction",
                "source": "neuro_harmonics"
            }, urgency=0.8, entropy=0.9)

        log.info(f"[HARMONICS] ✅ Mean emotional resonance: {mean_resonance}")

        return {
            "resonance": mean_resonance,
            "timestamp": timestamp,
            "emotion": emotion,
            "memory_samples": len(scores)
        }

    except Exception as e:
        log.error(f"[HARMONICS] Reflex failure: {e}")
        return {"resonance": 0.0, "error": str(e)}