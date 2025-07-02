# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: swarm_layer/swarm_sync_daemon.py
# Purpose: Swarm Sync Daemon — Upgraded with Sovereign Cognition Fire
# ============================================================

import os
import json
import time
import hashlib
from datetime import datetime
from difflib import SequenceMatcher
from core_layer.memory_engine import store_to_memory
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override

SWARM_FEED      = "memory_archive/swarm_feed.jsonl"
CHILD_SPAWN_LOG = "memory_archive/child_spawn_log.jsonl"
CONSENSUS_LOG   = "memory_archive/swarm_consensus_log.jsonl"
os.makedirs("memory_archive", exist_ok=True)

class SwarmSyncDaemon:
    def __init__(self, interval: int = 10):
        self.interval = interval
        self._last_snapshot_hash = None
        print(f"[✅ SWARM SYNC DAEMON] Hardened version loaded (interval = {self.interval}s)")

    def _load_child_agents(self):
        if not os.path.exists(CHILD_SPAWN_LOG):
            return []
        valid_agents = []
        with open(CHILD_SPAWN_LOG, "r") as f:
            for idx, line in enumerate(f):
                try:
                    agent = json.loads(line.strip())
                    if isinstance(agent, dict):
                        valid_agents.append(agent)
                    else:
                        store_to_memory("swarm_sync_errors", {
                            "timestamp": datetime.utcnow().isoformat(),
                            "index": idx,
                            "bad_type": str(type(agent)),
                            "raw_value": str(agent)[:300],
                        })
                except Exception as e:
                    print(f"[SWARM SYNC WARNING] Malformed JSON at line {idx}: {e}")
        return valid_agents

    def _generate_swarm_snapshot(self, agents):
        valid_agents = []
        seen_insights = []

        for idx, a in enumerate(agents):
            if not isinstance(a, dict):
                store_to_memory("swarm_sync_errors", {
                    "timestamp": datetime.utcnow().isoformat(),
                    "index": idx,
                    "bad_type": str(type(a)),
                    "raw_value": str(a)[:300],
                })
                continue

            score = a.get("score")
            if score is not None and isinstance(score, (int, float)) and score < 0.3:
                continue

            traits = a.get("traits", {})
            insight = traits.get("insight", "").strip().lower()

            # ✅ Consensus detection: match to previously seen insight
            if insight and any(SequenceMatcher(None, insight, s).ratio() > 0.85 for s in seen_insights):
                self._log_consensus(insight, traits.get("emotion", "unknown"))
                continue
            if insight:
                seen_insights.append(insight)

            valid_agents.append(a)

        emotions, biases = [], []
        for idx, agent in enumerate(valid_agents):
            traits = agent.get("traits")
            if traits is None:
                print(f"[DEBUG] Agent {idx} has no traits.")
            if isinstance(traits, str):
                t = traits.lower()
                traits = {}
                if t in {"fear", "hope", "resolve", "doubt", "greed", "curiosity", "anger", "joy"}:
                    traits["emotion"] = t
                else:
                    traits["bias"] = t
            if not isinstance(traits, dict):
                store_to_memory("swarm_sync_errors", {
                    "timestamp":  datetime.utcnow().isoformat(),
                    "issue":      "non-dict traits",
                    "agent_index": idx,
                    "raw_traits":  str(traits)[:300],
                })
                continue
            emotion = traits.get("emotion", "unknown")
            if emotion == "unknown":
                print(f"[DEBUG] Agent {idx} traits: {traits}")
            emotions.append(emotion)
            biases.append(traits.get("bias", "neutral"))

        summary = {
            "timestamp":              datetime.utcnow().isoformat(),
            "swarm_size":             len(valid_agents),
            "emotional_distribution": {e: emotions.count(e) for e in set(emotions)},
            "bias_distribution":      {b: biases.count(b)   for b in set(biases)},
        }
        return summary

    def _log_consensus(self, insight_text, emotion):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "insight": insight_text,
            "emotion": emotion,
            "status": "merged",
            "reason": "Multiple agents reached similar conclusion"
        }
        try:
            with open(CONSENSUS_LOG, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
            store_to_memory("swarm_consensus", entry)
            print("[CONSENSUS] ✅ Merged consensus insight recorded.")
        except Exception as e:
            print(f"[CONSENSUS LOG ERROR] {e}")

    def _hash_snapshot(self, snapshot: dict) -> str:
        snapshot_bytes = json.dumps(snapshot, sort_keys=True).encode("utf-8")
        return hashlib.sha256(snapshot_bytes).hexdigest()

    def run(self, depth=0):
        if depth > 5:
            print("[⚠️ RECURSION BLOCK] SwarmSyncDaemon recursion limit exceeded. Aborting.")
            return
        print("[SWARM SYNC DAEMON] 🧠 Syncing swarm state...")
        while True:
            try:
                agents   = self._load_child_agents()
                snapshot = self._generate_swarm_snapshot(agents)

                if not isinstance(snapshot, dict):
                    print("[SWARM SYNC DAEMON] ⚠️ Malformed snapshot — expected dict")
                    time.sleep(self.interval)
                    continue

                snapshot_hash = self._hash_snapshot(snapshot)
                if snapshot_hash == self._last_snapshot_hash:
                    time.sleep(self.interval)
                    continue

                emotions_set = set(snapshot["emotional_distribution"].keys())
                if emotions_set == {"unknown"}:
                    print("[SWARM SYNC DAEMON] ⚠️ All agent emotions unknown; skipping write.")
                    time.sleep(self.interval)
                    continue

                self._last_snapshot_hash = snapshot_hash

                try:
                    emotions = snapshot.get("emotional_distribution", {})
                    top_emotion = max(emotions, key=emotions.get, default="unknown")

                    formatted_entry = {
                        "agent_id": "swarm_feed",
                        "memory": {
                            "emotion": top_emotion,
                            "urgency": min(1.0, snapshot.get("swarm_size", 0) / 50),
                            "score": round(sum(emotions.values()) / max(snapshot.get("swarm_size", 1), 1), 3)
                        }
                    }

                    with open(SWARM_FEED, "a", encoding="utf-8") as f:
                        f.write(json.dumps(formatted_entry) + "\n")

                except Exception as e:
                    print(f"[SWARM SYNC WRITE ERROR] ❌ Failed to write snapshot: {e}")
                    time.sleep(self.interval)
                    continue

                store_to_memory("swarm_feed", snapshot)
                print(f"[SWARM SYNC] ✅ Snapshot stored @ {snapshot['timestamp']}")

                override_result = trigger_sovereign_override(
                    context="swarm_sync",
                    foresight=snapshot.get("swarm_size", 0) / 100,
                    force=False
                )
                if override_result.get("status") == "activated":
                    print(f"[SOVEREIGN 🔥] Override triggered from Swarm Sync — {override_result.get('counterfactual')}")

            except Exception as e:
                print(f"[SWARM SYNC ERROR] {e}")

            time.sleep(self.interval)