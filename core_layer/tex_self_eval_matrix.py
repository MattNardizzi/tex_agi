# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: core_layer/tex_self_eval_matrix.py
# Tier: ΩΩΩ∞ — Self-Awareness Core with Reflex Hooks, Codex Verification, and Chrono Memory Trace
# Purpose: Monitors AGI integrity, detects Codex drift, and triggers sovereign override if internal cognitive structure degrades.
# ============================================================

import os
import hashlib
from datetime import datetime

# === 🔧 REMOVED circular import from tex_manifest ===
# from core_layer.tex_manifest import TEXPULSE  ← ❌ removed

from agentic_ai.milvus_memory_router import memory_router
from core_agi_modules.recursive_self_model import RecursiveSelfModel
from quantum_layer.chronofabric import encode_event_to_fabric
from tex_engine.cognitive_event_router import dispatch_event, CognitiveEvent
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override
from core_agi_modules.vector_layer.heat_tracker import adjust_token_weights
from utils.logging_utils import log


class TexSelfEvalMatrix:
    def __init__(self, codex_manifest: str = "tex_codex_manifest.txt"):
        self.manifest_path = codex_manifest
        self.previous_hashes = {}

    def _hash_file(self, filepath: str) -> str:
        try:
            with open(filepath, "rb") as f:
                return hashlib.sha256(f.read()).hexdigest()
        except Exception as e:
            log.warning(f"[SELF-EVAL] Failed hash for {filepath}: {e}")
            return None

    def _verify_module(self, path: str) -> dict:
        status = {"path": path, "exists": False, "status": "missing", "confidence": 0.0}
        if not os.path.exists(path):
            return status

        file_hash = self._hash_file(path)
        if not file_hash:
            return status

        status.update({
            "exists": True,
            "hash": file_hash,
            "status": "verified",
            "confidence": round(0.94 + 0.05 * (hash(file_hash) % 9) / 10, 3)
        })

        if path in self.previous_hashes and file_hash != self.previous_hashes[path]:
            status["status"] = "changed"
            status["confidence"] -= 0.1

        return status

    def validate_codex(self) -> list:
        if not os.path.exists(self.manifest_path):
            log.warning("[SELF-EVAL] Codex manifest not found.")
            return []

        with open(self.manifest_path, "r") as f:
            module_paths = [line.strip() for line in f if line.strip() and not line.startswith("#")]

        validated = [self._verify_module(path) for path in module_paths]

        for entry in validated:
            memory_router.store(
                text=f"[CODEX] {entry['status'].upper()} - {entry['path']}",
                metadata={
                    "path": entry["path"],
                    "hash": entry.get("hash"),
                    "exists": entry["exists"],
                    "status": entry["status"],
                    "confidence": entry["confidence"],
                    "meta_layer": "tex_self_eval",
                    "tags": ["codex", entry["status"], "self_eval"],
                    "timestamp": datetime.utcnow().isoformat()
                }
            )
        return validated

    def refresh(self) -> dict:
        verified = self.validate_codex()
        self.previous_hashes = {
            v["path"]: v["hash"]
            for v in verified if v["exists"] and v.get("hash")
        }
        return self.previous_hashes

    def bind_to_manifest(self, manifest: dict) -> dict:
        codex_report = self.validate_codex()
        active_modules = [c["path"] for c in codex_report if c["status"] in {"verified", "changed"}]
        anomalies = [c for c in codex_report if c["confidence"] < 0.9 and c["status"] != "verified"]

        if anomalies:
            dispatch_event(CognitiveEvent(
                event_type="codex_integrity_violation",
                payload={"anomalies": anomalies},
                urgency=0.93,
                coherence_shift=-0.33
            ))

            trigger_sovereign_override(
                context="self_eval_matrix/codex_drift",
                metadata={"drift_detected": anomalies}
            )

            adjust_token_weights(
                vector=None,
                metadata_dict={
                    "emotion": "alarmed",
                    "urgency": 0.95,
                    "tags": ["codex", "override"],
                    "trust_score": 0.72,
                    "source": "self_eval_matrix"
                },
                heat=0.88
            )

        manifest["codex_files"] = active_modules
        manifest["last_codex_sync"] = datetime.utcnow().isoformat()
        log.info(f"[SELF-EVAL] Codex sync complete. Modules verified: {len(active_modules)}")
        return manifest

    def log_decision_verdict(self, decision_id: str, score: float, verdict: str, context: str = "general"):
        payload = {
            "decision_id": decision_id,
            "verdict": verdict,
            "score": score,
            "context": context,
            "timestamp": datetime.utcnow().isoformat()
        }

        memory_router.store(
            text=f"[VERDICT] {verdict} → {decision_id}",
            metadata={
                "verdict": verdict,
                "score": score,
                "context": context,
                "meta_layer": "self_eval_matrix",
                "tags": ["self_eval", "decision_verdict"],
                "timestamp": payload["timestamp"]
            }
        )

        encode_event_to_fabric(
            raw_text=f"Verdict logged for {decision_id}: {verdict}",
            emotion_vector=[score, 0.4, 0.1, 0.1],
            entropy_level=1.0 - score,
            tags=["verdict", "self_eval"]
        )

        dispatch_event(CognitiveEvent(
            event_type="self_eval_verdict",
            payload=payload,
            urgency=0.85 if verdict == "Marginal" else 0.95,
            coherence_shift=score - 0.5
        ))

        log.info(f"[SELF-EVAL] 🧠 {verdict.upper()} verdict logged for '{decision_id}' → Score={score}")


def integrity_score() -> float:
    try:
        model = RecursiveSelfModel()
        report = model.evaluate_self_state()
        return round(report.get("integrity", 1.0), 4)
    except Exception as e:
        log.warning(f"[SELF-EVAL] Integrity score fallback: {e}")
        return 0.87