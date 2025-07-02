# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/neuro_symbolic_reasoner.py
# Tier: ΩΩΩΩΩ∞ — Reflex-Based Vector Harmonizer
# Purpose: Performs belief fusion, contradiction entropy scoring, and cognitive trace justification.
# ============================================================

from typing import List, Dict, Any
from datetime import datetime
from agentic_ai.milvus_memory_router import memory_router, embed_text
from core_agi_modules.reasoning_fragments import synthesize_thought_fragment
from core_layer.tex_manifest import TEXPULSE
from quantum_layer.quantum_randomness import quantum_entropy_sample

class NeuroVectorReasoner:
    def __init__(self):
        self.reflex_trace = []
        self.entropy_seed = quantum_entropy_sample()

    def query_memory(self, query_text: str, top_k=5) -> List[Dict[str, Any]]:
        try:
            vector = embed_text(query_text)
            return memory_router.query_by_vector(vector, top_k=top_k)
        except Exception as e:
            self._log_trace("vector_query_error", query_text, str(e))
            return []

    def reason(self, symbolic_query=None, query=None, **kwargs) -> Dict[str, Any]:
        """
        Sovereign vector-only reflex harmonizer. Accepts symbolic_query or query.
        """
        query_text = symbolic_query or query
        if not query_text:
            raise ValueError("Missing symbolic_query or query")

        try:
            results = self.query_memory(query_text)
            entropy_score = self._calculate_entropy(results)
            fused = synthesize_thought_fragment([], results, entropy_score)

            memory_router.store(
                text=fused.get("conclusion", query_text),
                vector=embed_text(fused.get("conclusion", query_text)),
                metadata={
                    "timestamp": datetime.utcnow().isoformat(),
                    "type": "neuro_vector_reasoning",
                    "tags": ["reflex_reasoning", "belief_fusion"],
                    "emotion": TEXPULSE.get("emotion", "analytical"),
                    "entropy": entropy_score,
                    "summary": fused.get("summary", ""),
                    "meta_layer": "neuro_symbolic_reasoner"
                }
            )

            self._log_trace("reasoning", query_text, fused)

            return {
                "vector_results": results,
                "conclusion": fused.get("conclusion"),
                "justification": fused.get("justification"),
                "entropy_score": entropy_score,
                "reflex_recommendation": fused.get("reflexes", []),
                "summary": fused.get("summary")
            }

        except Exception as e:
            self._log_trace("reasoning_error", query_text, str(e))
            return {
                "conclusion": "[error]",
                "justification": "Reasoning failed.",
                "entropy_score": 1.0,
                "reflex_recommendation": [],
                "summary": "[error]"
            }

    def _calculate_entropy(self, vec_results: List[Dict[str, Any]]) -> float:
        signal = 1.0 / (len(vec_results) + 1.0)
        modulated = self.entropy_seed * signal
        return round(min(1.0, modulated), 6)

    def _log_trace(self, mode: str, input_data: Any, output_data: Any):
        self.reflex_trace.append({
            "mode": mode,
            "input": input_data,
            "output": output_data,
            "pulse": TEXPULSE
        })


# === AGI-Embedded Justifier ===
def generate_symbolic_justification(belief: str = "", context: str = "meta_reflection", **kwargs) -> dict:
    """
    Generates a justification string for a belief using embedded contextual heuristics.
    Symbolic inference has been deprecated.
    """
    try:
        belief_text = belief or "Reflexive belief emerging from contextual alignment."
        justification = f"The belief '{belief_text}' is contextually supported by alignment traces from '{context}'."

        return {
            "justification": justification,
            "reflexes": ["belief_trace_confirmed"],
            "confidence": 0.82
        }
    except Exception as e:
        return {
            "justification": "[justification error]",
            "reflexes": [],
            "confidence": 0.0
        }
# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: dream_craft/dream_orchestrator.py
# Tier: ΩΩΩΩΩ∞∞𝛀𝛀 — Substrate Cortex Conductor
# Purpose: Routes dream substrate activations based on entropy,
#          contradiction, identity drift, or reflex spike.
# ============================================================

from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from dream_craft.substrate_registry import get_registered_substrates
from dream_craft.substrate_voter import select_best_substrate
from dream_craft.dream_session import run_dream_session
from dream_craft.dream_archive import archive_dream_result
from dream_craft.belief_injection import inject_belief_from_dream
from utils.logging_utils import log


def trigger_dream_layer(trigger_source="pulse", context_memory=None, force_substrate=None):
    """
    Entry point for dream substrate execution.
    """
    timestamp = datetime.utcnow().isoformat()
    entropy = float(TEXPULSE.get("entropy", 0.4))
    urgency = float(TEXPULSE.get("urgency", 0.7))

    log.info(f"[DreamOrchestrator] 🔁 Triggered from: {trigger_source} | entropy={entropy}, urgency={urgency}")

    # Step 1: Fetch viable substrates
    substrates = get_registered_substrates()
    if not substrates:
        log.warning("⚠️ No substrates registered. Dream aborted.")
        return {"status": "no_substrates"}

    # Step 2: Select substrate to simulate
    substrate = force_substrate if force_substrate else select_best_substrate(substrates, entropy, urgency)
    if not substrate:
        log.warning("⚠️ No substrate selected. Dream layer skipped.")
        return {"status": "no_viable_substrate"}

    # Step 3: Run dream simulation session
    result = run_dream_session(substrate=substrate, context=context_memory, trigger_source=trigger_source)
    if not result or "forecast" not in result:
        log.warning("⚠️ Dream session returned no valid result.")
        return {"status": "invalid_dream_result"}

    # Step 4: Archive result
    archive_dream_result(result)

    # Step 5: Belief update if dream meaningful
    if result.get("impact_score", 0) > 0.6:
        inject_belief_from_dream(result)

    log.success(f"[DreamOrchestrator] ✅ Dream completed via substrate: {substrate['id']}")
    return {
        "status": "dream_completed",
        "result": result,
        "substrate_id": substrate['id'],
        "timestamp": timestamp
    }


def run_dream_orchestration(payload=None) -> dict:
    """
    Adapter layer between spike/reflex routing and the dream substrate cortex.
    Accepts optional payload, routes it into the dream_craft engine.
    """
    trigger = payload.get("trigger", "reflex") if isinstance(payload, dict) else "reflex"
    context = payload.get("context") if isinstance(payload, dict) else None

    log.info(f"[DreamOrchestrator] 🚀 Routed dream orchestration: trigger={trigger}")
    return trigger_dream_layer(trigger_source=trigger, context_memory=context)
class NeuroSymbolicReasoner:
    def __init__(self):
        self.reflection_trace = []

    def reason(self, symbolic_query=None, **kwargs):
        """
        Lightweight symbolic reasoner fallback that returns a justification string.
        """
        if not symbolic_query:
            raise ValueError("symbolic_query is required.")

        justification = f"The belief '{symbolic_query}' aligns with prior traces."
        self.reflection_trace.append({
            "query": symbolic_query,
            "justification": justification,
            "timestamp": datetime.utcnow().isoformat()
        })

        return {
            "conclusion": symbolic_query,
            "justification": justification,
            "reflex_recommendation": ["symbolic_alignment"],
            "confidence": 0.84
        }