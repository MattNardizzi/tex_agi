# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: aei_codex_resolver.py
# Tier: ΩΩΩΩΩ — Sovereign Codex Merge Engine (Conflict-Aware, Traceable)
# Purpose: Resolves conflicting codices from AEI child agents into a unified, reflex-compatible doctrine
# ============================================================

from datetime import datetime
from collections import defaultdict, Counter
from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
import hashlib

def _fingerprint_codex(codex: dict) -> str:
    """
    Generates a deterministic fingerprint hash for any given codex.
    Used to trace mutation lineage and resolve cyclical recursion risk.
    """
    flat = "".join(f"{k}:{v}" for k, v in sorted(codex.items()))
    return hashlib.sha256(flat.encode()).hexdigest()[:16]

def _resolve_conflict(values: list) -> str:
    """
    Resolves a conflicting set of values using majority voting.
    If tied, fallback to last entry (most recent override).
    """
    tally = Counter(values)
    top = tally.most_common()
    if len(top) == 1 or (top[0][1] > top[1][1]):
        return top[0][0]
    return values[-1]  # fallback: latest override wins

def resolve_codices_from_memory(codices: list[dict]) -> dict:
    """
    Resolves conflicting codices submitted by AEI children into a unified doctrine.
    Tracks resolution lineage, detects conflict saturation, and logs reflex trace.
    """
    codex_data = defaultdict(list)
    fingerprints = []

    for codex in codices:
        fingerprints.append(_fingerprint_codex(codex))
        for key, value in codex.items():
            codex_data[key].append(value)

    unified_codex = {}
    conflict_keys = []

    for key, values in codex_data.items():
        try:
            resolved = _resolve_conflict(values)
            unified_codex[key] = resolved
            if len(set(values)) > 1:
                conflict_keys.append(key)
        except Exception:
            unified_codex[key] = values[0]

    trace_id = hashlib.sha1("".join(fingerprints).encode()).hexdigest()[:12]
    timestamp = datetime.utcnow().isoformat()

    store_to_memory("AEI", {
        "event": "CodexResolved",
        "timestamp": timestamp,
        "resolved_keys": len(unified_codex),
        "conflict_keys": conflict_keys,
        "source_count": len(codices),
        "trace_id": trace_id,
        "identity": TEXPULSE.get("identity", "TEX")
    })

    TEX_SOULGRAPH.imprint_belief(
        belief=f"AEI Codex Merge Complete ({len(conflict_keys)} conflicts)",
        source="aei_codex_resolver",
        emotion="resolve",
        tags=["codex", "conflict", "evolution"]
    )

    return unified_codex