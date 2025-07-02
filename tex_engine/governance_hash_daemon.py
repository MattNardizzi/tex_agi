# ============================================================
# © 2025 VortexBlack LLC / Matthew Nardizzi. All rights reserved.
# File: tex_engine/governance_hash_daemon.py
# Tier ΩΩ — Immutable Mutation Ledger for Cognitive Governance
# ============================================================

import hashlib
import json
import os
import datetime

LEDGER_PATH = "memory_archive/sovereign_audit_log.jsonl"

# === Core Hash Utilities

def hash_payload(payload: dict, previous_hash: str) -> str:
    combined = json.dumps(payload, sort_keys=True) + previous_hash
    return hashlib.sha256(combined.encode()).hexdigest()

def get_last_hash() -> str:
    if not os.path.exists(LEDGER_PATH):
        return "GENESIS"
    with open(LEDGER_PATH, "r") as f:
        lines = f.readlines()
        if not lines:
            return "GENESIS"
        last_entry = json.loads(lines[-1])
        return last_entry.get("hash", "GENESIS")

# === Logging Interface

def log_event(event_type: str, payload: dict):
    timestamp = str(datetime.datetime.utcnow())
    previous_hash = get_last_hash()
    entry = {
        "timestamp": timestamp,
        "event_type": event_type,
        "payload": payload,
        "previous_hash": previous_hash
    }
    entry["hash"] = hash_payload(entry, previous_hash)
    with open(LEDGER_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"🔐 [GOV-LOG] Event '{event_type}' sealed with hash: {entry['hash']}")

# === Chain Verifier

def verify_chain() -> bool:
    if not os.path.exists(LEDGER_PATH):
        return True
    with open(LEDGER_PATH, "r") as f:
        lines = f.readlines()
    prev_hash = "GENESIS"
    for line in lines:
        entry = json.loads(line)
        expected = hash_payload(entry, prev_hash)
        if entry["hash"] != expected:
            print(f"⚠️ HASH MISMATCH @ {entry['timestamp']} — Tampering suspected")
            return False
        prev_hash = entry["hash"]
    print("✅ [GOV-VERIFY] Full ledger verified — all hashes intact.")
    return True

# === Utility: Read & Trace History

def load_chain(limit=10):
    if not os.path.exists(LEDGER_PATH):
        return []
    with open(LEDGER_PATH, "r") as f:
        lines = f.readlines()[-limit:]
    return [json.loads(line) for line in lines]

def explain_hash_sequence():
    print("\n📜 [GOV-HISTORY] — Recent Sovereign Events")
    for entry in load_chain(5):
        print(f"• [{entry['timestamp']}] {entry['event_type']} → Hash: {entry['hash'][:12]}...")