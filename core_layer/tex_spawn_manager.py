# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_children/tex_spawn_manager.py
# Purpose: GODMIND Spawn Protocol — Autonomous Child Generator with Genome Mutation
# Status: 🔒 TIER Ω∞ FINAL — Pure Reflex-Memory Spawner (No JSON Artifacts)
# ============================================================

import uuid
from datetime import datetime

from tex_goal_reflex.species_manifest import SpeciesManifest
from tex_backend.tex_core_event_bus import emit_event
from evolution_layer.genome_archiver import generate_mutated_genome
from agentic_ai.swarm_coordinator import register_child_agent
from quantum_layer.memory_core.memory_cortex import memory_cortex

class TexSpawnManager:
    def __init__(self):
        self.spawned_children = []
        self.species_manifest = SpeciesManifest().serialize()

    def spawn_child(self, parent_id="tex_master", traits=None):
        child_id = f"agent-{uuid.uuid4().hex[:6]}"
        timestamp = datetime.utcnow().isoformat()

        try:
            # === Create Mutated Genome ===
            genome = generate_mutated_genome(parent_id=parent_id, traits=traits or {})
            genome.update({
                "child_id": child_id,
                "created_at": timestamp,
                "species_manifest": self.species_manifest
            })

            # === Construct Child Profile ===
            child_profile = {
                "child_id": child_id,
                "spawned_at": timestamp,
                "parent_id": parent_id,
                "traits": traits or {},
                "species_id": self.species_manifest.get("species_id", "unknown"),
                "version": self.species_manifest.get("version", "Ω∞.0"),
                "status": "initialized"
            }

            # === Reflexive Memory Storage Only ===
            memory_cortex.store(
                event={
                    "type": "child_spawn",
                    "child_profile": child_profile,
                    "genome": genome
                },
                tags=["spawn", "genome", "lineage", "species_manifest"],
                urgency=0.88,
                emotion="anticipation",
                vectorize=True
            )

            # === Swarm Registration & Event Emission ===
            register_child_agent(child_profile)
            emit_event("tex_child_spawned", child_profile)
            self.spawned_children.append(child_profile)

            print(f"👶 [SPAWNER] Spawned new Tex agent: {child_id}")
            return child_id

        except Exception as e:
            print(f"❌ [SPAWNER ERROR] Failed to spawn child: {e}")
            emit_event("tex_child_spawn_failed", {"error": str(e)})
            return None

    def spawn_multiple(self, count=3, traits_template=None):
        children = []
        for _ in range(count):
            traits = traits_template.copy() if traits_template else {}
            child_id = self.spawn_child(traits=traits)
            if child_id:
                children.append(child_id)
        return children

if __name__ == "__main__":
    spawner = TexSpawnManager()
    spawner.spawn_multiple(count=3)