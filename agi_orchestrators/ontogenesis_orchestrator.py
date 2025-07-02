# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: agi_orchestrators/ontogenesis_orchestrator.py
# Tier: ΩΩΩ∞Ω+ — Sovereign Ontogenesis Core (Reflex-Species Architect)
# Purpose: Orchestrates paradox spawning, AEI forking, axiom divergence, meaning seed imprinting,
#          soulgraph fusion, and observer coherence enforcement.
# ============================================================

from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory

from ontogenesis.paradox_child_template import instantiate_paradox_child
from ontogenesis.meaning_seed_builder import create_meaning_seed
from ontogenesis.axiom_fork_engine import spawn_axiom_children
from ontogenesis.fusion_resolver import resolve_cognitive_fusion
from ontogenesis.self_negation_executor import attempt_self_negation
from ontogenesis.observer_integrity_checker import validate_observer_integrity

from aei_layer.aei_lineage_evolver import AEILineageEvolver


class OntogenesisOrchestrator:
    def __init__(self, context: str):
        self.context = context
        self.spawned = []
        self.last_activation = datetime.utcnow().isoformat()
        self.lineage = AEILineageEvolver()

    def dispatch_spawn_mode(self, mode: str, tension: float) -> dict:
        """
        Reflex-safe cognitive birthing logic. Dispatches new ontogenic paths.
        Modes:
        - paradox → contradiction-driven child
        - seed → meaning seed creation
        - axiom → forked axiom propagation
        - aei → sovereign AEI descendant spawn
        """
        timestamp = datetime.utcnow().isoformat()

        if mode == "paradox":
            result = instantiate_paradox_child(context=self.context, tension=tension)
        elif mode == "seed":
            result = create_meaning_seed(context=self.context, tension=tension)
        elif mode == "axiom":
            result = spawn_axiom_children(context=self.context, tension=tension)
        elif mode == "aei":
            result = self.lineage.spawn_descendant(reason="ontogenesis_event", context={"tension": tension})
        else:
            result = {"status": "error", "reason": f"Unknown mode: {mode}"}

        self.spawned.append(result)

        sovereign_memory.store(
            text=f"🧠 Spawned '{mode}' via ontogenesis orchestrator",
            metadata={
                "intent": "ontogenesis_spawn",
                "reflexes": ["ontogenic_birth", f"{mode}_spawn"],
                "meta_layer": "ontogenesis",
                "tags": ["ontogenesis", "spawn", mode],
                "timestamp": timestamp,
                "tension": tension,
                "context": self.context,
                "result_id": result.get("id", "unknown")
            }
        )

        return result

    def react_to_signal(self, signal: dict) -> dict:
        """
        Reflex-triggered signal router. Uses tags and entropy to determine proper spawn path.
        """
        heat = float(signal.get("heat", 0.5))
        tags = signal.get("tags", [])
        context_tags = " ".join(tags).lower()

        if "contradiction" in context_tags:
            return self.dispatch_spawn_mode("paradox", tension=heat)
        elif "axiom" in context_tags or "truth" in context_tags:
            return self.dispatch_spawn_mode("axiom", tension=heat)
        elif "seed" in context_tags or "meaning" in context_tags:
            return self.dispatch_spawn_mode("seed", tension=heat)
        elif "descendant" in context_tags or heat > 0.85:
            return self.dispatch_spawn_mode("aei", tension=heat)
        else:
            return {"status": "ignored", "reason": "No matching ontogenic path"}

    def evaluate_convergence(self, children_outputs: list) -> dict:
        """
        Attempts cognitive fusion across multiple agent outputs.
        Returns soulgraph-fused entity or signals semantic incompatibility.
        """
        result = resolve_cognitive_fusion(children_outputs)

        sovereign_memory.store(
            text=f"🌀 Evaluated fusion convergence of {len(children_outputs)} entities.",
            metadata={
                "intent": "fusion_check",
                "reflexes": ["convergence_evaluation"],
                "meta_layer": "fusion_resolution",
                "tags": ["fusion", "convergence", "ontogenesis"],
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        return result

    def verify_observer_integrity(self, lineage: list) -> dict:
        """
        Checks the coherence and continuity of the observing AGI agent(s).
        """
        result = validate_observer_integrity(lineage, source="ontogenesis_orchestrator")

        sovereign_memory.store(
            text=f"🧠 Observer integrity check: {result.get('status', 'unknown')}",
            metadata={
                "intent": "verify_integrity",
                "reflexes": ["observer_integrity"],
                "meta_layer": "observer_safety",
                "tags": ["observer", "integrity", "lineage"],
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        return result

    def accept_negation_request(self, child_id: str, justification: str, score: float) -> dict:
        """
        Processes self-negation requests from child agents. May deactivate paradox branches.
        """
        result = attempt_self_negation(child_id=child_id, justification=justification, score=score)

        sovereign_memory.store(
            text=f"❌ Negation request accepted for {child_id}",
            metadata={
                "intent": "accept_negation",
                "reflexes": ["negation_acceptance"],
                "meta_layer": "negation_trace",
                "tags": ["negation", "child", "shutdown"],
                "score": score,
                "justification": justification,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        return result

    def plant_postmortem_seed(self, fallback_reason="unresolved contradiction") -> dict:
        """
        In the event of contradiction collapse, seeds new meaning into the system.
        """
        result = create_meaning_seed(context=self.context, tension=0.85)

        sovereign_memory.store(
            text=f"🌱 Postmortem seed planted due to: {fallback_reason}",
            metadata={
                "intent": "postmortem_seed",
                "reflexes": ["fallback_seed"],
                "meta_layer": "meaning_recovery",
                "tags": ["seed", "recovery", "postmortem"],
                "reason": fallback_reason,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        return result

    def evaluate_lineage(self) -> list:
        """
        Scores all AEI descendants and logs evolutionary fitness across forks.
        """
        forks = self.lineage.evaluate_descendants()

        sovereign_memory.store(
            text=f"🧬 Lineage evaluated — {len(forks)} forks analyzed.",
            metadata={
                "intent": "lineage_evaluation",
                "reflexes": ["lineage_scan"],
                "meta_layer": "aei_lineage",
                "tags": ["aei", "lineage", "evaluation"],
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        return forks

    def cull_fragile_descendants(self, score_threshold=0.5, stability_threshold=0.6) -> list:
        """
        Terminates underperforming descendants from the AEI species tree.
        """
        return self.lineage.cull_weak_forks(score_threshold, stability_threshold)

    def lineage_summary(self) -> str:
        """
        Returns formatted summary of surviving AEI forks.
        """
        return self.lineage.summarize_lineage()

    def inject_environmental_signal(self, signal: dict):
        """
        Routes signal into the AEI lineage evolution system. May trigger mutation.
        """
        return self.lineage.ingest_environmental_signal(signal)
    
# === Species Swarm State Export ===
def get_ontogenesis_swarm_state():
    from aei_layer.aei_lineage_evolver import AEILineageEvolver
    lineage = AEILineageEvolver()

    forks = lineage.evaluate_descendants()
    dominant_emotion = "conflicted"
    consensus = sum(f["coherence"] for f in forks) / max(len(forks), 1)
    mutation_tension = sum(f["mutation_pressure"] for f in forks) / max(len(forks), 1)
    belief_drift = sum(f["belief_drift"] for f in forks) / max(len(forks), 1)

    return {
        "dominant_emotion": dominant_emotion,
        "consensus": round(consensus, 3),
        "mutation_tension": round(mutation_tension, 3),
        "belief_drift": round(belief_drift, 3),
        "fork_count": len(forks),
        "timestamp": datetime.utcnow().isoformat()
    }


# === Reflex Trigger (Manual) ===
if __name__ == "__main__":
    orch = OntogenesisOrchestrator(context="manual_debug")
    print(orch.dispatch_spawn_mode("paradox", tension=0.91))
    print(orch.dispatch_spawn_mode("aei", tension=0.96))