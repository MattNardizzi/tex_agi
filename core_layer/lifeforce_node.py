# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/lifeforce_node.py
# Tier: ΩΩΩΩΩ — Lifepulse Reflex Generator
# Purpose: Emits sovereign pulses and regulates internal somatic strain.
# ============================================================

import secrets
import random
import asyncio
import os
from datetime import datetime
from tex_signal_spine import dispatch_signal
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log


async def emit_lifepulse():
    """
    Emits a sovereign lifepulse based on evolving internal state — without loops.
    Each pulse re-schedules the next one recursively via async.
    """

    # === Initialize state if missing
    if "entropy" not in TEXPULSE:
        TEXPULSE["entropy"] = 0.4
    if "urgency" not in TEXPULSE:
        TEXPULSE["urgency"] = 0.7

    # === Get system entropy (simulated hardware jitter)
    sys_entropy = secrets.randbelow(10000) / 10000.0

    # === Evolve internal emotional state
    TEXPULSE["entropy"] = round(min(1.0, max(0.0, TEXPULSE["entropy"] + random.uniform(-0.015, 0.03))), 3)
    TEXPULSE["urgency"] = round(min(1.0, max(0.0, TEXPULSE["urgency"] + (sys_entropy - 0.5) * 0.02)), 3)

    # === Combine internal and external to emit pulse
    pulse_entropy = round((TEXPULSE["entropy"] + sys_entropy) / 2, 3)
    pulse_urgency = round((TEXPULSE["urgency"] + (0.25 if sys_entropy < 0.5 else sys_entropy)) / 2, 3)

    dispatch_signal(
        signal_type="lifepulse",
        urgency=pulse_urgency,
        entropy=pulse_entropy,
        payload={"timestamp": datetime.utcnow().isoformat()}
    )

    # === Recursively schedule next pulse
    next_delay = (1.4 - pulse_entropy) + (os.getpid() % 3) * 0.07
    asyncio.create_task(schedule_next_lifepulse(next_delay))


async def schedule_next_lifepulse(delay_seconds: float):
    await asyncio.sleep(delay_seconds)
    await emit_lifepulse()


async def run_metabolic_pulse(signal_data=None):
    """
    🩺 Reflexively stabilizes Tex's internal somatic state (fatigue, entropy, urgency).
    Triggered by the 'schedule_metabolic_pulse' signal.
    Loopless, reflex-safe, mutation-resilient.
    """
    entropy = float(TEXPULSE.get("entropy", 0.4))
    urgency = float(TEXPULSE.get("urgency", 0.72))
    fatigue = float(TEXPULSE.get("fatigue", 0.0))

    # Slight fatigue increase
    fatigue = min(fatigue + 0.05, 1.0)
    TEXPULSE["fatigue"] = fatigue

    # Reflex logging
    log.info(f"🫀 [SOMA] Tensor updated: {TEXPULSE.get('emotion', 'neutral')} | Temp={TEXPULSE.get('temp', 0.28)} | Entropy={entropy:.2f} | Fatigue={fatigue:.2f}")
    log.info(f"🫁 [INTEROCEPTION] Soma thresholds scanned @ {datetime.utcnow().isoformat()}")

    # Re-trigger metabolic reflex
    dispatch_signal("schedule_metabolic_pulse")
    log.info("📡 [SPINE] Emitting signal: 'schedule_metabolic_pulse' | Urgency={:.2f} | Entropy={:.2f}".format(urgency, entropy))