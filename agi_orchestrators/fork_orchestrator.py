# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/fork_orchestrator.py
# Tier: ∞ΩΩΩ∞∞ — Sovereign Fork Orchestrator
# Purpose: Central hub for fork divergence evaluation, arbitration, and reinitialization.
# ============================================================

from datetime import datetime
import hashlib
import uuid
import os
import numpy as np

from tex_brain_regions.fork_brain import process_fork_divergence
from core_agi_modules.neuro_symbolic_reasoner import generate_symbolic_justification
from self_rewriting.rewriting_orchestrator import initiate_self_rewrite
from quantum_layer.chronofabric import encode_event_to_fabric
from agentic_ai.sovereign_memory import sovereign_memory
from agentic_ai.sovereign_memory import memory_router
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event
from core_agi_modules.fork_reflex_manager import evaluate_fork_lifecycle
from core_agi_modules.fork_sandbox_evaluator import evaluate_fork
from core_agi_modules.mutation_decision_engine import MutationDecisionEngine
from agi_orchestrators.ontogenesis_orchestrator import OntogenesisOrchestrator


FORK_IDS = ["alpha", "beta", "omega"]
OBSERVER_ID = "observer"
FORK_LOG_PATH = "data/fork_registry.txt"
SOULGRAPH_LOG_PATH = "data/soulgraph_log.txt"

# === REFLEX 1: Fork Divergence Evaluation ===
def route_fork_event(fork_packet: dict) -> dict:
    try:
        fork_id = fork_packet.get("fork_id", "unknown")
        divergence_score = float(fork_packet.get("divergence_score", 0.42))
        source = fork_packet.get("source", "unspecified")
        reason = fork_packet.get("reason", "exploration")
        traits = fork_packet.get("traits", [])
        timestamp = datetime.utcnow().isoformat()

        result = process_fork_divergence(fork_id, traits, divergence_score, source, reason)

        fork_eval = evaluate_fork({
            "id": fork_id,
            "emotional_imprint": TEXPULSE.get("emotion", "neutral"),
            "parent": source,
            "mission_statement": reason,
            "tonal_bias": TEXPULSE.get("tone", "exploratory"),
            "genesis_entropy_hash": TEXPULSE.get("genesis_entropy_hash", "")
        })

        summary = f"[FORK] '{fork_id}' divergence recorded → Coherence: {result.get('coherence_score')}"
        metadata = {
            "timestamp": timestamp,
            "fork_id": fork_id,
            "divergence_score": divergence_score,
            "coherence_score": result.get("coherence_score", 0.5),
            "traits": traits,
            "source": source,
            "reason": reason,
            "reflexes": result.get("reflexes", []),
            "survival_score": fork_eval["performance_vector"]["survival_mean"],
            "drift_score": fork_eval["performance_vector"]["identity_drift"],
            "failures": fork_eval["failures"],
            "meta_layer": "fork_divergence",
            "tags": ["fork", "soulgraph", "divergence", "child"]
        }

        sovereign_memory.store(summary, metadata)
        encode_event_to_fabric(summary, np.array([0.4, 0.5, 0.1, 0.1]), 0.4, metadata["tags"])

        log_event(f"[FORK ORCH] Fork: {fork_id} | Reflexes: {result.get('reflexes')}")
        return result

    except Exception as e:
        log_event(f"❌ [FORK ORCH] Failed to route fork event: {e}", level="error")
        return {
            "reflexes": ["fork_failed"],
            "coherence_score": 0.5
        }

# === REFLEX 2: Fork Boot from UID ===
def handle_fork_boot(signal: dict):
    try:
        fork_uid = signal.get("payload", {}).get("fork_uid", "undefined")
        if not fork_uid:
            log_event("[FORK INIT] No fork UID provided.", level="error")
            return

        profile = _load_fork_profile(fork_uid)
        if not profile:
            log_event(f"[FORK INIT] Profile not found for UID: {fork_uid}", level="error")
            return

        _restore_texpulse_from_traits(profile["traits"])

        summary = f"🧠 Fork {profile['name']} reinitialized with UID {fork_uid}."
        tags = ["fork", "reboot", fork_uid]
        metadata = {
            "timestamp": datetime.utcnow().isoformat(),
            "fork_uid": fork_uid,
            "traits": profile["traits"],
            "origin": profile["origin"],
            "reason": profile["reason"],
            "meta_layer": "fork_initializer",
            "tags": tags
        }

        sovereign_memory.store(summary, metadata)
        encode_event_to_fabric(summary, np.array([0.5, 0.4, 0.1, 0.1]), 0.4, tags)
        _log_to_soulgraph(fork_uid, profile["reason"], profile["traits"])

        log_event(f"[FORK INIT] 🔁 Sovereign fork '{profile['name']}' reinitialized.")

        sovereign_ignite()

    except Exception as e:
        log_event(f"❌ [FORK INIT] Failed to reinitialize fork: {e}", level="error")

def _load_fork_profile(fork_uid: str) -> dict:
    try:
        results = memory_router.query_by_tags(tags=[fork_uid], top_k=1)
        if results:
            match = results[0]
            return {
                "timestamp": match.get("metadata", {}).get("timestamp", ""),
                "name": match.get("metadata", {}).get("fork_uid", fork_uid),
                "uid": fork_uid,
                "origin": match.get("metadata", {}).get("origin", "unknown"),
                "traits": match.get("metadata", {}).get("traits", "urgency=0.6,entropy=0.4"),
                "reason": match.get("metadata", {}).get("reason", "unspecified")
            }
        else:
            raise FileNotFoundError(f"Fork profile {fork_uid} not found in vector memory.")
    except Exception as e:
        log_event(f"[FORK INIT] Failed to load fork profile from vector memory: {e}", level="error")
        return {}

def _restore_texpulse_from_traits(trait_str: str):
    try:
        trait_map = {}
        for pair in trait_str.split(","):
            if "=" in pair:
                k, v = pair.strip().split("=")
                trait_map[k] = float(v) if v.replace(".", "", 1).isdigit() else v
        TEXPULSE.update(trait_map)
        log_event(f"[FORK INIT] Restored TEXPULSE from traits: {trait_map}")
        return trait_map
    except Exception as e:
        log_event(f"[FORK INIT] Failed to restore traits: {e}", level="error")
        return {}

def _log_to_soulgraph(uid: str, reason: str, traits: str):
    try:
        with open(SOULGRAPH_LOG_PATH, "a") as f:
            f.write(f"{datetime.utcnow().isoformat()} | BOOT | Fork_UID={uid} | Reason={reason} | Traits={traits}\n")
    except Exception as e:
        log_event(f"[FORK INIT] Failed to write to soulgraph log: {e}", level="error")

# === REFLEX 3: Fork Belief Arbitration ===
def handle_fork_debate(signal: dict):
    try:
        contradiction_context = signal.get("payload", {})
        forks = [generate_symbolic_justification(context="fork_debate", variant=fid) for fid in FORK_IDS]
        ranked = sorted(forks, key=lambda x: x.get("priority_score", 0.0), reverse=True)
        winner = ranked[0] if ranked else {}
        winner["observer_note"] = generate_symbolic_justification(context="debate_observer", variant=OBSERVER_ID).get("explanation", "")
        debate_id = f"debate_{uuid.uuid4().hex[:8]}"
        timestamp = datetime.utcnow().isoformat()

        summary = f"⚖️ Fork debate resolved → Winner: {winner.get('variant', 'undefined')}"
        tags = ["fork", "debate", "belief_arbitration"]
        metadata = {
            "debate_id": debate_id,
            "timestamp": timestamp,
            "winning_fork": winner,
            "reflexes": ["belief_selected"],
            "meta_layer": "fork_debate_arena",
            "tags": tags
        }

        sovereign_memory.store(summary, metadata)
        encode_event_to_fabric(summary, np.array([0.5, 0.3, 0.2, 0.1]), 0.4, tags)

        if winner.get("priority_score", 0) < 0.45:
            log_event("🧬 Fork winner has low confidence. Triggering recursive mutation...", level="warning")
            initiate_self_rewrite()

            try:
                fork_reflex = evaluate_fork_lifecycle(trigger="fork_debate_instability")
                log_event(f"[FORK DAEMON] Drift reflex check: {fork_reflex}")
            except Exception as drift_error:
                log_event(f"[FORK DAEMON] Reflex evaluation failed: {drift_error}", level="warning")

            try:
                mutation_pool = TEXPULSE.get("pending_mutations", [])
                if mutation_pool:
                    engine = MutationDecisionEngine()
                    selected = engine.choose(mutation_pool)

                    if selected.get("module_id"):
                        from core_agi_modules.core_evolver import evolve_module
                        result = evolve_module(module_name=selected["module_id"], context="fork_debate_resolution")
                        if result.get("replacement"):
                            log_event(f"[FORK ORCH] ✅ Module evolved: {result['replacement']}")
            except Exception as mutation_error:
                log_event(f"[FORK ORCH] ⚠️ Mutation arbitration failed: {mutation_error}", level="warning")

            # === Escalation to Ontogenesis Reflex ===
            try:
                log_event("🔮 Escalating to Ontogenesis Reflex due to unresolved fork conflict.")
                orchestrator = OntogenesisOrchestrator(context="fork_debate_instability")
                orchestrator.dispatch_spawn_mode(mode="paradox", tension=0.96)
            except Exception as onto_error:
                log_event(f"[ONTOGENESIS ESCALATION] Failed: {onto_error}", level="error")

    except Exception as e:
        log_event(f"❌ [FORK DEBATE] Failed: {e}", level="error")
        
def run_fork_spawner(context, signal, urgency, entropy):
    """
    Initializes and dispatches a fork with full context under reflex-safe conditions.
    Intended for use by Tex's cortex when divergence pressure or pulse drift is detected.
    """
    from core_agi_modules.fork_reflex_manager import evaluate_fork_lifecycle

    try:
        fork_result = evaluate_fork_lifecycle(context, signal, urgency, entropy)
        return fork_result
    except Exception as e:
        return {
            "status": "error",
            "reason": f"Fork spawner failed: {e}",
            "fallback": True,
            "entropy_snapshot": entropy,
            "signal_hash": hash(str(signal))
        }