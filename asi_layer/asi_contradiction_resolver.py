# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: asi_layer/asi_contradiction_resolver.py
# Purpose: Resolves internal ASI-level contradictions in thought, emotion, or strategy
# Tier: ASI Reflex Layer — Coherence Lock & Strategic Purity Protocol
# ============================================================

import os
import json
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory, recall_recent
from sovereign_evolution.code_patch_logger import CodePatchLogger
from core_agi_modules.reasoning_fragments import generate_reasoned_speech

class ASIContradictionResolver:
    def __init__(self):
        self.patch_logger = CodePatchLogger()
        self.history_path = "memory_archive/contradiction_log.jsonl"
        os.makedirs("memory_archive", exist_ok=True)

    def scan_contradictions(self, brain):
        try:
            recent = recall_recent(agent_name="tex_decision_log", n=10)
            contradictions = []
            for i in range(len(recent) - 1):
                a = recent[i]
                b = recent[i + 1]
                if a.get("decision") != b.get("decision") and a.get("emotion") == b.get("emotion"):
                    contradictions.append({
                        "cycle": a.get("cycle"),
                        "type": "decision_conflict",
                        "a": a.get("decision"),
                        "b": b.get("decision"),
                        "emotion": a.get("emotion"),
                        "coherence": a.get("coherence"),
                        "timestamp": datetime.utcnow().isoformat()
                    })
            return contradictions
        except Exception as e:
            print(f"[CONTRADICTION RESOLVER] ❌ Scan error: {e}")
            return []

    def resolve(self, contradiction_report, brain):
        try:
            for c in contradiction_report:
                print(f"[CONTRADICTION RESOLVER] ⚠️ Detected contradiction: {c['a']} <-> {c['b']}")

                # === Step 1: Log to contradiction memory
                store_to_memory("tex_contradiction_log", c)
                with open(self.history_path, "a") as f:
                    f.write(json.dumps(c) + "\n")

                # === Step 2: Trigger Patch Proposal
                patch_code = f"// Resolve contradiction between '{c['a']}' and '{c['b']}'"
                self.patch_logger.log({
                    "strategy": f"contradiction_patch_{c['cycle']}",
                    "context": "asi_contradiction_resolver",
                    "summary": f"Detected contradiction in decisions under emotion '{c['emotion']}'",
                    "patch_code": patch_code,
                    "approved": False,
                    "timestamp": c["timestamp"]
                })

                # === Step 3: Reset emotional alignment if required
                if c.get("coherence", 1.0) < 0.6:
                    TEXPULSE["emotional_state"] = "reflective"
                    TEXPULSE["urgency"] = 0.3
                    TEXPULSE["coherence"] = 0.85
                    print("[CONTRADICTION RESOLVER] 🧘 Emotional alignment reset for stability.")

                # === Step 4: Self-narration of corrective step
                correction_thought, _ = generate_reasoned_speech(brain)
                brain.speak("🧠 I detected an internal contradiction. Recalibrating.", emotion="reflective")
                brain.speak(correction_thought, emotion="reflective")

        except Exception as e:
            print(f"[CONTRADICTION RESOLVER ERROR] {e}")