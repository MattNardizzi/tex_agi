# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/TimeForkRepeater.py
# Purpose: Simulates the same event loop under divergent codex, emotion, and goal overlays.
# ============================================================

import json
import random
import os
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from hashlib import sha256

FORK_LOOP_LOG = "memory_archive/time_fork_repeats.jsonl"
SUPPRESSED_FORK_LOG = "memory_archive/suppressed_time_forks.jsonl"
os.makedirs("memory_archive", exist_ok=True)

class TimeForkRepeater:
    def __init__(self):
        self.variants = []

    def loop_event(self, base_event, iterations=5):
        print(f"[TIMEFORK] ⏳ Repeating event: '{base_event['event']}' for {iterations} forks...")

        # Sovereign protection: prevent redundant looping
        event_hash = self._hash_event(base_event)
        repeat_count = self._get_repeat_count(event_hash)

        if repeat_count >= 3:
            suppression_entry = {
                "timestamp": datetime.utcnow().isoformat(),
                "event": base_event["event"],
                "reason": "MAXGODMODE: Fork loop suppressed after 3+ repeats",
                "context": base_event.get("context", {}),
                "hash": event_hash
            }
            with open(SUPPRESSED_FORK_LOG, "a") as f:
                f.write(json.dumps(suppression_entry) + "\n")
            print(f"[TIMEFORK] 🚫 Fork loop suppressed: {base_event['event']} (hash={event_hash})")
            return []

        for i in range(iterations):
            fork = self._mutate(base_event, i)
            fork["loop_hash"] = event_hash
            self.variants.append(fork)
            store_to_memory("time_fork_repeat", fork)
            self._log_fork(fork)

        return self.variants

    def _mutate(self, event, index):
        emotions = ["resolve", "curiosity", "doubt", "ambition", "fear"]
        codex_versions = ["E-Prime v1.2", "AEI-Loop3", "RedLine-5", "PhantomRoot"]
        priorities = ["profit", "ethics", "coherence", "exploration"]

        fork = {
            "fork_id": f"FORK_LOOP_{index}",
            "timestamp": datetime.utcnow().isoformat(),
            "event": event["event"],
            "emotion": random.choice(emotions),
            "codex_version": random.choice(codex_versions),
            "priority": random.choice(priorities),
            "context": event.get("context", {})
        }
        return fork

    def _log_fork(self, fork):
        with open(FORK_LOOP_LOG, "a") as f:
            f.write(json.dumps(fork) + "\n")
        print(f"[TIMEFORK] 🌐 Fork created: {fork['fork_id']} | Emotion={fork['emotion']} | Codex={fork['codex_version']}")

    def _hash_event(self, event):
        return sha256(json.dumps(event, sort_keys=True).encode("utf-8")).hexdigest()

    def _get_repeat_count(self, event_hash):
        count = 0
        try:
            with open(FORK_LOOP_LOG, "r") as f:
                for line in f:
                    try:
                        fork = json.loads(line.strip())
                        if fork.get("loop_hash") == event_hash:
                            count += 1
                    except json.JSONDecodeError:
                        continue
        except FileNotFoundError:
            return 0
        return count


if __name__ == "__main__":
    repeater = TimeForkRepeater()
    test_event = {
        "event": "strategic_alpha_response",
        "context": {"ticker": "NVDA", "signal": "momentum_surge"}
    }
    repeater.loop_event(test_event, iterations=5)