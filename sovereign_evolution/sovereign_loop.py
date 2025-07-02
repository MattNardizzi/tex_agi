"""
Ω-tier Module: sovereign_loop.py
Author: Sovereign Cognition / Tex
Purpose: Sovereign Cognition Audit Loop — Reflexive override evaluation + strategic coherence validation
"""

import json
import os
import time
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import recall_agent_memory, store_to_memory
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override

# === File paths ===
OVERRIDE_PATH = "memory_archive/sovereign_overrides.jsonl"
AUDIT_LOG_PATH = "memory_archive/sovereign_audit_log.jsonl"
os.makedirs("memory_archive", exist_ok=True)

# === Main audit logic ===
def run_sovereign_loop_once():
    try:
        print("\n🧠 [SOVEREIGN LOOP] Running sovereign cognition audit...")

        if not os.path.exists(OVERRIDE_PATH):
            print("[SOVEREIGN LOOP] No override history found.")
            return

        with open(OVERRIDE_PATH, "r") as f:
            overrides = [json.loads(line) for line in f if line.strip()]

        if not overrides:
            print("[SOVEREIGN LOOP] Override log is empty.")
            return

        last = overrides[-1]
        last_score = last.get("override_score", 0.0)
        last_cycle = last.get("cycle", 0)

        # === Memory coherence snapshot ===
        recent_memory = recall_agent_memory("tex", n=5)
        recent_coherence = [
            m.get("coherence") for m in recent_memory
            if isinstance(m.get("coherence"), (int, float)) and m.get("coherence") > 0.05
        ]

        avg_coherence = round(sum(recent_coherence) / len(recent_coherence), 3) if recent_coherence else 0.12
        status = "successful" if avg_coherence >= 0.7 else "needs_followup"

        # === Audit report ===
        audit = {
            "timestamp": datetime.utcnow().isoformat(),
            "last_override_cycle": last_cycle,
            "last_override_score": last_score,
            "avg_recent_coherence": avg_coherence,
            "status": status,
            "recommendation": "continue_path" if status == "successful" else "re-evaluate logic"
        }

        with open(AUDIT_LOG_PATH, "a") as f:
            f.write(json.dumps(audit) + "\n")

        store_to_memory("sovereign_audit", audit)

        print(f"[SOVEREIGN LOOP] ✅ Audit complete → Avg Coherence: {avg_coherence} → Status: {status}")

        if status == "needs_followup":
            print("[SOVEREIGN LOOP] 🔁 Override reflex re-engaging...")
            result = trigger_sovereign_override(context="sovereign_loop_auto", force=True)
            print(f"[SOVEREIGN LOOP] Result: {result.get('status')} | Insight: {result.get('counterfactual', {}).get('counterfactual')}")

    except Exception as e:
        print(f"[SOVEREIGN LOOP ERROR] ❌ {e}")


# === Background (timed) sovereign thread ===
def launch_sovereign_loop_thread(interval_seconds=180):
    import threading

    def loop():
        while True:
            run_sovereign_loop_once()
            time.sleep(interval_seconds)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()
    print("✅ [SOVEREIGN LOOP] Reflection thread started (every", interval_seconds, "seconds)")


# === Reflex-compatible event hook ===
def sovereign_loop_event_handler(event):
    print(f"[SOVEREIGN REFLEX] 🧠 Triggered by event: {event.event_type}")
    run_sovereign_loop_once()