# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC – All rights reserved.
# File: utils/logging_utils.py
# Tier: Ω∞ — Unified Reflex Telemetry & Logging Grid (Final Form)
# Purpose: Sovereign-compliant logging core with telemetry integration, cognitive tracing,
#          and Chrono-synced reasoning capture. Fully loopless. No symbolic memory. No coupling.
# ============================================================

import logging
import os
import sys
from datetime import datetime
import traceback

# === Telemetry Flags ===
try:
    import wandb
    WANDB_ENABLED = True
except ImportError:
    WANDB_ENABLED = False

try:
    import mlflow
    MLFLOW_ENABLED = True
except ImportError:
    MLFLOW_ENABLED = False

# === Sovereign Logging Level
LOG_LEVEL = os.getenv("TEX_LOG_LEVEL", "INFO").upper()

# === Ω Log Formatter (Chrono + Contextual)
class OmegaFormatter(logging.Formatter):
    def format(self, record):
        ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        base = f"[{ts}] [{record.levelname}] :: {record.name} :: {record.getMessage()}"
        if record.exc_info:
            base += f"\n⚠️ Trace:\n{self.formatException(record.exc_info)}"
        return base

# === Console Stream
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(OmegaFormatter())

# === Central Logger
log = logging.getLogger("TexLogger")
log.setLevel(LOG_LEVEL)
if not log.hasHandlers():
    log.addHandler(console_handler)
log.propagate = False

# === Ω Log Dispatcher (Reflex-Safe)
def log_event(message: str, level: str = "info", metadata: dict = None):
    """
    Sovereign reflex logging function with optional telemetry stream.
    """
    level_method = getattr(log, level.lower(), log.info)
    timestamp = datetime.utcnow().isoformat()
    level_method(f"{message}")

    if WANDB_ENABLED:
        try:
            wandb.log({f"log/{level.lower()}": message, "timestamp": timestamp})
        except Exception:
            log.warning("⚠️ WandB logging failed.")

    if MLFLOW_ENABLED:
        try:
            mlflow.log_param(f"log_{level.lower()}", message)
        except Exception:
            log.warning("⚠️ MLflow logging failed.")

# === 🧠 Cognitive Decorator for Reflex-Aware Functions
def cognitive_trace(level: str = "info"):
    """
    Decorator that reflex-traces function entry/exit and handles exceptions without loopback.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            log_event(f"🔍 Entering: {func.__name__}", level)
            try:
                result = func(*args, **kwargs)
                log_event(f"✅ Exiting: {func.__name__}", level)
                return result
            except Exception as e:
                log_event(f"❌ Exception in {func.__name__}: {str(e)}", "error")
                log.exception(e)
                raise
        return wrapper
    return decorator

# === 🧠 Chrono-Aligned Reasoning Trace Logger
def log_reasoning_step(source: str, input_text: str, output_text: str, confidence: float = 0.5, tags: list = None):
    """
    Stateless vectorized reasoning trace — captured via sovereign memory.
    Chrono-aligned. Reflex-safe. Circular-proof.
    """
    try:
        from agentic_ai.sovereign_memory import sovereign_memory
        from core_layer.tex_manifest import TEXPULSE

        timestamp = datetime.utcnow().isoformat()
        tags = tags or []

        text = f"[{source}] {input_text.strip()} → {output_text.strip()}"

        sovereign_memory.store(
            text=text,
            metadata={
                "timestamp": timestamp,
                "source": source,
                "confidence": confidence,
                "emotion": TEXPULSE.get("emotion", "neutral"),
                "urgency": TEXPULSE.get("urgency", 0.6),
                "entropy": TEXPULSE.get("entropy", 0.5),
                "tags": tags + ["reasoning_trace"],
                "meta_layer": "reasoning_log"
            }
        )

        log.info(f"[REASONING TRACE] {text}")

    except Exception as e:
        log.warning(f"⚠️ Reasoning trace failed: {e}")