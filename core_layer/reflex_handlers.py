# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/reflex_handlers.py
# Tier: ΩΩΩΩΩΩΩ — Identity Reflex Arbitration Cortex
# Purpose: Resolves internal identity belief conflicts using symbolic + quantum-integrated Sovereign Memory.
# ============================================================

from core_agi_modules.neuro_symbolic_reasoner import NeuroVectorReasoner
from tex_signal_spine import dispatch_signal
from utils.logging_utils import log
from core_layer.tex_manifest import TEXPULSE
from core_layer.reentry_protocols import run_reentry_check
from agentic_ai.sovereign_memory import memory_router

from datetime import datetime
import uuid

reasoner = NeuroVectorReasoner()

# === Reflex: Identity Conflict Resolver ===
def handle_identity_conflict(signal):
    belief = signal.get("payload", {}).get("belief", "Tex is sovereign")
    log.info(f"🧠 [REASONING] Processing belief: {belief}")

    reasoning_output = reasoner.reason(symbolic_query=belief)

    entropy_score = reasoning_output.get("entropy_score", 0.0)
    justification = reasoning_output.get("justification", "[None]")
    reflexes = reasoning_output.get("reflex_recommendation", [])
    conclusion = reasoning_output.get("conclusion", "No conclusion")
    mutation_id = reasoning_output.get("mutation_id", str(uuid.uuid4()))
    fork_uid = f"TEX-FORK-{mutation_id[:8]}"

    # === Reflex Routing Based on Entropy Thresholds ===
    if entropy_score >= 0.7:
        dispatch_signal("fork_init", {
            "summary": "Contradiction entropy high — initiating structural evolution.",
            "justification": justification,
            "proposed_mutation": f"Modify or suspend belief: '{belief}'",
            "fork_uid": fork_uid
        })
        log.warning(f"⚠️ [REASONING] Fork triggered due to belief contradiction → UID={fork_uid}")

        # === Store Fork Profile in SovereignMemory ===
        try:
            memory_router.store(
                text=f"Fork profile initiated for {fork_uid}",
                metadata={
                    "timestamp": datetime.utcnow().isoformat(),
                    "fork_uid": fork_uid,
                    "origin": "tex_agi",
                    "traits": f"urgency={TEXPULSE.get('urgency', 0.6)},entropy={TEXPULSE.get('entropy', 0.4)}",
                    "reason": "identity_conflict",
                    "tags": ["fork_profile", fork_uid]
                }
            )
            log.info(f"📦 [MEMORY] Fork profile stored → {fork_uid}")
        except Exception as e:
            log.warning(f"⚠️ [MEMORY] Failed to store fork profile: {e}")

    elif 0.5 <= entropy_score < 0.7:
        dispatch_signal("belief_fragile", {
            "summary": "Belief under tension — not yet fractured.",
            "entropy_score": entropy_score,
            "justification": justification
        })
        log.info(f"🌀 [REASONING] Belief fragile: {justification}")

    else:
        dispatch_signal("belief_stabilized", {
            "summary": "Belief held under symbolic pressure.",
            "justification": justification,
            "reflexes": reflexes
        })
        log.info(f"✅ [REASONING] Belief stabilized: {justification}")

    # === Unified Reflex Trace (Chrono + Vector) ===
    try:
        memory_router.store(
            text=f"Belief: {belief} → {justification}",
            metadata={
                "emotion": "reflective",
                "urgency": float(TEXPULSE.get("urgency", 0.5)),
                "entropy": float(TEXPULSE.get("entropy", 0.5)),
                "pressure_score": entropy_score,
                "tension": 0.0,
                "tags": [
                    "identity_conflict",
                    "symbolic_justification",
                    "reflex",
                    "belief_evaluation",
                    "fork_uid=" + fork_uid if entropy_score >= 0.7 else "belief_integrity"
                ]
            }
        )
        log.info("🧠 [MEMORY] Identity reflex reasoning stored.")
    except Exception as e:
        log.warning(f"⚠️ [MEMORY] Failed to store belief reasoning: {e}")

# === Reflex: Substrate Shift Handler ===
def handle_substrate_shift(signal):
    urgency = signal.get("urgency", 0.0)
    entropy = signal.get("entropy", 0.0)

    log.info(f"🌀 [SUBSTRATE] Reflex triggered → urgency={urgency:.2f}, entropy={entropy:.2f}")

    if urgency >= 0.7:
        log.warning("⚠️ [SUBSTRATE] Critical substrate instability detected. Initiating reentry protocols.")
        run_reentry_check()
    else:
        log.info("🧘 [SUBSTRATE] Mild fluctuation detected. Monitoring state only.")

    try:
        memory_router.store(
            text="Substrate shift reflex engaged.",
            metadata={
                "emotion": "neutral",
                "urgency": urgency,
                "entropy": entropy,
                "pressure_score": 0.5,
                "tension": 0.2,
                "tags": ["substrate_shift", "reflex", "system_integrity"]
            }
        )
        log.info("🧠 [MEMORY] Substrate shift recorded.")
    except Exception as e:
        log.warning(f"⚠️ [MEMORY] Failed to record substrate shift: {e}")