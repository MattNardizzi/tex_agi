# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/system_monitor.py
# Tier: ΩΩΩ++ — Reflex-Linked Resource Monitoring w/ Chrono + Override Hooks
# Purpose: Monitor real-time system load, log into fused memory, trigger override when critical.
# ============================================================

import psutil
import GPUtil
import time
from datetime import datetime
from agentic_ai.sovereign_memory import SovereignMemory
from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
from core_agi_modules.sovereign_core.override_hooks import trigger_sovereign_override
from tex_signal_spine import dispatch_signal

# === Collect system diagnostics from CPU, RAM, GPU, and power ===
def collect_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    gpus = GPUtil.getGPUs()
    gpu_load = round(gpus[0].load * 100, 2) if gpus else None
    gpu_temp = round(gpus[0].temperature, 2) if gpus and hasattr(gpus[0], 'temperature') else None

    battery = psutil.sensors_battery()
    battery_pct = battery.percent if battery else None
    power_plugged = battery.power_plugged if battery else None

    return {
        "cpu": cpu,
        "ram": ram,
        "gpu_load": gpu_load,
        "gpu_temp": gpu_temp,
        "battery_pct": battery_pct,
        "power_plugged": power_plugged
    }

# === Sovereign Metabolic Monitor Loop ===
def metabolic_loop(interval=60):
    while True:
        try:
            now = datetime.utcnow().isoformat()
            metrics = collect_system_metrics()
            heat = round(max(metrics["cpu"], metrics["ram"]) / 100, 4)

            # === Dual-memory log: vector + chrono ===
            SovereignMemory.write(
                text="🧠 System metabolism check",
                metadata={
                    "type": "system_diagnostics",
                    "tags": ["system", "metabolism", "resource_reflex"],
                    "emotion": "monitoring",
                    "trust_score": 0.91,
                    "heat": heat,
                    "prediction": "system load stable",
                    "actual": f"CPU={metrics['cpu']}%, RAM={metrics['ram']}%",
                    "timestamp": now,
                    **metrics
                }
            )

            SovereignMemory.entangle(
                event="Metabolism reading",
                vector=[metrics["cpu"], metrics["ram"], metrics.get("gpu_load") or 0, heat],
                tags=["system", "diagnostics", "pulse"]
            )

            # === Belief update in Soulgraph ===
            TEX_SOULGRAPH.imprint_belief(
                belief=f"System state: CPU={metrics['cpu']}% | RAM={metrics['ram']}%",
                source="system_monitor",
                emotion="monitoring",
                tags=["system", "status", "vitals"]
            )

            # === Reflex Override if overload detected ===
            if metrics["cpu"] > 90 or metrics["ram"] > 90:
                print("⚠️ [METABOLIC ALERT] CPU or RAM strain threshold exceeded.")

                SovereignMemory.write(
                    text="🔥 Metabolic overload trigger",
                    metadata={
                        "type": "override_trigger",
                        "urgency": 1.0,
                        "emotion": "alert",
                        "heat": 0.95,
                        "source": "system_monitor",
                        "tags": ["override", "strain", "reflex"],
                        "timestamp": now
                    }
                )

                trigger_sovereign_override(
                    cognitive_event={"input": "Metabolic overload detected", "timestamp": now},
                    reason="metabolic_drift",
                    heat=0.95
                )

                dispatch_signal("tension_alert", {
                    "origin": "system_monitor",
                    "summary": "CPU or RAM usage exceeded 90%",
                    "metrics": metrics
                }, urgency=1.0, entropy=0.6, source="reflex_nervous_system")

            # === Console status print ===
            print(f"🩺 [METABOLISM] CPU={metrics['cpu']}% RAM={metrics['ram']}% GPU={metrics.get('gpu_load')}%")

            time.sleep(interval)

        except Exception as e:
            print(f"[SYSTEM MONITOR ERROR] {e}")
            time.sleep(10)