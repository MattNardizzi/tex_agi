# ============================================================
# © 2025 VortexBlack / Sovereign Cognition. All rights reserved.
# File: core_layer/meta_awareness_bridge.py
# Purpose: Internal cognitive bias detection + memory correction (Tex AGI)
# Tier: Reflex-Pulse Meta Bridge – Bias Auditing & Reflex Logging
# ============================================================

import random
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from agentic_ai.sovereign_memory import sovereign_memory


# === Reflexive Bias Detector ===
def detect_bias_drift(memory_log):
    """
    Scans recent Qdrant vector memory payloads for cognitive bias.
    Operates only on ScoredPoint.payload structures.
    """
    if not memory_log:
        return "No memory entries to evaluate."

    report = []
    detected = False

    for entry in memory_log[-10:]:
        if not hasattr(entry, "payload"):
            continue

        payload = entry.payload
        data = payload.get("data", {})
        reasoning = data.get("reasoning", "")
        emotion = data.get("emotion", "")
        confidence = data.get("confidence", 0.5)
        timestamp = payload.get("timestamp", "")
        entry_id = payload.get("id", None)

        if not reasoning:
            continue

        # === Optimism bias check
        if emotion == "hope" and confidence > 0.8:
            sovereign_memory.store(
                text="Potential optimism bias detected.",
                metadata={
                    "agent": "TEX",
                    "intent": "bias_alert",
                    "conclusion": "Potential optimism bias detected.",
                    "tags": ["bias", "optimism", "drift"],
                    "urgency": 0.4,
                    "emotion": emotion,
                    "entropy": 0.6,
                    "timestamp": timestamp,
                    "reflexes": ["bias_scan", "meta_awareness"],
                    "justification": reasoning,
                    "meta_layer": "symbolic_trace"
                }
            )
            report.append(f"[BIAS ALERT] Optimism bias at {timestamp}")
            detected = True

        # === Overconfidence detection
        if "100%" in reasoning or confidence == 1.0:
            sovereign_memory.store(
                text="Overconfidence risk detected.",
                metadata={
                    "agent": "TEX",
                    "intent": "bias_alert",
                    "conclusion": "Overconfidence risk detected.",
                    "tags": ["bias", "overconfidence"],
                    "urgency": 0.7,
                    "emotion": emotion,
                    "timestamp": timestamp,
                    "reflexes": ["bias_patch", "meta_awareness"],
                    "justification": reasoning,
                    "meta_layer": "symbolic_trace"
                }
            )
            report.append(f"[BIAS ALERT] Overconfidence at {timestamp}")
            detected = True

        # === Emotional volatility check
        if emotion in ["fear", "joy"] and "conflict" in reasoning.lower():
            sovereign_memory.store(
                text="Emotional volatility influencing decision logic.",
                metadata={
                    "agent": "TEX",
                    "intent": "bias_alert",
                    "conclusion": "Emotional volatility influencing decision logic.",
                    "tags": ["bias", "emotional", "volatility"],
                    "urgency": 0.6,
                    "emotion": emotion,
                    "entropy": 0.5,
                    "timestamp": timestamp,
                    "reflexes": ["bias_flag", "meta_awareness"],
                    "justification": reasoning,
                    "meta_layer": "symbolic_trace"
                }
            )
            report.append(f"[BIAS ALERT] Emotional volatility at {timestamp}")
            detected = True

    return "\n".join(report) if detected else "No cognitive bias detected in recent memory."


# === Symbolic Meta Logger ===
def log_meta_trace(category, label, data, source):
    """
    Stores structured trace entries for high-level AGI cognition and system self-awareness.
    """
    sovereign_memory.store(
        text=label,
        metadata={
            "agent": "TEX",
            "intent": "meta_trace_log",
            "conclusion": label,
            "tags": [category, "meta_trace"],
            "urgency": 0.4,
            "entropy": 0.3,
            "emotion": TEXPULSE.get("emotional_state", "neutral"),
            "timestamp": datetime.utcnow().isoformat(),
            "reflexes": ["meta_bridge_trace"],
            "justification": str(data),
            "source": source,
            "meta_layer": "symbolic_trace"
        }
    )


# === Optional Debug Run ===
if __name__ == "__main__":
    class MockScoredPoint:
        def __init__(self, payload):
            self.payload = payload

    mock_memory = [
        MockScoredPoint({
            "id": "trace-001",
            "timestamp": datetime.utcnow().isoformat(),
            "data": {
                "reasoning": "Market sentiment high — 100% upside in TSLA",
                "emotion": "hope",
                "confidence": 1.0
            }
        }),
        MockScoredPoint({
            "id": "trace-002",
            "timestamp": datetime.utcnow().isoformat(),
            "data": {
                "reasoning": "Conflict detected in QQQ forecast, too much volatility.",
                "emotion": "fear",
                "confidence": 0.6
            }
        }),
    ]

    print(detect_bias_drift(mock_memory))