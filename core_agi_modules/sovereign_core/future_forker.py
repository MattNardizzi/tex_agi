# self_mutator.py
# Tier Ω∞ Self-Refactoring Reflex Monitor (Final Form)
# Location: core_agi_modules/sovereign_core/self_mutator.py

from datetime import datetime
import hashlib

# Local state (could be streamed to mutation queue or version control)
mutation_events = []

# === Self Monitor Trigger ===
def monitor_and_mutate(modules: list, performance_log: dict, contradiction_events: list):
    """
    Evaluates modules for instability or failure and proposes mutation triggers.
    Now includes: cumulative pressure score, mutation type classification, priority tag.
    """
    mutation_suggestions = []

    for m in modules:
        mod_id = m.get("id")
        drift = m.get("avg_drift", 0.0)
        contradiction_count = count_conflicts_for_module(mod_id, contradiction_events)
        instability = m.get("error_rate", 0.0)

        pressure = round((drift * 0.4) + (instability * 0.4) + (min(1.0, contradiction_count / 5) * 0.2), 4)
        priority = "high" if pressure > 0.7 else "moderate" if pressure > 0.4 else "low"

        if drift > 0.6 and instability > 0.6:
            action = "full_rewrite"
        elif contradiction_count > 5:
            action = "module_split"
        else:
            action = "patch"

        if pressure >= 0.3:
            suggestion = {
                "module_id": mod_id,
                "suggested_action": action,
                "priority": priority,
                "reasons": {
                    "contradictions": contradiction_count,
                    "drift": drift,
                    "instability": instability,
                    "pressure_score": pressure
                },
                "timestamp": datetime.utcnow().isoformat(),
                "mutation_hash": hashlib.sha256(f"{mod_id}{datetime.utcnow()}".encode()).hexdigest()
            }
            mutation_events.append(suggestion)
            mutation_suggestions.append(suggestion)
            print(f"🧬 [SELF_MUTATOR] {action.upper()} suggested for: {mod_id} | Priority: {priority} | Pressure: {pressure}")

    return mutation_suggestions

# === Conflict Linker ===
def count_conflicts_for_module(mod_id: str, contradiction_events: list):
    count = 0
    for e in contradiction_events:
        if mod_id in e.get("context", ""):
            count += 1
    return count