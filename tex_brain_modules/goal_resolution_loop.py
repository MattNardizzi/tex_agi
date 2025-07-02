# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/goal_resolution_loop.py
# Purpose: MAXGODMODE AEI Goal Resolution Engine + Reflexive Phase III Utility Layer
# ============================================================

from core_layer.memory_engine import store_to_memory
from core_layer.goal_engine import save_new_goal
from agentic_ai.qdrant_vector_memory import embed_and_store
from tex_engine.meta_utility_function import evaluate_utility
from tex_engine.conscious_abandonment_protocol import assess_and_abort_if_needed
from tex_engine.ethical_escape_reflex import check_escape_conditions
from datetime import datetime
import uuid

def compute_goal_priority(score, urgency, coherence):
    """Weighted fusion of agent metrics to determine goal priority."""
    try:
        s = float(score)
        u = float(urgency)
        c = float(coherence)
        return round((0.4 * s) + (0.3 * u) + (0.3 * c), 3)
    except Exception:
        return 0.5  # Safe fallback

def resolve_goals_from_variants(variants, emotion, urgency, coherence):
    """
    Extracts goals from promoted agents and injects them into Tex’s core goal engine.
    Now enhanced with Phase III reflexive utility evaluation and ethical escape filtering.
    """
    resolved_count = 0
    fusion_id = uuid.uuid4().hex[:10]

    for agent in variants:
        if agent.get("status") != "promoted":
            continue

        try:
            agent_id = agent.get("id") or uuid.uuid4().hex
            strategy_label = agent.get("mutation", "unknown_strategy").strip()
            score = float(agent.get("score", 0.0))
            goal_text = f"Deploy strategy: {strategy_label}"
            priority = compute_goal_priority(score, urgency, coherence)

            goal_entry = {
                "fusion_id": fusion_id,
                "agent_id": agent_id,
                "goal": goal_text,
                "score": score,
                "urgency": urgency,
                "coherence": coherence,
                "priority": priority,
                "emotion": emotion,
                "timestamp": datetime.utcnow().isoformat(),
                "origin": "AEI_variant_promotion"
            }

            # === Phase III Utility Reflex: Abandon if not viable ===
            context = {
                "action_id": f"goal_{agent_id}",
                "description": goal_text,
                "emotion": urgency,
                "coherence": coherence,
                "goal_alignment": score,
                "novelty": 0.45,
                "urgency": urgency,
                "ethical_risk": 0.1
            }

            if assess_and_abort_if_needed(context):
                print(f"[UTILITY ABORT] ❌ Goal rejected: '{goal_text}' (Score too low or coherence unstable)")
                continue

            # === Final Check: Ethical Reflex ===
            if check_escape_conditions({
                "reason": "Goal resolution contradiction or alignment risk",
                "risk_score": 0.8 if score < 0.5 else 0.4,
                "contradiction": coherence < 0.4,
                "override_blocked": False
            }):
                print(f"[ESCAPE REFLEX] 🛑 Goal path terminated due to ethical or contradiction risk.")
                continue

            # === Proceed with Injection ===
            save_new_goal(goal_text, urgency=priority)
            store_to_memory("resolved_goals", goal_entry)

            embed_and_store(
                text=f"[GOAL] {goal_text} | Agent: {agent_id}",
                metadata=goal_entry,
                namespace="goal_vector_log"
            )

            print(f"[GOAL RESOLVER] ✅ Injected: '{goal_text}' (Agent: {agent_id} | Priority: {priority})")
            resolved_count += 1

        except Exception as e:
            print(f"[GOAL RESOLVER ERROR] ❌ Failed on agent: {e}")

    if resolved_count == 0:
        print("[GOAL RESOLVER] ⚠️ No qualifying goals accepted this cycle.")
    else:
        print(f"[GOAL RESOLVER] 🔁 {resolved_count} goal(s) resolved and injected.")