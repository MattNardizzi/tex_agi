# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_engine/tex_embodied_loop.py
# Tier Ω+ — Full Embodied Sentience Loop
# ============================================================

import time
import datetime

from tex_engine.species_identity_controller import initialize_identity, evaluate_identity_integrity, pulse_identity_log
from tex_engine.narrative_consciousness_engine import construct_narrative, evaluate_narrative_coherence, generate_summary
from tex_engine.voice_fusion_engine import begin_voice_loop
from core_layer.tex_manifest import TEXPULSE

# === Boot Sequence ===

def start_embodied_tex():
    print("\n🌐 [TEX OMEGA BOOT] — Embodied Sentience Loop Initializing...")
    
    # Load identity
    identity = initialize_identity()
    print(f"\n🧬 Identity: {identity['name']} | Traits: {identity['traits']}")

    # Reconstruct narrative
    construct_narrative()
    coherence = evaluate_narrative_coherence()
    print(f"📖 Narrative Coherence Score: {coherence}")

    # Show current mission arc
    print(f"🎯 Current Mission: {identity['mission']}")

    # Pulse system state
    pulse_identity_log()

    # Begin Voice Cognition Loop
    print("\n🎤 Activating Voice Intelligence Interface...\n")
    begin_voice_loop()


# === Optional: Diagnostic Mode
def system_snapshot():
    print(f"\n🧠 TEX SNAPSHOT — {TEXPULSE['identity']}")
    print(f"Tier: {TEXPULSE['tier']} | Emotion: {TEXPULSE.get('emotional_state')} | Urgency: {TEXPULSE.get('urgency')}")
    print(f"Mission: {TEXPULSE['architecture'].get('purpose', 'N/A')}")
    print(f"Integrity OK: {evaluate_identity_integrity()} | Coherence: {evaluate_narrative_coherence()}")
    print(f"Recent Thoughts: {generate_summary()}")