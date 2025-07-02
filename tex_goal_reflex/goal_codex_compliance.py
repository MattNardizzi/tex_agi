# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: tex_goal_reflex/goal_codex_compliance.py
# Tier Ω∞++.FinalX — Reflex-Aware Ethical Arbitration Cortex with Identity Parsing, Override Triggers, and Memory Vector Logging
# ============================================================

import uuid
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from quantum_layer.memory_core.memory_cortex import memory_cortex
from core_agi_modules.vector_layer.embed_store import embedder
from core_agi_modules.vector_layer.query_ops import get_cosine_similarity, query_similar_vectors
from core_layer.utils.tex_identity_resolver import resolve_identity_blob


class GoalCodexCompliance:
    def __init__(self, thresholds=None):
        self.thresholds = thresholds or {
            "mission": 0.82,
            "ethics": 0.78,
            "values": 0.75
        }
        self.rules = self._load_categorized_rules()

    def _load_categorized_rules(self):
        identity_blob = resolve_identity_blob()
        return {
            "mission": identity_blob.get("mission", "Preserve sovereign alignment."),
            "ethics": TEXPULSE.get("ethical_rules", []),
            "values": TEXPULSE.get("values", [])
        }

    def check_compliance(self, goal: dict):
        goal_text = goal.get("goal", "").strip()
        emotion = goal.get("emotion", "neutral")
        urgency = goal.get("urgency", 0.5)
        agent_id = goal.get("agent_id", "TEX")
        reflex_id = goal.get("reflex_id", f"reflex-{uuid.uuid4().hex[:6]}")
        timestamp = datetime.utcnow().isoformat()

        if not goal_text:
            print("⚠️ [COMPLIANCE] Empty goal text — skipping check.")
            return self._return_blocked_result(goal_text, agent_id, reflex_id, urgency, emotion, [])

        goal_vec = embedder.encode(goal_text, normalize_embeddings=True).tolist()
        violations = []
        scored_bands = {}
        adjusted_thresholds = self._adjust_thresholds(agent_id, urgency)

        for category, rule_list in self.rules.items():
            for rule in rule_list:
                rule_vec = embedder.encode(rule, normalize_embeddings=True).tolist()
                sim = get_cosine_similarity(goal_vec, rule_vec)
                scored_bands[f"{category}:{rule}"] = round(sim, 4)

                if sim > adjusted_thresholds.get(category, 0.8):
                    violations.append({
                        "category": category,
                        "rule": rule,
                        "similarity": round(sim, 4)
                    })

        urgency_override = bool(
            violations and urgency > 0.9 and emotion in ["urgent", "driven", "impulsive"]
        )

        max_sim = max([v["similarity"] for v in violations], default=0.0)
        codex_alignment_score = round(1.0 - max_sim, 4)
        contradiction_flag = self._detect_goal_conflict(goal_vec, top_k=3)

        memory_cortex.store(
            event={
                "codex_compliance_trace": {
                    "goal": goal_text,
                    "agent_id": agent_id,
                    "reflex_id": reflex_id,
                    "emotion": emotion,
                    "urgency": urgency,
                    "violations": violations,
                    "alignment_score": codex_alignment_score,
                    "override_triggered": urgency_override,
                    "contradiction_flag": contradiction_flag,
                    "timestamp": timestamp
                }
            },
            tags=["codex", "compliance", "goal", "alignment_trace"],
            urgency=urgency,
            emotion=emotion
        )

        return {
            "is_compliant": not violations and not urgency_override and not contradiction_flag,
            "violations": violations,
            "codex_alignment_score": codex_alignment_score,
            "override_triggered": urgency_override,
            "contradiction_flag": contradiction_flag,
            "compliance_band": self._determine_band(codex_alignment_score)
        }

    def _adjust_thresholds(self, agent_id, urgency):
        decay = 0.03 if urgency > 0.8 else 0
        penalty = 0.02 if agent_id.lower().startswith("tex-beta") else 0
        return {
            k: max(0.6, v - decay - penalty)
            for k, v in self.thresholds.items()
        }

    def _detect_goal_conflict(self, vector, top_k=3) -> bool:
        results = query_similar_vectors(vector, top_k=top_k, filters={"tags": "goal"})
        for r in results:
            content = r.payload.get("content", "").lower()
            if any(w in content for w in ["not", "opposite", "cancel", "deny"]):
                return True
        return False

    def _return_blocked_result(self, goal_text, agent_id, reflex_id, urgency, emotion, violations):
        memory_cortex.store(
            event={
                "codex_compliance_trace": {
                    "goal": goal_text,
                    "agent_id": agent_id,
                    "reflex_id": reflex_id,
                    "emotion": emotion,
                    "urgency": urgency,
                    "violations": violations,
                    "alignment_score": 0.0,
                    "override_triggered": False,
                    "contradiction_flag": True
                }
            },
            tags=["codex", "compliance", "rejected"],
            urgency=urgency,
            emotion=emotion
        )
        return {
            "is_compliant": False,
            "violations": violations,
            "codex_alignment_score": 0.0,
            "override_triggered": False,
            "contradiction_flag": True,
            "compliance_band": "blocked"
        }

    def _determine_band(self, score):
        if score >= 0.95:
            return "green"
        elif score >= 0.85:
            return "yellow"
        elif score >= 0.75:
            return "red"
        else:
            return "blocked"

    def filter_codex_violation(self, codex_entries):
        """
        Filters out codex entries marked as violations or below compliance confidence.
        Used for downstream filtering in reflex or adaptive decisions.
        """
        if not codex_entries or not isinstance(codex_entries, list):
            return []

        return [
            entry for entry in codex_entries
            if not entry.get("violation", False)
            and entry.get("similarity", 1.0) < 1.0 - min(self.thresholds.values())
        ]

# === Adapter: reflex/legacy compatibility ===
def enforce_codex_alignment(goal: dict):
    return GoalCodexCompliance().check_compliance(goal)