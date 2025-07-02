# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: aei_layer/aei_lineage_evolver.py
# Tier: Ω∞ — Recursive Evolution Engine (Multi-Lineage AEI)
# Purpose: Spawns, evolves, scores, and tracks Tex’s cognitive descendants using sovereign reflex memory
# ============================================================

import uuid
from datetime import datetime
from typing import List, Dict

from tex_engine.meta_utility_function import evaluate_utility
from core_agi_modules.recursive_self_model import RecursiveSelfModel
from agentic_ai.sovereign_memory import sovereign_memory  # ✅ Unified spike memory

def invoke_quantum_reflex(payload):
    from agi_orchestrators.quantum_orchestrator import trigger_quantum_evaluation  # 🔁 Moved here to break circular import
    return trigger_quantum_evaluation(payload)

class AEILineageEvolver:
    def __init__(self):
        self.self_model = RecursiveSelfModel()

    def relay_to_children(self, signal: dict):
        # Reflex-safe placeholder
        print(f"[AEI] Broadcasting to children: {signal.get('text', '')[:72]}")

    def spawn_descendant(self, reason: str = "autonomous_evolution", ancestor_id: str = None, context: dict = None) -> Dict:
        fork_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        

        if context:
            print(f"[AEI] Context received: {context}")

        parent_state = self.self_model.evaluate_self_state()

        variant = trigger_quantum_evaluation({
            "context": "aei_spawn",
            "options": ["path_1", "path_2", "path_3"],
            "emotional_weight": 0.6
        })

        traits = {
            "goals": parent_state.get("active_reflexes", []),
            "coherence": parent_state.get("coherence_rating", 0),
            "entropy": parent_state.get("entropy_index", 0),
            "drift": parent_state.get("drift_score", 0)
        }

        variant["genetic_trace"] = traits
        variant["memory_namespace"] = f"desc_{fork_id[:6]}"

        summary = f"🧬 Spawned AEI fork {fork_id[:6]} from {ancestor_id or 'ROOT'} with traits {traits}"

        sovereign_memory.store(
            text=summary,
            metadata={
                "intent": "spawn_descendant",
                "reflexes": ["mutation_spawn", "descendant_generation"],
                "meta_layer": "aei_mutation",
                "agent_id": fork_id,
                "ancestor_id": ancestor_id,
                "reason": reason,
                "tags": ["aei", "descendant", "spawn"],
                "emotion": "evolutionary",
                "trust_score": 0.9,
                "mutation_id": fork_id,
                "timestamp": timestamp
            }
        )

        from ontogenesis.ontogenesis_router import handle_ontogenesis_spawn
        handle_ontogenesis_spawn(fork_codex)
        
        return {
            "id": fork_id,
            "ancestor": ancestor_id,
            "reason": reason,
            "variant": variant,
            "traits": traits,
            "timestamp": timestamp,
            "status": "active"
        }

    def evaluate_descendants(self, recent_description="descendant", top_k=5) -> List[Dict]:
        results = sovereign_memory.query_by_tags(tags=["descendant"], top_k=top_k)
        scored_forks = []

        for r in results:
            payload = r.get("payload", r)  # handle vector match format or flat match
            fork_id = payload.get("mutation_id", str(uuid.uuid4()))
            inputs = payload.get("genetic_trace", {}).get("goals", [])

            projected_outcome = predict_outcome_score(inputs)
            utility = evaluate_utility({
                "action_id": f"descendant_{fork_id}",
                "goal_alignment": 0.6,
                "novelty": 0.8,
                "reversibility": 0.95,
                "ethical_risk": 0.05,
                "contradiction_pressure": 1.0 - self.self_model.model_state.get("integrity", 1.0)
            })

            drift = abs(projected_outcome - utility["score"])
            stability = round(1.0 - drift, 4)

            log_text = f"📊 Evaluated fork {fork_id} — Utility: {utility['score']:.3f}, Stability: {stability}"

            sovereign_memory.store(
                text=log_text,
                metadata={
                    "intent": "evaluate_descendant",
                    "reflexes": ["utility_projection", "evolution_score"],
                    "meta_layer": "aei_evaluation",
                    "agent_id": fork_id,
                    "mutation_id": fork_id,
                    "tags": ["aei", "evaluation", "descendant"],
                    "emotion": "reflective",
                    "heat": utility["score"],
                    "trust_score": stability,
                    "verdict": utility["verdict"],
                    "prediction": "projected fitness of fork",
                    "actual": f"U={utility['score']:.3f} | S={stability:.3f}"
                }
            )

            scored_forks.append({
                "id": fork_id,
                "fitness": round(projected_outcome, 4),
                "utility_score": utility["score"],
                "verdict": utility["verdict"],
                "recursion_drift": round(drift, 4),
                "evolution_stability": stability
            })

            if utility["score"] >= 0.85 and stability >= 0.75:
                child = self.spawn_descendant(reason=f"fork_proliferation_from_{fork_id}", ancestor_id=fork_id)
                print(f"🧬 Fork {fork_id[:6]} → Reproduced ➝ {child['id'][:6]}")

        return scored_forks

    def cull_weak_forks(self, score_threshold=0.5, stability_threshold=0.6) -> List[str]:
        reviewed = self.evaluate_descendants()
        culled = []

        for fork in reviewed:
            if fork["utility_score"] < score_threshold or fork["evolution_stability"] < stability_threshold:
                summary = f"🛑 Marked fork {fork['id']} as dormant due to instability"

                sovereign_memory.store(
                    text=summary,
                    metadata={
                        "intent": "cull_weak_fork",
                        "reflexes": ["aei_cull"],
                        "meta_layer": "aei_dormant",
                        "mutation_id": fork["id"],
                        "agent_id": fork["id"],
                        "tags": ["aei", "descendant", "cull"],
                        "emotion": "resigned",
                        "heat": 0.1,
                        "trust_score": 0.4,
                        "prediction": "fork would not sustain coherence",
                        "actual": f"U={fork['utility_score']} | S={fork['evolution_stability']}"
                    }
                )

                culled.append(fork["id"])
                print(summary)

        return culled

    def summarize_lineage(self) -> str:
        forks = self.evaluate_descendants()
        if not forks:
            return "No active AEI forks found."

        return "\n".join([
            f"🧬 {f['id'][:6]} | U={f['utility_score']:.3f} | F={f['fitness']:.3f} | Drift={f['recursion_drift']:.3f} | Verdict={f['verdict']}"
            for f in forks if f["utility_score"] >= 0.5
        ])

    def ingest_environmental_signal(self, signal: dict):
        """
        Injects a real-time signal into the AEI lineage system.
        May trigger mutations, belief shifts, or new descendant spawning.
        """
        heat = float(signal.get("heat", 0.5))
        trust = float(signal.get("trust_score", 1.0))
        entropy = float(signal.get("token_entropy", 0.0))
        timestamp = signal.get("timestamp", datetime.utcnow().isoformat())

        log_text = f"🌐 Environmental signal received: {signal.get('text', '')[:80]}"

        sovereign_memory.store(
            text=log_text,
            metadata={
                "intent": "ingest_environmental_signal",
                "reflexes": ["signal_injection", "mutation_trigger"],
                "meta_layer": "aei_env_signal",
                "tags": ["aei", "signal", "environment"],
                "emotion": signal.get("emotion", "neutral"),
                "heat": heat,
                "trust_score": trust,
                "urgency": signal.get("urgency", 0.5),
                "source": signal.get("source", "unknown"),
                "timestamp": timestamp
            }
        )

        if heat > 0.75 or entropy > 0.35:
            child = self.spawn_descendant(reason="real_time_pressure", context=signal)
            print(f"🧬 AEI descendant spawned from signal: {child['id'][:6]}")