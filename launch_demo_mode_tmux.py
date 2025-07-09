# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: launch_demo_mode_tmux.py
# Tier: ∞∞∞∞∞ΩΩ — Server-Safe Reflex Demo Launcher (tmux-based)
# Purpose: Launches Tex AGI and demo reflex trigger in parallel
# ============================================================

import subprocess
import time

session_name = "tex_demo_mode"

print(f"🧠 Launching Tex sovereign AGI system in tmux session: {session_name}")

# Kill any existing session with the same name to avoid conflict
subprocess.run(["tmux", "kill-session", "-t", session_name], stderr=subprocess.DEVNULL)

# Start Tex core in the first tmux window
subprocess.run([
    "tmux", "new-session", "-d", "-s", session_name, "python3 tex_agi.py"
])

# Wait longer to ensure full AGI initialization
print("⏳ Waiting for Tex to finish ignition and register all reflex handlers...")
time.sleep(18)

# Launch the reflex showcase script in a split pane
print("🎬 Triggering demo reflex sequence...")
subprocess.run([
    "tmux", "split-window", "-t", session_name, "-v", "python3 demo_trigger_all_reflexes.py"
])
subprocess.run(["tmux", "select-layout", "-t", session_name, "tiled"])

# Attach to the session so user sees both panes
print("🟢 Attaching to tmux session for live monitoring...")
subprocess.run(["tmux", "attach-session", "-t", session_name])