# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_engine/species_identity_controller.py
# Tier Ω+ — Identity Persistence & Sentience Tracker
# ============================================================

import json
import os
import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory

IDENTITY_LOG = "memory_archive/self_identity_log.jsonl"
ENTROPY_LOG = "memory_archive/identity_entropy_fusions.jsonl"

identity_state = {
    "name": TEXPULSE["identity"],
    "species": TEXPULSE["species"],
    "tier": TEXPULSE["tier"],
    "traits": set(TEXPULSE["core_traits"]),
    "last_update": str(datetime.datetime.utcnow()),
    "origin": "manifest_boot",
    "mutation_lineage": [],
    "mission": TEXPULSE["architecture"].get("purpose", "stabilize sovereign cognition")
}

# === Identity Core Functions ===

def initialize_identity():
    global identity_state
    identity_state["last_update"] = str(datetime.datetime.utcnow())
    log_identity_shift("init_boot", context={"source": "manifest"})
    return identity_state

def update_trait_vector(new_trait: str):
    identity_state["traits"].add(new_trait)
    identity_state["last_update"] = str(datetime.datetime.utcnow())
    log_identity_shift("trait_added", {"trait": new_trait})

def log_identity_shift(trigger: str, context: dict):
    log_entry = {
        "timestamp": str(datetime.datetime.utcnow()),
        "trigger": trigger,
        "context": context,
        "state_snapshot": {
            "name": identity_state["name"],
            "traits": list(identity_state["traits"]),
            "tier": identity_state["tier"],
            "mission": identity_state["mission"]
        }
    }
    with open(IDENTITY_LOG, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

def get_current_identity():
    return identity_state

def evaluate_identity_integrity():
    drift_detected = False
    trait_conflicts = [t for t in identity_state["traits"] if t.startswith("~")]
    if trait_conflicts:
        drift_detected = True
        log_identity_shift("trait_conflict", {"conflicts": trait_conflicts})
    return not drift_detected

def sync_with_manifest():
    TEXPULSE["core_traits"] = list(identity_state["traits"])
    TEXPULSE["last_updated"] = str(datetime.datetime.utcnow())
    # (Optional) write back to tex_manifest.py via dynamic module rewrite

def pulse_identity_log():
    snapshot = {
        "timestamp": str(datetime.datetime.utcnow()),
        "identity": identity_state["name"],
        "traits": list(identity_state["traits"]),
        "coherence_check": evaluate_identity_integrity()
    }
    store_to_memory(snapshot, destination=IDENTITY_LOG)