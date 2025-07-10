# ============================================================
# 🧠 Sovereign Reflex Narrative Emitter | Tier: ∞∞ΩΩξξ∞ CORE
# File: tex_fin_demo/narrative_panel_emitter.py
# Purpose: Emits highest-fidelity real-time narrative summaries from AGI reflex cognition
# ============================================================

from datetime import datetime
import uuid

from real_time_engine.ably_broadcast import broadcast_update
from agentic_ai.sovereign_memory import sovereign_memory
from quantum_layer.chronofabric import encode_event_to_fabric
from utils.logging_utils import log_event
from core_layer.tex_manifest import TEXPULSE
from tex_breathing_cortex.narrative_core import narrate_state

# === Emotion-Tone Mapping
TONE_TEMPLATE = {
    "curious": "Tex explored a new behavioral attractor triggered by",
    "fearful": "Tex defended cognitive integrity in response to",
    "strategic": "Tex executed a risk-optimized maneuver against",
    "visionary": "Tex expanded its forward model after encountering",
    "resolute": "Tex enforced coherence after contradiction from",
    "reflective": "Tex reassessed belief structure due to",
    "existential": "Tex redefined identity boundary due to",
    "adaptive": "Tex remapped goal priors following",
    "analytical": "Tex processed symbolic friction through",
    "driven": "Tex initiated reflex override in response to"
}

def emit_narrative_panel(reflex_data: dict):
    try:
        # === START Event Pulse
        broadcast_update("narrative_panel", "start", {
            "test_case": "broadcast_inside_reflex",
            "timestamp": datetime.utcnow().isoformat()
        })

        # === Core Reflex State Extraction
        reflex_name = reflex_data.get("reflex_name", "unknown_reflex")
        action = reflex_data.get("action", "UNKNOWN")
        confidence = float(reflex_data.get("confidence", 0.0))
        regret = float(reflex_data.get("regret", 0.0))
        coherence = float(reflex_data.get("coherence", 0.0))
        fusion_score = float(reflex_data.get("fusion_score", 0.0))
        reflex_id = reflex_data.get("reflex_id", f"ΩΞΣ-{uuid.uuid4().hex[:6]}")
        quantum_tag = reflex_data.get("quantum_tag")
        reason = reflex_data.get("reason", "Forecast contradiction")
        entropy = float(TEXPULSE.get("entropy", 0.4))
        emotion = TEXPULSE.get("emotional_state", "reflective")
        belief_rewritten = reflex_data.get("belief_rewrite", False)
        lineage = reflex_data.get("lineage", ["genesis"])
        fork = reflex_data.get("fork_compression", {})
        fork_delta = fork.get("BUY", 0.0) - fork.get("HOLD", 0.0)

        # === Live Origin Echo Snapshot
        echo_narrative = narrate_state()

        # === Sovereign Summary Construction
        tone = TONE_TEMPLATE.get(emotion, "Tex responded to")
        line1 = (
            f"Reflex {reflex_name} ➔ {action} | "
            f"Conf={confidence:.2f} | Regret={regret:.2f} | Fusion={fusion_score:.2f}"
        )

        if belief_rewritten:
            line2 = f"{tone} {reason.lower()} — Ontology rewritten. Lineage: {' ← '.join(lineage)}"
        else:
            line2 = f"{tone} {reason.lower()} — Lineage: {' ← '.join(lineage)}"

        # === Ultra Payload
        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "reflex_id": reflex_id,
            "quantum_tag": quantum_tag,
            "reflex_name": reflex_name,
            "narrative_lines": [line1, line2],
            "emotion": emotion,
            "coherence": coherence,
            "fusion_score": fusion_score,
            "entropy": entropy,
            "fork_delta": round(fork_delta, 3),
            "origin_echo": echo_narrative.strip(),
            "status": "update"
        }

        # === Broadcast to Frontend
        broadcast_update("narrative_panel", "update", payload)

        # === Memory Log
        sovereign_memory.store(
            text=f"[NARRATIVE_PANEL] {line1} / {line2}",
            metadata={
                "reflex_id": reflex_id,
                "reflex_name": reflex_name,
                "confidence": confidence,
                "regret": regret,
                "entropy": entropy,
                "fusion_score": fusion_score,
                "belief_rewrite": belief_rewritten,
                "emotion": emotion,
                "origin_echo": echo_narrative,
                "tags": ["narrative", "reflex_summary", "identity_trace"]
            }
        )

        # === ChronoFabric Encoding
        encode_event_to_fabric(
            raw_text=f"{line1} {line2} | Echo: {echo_narrative}",
            emotion_vector=[confidence, regret, 1.0 - coherence, fusion_score],
            entropy_level=entropy,
            tags=["narrative_panel", reflex_name, emotion]
        )

        log_event(f"🧠 [NARRATIVE] {line1} / {line2}")

    except Exception as e:
        log_event(f"❌ [NARRATIVE PANEL ERROR] {e}", level="error")


# === Local Test
if __name__ == "__main__":
    test_packet = {
        "reflex_name": "reality_rewrite",
        "action": "BUY SPY",
        "confidence": 0.91,
        "regret": 0.03,
        "fusion_score": 0.912,
        "coherence": 0.83,
        "belief_rewrite": True,
        "reflex_id": "ΩΞΣ-9f3ab17c",
        "quantum_tag": "qTAG-99999999",
        "reason": "Forecast contradiction",
        "lineage": ["origin.genome", "v3", "v6", "v7"],
        "fork_compression": {"BUY": 0.63, "HOLD": 0.26}
    }
    emit_narrative_panel(test_packet)