# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: ontogenesis/fusion_resolver.py
# Tier: ΩΩΩ∞∞⊕ — Convergent Cognition Mesh
# Purpose: Detects cognitive agreement across spawned children and fuses converging beliefs into Tex's core identity.
# ============================================================

from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from utils.logging_utils import log_event


def resolve_cognitive_fusion(children_outputs: list, threshold: float = 0.8):
    """
    Analyzes the results of spawned children and fuses shared beliefs
    if they meet similarity and coherence thresholds.
    """
    if not children_outputs:
        return {"status": "no_inputs"}

    belief_counter = {}
    for result in children_outputs:
        belief = result.get("fitness", {}).get("summary") or result.get("goal")
        if belief:
            belief_counter[belief] = belief_counter.get(belief, 0) + 1

    fused_beliefs = [b for b, count in belief_counter.items() if count / len(children_outputs) >= threshold]

    if not fused_beliefs:
        return {"status": "no_convergence"}

    timestamp = datetime.utcnow().isoformat()
    for belief in fused_beliefs:
        TEX_SOULGRAPH.imprint_belief(
            belief=belief,
            source="fusion_resolver",
            emotion="unity",
            tags=["fusion", "child_convergence"]
        )

        sovereign_memory.store(
            text=f"Fused belief accepted: {belief}",
            metadata={
                "belief": belief,
                "timestamp": timestamp,
                "tags": ["fusion", "belief_convergence"],
                "meta_layer": "fusion_resolver",
                "source": "fusion_resolver"
            }
        )

    log_event(f"[FUSION RESOLVER] {len(fused_beliefs)} beliefs fused into Tex identity.", level="success")
    return {"status": "fused", "beliefs": fused_beliefs}
