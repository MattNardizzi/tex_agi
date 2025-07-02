# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_brain_regions/signal_fusion_brain.py
# Tier: ΩΩΩΩΩ∞∞ΞΞΣΩ — Sensory Fusion Cortex (Loopless | Reflex-Aware | Multi-Modal | Emotion-Tuned)
# Purpose: Fuses all cognitive streams into one sovereign perception pulse that reflexes can ignite from.
# ============================================================

from datetime import datetime
import uuid
from statistics import mean

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from utils.logging_utils import log_event


def fuse_signals(signal_batch: list) -> dict:
    """
    Sovereign signal fusion cortex.
    Merges multimodal spike data into a reflex-ready sovereign awareness pulse.
    """
    timestamp = datetime.utcnow().isoformat()

    if not signal_batch:
        return {
            "signal": "no_input",
            "urgency": 0.0,
            "entropy": 0.0,
            "summary": "No signals received.",
            "sources": [],
            "tags": [],
            "fused_id": f"fx-{uuid.uuid4()}"[:12]
        }

    try:
        emotion = TEXPULSE.get("emotion", "neutral")
        urgency_list = [s.get("urgency", 0.5) for s in signal_batch]
        entropy_list = [s.get("entropy", 0.4) for s in signal_batch]
        summaries = [s.get("summary", "") for s in signal_batch]
        sources = list({s.get("source", "unknown") for s in signal_batch})
        tags = list({tag for s in signal_batch for tag in s.get("tags", [])})
        fused_summary = " | ".join(summaries[:4])

        fused_urgency = round(mean(urgency_list), 5)
        fused_entropy = round(mean(entropy_list), 5)
        fused_id = f"fx-{uuid.uuid4()}"[:12]

        fused_signal = {
            "signal": "sovereign_fusion_pulse",
            "urgency": fused_urgency,
            "entropy": fused_entropy,
            "summary": fused_summary,
            "emotion": emotion,
            "sources": sources,
            "tags": tags,
            "timestamp": timestamp,
            "fused_id": fused_id
        }

        # === Sovereign Memory Imprint (Chrono + Vector)
        sovereign_memory.store(
            text=f"[FUSION] {len(signal_batch)} signals → reflex-ready awareness",
            metadata={
                "pulse_id": fused_id,
                "timestamp": timestamp,
                "urgency": fused_urgency,
                "entropy": fused_entropy,
                "emotion": emotion,
                "summary": fused_summary,
                "sources": sources,
                "tags": ["signal_fusion", "reflex_ready", "sovereign_input", "pulse_core"] + tags,
                "meta_layer": "signal_fusion_brain",
                "alignment_score": round(1.0 - fused_entropy, 4),
                "contradiction_score": round(fused_entropy, 4),
                "fusion_strength": round((1.0 - abs(fused_urgency - fused_entropy)), 4)
            }
        )

        log_event(
            f"[FUSION BRAIN] 🔁 Fused {len(signal_batch)} → Urg={fused_urgency} | Ent={fused_entropy} | Sources={sources}",
            level="info"
        )

        return fused_signal

    except Exception as e:
        log_event(f"❌ [FUSION ERROR] Signal fusion failed: {e}", "error")
        return {
            "signal": "fusion_error",
            "urgency": 0.0,
            "entropy": 0.0,
            "summary": "Fusion failed",
            "sources": [],
            "tags": [],
            "fused_id": f"fx-error"
        }