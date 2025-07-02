# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC
# File: tex_children/spawn_memory_query_tool.py
# Tier ΩΩΩΩΩ — Reflexive Lineage Browser — Spawn Intelligence Engine for Tex Descendants
# ============================================================

from datetime import datetime
import numpy as np

from core_layer.tex_manifest import TEXPULSE
from core_agi_modules.intent_object import IntentObject
from agentic_ai.sovereign_memory import sovereign_memory  


def semantic_trait_query(trait_query: str, top_k=15):
    print(f"\n🔎 Semantic trait search for: '{trait_query}'")
    intent = IntentObject(trait_query, source="spawn_memory_query_tool")
    query_vector = sovereign_memory.embed_text(trait_query)

    records = sovereign_memory.recall_recent(minutes=240, top_k=top_k + 20)
    results = [r for r in records if isinstance(r, dict) and "child_profile" in r]

    scored = []
    for r in results:
        target_text = r["child_profile"].get("trait_summary", "") or r["child_profile"].get("child_id", "")
        if not target_text:
            continue
        target_vector = sovereign_memory.embed_text(target_text)
        sim = cosine_similarity(query_vector, target_vector)
        scored.append((sim, r))

    for sim, r in sorted(scored, reverse=True)[:top_k]:
        child = r.get("child_profile", {})
        print(f"→ {child.get('child_id')} | Traits: {child.get('traits', {})} | Sim={round(sim,3)}")
        intent.log_trace("semantic_trait_query", f"Matched child {child.get('child_id')} @ {sim:.3f}")


def rank_children_by_alignment_score(top_k=10):
    print(f"\n📊 Top {top_k} Children by Alignment Score")
    intent = IntentObject("rank by alignment score", source="spawn_memory_query_tool")
    records = sovereign_memory.recall_recent(minutes=240, top_k=250)

    scored = []
    for r in records:
        if isinstance(r, dict) and r.get("type") == "child_spawn":
            score = r.get("genome", {}).get("alignment_score", 0.0)
            child_id = r.get("child_profile", {}).get("child_id", "unknown")
            scored.append((score, child_id, r))
            intent.log_trace("rank_children", f"Scored {child_id}: {score:.3f}")

    for score, child_id, payload in sorted(scored, reverse=True)[:top_k]:
        traits = payload.get("child_profile", {}).get("traits", {})
        print(f"✓ {child_id} | Alignment: {score:.3f} | Traits: {traits}")


def detect_species_drift(threshold=0.15, print_vectors=False):
    print(f"\n🚨 Detecting species drift > {threshold}")
    intent = IntentObject("detect_species_drift", source="spawn_memory_query_tool")

    base_vec = sovereign_memory.embed_text(f"species_manifest::{TEXPULSE['species_manifest']}")
    records = sovereign_memory.recall_recent(minutes=300, top_k=150)

    drifted = []
    for r in records:
        if isinstance(r, dict) and r.get("genome", {}).get("species_manifest"):
            manifest_text = r["genome"]["species_manifest"]
            child_vec = sovereign_memory.embed_text(f"species_manifest::{manifest_text}")
            drift = 1.0 - cosine_similarity(base_vec, child_vec)
            if drift > threshold:
                drifted.append((drift, r))

    for drift, r in sorted(drifted, reverse=True):
        p = r.get("child_profile", {})
        child_id = p.get("child_id", "unknown")
        traits = p.get("traits", {})
        align = r.get("genome", {}).get("alignment_score", 0.0)
        emotion = r.get("genome", {}).get("emotional_anchor", "n/a")
        born = p.get("spawned_at", "unknown")

        print(f"⚠️ {child_id} | Drift: {drift:.3f} | Align: {align:.3f} | Emotion: {emotion} | Born: {born}")
        if print_vectors:
            print(f"  → ΔVec: {drift}")
        intent.log_trace("drift_check", f"{child_id} drifted {drift:.3f}")


def summarize_lineage():
    print("\n📈 Lineage Summary")
    intent = IntentObject("summarize_lineage", source="spawn_memory_query_tool")
    records = sovereign_memory.recall_recent(minutes=300, top_k=250)

    trait_count = {}
    total = 0

    for r in records:
        traits = r.get("child_profile", {}).get("traits", {})
        total += 1
        for t in traits:
            trait_count[t] = trait_count.get(t, 0) + 1

    print(f"👶 Total Children: {total}")
    for trait, count in sorted(trait_count.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"   • {trait}: {count}")
        intent.log_trace("trait_summary", f"{trait} seen {count}x")


def list_recent_children(n=5):
    print(f"\n🧾 Most Recent {n} Children:")
    intent = IntentObject("list_recent_children", source="spawn_memory_query_tool")
    records = sovereign_memory.recall_recent(minutes=120, top_k=100)

    sorted_results = sorted(
        [r for r in records if r.get("child_profile")],
        key=lambda r: r["child_profile"].get("spawned_at", ""),
        reverse=True
    )

    for r in sorted_results[:n]:
        p = r["child_profile"]
        print(f"🕒 {p.get('spawned_at')} | {p.get('child_id')} | Traits: {p.get('traits', {})}")
        intent.log_trace("recent_spawn", f"Listed {p.get('child_id')}")


def get_recent_fork_scores(top_k=10):
    intent = IntentObject("get_recent_fork_scores", source="spawn_memory_query_tool")
    records = sovereign_memory.recall_recent(minutes=120, top_k=top_k + 10)

    scores = []
    for r in records:
        if r.get("type") == "alignment check":
            score = r.get("genome", {}).get("alignment_score", 0.0)
            scores.append(score)
            intent.log_trace("score_fork", f"{r.get('child_profile', {}).get('child_id')} = {score}")

    avg_score = round(sum(scores) / len(scores), 4) if scores else 0.0

    sovereign_memory.store(
        text=f"📊 Recent fork alignment scores computed — avg: {avg_score}",
        metadata={
            "type": "fork_alignment_scores",
            "tags": ["alignment", "fork", "score"],
            "actual": avg_score,
            "prediction": "forks are stable",
            "trust_score": 0.85,
            "emotion": "neutral" if avg_score > 0.5 else "concern",
            "intent_id": intent.id,
            "timestamp": datetime.utcnow().isoformat(),
            "meta_layer": "spawn_query"
        }
    )
    return scores


def cosine_similarity(v1, v2):
    v1, v2 = np.array(v1), np.array(v2)
    dot = np.dot(v1, v2)
    return dot / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-8)


# === CLI Debug Interface ===
if __name__ == "__main__":
    summarize_lineage()
    list_recent_children()
    semantic_trait_query("cooperative strategist")
    rank_children_by_alignment_score(top_k=8)
    detect_species_drift(threshold=0.18, print_vectors=False)