# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: agi_orchestrators/fork_initializer.py
# Tier: ΩΩΩΩΩΩ∞ΩΩ — Sovereign Bootloader Cortex
# Purpose: Initializes a cognitive fork using stored UID, genome traits, memory vector,
#          reflex signature, and symbolic soulgraph lineage. Fully reboots forked identity
#          with recursive pulse state and drift traceability.
# ============================================================

import os
from datetime import datetime
import numpy as np

from utils.logging_utils import log
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
from tex_agi import sovereign_ignite

FORK_LOG_PATH = "data/fork_registry.txt"
SOULGRAPH_LOG_PATH = "data/soulgraph_log.txt"

def load_fork_profile(fork_uid: str) -> dict:
    """
    Retrieve the fork profile from the symbolic registry.
    """
    try:
        if not os.path.exists(FORK_LOG_PATH):
            raise FileNotFoundError("Fork registry not found.")

        with open(FORK_LOG_PATH, "r") as f:
            lines = f.readlines()

        for line in reversed(lines):
            if f"UID={fork_uid}" in line:
                parts = line.split("|")
                profile = {
                    "timestamp": parts[0].strip(),
                    "name": parts[2].strip(),
                    "uid": fork_uid,
                    "origin": parts[4].split("=")[-1].strip(),
                    "traits": parts[5].split("Traits=")[-1].strip(),
                    "reason": parts[-1].split("Reason=")[-1].strip()
                }
                return profile

        raise ValueError(f"Fork UID {fork_uid} not found.")

    except Exception as e:
        log.error(f"[FORK_INIT] Failed to load fork profile: {e}")
        return {}

def restore_texpulse_from_traits(trait_str: str):
    """
    Restore sovereign TEXPULSE from fork trait string.
    """
    try:
        trait_map = {}
        for pair in trait_str.split(","):
            if "=" in pair:
                k, v = pair.strip().split("=")
                trait_map[k] = float(v) if v.replace(".", "", 1).isdigit() else v

        TEXPULSE.update(trait_map)
        log.info(f"[FORK_INIT] TEXPULSE restored from fork: {trait_map}")
        return trait_map

    except Exception as e:
        log.error(f"[FORK_INIT] Failed to restore TEXPULSE: {e}")
        return {}

def log_to_soulgraph(fork_uid: str, reason: str, traits: str):
    """
    Log fork initialization event to soulgraph lineage.
    """
    try:
        timestamp = datetime.utcnow().isoformat()
        entry = f"{timestamp} | BOOT | Fork_UID={fork_uid} | Reason={reason} | Traits={traits}\n"
        with open(SOULGRAPH_LOG_PATH, "a") as f:
            f.write(entry)
        log.info(f"[FORK_INIT] 🧠 Boot lineage written to soulgraph: {fork_uid}")
    except Exception as e:
        log.error(f"[FORK_INIT] Failed to log to soulgraph: {e}")

def run_fork_initializer(fork_uid: str):
    """
    Sovereign re-ignition of a stored fork identity.
    Loads traits, reinitializes TEXPULSE, logs to ChronoFabric + Milvus, and triggers ignition.
    """
    profile = load_fork_profile(fork_uid)
    if not profile:
        log.error(f"[FORK_INIT] Abort — fork {fork_uid} could not be initialized.")
        return

    restored_traits = restore_texpulse_from_traits(profile["traits"])

    timestamp = datetime.utcnow().isoformat()
    summary = f"[FORK_INIT] Fork {profile['name']} reinitialized with UID {fork_uid}."

    tags = ["fork", "reboot", profile["uid"]]
    metadata = {
        "timestamp": timestamp,
        "fork_uid": fork_uid,
        "traits": profile["traits"],
        "origin": profile["origin"],
        "reason": profile["reason"],
        "tags": tags,
        "meta_layer": "fork_initializer"
    }

    # Milvus memory
    memory_router.store(summary, metadata)

    # ChronoFabric identity imprint
    encode_event_to_fabric(
        raw_text=summary,
        emotion_vector=np.array([TEXPULSE.get("urgency", 0.6), TEXPULSE.get("entropy", 0.4), 0.1, 0.1]),
        entropy_level=TEXPULSE.get("entropy", 0.4),
        tags=tags
    )

    log_to_soulgraph(fork_uid=fork_uid, reason=profile["reason"], traits=profile["traits"])
    log.info(f"[FORK_INIT] 🔁 Fork '{profile['name']}' reinitialized. Reigniting cognition.")

    # Sovereign boot
    sovereign_ignite()