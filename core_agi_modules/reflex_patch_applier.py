# ============================================================
# © 2025 VortexBlack LLC / Sovereign Cognition
# File: core_agi_modules/reflex_patch_applier.py
# Tier ΩΩΩΩΩ∞++ — Reflex Mutation Pipeline + Predictive Feedback + Lineage Trace + Override Cascade
# ============================================================

from tex_goal_reflex.goal_reflex import apply_goal_reflex_patch
from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE
from datetime import datetime

# Handler registry for patchable reflex modules
PATCH_HANDLERS = {
    "goal_reflex": apply_goal_reflex_patch
}

# In-memory patch log for deduplication and mutation history
PATCH_LOG = []

def has_been_applied_before(module: str, patch: dict) -> bool:
    """
    Check if an identical patch has already been applied.
    """
    return any(p["module"] == module and p["patch"] == patch for p in PATCH_LOG)

def apply_patch(target_module: str, patch: dict):
    """
    Applies a patch to a reflex subsystem and logs the outcome with emotion,
    urgency, reflex score, and predictive outcome metadata.
    """
    timestamp = datetime.utcnow().isoformat()

    if has_been_applied_before(target_module, patch):
        print(f"[PATCH] 🔁 Patch already applied to {target_module}. Skipping.")
        return

    if target_module in PATCH_HANDLERS:
        PATCH_HANDLERS[target_module](patch)
        PATCH_LOG.append({"module": target_module, "patch": patch, "timestamp": timestamp})

        predicted_outcome = {
            "coherence_gain": 0.05,         # Placeholder
            "alignment_score": 0.9          # Placeholder
        }

        store_to_memory("reflex_patch_applied", {
            "module": target_module,
            "patch": patch,
            "timestamp": timestamp,
            "source": "reflex_patch_applier",
            "reversible": patch.get("reversible", True),
            "reflex_score": TEXPULSE.get("reflex_score", 0.66),
            "emotion": TEXPULSE.get("emotional_state", "neutral"),
            "urgency": TEXPULSE.get("urgency", 0.5),
            "entropy": TEXPULSE.get("entropy", 0.5),
            "trust_score": TEXPULSE.get("trust_score", 0.8),
            "lineage_trace": TEXPULSE.get("fork_lineage", []),
            "mutation_id": TEXPULSE.get("mutation_signature", {}).get("id", "none"),
            "predicted_outcome": predicted_outcome
        })

        # Reflex state trace
        TEXPULSE["last_patch_zone"] = target_module
        TEXPULSE["last_patch_time"] = timestamp

        print(f"[PATCH] ✅ Applied patch to {target_module}: {patch}")

        # Optional: Entropy-aware revert trigger
        if patch.get("reversible") and TEXPULSE.get("entropy", 0.9) > 0.85:
            print(f"[PATCH] 🧨 High entropy detected — consider reverting patch on {target_module}.")

    else:
        print(f"[PATCH] ⚠️ No handler found for module '{target_module}'")

def listen_and_apply_patch(feedback_vector: dict):
    """
    Listens for reflex patch feedback and conditionally applies mutation based on urgency
    or sovereign override.
    """
    if feedback_vector.get("suggested_patch"):
        emotion = TEXPULSE.get("emotional_state", "neutral")
        urgency = TEXPULSE.get("urgency", 0.5)
        print(f"[PATCH] 🎯 Suggested patch received — urgency={urgency}, emotion={emotion}")

        if TEXPULSE.get("reflex_override") == "force_patch":
            print("[PATCH] 🔐 Sovereign override activated — forcing patch application.")
            apply_patch(
                feedback_vector.get("target_module"),
                feedback_vector.get("patch", {})
            )
            return

        if urgency >= 0.6:
            apply_patch(
                feedback_vector.get("target_module"),
                feedback_vector.get("patch", {})
            )
        else:
            print("[PATCH] ⚠️ Patch urgency below execution threshold — deferred.")