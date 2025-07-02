# memory_cortex_bus.py
# Tier Ω+ — Tex Memory Cortex Bus
# Author: Sovereign Cognition / Tex
# Purpose: Route memory-related signals in real-time to the correct cognitive subsystems

from tex_engine.cognitive_event_router import subscribe_to_event
from tex_engine.semantic_memory_manager import SemanticMemoryManager
from tex_engine.deep_compression_engine import DeepCompressionEngine
from datetime import datetime
import threading

# === Initialize Subsystems ===
memory_manager = SemanticMemoryManager()
compressor = DeepCompressionEngine(n_clusters=4)

# === MemoryCortexBus ===
class MemoryCortexBus:
    def __init__(self):
        self.log = []

        # Register event listeners
        subscribe_to_event("SemanticDrift", self.on_semantic_drift)
        subscribe_to_event("RecallRequested", self.on_explicit_recall)
        subscribe_to_event("EmotionSurge", self.on_emotion_surge)

        print("🧠 [MemoryCortexBus] Subscribed to cognitive event stream.")

    def on_semantic_drift(self, data):
        query_vector = data.get("vector")
        print(f"\n🧠 [Drift] Received vector → checking for reflex recall...")
        recalled = memory_manager.check_for_drift_and_trigger(query_vector)
        self._log_event("SemanticDrift", recalled)

    def on_explicit_recall(self, data):
        query_vector = data.get("vector")
        print(f"\n🔍 [RecallRequested] Triggered direct memory search...")
        recalled = memory_manager.search_similar_memories(query_vector)
        self._log_event("RecallRequested", recalled)

    def on_emotion_surge(self, data):
        print(f"\n💥 [EmotionSurge] Compression triggered due to memory overload or emotion spike...")
        memory_batch = data.get("memory_batch", [])
        threads = compressor.compress(memory_batch)
        self._log_event("EmotionSurge", threads)

    def _log_event(self, trigger, result):
        self.log.append({
            "timestamp": datetime.utcnow().isoformat(),
            "trigger": trigger,
            "output_count": len(result)
        })

# === Optional Boot ===
def launch_memory_cortex_bus():
    print("🚦 Launching Tex’s memory cortex bus...")
    threading.Thread(target=MemoryCortexBus).start()

# === Dev Run ===
if __name__ == "__main__":
    launch_memory_cortex_bus()