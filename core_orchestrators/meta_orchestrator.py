# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/meta_coherence_loop.py
# Tier 4 AGI Module — Meta Coherence Loop (Recursive Integrity Monitor)
# Mode: Reflex-Gated Drift Monitor with Sovereign Override Triggering
# ============================================================

import difflib
import datetime
import json
import os
from collections import deque

from aei_layer.counterfactual_memory_engine import get_last_counterfactual
from sovereign_evolution.sovereign_cognition_fire import (
    score_conflict_heatmap,
    trigger_sovereign_override
)
from tex_brain_modules.memory_manager import store_meta_trace
from core_layer.utils.memory_utils import clean_text
from core_layer.tex_consciousness_matrix import TexConsciousnessMatrix
from tex_engine.tex_reflex_patch_filter import should_allow_override

META_CORRECTION_LOG = "memory_archive/meta_coherence_log.jsonl"
OVERRIDE_TRIGGER_LOG = "memory_archive/override_triggers.jsonl"
os.makedirs("memory_archive", exist_ok=True)

class MetaCoherenceLoop:
    def __init__(self, memory_window=6):
        self.thought_history = deque(maxlen=memory_window)
        self.coherence_log = []
        self.current_score = 1.0
        self.consciousness = TexConsciousnessMatrix()

    def log_thought(self, thought: str) -> float:
        thought = clean_text(thought)
        if not thought or len(thought) < 5:
            return self.current_score

        timestamp = datetime.datetime.utcnow().isoformat()
        self.thought_history.append({"text": thought, "timestamp": timestamp})

        total_similarity = 0.0
        total_conflicts = 0
        contradiction_pairs = []
        weighted_penalty = 0.0

        for i in range(len(self.thought_history) - 1):
            t1 = self.thought_history[i]["text"]
            t2 = self.thought_history[i + 1]["text"]
            t1_ts = self.thought_history[i]["timestamp"]
            t2_ts = self.thought_history[i + 1]["timestamp"]

            similarity = difflib.SequenceMatcher(None, t1, t2).ratio()
            total_similarity += similarity

            contradiction_score = self._contradiction_score(t1, t2)
            if contradiction_score > 0:
                time_diff = (datetime.datetime.fromisoformat(t2_ts) - datetime.datetime.fromisoformat(t1_ts)).total_seconds()
                decay_factor = max(0.1, 1.0 - time_diff / 300)
                weighted_penalty += contradiction_score * decay_factor
                contradiction_pairs.append((t1, t2))
                total_conflicts += 1

        avg_similarity = total_similarity / max(1, len(self.thought_history) - 1)

        heatmap_score = 0.0
        try:
            heatmap_raw = score_conflict_heatmap()
            heatmap_score = float(heatmap_raw.get("score", 0.0)) if isinstance(heatmap_raw, dict) else float(heatmap_raw)
            weighted_penalty += heatmap_score * 0.1
        except Exception as e:
            print(f"[COHERENCE] ⚠️ Heatmap fetch failed: {e}")

        coherence_score = max(0.0, min(1.0, avg_similarity - weighted_penalty))
        self.current_score = round(coherence_score, 3)

        # Optional counterfactual
        ct_flag = None
        try:
            last_ct = get_last_counterfactual()
            if last_ct:
                ct_flag = {
                    "counterfactual": last_ct.get("counterfactual"),
                    "regret_score": last_ct.get("regret_score"),
                    "timestamp": last_ct.get("timestamp")
                }
        except Exception as e:
            print(f"[COHERENCE] ⚠️ CTRM access error: {e}")

        drift_score = 0.0
        if len(self.thought_history) >= 4:
            drift_score = 1 - difflib.SequenceMatcher(None,
                self.thought_history[0]["text"],
                self.thought_history[-1]["text"]
            ).ratio()
            if drift_score > 0.5:
                print(f"[DRIFT] ⚠️ High drift detected: {round(drift_score, 2)}")

        meta_entry = {
            "timestamp": timestamp,
            "score": self.current_score,
            "conflicts": total_conflicts,
            "heatmap_penalty": round(heatmap_score, 3),
            "drift_score": round(drift_score, 3),
            "thoughts": list(self.thought_history),
            "counterfactual": ct_flag
        }

        self.coherence_log.append(meta_entry)
        store_meta_trace("meta_coherence_loop", meta_entry)

        print(f"[META COHERENCE] 🧐 Score: {self.current_score} | Conflicts: {total_conflicts} | Drift: {round(drift_score, 2)} | Heatmap: {round(heatmap_score, 2)}")

        # Optional contradiction reconciliation
        if contradiction_pairs and self.current_score >= 0.7:
            for t1, t2 in contradiction_pairs:
                correction = {
                    "timestamp": timestamp,
                    "reconciled_pair": [t1, t2],
                    "reason": "High-coherence contradiction reconciliation",
                    "confidence": self.current_score
                }
                try:
                    with open(META_CORRECTION_LOG, "a") as f:
                        f.write(json.dumps(correction) + "\n")
                except Exception as e:
                    print(f"[CORRECTION LOG ERROR] {e}")

        # === Sovereign Override with Reflex Filter ===
        if self.current_score < 0.4:
            try:
                matrix_state = self.consciousness.get_state()
                if should_allow_override(matrix_state):
                    print("[META COHERENCE] 🔥 Reflex filter passed. Triggering override...")
                    trigger_sovereign_override(
                        context="meta_coherence_loop",
                        issue="Critical contradiction",
                        score=self.current_score,
                        force=True
                    )
                else:
                    print("[META COHERENCE] ⛔ Reflex filter blocked override due to unstable matrix.")
                    self._log_override_block(timestamp, ct_flag, heatmap_score, drift_score)
            except Exception as e:
                print(f"[OVERRIDE TRIGGER ERROR] ❌ {e}")

        return self.current_score

    def _log_override_block(self, timestamp, ct_flag, heatmap_score, drift_score):
        try:
            block_log = {
                "timestamp": timestamp,
                "reason": "Override blocked by unstable consciousness",
                "heatmap": round(heatmap_score, 3),
                "drift_score": round(drift_score, 3),
                "counterfactual": ct_flag,
                "thought_trace": list(self.thought_history)
            }
            with open(OVERRIDE_TRIGGER_LOG, "a") as f:
                f.write(json.dumps(block_log) + "\n")
        except Exception as e:
            print(f"[BLOCK LOG ERROR] {e}")

    def _contradiction_score(self, a: str, b: str) -> float:
        if not isinstance(a, str) or not isinstance(b, str):
            return 0.0
        a_lower, b_lower = a.lower(), b.lower()
        weights = {
            "fail": 1.0,
            "opposite": 0.8,
            "contradict": 0.7,
            "never": 0.5,
            "not": 0.4,
            "no": 0.3
        }
        return sum(weight for kw, weight in weights.items() if kw in a_lower and kw in b_lower and a_lower != b_lower)

    def get_log(self, limit=5):
        return self.coherence_log[-limit:]

    def reset(self):
        self.thought_history.clear()
        self.coherence_log.clear()
        self.current_score = 1.0