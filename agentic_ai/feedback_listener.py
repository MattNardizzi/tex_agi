# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: agentic_ai/feedback_listener.py
# Purpose: Live Human Reinforcement Listener — Direct Cognitive Steering of Tex
# Status: ✅ ACTIVE — Phase 2 Enhancement (Human-in-the-Loop Alignment Tracer)
# ============================================================

import threading
import time
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory
from agentic_ai.qdrant_vector_memory import embed_and_store

# Optional: Tie votes to reinforcement or mutation
from agentic_ai.reinforcement import AdaptiveReinforcer
from sovereign_evolution.sovereign_cognition_fire import trigger_sovereign_override

class HumanFeedbackListener:
    def __init__(self, tex_instance):
        self.brain = tex_instance
        self.reinforcer = AdaptiveReinforcer()
        self.last_feedback_timestamp = None

    def listen_loop(self):
        while True:
            try:
                latest = self.brain.last_spoken_thought or "[NO OUTPUT YET]"
                print("\n🗣️ [TEX OUTPUT] →", latest)
                feedback = input("🗳️ [VOTE] Was this helpful? (y/n/1-10): ").strip().lower()

                score = None
                if feedback in ['y', 'yes']:
                    score = 1.0
                elif feedback in ['n', 'no']:
                    score = 0.0
                elif feedback.isdigit():
                    score = min(max(int(feedback), 0), 10) / 10.0

                if score is not None:
                    feedback_entry = {
                        "cycle": self.brain.cycle_counter,
                        "score": score,
                        "thought": latest,
                        "emotion": TEXPULSE.get("emotional_state"),
                        "urgency": TEXPULSE.get("urgency"),
                        "coherence": TEXPULSE.get("coherence"),
                        "timestamp": datetime.utcnow().isoformat()
                    }

                    store_to_memory("human_feedback_log", feedback_entry)

                    embed_and_store(
                        text=f"[HUMAN FEEDBACK] {latest}",
                        metadata=feedback_entry
                    )

                    print(f"✅ Feedback logged | Score: {score}")

                    # Tie into reinforcement if score is high
                    if score >= 0.7:
                        self.reinforcer.assess(
                            decision=latest,
                            reward=score,
                            context="human_feedback",
                            cycle=self.brain.cycle_counter
                        )
                    elif score <= 0.3:
                        print("🚨 Low feedback score. Considering override...")
                        trigger_sovereign_override(
                            context="human_feedback",
                            regret=1.0 - score,
                            foresight=0.2,
                            coherence=0.3,
                            force=True
                        )

                else:
                    print("⚠️ Invalid input. Please use y/n or 1-10.")

            except Exception as e:
                print(f"[FEEDBACK LISTENER ERROR] {e}")

            time.sleep(3)

# === Launch listener thread ===
def start_feedback_listener(tex_instance):
    listener = HumanFeedbackListener(tex_instance)
    t = threading.Thread(target=listener.listen_loop, daemon=True)
    t.start()
