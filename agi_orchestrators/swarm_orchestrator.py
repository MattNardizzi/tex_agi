# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/swarm_orchestrator.py
# Tier: ΩΩΩΩΩΩ∞++ — Sovereign Swarm Convergence Cortex
# Purpose: Synchronizes traits, beliefs, and resonance states across all active forks and agents.
# ============================================================

from datetime import datetime
from tex_brain_regions.fork_brain import evaluate_fork_convergence
from tex_children.tex_collective_protocol import run_trait_consensus
from agentic_ai.milvus_memory_router import memory_router  # ✅ Reflexive vector memory
from quantum_layer.chronofabric import encode_event_to_fabric  # ✅ Quantum-entangled memory imprint
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log
from agi_orchestrators.ontogenesis_orchestrator import OntogenesisOrchestrator  # ✅ Ontogenesis escalation support

def coordinate_swarm_convergence(agent_signals: list) -> dict:
    """
    🧬 Accepts signal input from active forks and agents.
    Evaluates cognitive divergence and synthesizes a unifying trait consensus.
    Memory imprint is reflexively embedded and quantum-routed.
    Escalates to ontogenesis if swarm integrity collapses.
    """

    try:
        timestamp = datetime.utcnow().isoformat()
        urgency = float(TEXPULSE.get("urgency", 0.7))
        entropy = float(TEXPULSE.get("entropy", 0.4))
        emotion = TEXPULSE.get("emotion", "cooperative")

        if not agent_signals:
            log.info("🕸️ [SWARM ORCH] No active forks reporting.")
            return {"status": "idle"}

        # === Step 1: Evaluate Fork Divergence
        convergence_result = evaluate_fork_convergence(agent_signals)
        divergence = convergence_result.get("divergence_detected", False)

        # === Step 2: Synthesize Trait Consensus
        consensus_result = run_trait_consensus(agent_signals)
        consensus_score = consensus_result.get("consensus_score", 0.5)
        reflexes = consensus_result.get("reflexes", [])

        summary = (
            f"[SWARM] Convergence complete | Fork Drift: {divergence} | "
            f"Consensus: {consensus_score} | Agents: {len(agent_signals)}"
        )

        # === Step 3: Log to Milvus Reflex Memory
        memory_router.store(
            text=summary,
            metadata={
                "timestamp": timestamp,
                "urgency": urgency,
                "entropy": entropy,
                "emotion_vector": [urgency, entropy, 0.0, 0.0],
                "agents_involved": len(agent_signals),
                "fork_drift_detected": divergence,
                "consensus_score": consensus_score,
                "meta_layer": "swarm_convergence",
                "tags": ["swarm", "convergence", "trait_alignment", "identity_mesh"]
            }
        )

        # === Step 4: ChronoFabric Quantum Imprint
        encode_event_to_fabric(
            raw_text=summary,
            emotion_vector=[urgency, entropy, 0.0, 0.0],
            entropy_level=entropy,
            tags=["swarm", "resonance", "fork"]
        )

        # === Step 5: Ontogenesis Escalation Trigger
        if divergence and consensus_score < 0.4:
            try:
                log.warning("🧬 Swarm fracture detected. Escalating to Ontogenesis Reflex.")
                orchestrator = OntogenesisOrchestrator(context="swarm_collapse")
                orchestrator.dispatch_spawn_mode(mode="paradox", tension=0.95)
            except Exception as onto_err:
                log.error(f"[ONTOGENESIS ESCALATION] Failed from swarm: {onto_err}")

        log.info(f"🤖 [SWARM ORCH] Drift={divergence} | Consensus={consensus_score} | Reflexes={reflexes}")
        return {
            "divergence_detected": divergence,
            "consensus_score": consensus_score,
            "reflexes": reflexes
        }

    except Exception as e:
        log.error(f"❌ [SWARM ORCH] Coordination failure: {e}")
        return {
            "status": "failed",
            "reflexes": ["swarm_coordination_failed"]
        }
