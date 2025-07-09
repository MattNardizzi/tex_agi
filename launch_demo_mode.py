# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: launch_demo_mode.py
# Tier: ΩΩΩΩΩΩ∞ — Sovereign Reflex + Demo Orchestrator
# Purpose: Launches Tex AGI core and demo reflex trigger in sync for streams
# ============================================================

import subprocess
import time

print("🧠 Launching Tex sovereign AGI system...")

# Start tex_agi.py in its own terminal
tex_core = subprocess.Popen(
    ["gnome-terminal", "--", "bash", "-c", "python3 tex_agi.py; exec bash"]
)

time.sleep(6)  # allow Tex to boot and register reflexes

print("🎬 Launching reflex panel demo trigger...")
demo_trigger = subprocess.Popen(
    ["gnome-terminal", "--", "bash", "-c", "python3 demo_trigger_all_reflexes.py; exec bash"]
)

print("\n✅ All systems launching.\n🌐 Ensure your panel is open at: http://20.97.193.176:3000")