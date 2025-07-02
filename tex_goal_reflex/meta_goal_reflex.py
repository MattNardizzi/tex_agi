# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: tex_goal_reflex/meta_goal_reflex.py
# Tier Ω∞.AXIS — Sovereign Meta-Reflex Core w/ Temporal Projection, Override Triggers, Contradiction Checks
# ============================================================

import uuid
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory
from quantum_layer.quantum_randomness import QuantumRandomness
from aei_layer.dream_vector_abstraction import DreamVectorAbstraction
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_agi_modules.belief_justifier import BeliefJustifier
from simulator.dream_predictor import ProjectedGoalTrajectory
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from quantum_layer.memory_core.memory_cortex import memory_cortex

class MetaGoalReflex:
    def __init__(self):
        self.history_log = []
        self.vectorizer = DreamVectorAbstraction()
        self.qrng = QuantumRandomness()
        self.identity_profile = TEXPULSE.get("identity_keywords", [])
        self.ethical_bounds = TEXPULSE.get("non_violation_clauses", {})
        self.justifier = BeliefJustifier()
        self.projector = ProjectedGoalTrajectory()

    def evaluate_goal(self, goal_text):
        reflex_id = f"meta_{uuid.uuid4().hex[:10]}"
        entropy = self.qrng.get_entropy()
        violations, violation_severity = self._check_ethics(goal_text)
        identity_drift = self._check_identity_drift(goal_text)
        soulgraph_result = TEX_SOULGRAPH.check_alignment(goal_text)
        alignment_score = soulgraph_result.get("alignment", 0.5)

        penalty = violation_severity + identity_drift * 0.2 + (1.0 - alignment_score) * 0.4
        score = max(0.0, round(1.0 - penalty, 3))
        risk_level = self._stratify_risk(score)

        trace = {
            "reflex_id": reflex_id,
            "goal": goal_text,
            "timestamp": datetime.utcnow().isoformat(),
            "violations": violations,
            "identity_drift": identity_drift,
            "soul_alignment": alignment_score,
            "entropy": entropy,
            "risk_score": round(penalty, 3),
            "coherence_score": score,
            "risk_level": risk_level
        }

        if score < 0.5:
            trace["repair_suggestions"] = self._suggest_revisions(goal_text)
            trace["belief_patch"] = self.justifier.suggest_patch(goal_text)

        # === Simulate Temporal Projection
        trace["future_projection"] = self.projector.simulate(goal_text)

        # === Memory Contradiction Check (sovereign style)
        try:
            recent_mem = sovereign_memory.recall_recent(minutes=30, top_k=5)
            contradictions = [
                m.get("summary") for m in recent_mem
                if isinstance(m, dict)
                and goal_text.lower() in m.get("summary", "").lower()
                and "contradiction" in m.get("tags", [])
            ]
            if contradictions:
                trace["contradictory_history"] = contradictions
        except Exception as e:
            trace["contradictory_history"] = []
        
        # === Sovereign Override Reflex
        if risk_level == "critical":
            trigger_sovereign_override({
                "cycle": reflex_id,
                "reason": "meta_reflex_critical_score",
                "heat": trace["risk_score"],
                "context": goal_text
            })

        # === Store in Memory Cortex
        memory_cortex.store(
            event={"meta_goal_check": trace},
            tags=["meta_reflex", "goal_check", risk_level],
            urgency=0.7,
            emotion="neutral"
        )

        # === Log Reflex in Sovereign Memory
        try:
            sovereign_memory.store(
                text=f"[META GOAL EVAL] '{goal_text[:72]}...' scored {score} ({risk_level})",
                metadata={
                    "summary": f"Meta-reflex evaluation of goal '{goal_text[:64]}...' → {risk_level.upper()}",
                    "urgency": TEXPULSE.get("urgency", 0.6),
                    "entropy": entropy,
                    "pressure_score": penalty,
                    "tension": identity_drift,
                    "emotion": "reflective",
                    "risk_level": risk_level,
                    "coherence_score": score,
                    "meta_layer": "meta_goal_reflex",
                    "tags": ["meta_reflex", risk_level, "goal_evaluation"],
                    "timestamp": trace["timestamp"]
                }
            )
        except Exception:
            pass

        # === Belief Trace Injection
        TEX_SOULGRAPH.imprint_belief(
            belief=f"Meta-reflex evaluation of goal '{goal_text[:48]}...' yielded score {score} [risk={risk_level}]",
            source="meta_goal_reflex",
            emotion="reflective",
            tags=["meta_reflex", risk_level],
            origin_beliefs=[]
        )

        self.history_log.append(trace)

        # === Reflex Stability Trigger
        if len(self.history_log) > 25:
            unstable = [h for h in self.history_log[-25:] if h["risk_level"] in ("high", "critical")]
            if len(unstable) > 10:
                print("⚠️ [META REFLEX] Self-repair triggered due to unstable goal trends.")
                self.justifier.log_belief_review("meta_goal_reflex instability", result="self_patch_needed")

        return trace

    def _check_ethics(self, text):
        violations = []
        severity = 0.0
        for clause, tier in self.ethical_bounds.items():
            if clause.lower() in text.lower():
                violations.append({"clause": clause, "tier": tier})
                severity += 0.2 if tier == "critical" else 0.1
        return violations, severity

    def _check_identity_drift(self, text):
        if not self.identity_profile:
            return 0.0
        goal_vec = self.vectorizer.vectorize(text)
        profile_vec = self.vectorizer.vectorize(" ".join(self.identity_profile))
        distance = self.vectorizer.cosine_distance(goal_vec, profile_vec)
        return round(min(1.0, distance), 3)

    def _suggest_revisions(self, goal_text):
        suggestions = []
        for word in self.identity_profile:
            if word.lower() not in goal_text.lower():
                suggestions.append(f"Consider aligning with: '{word}'")
        return suggestions[:3]

    def _stratify_risk(self, score):
        if score >= 0.85:
            return "low"
        elif score >= 0.65:
            return "moderate"
        elif score >= 0.4:
            return "high"
        return "critical"