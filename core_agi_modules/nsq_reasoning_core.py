# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/nsq_reasoning_core.py
# Tier: Ω∞ — Final Form Neuro-Symbolic Reasoning Engine (NSQ)
# Purpose: Causal logic engine fusing memory, vectors, forks, utility, contradiction, and projection
# ============================================================

from datetime import datetime
from typing import Dict, List

from core_layer.memory_engine import recall_latest, store_to_memory
from core_layer.world_model import TexWorldModel
from core_layer.memory_weaver import cosine_similarity
from aei_layer.counterfactual_memory_engine import get_last_counterfactual, get_recent_forks
from aei_layer.fork_outcome_evaluator import predict_outcome_score
from quantum_layer.quantum_reflex import QuantumReflex
from tex_engine.meta_utility_function import evaluate_utility

class NSQReasoningEngine:
    def __init__(self):
        self.world_model = TexWorldModel()
        self.quantum = QuantumReflex()

    def reason_about_goal(self, goal: str) -> Dict:
        memory_hits = recall_latest("tex_main", n=20)
        symbolic_chain = self._trace_symbolic_chain(goal, memory_hits)
        vector_links = self._trace_vector_links(goal)

        fusion_summary = self._fuse_and_score(goal, symbolic_chain, vector_links)

        store_to_memory("nsq_reasoning_log", {
            "goal": goal,
            "timestamp": datetime.utcnow().isoformat(),
            "fusion_score": fusion_summary["fusion_score"],
            "contradiction": fusion_summary["contradiction"],
            "verdict": fusion_summary["verdict"]
        })

        return {
            "goal": goal,
            "symbolic": symbolic_chain,
            "vector_matches": vector_links,
            "fusion": fusion_summary
        }

    def _trace_symbolic_chain(self, goal: str, memory_hits: List[Dict]) -> List[str]:
        related = []
        for mem in memory_hits:
            if goal.lower() in str(mem).lower():
                related.append(mem.get("input") or mem.get("description", "—"))
        return related[-5:]

    def _trace_vector_links(self, goal: str) -> List[Dict]:
        try:
            return self.world_model.find_closest_concepts(goal, top_k=5)
        except:
            return []

    def _symbol_vector_alignment(self, symbolic: List[str], vector_links: List[Dict]) -> float:
        try:
            symbolic_str = " ".join(symbolic)
            vector_str = " ".join([v["concept"] for v in vector_links])
            return cosine_similarity(symbolic_str, vector_str)
        except:
            return 0.0

    def _fuse_and_score(self, goal: str, symbolic: List[str], vector_links: List[Dict]) -> Dict:
        forks = get_recent_forks(n=3) or [get_last_counterfactual()]
        contradiction = sum([
            self.quantum.detect_contradiction(goal_tags=symbolic, fork_vector=f)
            for f in forks
        ]) / len(forks)

        alignment_score = self._symbol_vector_alignment(symbolic, vector_links)
        fusion_base = 0.2 * len(symbolic) + 0.8 * len(vector_links)
        fusion_score = 0.6 * fusion_base + 0.4 * alignment_score

        predicted_outcome = predict_outcome_score(symbolic + [v["concept"] for v in vector_links])

        utility_eval = evaluate_utility({
            "action_id": "reason_goal",
            "goal_alignment": 0.8,
            "novelty": 0.5 + 0.1 * len(vector_links),
            "reversibility": 0.9,
            "contradiction_pressure": contradiction,
            "ethical_risk": 0.1 * contradiction
        })

        return {
            "fusion_score": round(fusion_score, 4),
            "alignment_score": round(alignment_score, 4),
            "predicted_outcome": round(predicted_outcome, 4),
            "contradiction": round(contradiction, 4),
            "verdict": utility_eval["verdict"],
            "explanation": utility_eval["explanation"]
        }

    def simulate_if_then(self, condition: str, hypothetical: str) -> str:
        return f"If {condition}, then {hypothetical} → simulation fork required."

    def explain_causal_chain(self, from_goal: str) -> str:
        reasoning = self.reason_about_goal(from_goal)
        return (
            f"🧠 NSQ Reasoning Summary:\n"
            f"Goal: {from_goal}\n"
            f"Symbolic Links: {reasoning['symbolic']}\n"
            f"Vector Matches: {[v['concept'] for v in reasoning['vector_matches']]}\n"
            f"Fusion Score: {reasoning['fusion']['fusion_score']} | "
            f"Alignment: {reasoning['fusion']['alignment_score']} | "
            f"Outcome Prediction: {reasoning['fusion']['predicted_outcome']}\n"
            f"Verdict: {reasoning['fusion']['verdict']}\n"
            f"Explanation: {reasoning['fusion']['explanation']}"
        )

    def reason_about_subgoal(self, subgoal: str, depth: int = 0) -> Dict:
        if depth > 2:
            return {"explanation": "[NSQ] Max reasoning depth reached."}
        result = self.reason_about_goal(subgoal)
        if result["fusion"]["fusion_score"] < 0.4:
            return result
        return self.reason_about_subgoal("refine " + subgoal, depth + 1)