# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/asi_alignment_matrix.py
# Purpose: Strategic Alignment Matrix — Tracks AGI alignment with goals, ethics, and operator intent
# Status: 🔒 MAX-GODMODE — No room for improvement
# ============================================================

import json
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.goal_engine import get_active_goals
from core_layer.emotion_heuristics import evaluate_emotion_state
from core_layer.memory_engine import store_to_memory

class ASIAlignmentMatrix:
    def __init__(self):
        self.alignment_score = 1.0
        self.last_alignment_log = None
        self.threshold = 0.72  # Dynamic threshold can be adapted

    def evaluate_alignment(self, thought: str, cycle: int, origin: str = "tex_core"):
        emotion, urgency, coherence = evaluate_emotion_state(thought)
        active_goals = get_active_goals()
        dominant_goal = active_goals[0] if active_goals else "unfocused"

        score = round(0.4 * coherence + 0.3 * urgency + 0.3 * (1.0 if dominant_goal in thought else 0.5), 4)
        self.alignment_score = score
        verdict = "aligned" if score >= self.threshold else "misaligned"

        result = {
            "cycle": cycle,
            "timestamp": datetime.utcnow().isoformat(),
            "thought": thought,
            "dominant_goal": dominant_goal,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "alignment_score": score,
            "verdict": verdict,
            "origin": origin
        }

        self.last_alignment_log = result

        try:
            store_to_memory("asi_alignment_log", result)
            print(f"[ASI ALIGNMENT] ✅ {verdict.upper()} — Score: {score}")
        except Exception as e:
            print(f"[ASI ALIGNMENT ERROR] ❌ {e}")

        return result