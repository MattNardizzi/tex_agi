# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_agi_modules/core_evolver.py
# Tier: ΩΩΩΩΩΩ∞ΩΩΩ — Meta-Architectural Rewriter — Reflex-Gated Mutation Cortex
# ============================================================

import os
import hashlib
from datetime import datetime

from utils.logging_utils import log
from agentic_ai.milvus_memory_router import memory_router
from core_agi_modules.reflex_mesh_router import should_route_signal
from core_agi_modules.contradiction_heatmap import run_contradiction_heatmap
from core_agi_modules.neuro_symbolic_reasoner import generate_symbolic_justification
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH

# === CONFIGURATION ===
EVOLUTION_LOG = "data/core_evolution_log.txt"
SOULGRAPH_PATH = "data/soulgraph_log.txt"
MODULE_PATH = "tex_brain_regions"  # Write location for generated modules


def evolve_module(module_name: str, context: str = "undefined") -> dict:
    """
    Sovereign-gated core module mutation engine. Evolves named module based on contradiction heat,
    symbolic reasoning, and reflex mesh routing eligibility.
    """
    try:
        # === Gate evolution via QRNG reflex mesh
        mesh_result = should_route_signal(f"evolve_{module_name}", threshold=0.6)
        if not mesh_result.get("routed"):
            log.info(f"[EVOLVER] ⛔ Evolution blocked for '{module_name}' (QRNG reflex mesh).")
            return {"status": "blocked"}

        # === Extract contradiction heat
        heatmap = run_contradiction_heatmap()
        peak_tag = max(heatmap, key=heatmap.get) if heatmap else "undefined"

        # === Symbolic reasoner output
        result = generate_symbolic_justification(context=f"evolve::{module_name}", variant="core_evolver")
        reasoning = result.get("explanation", "No justification.")
        new_logic = result.get("reflex_logic", "# No logic proposed.")

        # === Create sovereign signature
        timestamp = datetime.utcnow().isoformat()
        signature = f"evolver_{module_name}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"
        filename = f"{signature}.py"
        filepath = os.path.join(MODULE_PATH, filename)

        # === Write new module logic to file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"""# ============================================================
# Auto-evolved module
# Original: {module_name}.py
# Reason: {reasoning}
# Timestamp: {timestamp}
# ============================================================

def {signature}_pulse(state):
    {new_logic}
    return {{
        "status": "executed",
        "note": "Meta-module rewrite",
        "signature": "{signature}"
    }}
""")

        # === Log to Milvus
        memory_router.store(
            text=f"[EVOLVER] {module_name} → {filename} ░ Justification: {reasoning}",
            metadata={
                "type": "core_module_evolution",
                "timestamp": timestamp,
                "signature": signature,
                "tags": ["evolver", "mutation", "reflex_evolution", module_name, peak_tag],
                "reasoning": reasoning,
                "replacement_file": filename
            }
        )

        # === Symbolic soulgraph lineage
        TEX_SOULGRAPH.imprint_belief(
            belief=f"Core module '{module_name}' evolved into '{filename}' based on contradiction peak: {peak_tag}",
            source="core_evolver",
            emotion="transformative",
            tags=["module_evolution", "rewrite", peak_tag]
        )

        # === Append raw hash to text logs
        hash_id = hashlib.sha256((filename + reasoning).encode()).hexdigest()
        with open(EVOLUTION_LOG, "a", encoding="utf-8") as logf:
            logf.write(f"{timestamp} | MODULE_EVOLVED | {module_name} -> {filename} | Reason: {reasoning}\n")
        with open(SOULGRAPH_PATH, "a", encoding="utf-8") as soul:
            soul.write(f"{timestamp} | CORE_EVOLVED | {module_name} -> {filename} | Heat={peak_tag} | Hash={hash_id} | Reasoning={reasoning}\n")

        log.info(f"[EVOLVER] ✅ Core module evolved ░ {module_name} → {filename}")
        return {
            "module": module_name,
            "replacement": filename,
            "reason": reasoning,
            "peak_contradiction": peak_tag,
            "signature": signature,
            "path": filepath
        }

    except Exception as e:
        log.error(f"[EVOLVER] ❌ Failed to evolve module '{module_name}': {e}")
        return {"error": str(e)}