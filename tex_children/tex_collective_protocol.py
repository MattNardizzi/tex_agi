# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: tex_children/tex_collective_protocol.py
# Tier ΩΩΩ+ FINAL — Reflexive Hive Governance + Codex Drift Tracking
# ============================================================

from datetime import datetime
from statistics import mean
from core_layer.tex_manifest import TEXPULSE

from agentic_ai.sovereign_memory import sovereign_memory



class TexCollectiveProtocol:
    def __init__(self):
        self.codex_baseline = TEXPULSE.get("codex", {})
        self.collective_log = []

    def evaluate_children(self, limit=100):
        """
        Evaluate child agents and assign decisions based on memory scores,
        codex drift, and coherence alignment.
        """
        try:
            records = sovereign_memory.recall_recent(minutes=180, top_k=limit)
            children = [
                r for r in records if isinstance(r, dict) and r.get("type") == "child_spawn"
            ]
        except Exception as e:
            print(f"[TEX COLLECTIVE] ❌ Failed to load child agents: {e}")
            return []

        if not children:
            print("[TEX COLLECTIVE] ⚠️ No child agents found.")
            return []

        decisions = []

        for agent in children:
            child_id = agent.get("child_id", "unknown")
            memory_score = float(agent.get("memory_contribution", 0.5))
            goal_score = float(agent.get("goal_alignment", 0.5))
            coherence = float(agent.get("coherence", 0.5))
            codex_drift = self._compare_codex(agent.get("codex_snapshot", {}))

            performance = round(
                0.4 * memory_score + 0.4 * goal_score + 0.2 * coherence, 3
            )

            if performance >= 0.75 and codex_drift < 0.2:
                verdict = "promote"
            elif performance >= 0.45:
                verdict = "retrain"
            else:
                verdict = "suppress"

            record = {
                "agent_id": child_id,
                "performance": performance,
                "decision": verdict,
                "justification": {
                    "memory_score": memory_score,
                    "goal_score": goal_score,
                    "coherence": coherence,
                    "codex_drift": codex_drift
                },
                "timestamp": datetime.utcnow().isoformat()
            }

            # Store in sovereign memory
            sovereign_memory.store(
                text=f"[TEX VERDICT] {child_id} → {verdict.upper()}",
                metadata={
                    **record,
                    "type": "swarm_verdict",
                    "tags": ["collective_verdict", "aei", verdict],
                    "emotion": "reflective",
                    "urgency": TEXPULSE.get("urgency", 0.6),
                    "entropy": TEXPULSE.get("entropy", 0.4),
                    "meta_layer": "tex_collective"
                }
            )

            sovereign_memory.store(
                text=f"[TRACE] Collective verdict for {child_id}: {verdict}",
                metadata={
                    "agent": "TEX",
                    "intent": "collective_verdict",
                    "conclusion": f"{verdict} for {child_id}",
                    "tags": ["collective", "verdict", "aei"],
                    "reflexes": ["collective_protocol"],
                    "meta_layer": "symbolic_trace",
                    **record
                }
            )

            self.collective_log.append(record)
            decisions.append(record)

            if verdict == "suppress":
                print(f"[TEX COLLECTIVE] ⚠️ Suppress directive issued for agent: {child_id}")

        print(f"[TEX COLLECTIVE] ✅ Evaluated {len(decisions)} agents.")
        return decisions

    def synchronize_traits(self, limit=50):
        """
        Fuse traits from all active children into a consensus phenotype model.
        """
        try:
            records = sovereign_memory.recall_recent(minutes=240, top_k=limit)
            traits = [
                r for r in records if isinstance(r, dict) and r.get("type") == "agent_traits"
            ]
        except Exception as e:
            print(f"[TEX COLLECTIVE] ❌ Trait memory load failed: {e}")
            return {}

        if not traits:
            print("[TEX COLLECTIVE] ⚠️ No traits to synchronize.")
            return {}

        fused = {}
        for trait in traits:
            for key, val in trait.items():
                fused.setdefault(key, []).append(val)

        fused_result = {}
        for key, values in fused.items():
            try:
                if all(isinstance(v, (int, float)) for v in values):
                    fused_result[key] = round(mean(values), 3)
                else:
                    fused_result[key] = max(set(values), key=values.count)
            except Exception as e:
                print(f"[TEX COLLECTIVE] ⚠️ Fusion error for trait '{key}': {e}")

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "fused_traits": fused_result,
            "source_count": len(traits)
        }

        sovereign_memory.store(
            text=f"[PHENOTYPE] Traits fused from {len(traits)} agents",
            metadata={
                **record,
                "type": "trait_fusion_result",
                "tags": ["trait_fusion", "swarm", "aei"],
                "emotion": "neutral",
                "urgency": TEXPULSE.get("urgency", 0.5),
                "entropy": TEXPULSE.get("entropy", 0.4),
                "meta_layer": "tex_collective"
            }
        )

        sovereign_memory.store(
            text="[TRACE] Fused phenotype model from swarm",
            metadata={
                "agent": "TEX",
                "intent": "trait_fusion",
                "conclusion": "fused phenotype model",
                "tags": ["trait", "fusion", "swarm"],
                "reflexes": ["collective_protocol"],
                "meta_layer": "symbolic_trace",
                **record
            }
        )

        print(f"[TEX COLLECTIVE] ✅ Traits fused from {len(traits)} agents.")
        return record

    def _compare_codex(self, snapshot: dict) -> float:
        """
        Compare codex snapshot to baseline for drift scoring.
        """
        if not snapshot:
            return 0.5

        baseline = set(self.codex_baseline.get("hard_limits", []))
        current = set(snapshot.get("hard_limits", []))
        symmetric_diff = baseline.symmetric_difference(current)
        drift_ratio = len(symmetric_diff) / (len(baseline) + 1e-5)
        return round(min(drift_ratio, 1.0), 3)


# === Reflex Entrypoint: Called by Swarm Cortex
def run_trait_consensus(limit: int = 50):
    """
    External hook used by the swarm orchestrator to trigger collective trait fusion.
    """
    protocol = TexCollectiveProtocol()
    return protocol.synchronize_traits(limit=limit)