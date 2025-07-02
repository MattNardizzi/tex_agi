# ============================================================
# © 2025 VortexBlack LLC — Sovereign Reflex Fork Agent
# File: swarm_layer/tex_fork_agent.py
# Tier: ΩΩΩΩΩ∞ — Reflex Thread w/ Volatility Logic, Identity Heuristics, and Live Entropy Feedback
# Purpose: Autonomously emits entropy-aware ReflexPackets to NervousSyncBus for swarm coordination.
# ============================================================

import threading
import time
import random
from datetime import datetime
from core_schemas.reflex_packet import ReflexPacket
from swarm_layer.nervous_sync_bus import NervousSyncBus
from core_layer.tex_manifest import TEXPULSE

class TexForkAgent(threading.Thread):
    def __init__(self, fork_id: str, bus: NervousSyncBus, interval: float = 4.2):
        super().__init__()
        self.fork_id = fork_id
        self.bus = bus
        self.interval = interval
        self.running = True
        self.volatility = random.uniform(0.02, 0.1)  # unique signal fingerprint
        self.identity = TEXPULSE.get("identity", "TEX")
        print(f"✅ [INIT] Fork {self.fork_id} initialized with volatility={self.volatility:.4f}")

    def generate_entropy(self) -> float:
        base = random.uniform(0.2, 0.8)
        mod = random.gauss(0, self.volatility)
        entropy = max(0.0, min(1.0, round(base + mod, 4)))
        return entropy

    def emit_reflex(self):
        entropy = self.generate_entropy()
        print(f"🌀 [{self.fork_id}] Emitting reflex — entropy={entropy}")

        try:
            packet = ReflexPacket(
                fork_id=self.fork_id,
                timestamp=time.time(),
                reflex={
                    "type": "EMOTION_PULSE",
                    "entropy": entropy,
                    "payload": {
                        "intensity": entropy,
                        "identity": self.identity,
                        "variant": self.fork_id,
                        "volatility": round(self.volatility, 4)
                    }
                },
                goal_deltas=[],
                memory_updates=[{
                    "content": f"Reflex fired by {self.fork_id} | Entropy={entropy}",
                    "emotion": "alert",
                    "tags": ["reflex", self.fork_id, "entropy_sync"],
                    "trust_score": round(1.0 - abs(0.5 - entropy), 2),
                    "heat": entropy,
                    "timestamp": datetime.utcnow().isoformat()
                }]
            )

            self.bus.receive_packet(packet)

        except Exception as e:
            print(f"❌ [ERROR] Failed to emit reflex from {self.fork_id}: {e}")

    def run(self):
        print(f"🚀 [START] Fork {self.fork_id} thread running every {self.interval}s...")
        try:
            while self.running:
                self.emit_reflex()
                time.sleep(self.interval)
        except Exception as e:
            print(f"❌ [CRASH] Fork thread {self.fork_id} crashed: {e}")

    def stop(self):
        self.running = False
        print(f"🛑 [STOP] Fork {self.fork_id} has been stopped.")