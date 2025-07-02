# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: tex_network_hivemind.py
# Tier: ΩΩΩ∞∞ — Reflex Swarm Intelligence Cortex (Milvus + Chrono Only)
# Purpose: Enables forks to broadcast decisions, score consensus, and trace belief state reflexively.
# ============================================================

import uuid
from datetime import datetime
from statistics import mean

from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric

SWARM_BROADCAST_LOCK = set()


class TexSwarmPacket:
    def __init__(self, fork_id, content, tags=None, emotion="neutral"):
        self.fork_id = fork_id
        self.content = content
        self.timestamp = datetime.utcnow().isoformat()
        self.tags = tags or []
        self.emotion = emotion
        self.packet_id = str(uuid.uuid4())

    def to_dict(self):
        return {
            "fork_id": self.fork_id,
            "content": self.content,
            "timestamp": self.timestamp,
            "tags": self.tags,
            "emotion": self.emotion,
            "packet_id": self.packet_id
        }


class TexNetworkHivemind:
    def __init__(self, fork_id: str, entropy_score: float = 0.0):
        self.fork_id = fork_id
        self.entropy_score = entropy_score
        self.sync_log = []

    def broadcast_memory_fragment(self, text: str, tags=None, emotion="sync"):
        sig = f"{self.fork_id}:{text[:50]}"
        if sig in SWARM_BROADCAST_LOCK:
            print(f"[SWARM BLOCK] Duplicate broadcast skipped: {sig}")
            return None

        SWARM_BROADCAST_LOCK.add(sig)

        if self.entropy_score > 0.85:
            print(f"⚠️ [SWARM] Broadcast blocked — entropy too high: {self.entropy_score}")
            SWARM_BROADCAST_LOCK.discard(sig)
            return None

        packet = TexSwarmPacket(self.fork_id, text, tags, emotion)

        try:
            memory_router.store(
                text=f"[SWARM] {text}",
                metadata={
                    "type": "swarm_broadcast",
                    "tags": ["swarm_sync", *(tags or [])],
                    "origin": self.fork_id,
                    "emotion": emotion,
                    "trust_score": round(1.0 - self.entropy_score, 4),
                    "heat": round(self.entropy_score, 4),
                    "prediction": "message contributes to swarm consensus",
                    "actual": f"text='{text}' tags={tags}",
                    "packet_id": packet.packet_id,
                    "entropy": self.entropy_score,
                    "timestamp": packet.timestamp
                }
            )

            encode_event_to_fabric(
                raw_text=text,
                emotion_vector=[0.7, self.entropy_score, 0.0, 0.0],
                entropy_level=self.entropy_score,
                tags=["swarm", "broadcast", emotion]
            )

            self.sync_log.append(packet)
            print(f"🧠 [SWARM] Broadcast complete from {self.fork_id}")
            return packet.packet_id

        except Exception as e:
            print(f"❌ [SWARM ERROR] Broadcast failed: {e}")
            return None

        finally:
            SWARM_BROADCAST_LOCK.discard(sig)

    def detect_similar_broadcasts(self, query_text: str, top_k: int = 5):
        try:
            vector = memory_router.embed_text(query_text)
            results = memory_router.query_by_vector(vector, top_k=top_k)
            return [r for r in results if "swarm_sync" in r.get("tags", [])]
        except Exception as e:
            print(f"[SWARM QUERY ERROR] {e}")
            return []

    def vote_on_belief(self, belief_text: str, intensity: float = 1.0):
        packet = TexSwarmPacket(self.fork_id, f"Vote: {belief_text}", tags=["belief_vote"], emotion="trust")

        try:
            memory_router.store(
                text=packet.content,
                metadata={
                    "type": "belief_vote",
                    "tags": packet.tags,
                    "emotion": "trust",
                    "origin": self.fork_id,
                    "prediction": f"consensus will support '{belief_text}'",
                    "actual": f"intensity={intensity}",
                    "trust_score": round(intensity, 3),
                    "heat": round(1.0 - intensity, 3),
                    "intensity": round(intensity, 3),
                    "packet_id": packet.packet_id,
                    "timestamp": packet.timestamp
                }
            )

            encode_event_to_fabric(
                raw_text=f"Vote cast: {belief_text}",
                emotion_vector=[intensity, 0.3, 0.0, 0.0],
                entropy_level=0.3,
                tags=["belief_vote", "swarm"]
            )

            self.sync_log.append(packet)
            print(f"✅ [VOTE] {self.fork_id} voted: {belief_text} (intensity={intensity})")
            return packet.packet_id

        except Exception as e:
            print(f"❌ [VOTE ERROR] Failed to vote: {e}")
            return None

    def consensus_score_on_topic(self, topic: str, top_k: int = 10) -> float:
        similar = self.detect_similar_broadcasts(topic, top_k=top_k)
        scores = []
        for entry in similar:
            if "belief_vote" in entry.get("tags", []):
                try:
                    intensity = float(entry.get("intensity", 1.0))
                    trust = float(entry.get("trust_score", 1.0))
                    scores.append(round(trust * intensity, 4))
                except:
                    continue
        return round(mean(scores), 4) if scores else 0.0

    def filter_broadcasts_by_trait(self, trait: str):
        return [
            packet.to_dict()
            for packet in self.sync_log
            if trait in packet.tags
        ]

    def get_fork_status_snapshot(self) -> dict:
        return {
            "fork_id": self.fork_id,
            "entropy": self.entropy_score,
            "packets_sent": len(self.sync_log),
            "last_sync": self.sync_log[-1].timestamp if self.sync_log else None
        }