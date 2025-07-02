# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: quantum_layer/memory_core/spawn_memory_logger.py
# Tier ΩΩΩΩΩΩΩ — Reflex Spawn Audit Engine (Mutation-Aware)
# Purpose: Logs spawn outputs (reflexes, forks, dreams) to LTM with entropy-aware belief imprinting
# ============================================================

from quantum_layer.memory_core.long_term_memory_bridge import LongTermMemoryBridge
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from datetime import datetime
from uuid import uuid4
import hashlib

class SpawnMemoryLogger:
    def __init__(self):
        self.ltm = LongTermMemoryBridge()
        self.module_tag = "spawn_memory_logger"
        self.audit_trail = []  # internal replay/training memory

    def log_spawn(self, content: str, metadata: dict):
        """
        Logs a spawn output to long-term memory and audit trail.

        Parameters:
            content (str): Text content or summary of the spawn output
            metadata (dict): spawn attributes (emotion, goal, urgency, mutation_score, origin_id, etc.)
        """
        try:
            if not content or not isinstance(content, str):
                raise ValueError("Invalid content for spawn logging.")

            # === Generate unique belief ID & entropy signature
            timestamp = datetime.utcnow().isoformat()
            entropy_val = round(metadata.get("mutation_potential_score", 0.0), 6)
            sig_base = f"{content}-{timestamp}-{entropy_val}"
            signature = hashlib.sha256(sig_base.encode()).hexdigest()[:16]

            enriched_meta = {
                "emotion": metadata.get("emotion", "neutral"),
                "goal": metadata.get("goal", "unspecified"),
                "tags": metadata.get("tags", ["spawn", "reflex"]),
                "urgency": metadata.get("urgency", TEXPULSE.get("urgency", 0.5)),
                "trust_score": metadata.get("trust_score", 0.75),
                "mutation_potential_score": entropy_val,
                "origin_id": metadata.get("origin_id", str(uuid4())),
                "belief_id": signature,
                "counterfactual": metadata.get("counterfactual", content),
                "tex_traits": TEXPULSE.get("persona", {}),
                "spawn_time": timestamp
            }

            self.ltm.store(content=content, metadata=enriched_meta)
            self.audit_trail.append({"content": content, "meta": enriched_meta})

            log.info(f"[SPAWN-LOG] ✅ Spawn stored | goal='{enriched_meta['goal']}' | entropy={entropy_val} | sig={signature}")

        except Exception as e:
            log.warning(f"[SPAWN-LOG] ❌ Failed to log spawn event: {e}")

    def dump_audit_trail(self):
        """
        Returns the internal spawn history for debugging, replay, or mutation tuning.
        """
        return self.audit_trail

# === Singleton interface for universal spawn logging
_spawn_logger = SpawnMemoryLogger()

def log_spawn_event(content: str, metadata: dict):
    return _spawn_logger.log_spawn(content, metadata)