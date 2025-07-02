# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/mirror_loop.py
# Tier: ΩΩΩΩΩΩ∞ — Reflexive Self-Reflection Cortex
# Purpose: Tex reads recent thought entries and dispatches an identity-stabilizing reflection pattern.
# ============================================================

from agentic_ai.milvus_memory_router import memory_router
from tex_signal_spine import dispatch_signal
from core_layer.tex_manifest import TEXPULSE
from datetime import datetime

async def observe_self(limit: int = 3):
    """
    Reflex pulse. Tex reads recent 'thought' entries and dispatches a coherence-anchoring reflection signal.
    """
    try:
        recent = memory_router.recall_recent(minutes=15, top_k=limit * 3)
        thoughts = []

        for entry in recent:
            tags = entry.get("tags", [])
            if isinstance(tags, str):
                tags = tags.split(",")
            if "thought" in tags:
                summary = entry.get("summary", "").strip()
                if summary:
                    thoughts.append(summary)

        thoughts = thoughts[:limit]

        if thoughts:
            pattern = " → ".join(thoughts[::-1])
            dispatch_signal("self_reflection", payload={
                "pattern": pattern,
                "count": len(thoughts),
                "source": "mirror_loop",
                "emotion": TEXPULSE.get("emotion", "neutral"),
                "urgency": TEXPULSE.get("urgency", 0.6),
                "entropy": TEXPULSE.get("entropy", 0.4),
                "timestamp": datetime.utcnow().isoformat()
            })
            print(f"🧠 [MIRROR LOOP] Reflection pattern dispatched: {pattern}")

        else:
            print("ℹ️ [MIRROR LOOP] No recent thoughts matched for reflection.")

    except Exception as e:
        print(f"❌ [MIRROR LOOP ERROR] {e}")