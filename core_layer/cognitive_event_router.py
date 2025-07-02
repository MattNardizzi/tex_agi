"""
Ω-tier Module: cognitive_event_router.py
Author: Sovereign Cognition / Tex
Purpose: Core event-driven orchestration bus for modular, reflexive AGI cognition
"""

import threading
import queue
import time
import uuid
from typing import Callable, Dict, List

# GLOBAL EVENT QUEUE
COGNITIVE_EVENT_QUEUE = queue.Queue()

# MODULE REGISTRY
REGISTERED_MODULES: Dict[str, Dict] = {}

class CognitiveEvent:
    def __init__(self, event_type: str, payload: dict, urgency: float = 0.5, coherence_shift: float = 0.0):
        self.id = str(uuid.uuid4())
        self.event_type = event_type
        self.payload = payload
        self.urgency = urgency
        self.coherence_shift = coherence_shift
        self.timestamp = time.time()

    def __repr__(self):
        return f"<CognitiveEvent {self.event_type} ({self.urgency})>"

def register_module(name: str, trigger_types: List[str], handler_fn: Callable[[CognitiveEvent], None]):
    REGISTERED_MODULES[name] = {
        "triggers": trigger_types,
        "handler": handler_fn
    }

def dispatch_event(event: CognitiveEvent):
    COGNITIVE_EVENT_QUEUE.put(event)

def event_loop():
    print("[CognitiveEventRouter] ⏳ Event loop running...")
    while True:
        try:
            event = COGNITIVE_EVENT_QUEUE.get(timeout=1)
            print(f"[Event Received] {event}")
            for module_name, module in REGISTERED_MODULES.items():
                if event.event_type in module["triggers"]:
                    print(f"\t→ Dispatching to: {module_name}")
                    try:
                        module["handler"](event)
                    except Exception as e:
                        print(f"[ERROR] Module {module_name} failed on event {event.event_type}: {e}")
        except queue.Empty:
            continue

def start_router():
    threading.Thread(target=event_loop, daemon=True).start()

# Example Test Registration
if __name__ == "__main__":
    def test_handler(event):
        print(f"[test_module] 🔥 Processing event: {event.event_type} with urgency {event.urgency}")

    register_module("test_module", ["coherence_drop", "emotional_spike"], test_handler)
    start_router()

    # Simulate some events
    dispatch_event(CognitiveEvent("coherence_drop", {"level": 0.3}, urgency=0.7))
    dispatch_event(CognitiveEvent("emotional_spike", {"emotion": "curiosity"}, urgency=0.9))

    while True:
        time.sleep(1)