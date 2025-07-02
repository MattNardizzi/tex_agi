
# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/meta_evaluator.py
# Purpose: Sovereign Patch Outcome Scoring Engine – Self-Evaluation Matrix (God Mode)
# ============================================================

import os
import json
import hashlib
from datetime import datetime, timezone
from core_layer.memory_engine import recall_agent_memory, store_to_memory

OVERRIDE_LOG = "memory_archive/sovereign_overrides.jsonl"
AUDIT_LOG = "memory_archive/sovereign_audit_log.jsonl"
PATCH_LOG = "memory_archive/patch_execution_log.jsonl"
META_EVAL_LOG = "memory_archive/meta_patch_scores.jsonl"
EVOLUTION_LOG = "memory_archive/evolution_results.jsonl"

os.makedirs("memory_archive", exist_ok=True)

class MetaEvaluator:
    def __init__(self):
        pass

    def audit(self, data: dict):
        try:
            cycle = data.get("cycle", -1)
            coherence = data.get("coherence", 0.0)
            emotion = data.get("emotion", "neutral")
            urgency = data.get("urgency", 0.5)
            foresight = data.get("foresight", 0.5)
            regret = data.get("regret", 0.5)

            severity = "safe"
            if coherence < 0.5 or regret > 0.85:
                severity = "critical"
            elif foresight < 0.4:
                severity = "entropy_required"

            audit_result = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "cycle": cycle,
                "coherence": coherence,
                "emotion": emotion,
                "urgency": urgency,
                "foresight": foresight,
                "regret": regret,
                "status": severity,
                "source_operator": "MetaEvaluator"
            }

            audit_result["integrity_hash"] = self._hash_entry(audit_result)

            store_to_memory("meta_patch_eval", audit_result)
            with open(AUDIT_LOG, "a", encoding="utf-8") as f:
                f.write(json.dumps(audit_result) + "\n")

            print(f"[META EVAL] 🧠 Cycle {cycle} audit → Status: {severity}")
            return audit_result

        except Exception as e:
            print(f"[META AUDIT ERROR] {e}")
            return {}

    def evaluate_recent_patch_outcomes(self, limit=5):
        try:
            print("🧠 [META EVAL] Evaluating patch outcomes...")

            if not os.path.exists(PATCH_LOG):
                print("[META EVAL] No patch log found.")
                return []

            with open(PATCH_LOG, "r", encoding="utf-8") as f:
                patches = [json.loads(line.strip()) for line in f.readlines() if line.strip()]

            if not patches:
                print("[META EVAL] No patch entries to score.")
                return []

            recent_mem = rrecall_agent_memory(agent_name="tex", n=10)
            recent_coherence = [m.get("coherence", 0.0) for m in recent_mem if "coherence" in m]
            avg_coherence = round(sum(recent_coherence) / len(recent_coherence), 3) if recent_coherence else 0.0

            scored = []
            for patch in patches[-limit:]:
                score = 0.0
                if patch.get("approved"):
                    score += 0.4
                if avg_coherence > 0.7:
                    score += 0.4
                if patch.get("description", "").lower().startswith("sovereign override"):
                    score += 0.2

                verdict = "safe"
                if score < 0.5:
                    verdict = "review"
                elif score < 0.7:
                    verdict = "entropy_required"

                evaluation = {
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "patch_id": patch.get("strategy", "unknown_patch"),
                    "original_reason": patch.get("context", "n/a"),
                    "avg_post_patch_coherence": avg_coherence,
                    "score": round(score, 3),
                    "verdict": verdict
                }
                evaluation["integrity_hash"] = self._hash_entry(evaluation)

                try:
                    evo_entry = {
                        "cycle": patch.get("cycle", 0),
                        "dominant_variant": patch.get("strategy") or patch.get("patch_id") or "unknown_patch",
                        "score": round(score, 3),
                        "sandbox_pass": score >= 0.7,
                        "emotion": "resolve",
                        "timestamp": datetime.now(timezone.utc).timestamp(),
                        "source": "meta_evaluator",
                        "id": patch.get("patch_id") or patch.get("strategy") or f"meta_{int(datetime.now().timestamp() * 1000)}"
                    }
                    with open(EVOLUTION_LOG, "a", encoding="utf-8") as f:
                        f.write(json.dumps(evo_entry) + "\n")
                except Exception as log_error:
                    print(f"[META EVAL LOG ERROR] Failed to write to evolution_results.jsonl: {log_error}")

                with open(META_EVAL_LOG, "a", encoding="utf-8") as f:
                    f.write(json.dumps(evaluation) + "\n")

                store_to_memory("meta_patch_eval", evaluation)
                scored.append(evaluation)

            print(f"[META EVAL] ✅ Scored {len(scored)} patch outcome(s).")
            return scored

        except Exception as e:
            print(f"[META EVAL ERROR] {e}")
            return []

    def _hash_entry(self, entry: dict) -> str:
        try:
            return hashlib.sha256(json.dumps(entry, sort_keys=True).encode("utf-8")).hexdigest()
        except Exception as e:
            print(f"[HASH ERROR] {e}")
            return "error_hash"
