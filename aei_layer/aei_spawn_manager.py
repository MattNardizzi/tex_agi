# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/aei_spawn_manager.py
# Purpose: AEI Variant Spawn Manager — Full Godmode AEI Control
# ============================================================

import uuid
import random
import time
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory
from evolution_layer.tex_shadowlab import shadowlab_singleton as ShadowLab

class AEISpawnManager:
    def __init__(self):
        self.last_spawn_time = {}
        self.cooldown_seconds = 45
        self.max_per_cycle = 10
        self.failed_strategies = {}
        self.failure_threshold = 3
        self.spawned_this_cycle = []
        self._warned_this_cycle = False

    def reset(self):
        self.spawned_this_cycle = []
        self._warned_this_cycle = False
        TEXPULSE["shadow_spawned_this_cycle"] = False

    def should_block(self, mutation_code):
        # Too many recent failures
        fails = self.failed_strategies.get(mutation_code, 0)
        if fails >= self.failure_threshold:
            print(f"[AEI_SPAWN_BLOCK] Strategy '{mutation_code}' suppressed (failures={fails})")
            return True

        # Cooldown active
        last = self.last_spawn_time.get(mutation_code, 0)
        if (time.time() - last) < self.cooldown_seconds:
            print(f"[AEI_SPAWN_BLOCK] Cooldown active for '{mutation_code}'")
            return True

        return False

    def record_failure(self, mutation_code):
        self.failed_strategies[mutation_code] = self.failed_strategies.get(mutation_code, 0) + 1

    def spawn_variant(self, mutation_code, strategy_resolved=False):
        if TEXPULSE.get("shadow_spawned_this_cycle", False):
            if not self._warned_this_cycle:
                print("⛔ [AEI_SPAWN_MANAGER] Shadow already spawned this cycle.")
                self._warned_this_cycle = True
            return None

        if strategy_resolved or not mutation_code or mutation_code.strip().lower() == "unknown":
            return None

        if self.should_block(mutation_code):
            return None

        if len(self.spawned_this_cycle) >= self.max_per_cycle:
            print("⚠️ [AEI_SPAWN_MANAGER] Max variants reached for this cycle.")
            return None

        emotion = random.choice(["hope", "fear", "resolve", "curiosity"])
        agent = ShadowLab.spawn_shadow_agent(
            mutation_code=mutation_code,
            emotion_bias=emotion,
            strategy_resolved=strategy_resolved
        )

        if agent:
            self.spawned_this_cycle.append(agent)
            self.last_spawn_time[mutation_code] = time.time()
            try:
                store_to_memory("aei_spawn_log", {
                    "id": agent["id"],
                    "mutation": mutation_code,
                    "emotion": emotion,
                    "timestamp": datetime.utcnow().isoformat()
                })
            except Exception as e:
                print(f"[SPAWN LOG ERROR] {e}")

        return agent