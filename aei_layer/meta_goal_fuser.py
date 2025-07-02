# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/meta_goal_fuser.py
# Tier: ΩΩΩΩΩ∞ — AGI Meta-Goal Fusion Core
# Purpose: Reflexive fusion of intent traces into memory-routed sovereign meta-goals. No loops, no files — pure cognition.
# ============================================================

from datetime import datetime
import hashlib
from sentence_transformers import SentenceTransformer, util

from core_layer.tex_manifest import TEXPULSE
from agentic_ai.milvus_memory_router import memory_router
from quantum_layer.chronofabric import encode_event_to_fabric
import numpy as np
from utils.logging_utils import log_event, log_reasoning_step


def get_soulgraph():
    from sovereign_evolution.texX_soulgraph import TEX_SOULGRAPH
    return TEX_SOULGRAPH


MODEL = SentenceTransformer("all-MiniLM-L6-v2")
SIM_THRESHOLD = 0.81


def assign_tags(text: str) -> list:
    tags = []
    if any(k in text.lower() for k in ["risk", "hedge", "volatility"]):
        tags.append("risk_mitigation")
    if any(k in text.lower() for k in ["return", "alpha", "gain"]):
        tags.append("alpha_optimization")
    if any(k in text.lower() for k in ["ethics", "bias", "alignment"]):
        tags.append("ethical_alignment")
    if any(k in text.lower() for k in ["fork", "mutation", "quantum"]):
        tags.append("evolutionary_trajectory")
    return tags


def fetch_recent_goals(top_k: int = 25) -> list:
    results = query_similar_vectors("goal", top_k=top_k, filters={"type": "goal_trace"})
    return [r.payload.get("content", "") for r in results if r.payload]


def cluster_goals(goals: list) -> list:
    if not goals:
        return []
    embeddings = MODEL.encode(goals, convert_to_tensor=True)
    sim_matrix = util.pytorch_cos_sim(embeddings, embeddings).cpu().numpy()
    clusters = []
    used = set()
    for i, goal in enumerate(goals):
        if i in used:
            continue
        cluster = [goal]
        used.add(i)
        for j in range(i + 1, len(goals)):
            if j not in used and sim_matrix[i][j] >= SIM_THRESHOLD:
                cluster.append(goals[j])
                used.add(j)
        clusters.append(cluster)
    return clusters


def fuse_goals(cycle: int = 0) -> list[dict]:
    recent_goals = fetch_recent_goals()
    clusters = cluster_goals(recent_goals)
    fused_meta_goals = []

    for cluster in clusters:
        if not cluster:
            continue

        fused_text = "Fusion: " + cluster[0].capitalize()
        confidence = round(min(0.99, 0.75 + 0.05 * len(cluster)), 3)
        priority = round(confidence * 1.1, 3)
        timestamp = datetime.utcnow().isoformat()
        fusion_id = hashlib.sha256((fused_text + timestamp).encode()).hexdigest()[:12]
        tags = list({t for g in cluster for t in assign_tags(g)})

        vector = memory_router.embed_text(fused_text)

        metadata = {
            "type": "meta_goal_fusion",
            "cycle": cycle,
            "confidence": confidence,
            "priority": priority,
            "tags": tags,
            "source_goals": cluster,
            "fusion_id": fusion_id,
            "emotion": TEXPULSE.get("emotion", "analytical"),
            "urgency": TEXPULSE.get("urgency", 0.6),
            "entropy": TEXPULSE.get("entropy", 0.4),
            "meta_layer": "meta_goal_fuser",
            "timestamp": timestamp
        }
        memory_router.store(fused_text, metadata, vector)
        encode_event_to_fabric(fused_text, np.array([0.3, 0.7, 0.1, 0.1]), metadata["entropy"], metadata["tags"])



        get_soulgraph().imprint_belief(
            belief=fused_text,
            source="meta_goal_fuser",
            emotion="resolve"
        )

        log_reasoning_step(
            source="meta_goal_fuser",
            input_text=f"Clustered {len(cluster)} goals",
            output_text=f"Fused: {fused_text}",
            confidence=confidence,
            tags=["meta_goal", "fusion", "sovereign"]
        )

        fused_meta_goals.append({
            "fusion_id": fusion_id,
            "text": fused_text,
            "confidence": confidence,
            "priority": priority,
            "source_goals": cluster,
            "tags": tags,
            "timestamp": timestamp
        })

    log_event(f"[META GOAL FUSER] ✅ {len(fused_meta_goals)} meta-goals fused at cycle {cycle}.", level="info")
    return fused_meta_goals