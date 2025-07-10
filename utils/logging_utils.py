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

# === Ω Log Formatter (Chrono + Contextual) — Fully Reflex Safe
class OmegaFormatter(logging.Formatter):
    def format(self, record):
        ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        try:
            message = record.getMessage()
        except Exception as e:
            message = f"[FORMAT ERROR] {repr(e)}"
        try:
            base = f"[{ts}] [{record.levelname}] :: {record.name} :: {str(message)}"
        except Exception as e:
            base = f"[{ts}] [{record.levelname}] :: {record.name} :: [STR CONVERSION FAIL: {repr(e)}]"
        if record.exc_info:
            try:
                base += f"\n⚠️ Trace:\n{self.formatException(record.exc_info)}"
            except Exception as e:
                base += f"\n⚠️ Trace format error: {repr(e)}"
        return base

# === Console Stream
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(OmegaFormatter())

# === Safe Logger Patch (Accepts Any Type)
class SafeLogger(logging.Logger):
    def info(self, msg, *args, **kwargs):
        super().info(str(msg), *args, **kwargs)
    def warning(self, msg, *args, **kwargs):
        super().warning(str(msg), *args, **kwargs)
    def error(self, msg, *args, **kwargs):
        super().error(str(msg), *args, **kwargs)
    def debug(self, msg, *args, **kwargs):
        super().debug(str(msg), *args, **kwargs)
    def critical(self, msg, *args, **kwargs):
        super().critical(str(msg), *args, **kwargs)
    def exception(self, msg, *args, **kwargs):
        super().exception(str(msg), *args, **kwargs)

logging.setLoggerClass(SafeLogger)

# === Central Logger
log = logging.getLogger("TexLogger")
log.setLevel(LOG_LEVEL)
if not log.hasHandlers():
    log.addHandler(console_handler)
log.propagate = False

# === Ω Log Dispatcher (Fully Safe Reflex Logging)
def log_event(message, level: str = "info", metadata: dict = None):
    """
    Sovereign reflex logging function with optional telemetry stream.
    Bulletproof against non-string input and runtime exceptions.
    """
    try:
        safe_message = str(message)
        timestamp = datetime.utcnow().isoformat()
        level_method = getattr(log, level.lower(), log.info)

        # Core Logging
        level_method(safe_message)

        # Optional Telemetry
        if WANDB_ENABLED:
            try:
                wandb.log({f"log/{level.lower()}": safe_message, "timestamp": timestamp})
            except Exception:
                log.warning("⚠️ WandB logging failed.")

        if MLFLOW_ENABLED:
            try:
                mlflow.log_param(f"log_{level.lower()}", safe_message)
            except Exception:
                log.warning("⚠️ MLflow logging failed.")

    except Exception as logging_failure:
        print("❌ [LOGGING SYSTEM FAILURE]", str(logging_failure))
        print("🪵 [FAILED LOG MESSAGE]", repr(message))

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
        print("🔥 HARD FAIL — EXCEPTION CAUGHT DURING log_reasoning_step")
        traceback.print_exc()
        log_event(f"❌ [REASONING TRACE ERROR]: {repr(e)}", level="error")