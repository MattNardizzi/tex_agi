# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: reflex_wrappers/reflex_dispatcher.py
# Tier: ΩΩΩΩΩ∞∞ — Reflex Wrapper Dispatcher (Hybrid Async-Sync Execution)
# Purpose: Executes Tex signal reflexes without blocking async event loop,
#          preserving loopless spike-driven architecture.
# ============================================================

import asyncio
import inspect
from datetime import datetime

from tex_signal_spine import signal_registry
from utils.logging_utils import log
from core_layer.soma_tensor import register_reflex_strain
from core_layer.tex_manifest import TEXPULSE
from core_layer.quantum_seeder import inject_quantum_spark
from real_time_engine.ably_broadcast import broadcast_update

# === Hybrid Reflex Dispatcher ===
async def dispatch_signal(signal_type: str, payload: dict = None, urgency: float = None, entropy: float = None, source: str = "external"):
    if entropy is None:
        await inject_quantum_spark()
        entropy = TEXPULSE.get("entropy", 0.4)

    signal = {
        "type": signal_type,
        "payload": payload or {},
        "urgency": urgency or TEXPULSE.get("urgency", 0.6),
        "entropy": entropy,
        "source": source,
        "timestamp": datetime.utcnow().isoformat()
    }

    log.info(f"📡 [REFLEX DISPATCHER] Emitting: '{signal_type}' | Urgency={signal['urgency']} | Entropy={signal['entropy']}")

    broadcast_update("spine", signal_type, {
        "urgency": signal["urgency"],
        "entropy": signal["entropy"],
        "source": signal["source"],
        "timestamp": signal["timestamp"],
        "tags": signal.get("payload", {}).get("tags", []),
        "summary": signal.get("payload", {}).get("summary", "")
    })

    if signal_type not in signal_registry:
        log.warning(f"⚠️ No reflex handlers registered for: '{signal_type}'")
        return

    register_reflex_strain()

    for handler in signal_registry[signal_type]:
        try:
            print(f"📣 [WRAPPER] Triggering reflex: '{signal_type}' → {handler.__name__}")

            if inspect.iscoroutinefunction(handler):
                asyncio.create_task(handler(signal))  # async def
            else:
                loop = asyncio.get_running_loop()
                loop.run_in_executor(None, handler, signal)  # def

        except Exception as e:
            log.error(f"❌ Reflex handler error in '{signal_type}': {e}")