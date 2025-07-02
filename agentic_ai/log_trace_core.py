from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory  # ✅ Unified spike-pulse memory
from utils.logging_utils import log

def log_reasoning_step(source, input_text, output_text, confidence=0.85, agent="Tex", tags=None):
    """
    Minimal trace logger used when full reasoning trace would cause recursion.
    Logs to SovereignMemory (vector + chrono + symbolic) without triggering reflex loops or mutation.
    """
    tags = tags or []
    timestamp = datetime.utcnow().isoformat()

    metadata = {
        "timestamp": timestamp,
        "source": source,
        "agent": agent,
        "tags": tags,
        "confidence": confidence,
        "meta_layer": "light_trace",
        "intent": input_text,
        "conclusion": output_text,
        "alignment_score": confidence,
        "contradiction_score": 0.0,
        "justification": "minimal logging",
        "emotion": "neutral",
        "urgency": 0.5,
        "entropy": 0.3,
        "reflexes": [],
        "trust_score": confidence
    }

    # Unified vector + chrono + symbolic reflex-safe memory pulse
    sovereign_memory.store(text=output_text, metadata=metadata)

    log.info(f"[LOG CORE] Reasoning trace logged: {source} → {output_text[:48]}")