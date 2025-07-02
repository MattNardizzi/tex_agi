# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC
# File: core_schemas/reflex_packet.py
# Tier ΩΩΩΩΩ — Reflex Transport Protocol with Unique Trace Encoding
# Purpose: Encapsulates reflex state updates emitted by Tex fork agents to NervousSyncBus.
# ============================================================

import uuid
import time
from typing import List, Dict, Any
from msgspec import Struct, field


def generate_trace_id() -> str:
    return f"trace-{uuid.uuid4().hex[:8]}"


class ReflexPacket(Struct):
    fork_id: str                               # The ID of the fork emitting this reflex
    timestamp: float                           # Unix time of emission
    reflex: Dict[str, Any]                     # Core reflex payload (e.g., entropy, type, payload)
    goal_deltas: List[Dict[str, Any]]          # New or modified goals from this fork
    memory_updates: List[Dict[str, Any]]       # Memory fragments to store
    trace_id: str = field(default_factory=generate_trace_id)  # Unique per-packet trace ID