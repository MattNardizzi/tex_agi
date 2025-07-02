# agentic_ai/integrity_tools.py

from core_agi_modules.recursive_self_model import RecursiveSelfModel

def integrity_score() -> float:
    model = RecursiveSelfModel()
    state = model.evaluate_self_state()
    return round(state.get("integrity", 1.0), 4)