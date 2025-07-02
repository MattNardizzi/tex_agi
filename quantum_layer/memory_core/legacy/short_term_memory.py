# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: quantum_layer/memory_core/short_term_memory.py
# Purpose: Reflexive Short-Term Memory Buffer (STM) for Tex AGI
# ============================================================

from collections import deque
from datetime import datetime

class ShortTermMemory:
    def __init__(self, max_length=250):
        self.buffer = deque(maxlen=max_length)

    def store(self, event: dict, tags: list = [], urgency: float = 0.5, emotion: str = "neutral"):
        memory_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": event,
            "tags": tags,
            "urgency": urgency,
            "emotion": emotion
        }
        self.buffer.append(memory_entry)

    def recent(self, count=5):
        return list(self.buffer)[-count:]

    def find_by_tag(self, tag: str):
        return [entry for entry in self.buffer if tag in entry.get("tags", [])]

    def flush(self):
        """
        Flush current memory buffer and return all entries.
        """
        flushed = list(self.buffer)
        self.buffer.clear()
        return flushed

    def peek(self):
        """
        Return the most recent memory item.
        """
        return self.buffer[-1] if self.buffer else None

    def __len__(self):
        return len(self.buffer)