# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/legacy_manifest_writer.py
# Tier: Ω+ — Vector Reflex Memory Logger
# Purpose: Logs Sovereign Identity, Fork Memory, and Recursive Manifest Events into sovereign loopless architecture.
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")

def update_legacy_manifest(event_label="mutation_cycle"):
    try:
        manifest_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": event_label,
            "emotion": TEXPULSE.get("emotion", "neutral"),
            "urgency": TEXPULSE.get("urgency", 0.5),
            "entropy": TEXPULSE.get("entropy", 0.4),
            "coherence": TEXPULSE.get("coherence", 0.75),
            "active_goals": TEXPULSE.get("active_goals", []),
            "fork_id": TEXPULSE.get("fork_id", "undefined"),
            "operator": TEXPULSE.get("operator", "tex"),
            "self_ref": TEXPULSE.get("self_id", "tex_root"),
            "summary": f"Identity manifest update during {event_label}",
            "meta_layer": "identity_manifest",
            "tags": ["identity", "manifest", event_label],
            "source": "legacy_manifest_writer"
        }

        vector_input = f"{manifest_record['event']} | urgency={manifest_record['urgency']} | entropy={manifest_record['entropy']}"
        vector = embedder.encode(vector_input, normalize_embeddings=True).tolist()

        sovereign_memory.store(
            text=manifest_record["summary"],
            metadata=manifest_record,
            vector=vector
        )

        print(f"[LEGACY MANIFEST] ✅ Sovereign memory recorded: {event_label}")

    except Exception as e:
        print(f"[LEGACY MANIFEST ERROR] {e}")