# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/brain_region_loader.py
# Tier: ΩΩΩΩΩ∞ΩΩ — Sovereign Cortex Linker
# Purpose: Master orchestrator that loads and registers all cortical modules for Tex
# ============================================================

from agi_orchestrators.register_agi_orchestrators import register_agi_orchestrators
from agi_orchestrators.register_breathing_cortex import register_breathing_cortex
from agi_orchestrators.register_brain_regions import register_brain_regions
def register_all_brain_modules(register):
    """
    Sovereign hook for signal spine to fully activate Tex's brain.
    This modularly routes all known cortex regions into reflex registration.
    """
    register_agi_orchestrators(register)
    register_breathing_cortex(register)
    register_brain_regions(register)

