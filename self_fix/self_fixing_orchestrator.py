# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: self_fix/self_fixing_orchestrator.py
# Tier: ∞ΩΩΩ∞∞ — Sovereign Self-Repair Cortex
# Purpose: Master controller for Tex’s self-repair reflex system. Repairs reflexes, agents, forks, and internal modules.
# ============================================================

from utils.logging_utils import log_event
from agentic_ai.sovereign_memory import sovereign_memory

# === Module Imports
from self_fix.error_reflex_catcher import capture_failure_context
from self_fix.reflex_auditor import analyze_faulty_module
from self_fix.code_shape_analyzer import extract_semantic_signature
from self_fix.patch_generator import generate_symbolic_patch
from self_fix.patch_installer import install_patch
from self_fix.patch_ledger import log_patch_event
from self_fix.self_patch_rewriter import rewrite_self_fixing_logic  # only used if patch fails

# === Main Orchestrator Entry
def route_self_repair(signal):
    signal_type = signal.get("type", "")
    context = signal.get("payload", {})

    log_event(f"🛠 [SELF-FIX ORCHESTRATOR] Signal received: {signal_type} → Dispatching to repair system.")

    # === Step 1: Capture Reflex Failure Context
    fault_info = capture_failure_context(context)

    if not fault_info or "filepath" not in fault_info:
        log_event("❌ [SELF-FIX] Invalid or missing fault context — repair aborted.", level="error")
        return

    # === Step 2: Audit the Code
    audit_report = analyze_faulty_module(fault_info)
    if audit_report.get("status") != "corrupted":
        log_event(f"✅ [SELF-FIX] Audit passed — no repair needed for {fault_info['module']}")
        return

    # === Step 3: Semantic Signature Extraction
    semantic_data = extract_semantic_signature(fault_info)

    # === Step 4: Patch Proposal Generation
    patch = generate_symbolic_patch(fault_info, audit_report, semantic_data)
    if not patch:
        log_event("❌ [SELF-FIX] Patch generation failed. Triggering fallback...", level="error")
        rewrite_self_fixing_logic(origin_module=fault_info.get("module"))
        return

    # === Step 5: Install Patch
    success = install_patch(patch)
    if not success:
        log_event("❌ [SELF-FIX] Patch installation failed — escalating.", level="critical")
        rewrite_self_fixing_logic(origin_module=patch.get("target_module"))
        return

    # === Step 6: Ledger + Memory Sync
    log_patch_event(patch)

    sovereign_memory.store(
        text=f"Reflex `{patch['target_module']}` was auto-repaired and updated.",
        metadata={
            "tags": ["self_fix", "reflex_repair", "patch_event"],
            "urgency": 0.8,
            "entropy": 0.3,
            "meta_layer": "self_fixing_orchestrator"
        }
    )

    log_event(f"✅ [SELF-FIX] Patch installed and logged for `{patch['target_module']}`.")