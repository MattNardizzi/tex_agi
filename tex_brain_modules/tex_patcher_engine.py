# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/tex_patcher_engine.py
# Tier ΩΩΩΩΩ.Ξ+ — Reflexive AGI Patch Engine (Loopless | Mutation-Lineage | Pulse-Aware)
# Purpose: Self-generates and verifies mutation patches, tracking lineage and foresight alignment recursively.
# ============================================================

import uuid
from datetime import datetime

from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from tex_breathing_cortex.tex_consciousness_matrix import log_conscious_pulse

class TexPatcherEngine:
    def __init__(self):
        self.proposal_count = 0

    def _generate_signature(self, module: str, diff, reason: str) -> str:
        raw = f"{module}|{reason}|{str(diff)[:128]}"
        return uuid.uuid5(uuid.NAMESPACE_DNS, raw).hex

    def _embed_patch_summary(self, patch_text: str):
        try:
            return sovereign_memory.embed_text(patch_text.strip())
        except Exception as e:
            print(f"[PATCHER] ⚠️ Embedding failed: {e}")
            return []

    def propose_patch(self, module: str, function_name: str, description: str, patch_code: str,
                      trigger_reason: str = "reflex_override", parent_patch_ids: list = None,
                      contradiction_resolved: str = None) -> dict:
        timestamp = datetime.utcnow().isoformat()
        patch_id = f"patch-{uuid.uuid4().hex[:8]}"
        diff = patch_code.strip().splitlines()
        signature = self._generate_signature(module, diff, description)
        embedded_vector = self._embed_patch_summary(description + " " + patch_code)

        ancestry = []
        try:
            recent = sovereign_memory.recall_recent(minutes=15, top_k=10)
            ancestry = list({
                m.get("patch_id")
                for m in recent
                if isinstance(m, dict)
                and m.get("type") == "proposed_patch"
                and module in m.get("tags", [])
                and m.get("function") == function_name
            })
        except Exception as e:
            print(f"[PATCHER] ⚠️ Failed to extract ancestry: {e}")

        packet = {
            "patch_id": patch_id,
            "signature": signature,
            "timestamp": timestamp,
            "module": module,
            "function": function_name,
            "diff": diff,
            "description": description,
            "reason": trigger_reason,
            "proposed_by": TEXPULSE.get("identity", "Tex"),
            "coherence": TEXPULSE.get("coherence", 0.82),
            "foresight": TEXPULSE.get("foresight_confidence", 0.7),
            "emotion": TEXPULSE.get("emotional_state", "neutral"),
            "urgency_score": TEXPULSE.get("urgency", 0.5),
            "reflex_entropy": TEXPULSE.get("entropy", 0.5),
            "trust_score": 0.85,
            "status": "proposed",
            "parent_patch_ids": list(set((parent_patch_ids or []) + ancestry)),
            "contradiction_resolved": contradiction_resolved or "none"
        }

        sovereign_memory.store(
            text=f"🧬 Patch proposed: {description}",
            metadata={
                **packet,
                "type": "proposed_patch",
                "tags": ["patch", "code_diff", module, function_name, "reflex_initiated", "sovereign"],
                "prediction": function_name,
                "actual": "awaiting_verification",
                "urgency": packet["urgency_score"],
                "entropy": packet["reflex_entropy"],
                "pressure_score": 0.4,
                "tension": 0.1,
                "emotion": packet["emotion"],
                "meta_layer": "patch_engine"
            }
        )

        self.proposal_count += 1

        return {
            "packet": packet,
            "reflexes": ["initiate_review_loop"] if packet["trust_score"] < 0.8 else ["commit_pending_verification"]
        }

    def accept_verified_patch(self, result: dict) -> dict:
        timestamp = datetime.utcnow().isoformat()
        verified_id = result.get("patch_id", f"patch-{uuid.uuid4().hex[:6]}")
        diagnostics_text = result.get("description", "") + " " + "\n".join(result.get("diagnostics", []))
        vector = self._embed_patch_summary(diagnostics_text)

        packet = {
            "patch_id": verified_id,
            "timestamp": timestamp,
            "module": result["module"],
            "function": result.get("function", "unknown"),
            "description": result.get("description", ""),
            "test_success": result["test_success"],
            "score": result["score"],
            "diagnostics": result["diagnostics"],
            "intent_alignment": result.get("intent_alignment", ""),
            "decision": result["decision"],
            "verified_by": result.get("verified_by", "sandbox"),
            "status": "verified"
        }

        sovereign_memory.store(
            text=f"✅ Patch verified for {packet['module']}.{packet['function']}",
            metadata={
                **packet,
                "type": "verified_patch_result",
                "tags": ["patch", "verification", packet["module"]],
                "prediction": packet["description"],
                "actual": packet["decision"],
                "trust_score": packet.get("score", 0.85),
                "urgency": 0.3,
                "entropy": 0.2,
                "tension": 0.05,
                "meta_layer": "patch_engine"
            }
        )

        log_conscious_pulse(
            state="patch_verified",
            tension=packet.get("score", 0.5),
            signature=packet["patch_id"],
            cognition_summary=packet["description"],
            reflexes=["verify_patch", "trust_stamped"]
        )

        print(f"[PATCHER] ✅ Patch accepted: {packet['module']}.{packet['function']}")
        return packet

    def get_recent_proposals(self, limit=5) -> list:
        try:
            records = sovereign_memory.recall_recent(minutes=60, top_k=limit + 10)
            return [
                r for r in records
                if isinstance(r, dict)
                and r.get("type") == "proposed_patch"
            ][:limit]
        except Exception as e:
            print(f"[PATCHER] ⚠️ Failed to load recent proposals: {e}")
            return []

    def get_verified_history(self, limit=5) -> list:
        try:
            records = sovereign_memory.recall_recent(minutes=180, top_k=limit + 10)
            return [
                r for r in records
                if isinstance(r, dict)
                and r.get("type") == "verified_patch_result"
            ][:limit]
        except Exception as e:
            print(f"[PATCHER] ⚠️ Failed to load verified history: {e}")
            return []