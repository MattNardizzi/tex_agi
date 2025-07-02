# ============================================================
# Tex Awareness Sync – Cognitive State Broadcasting Engine
# Tier: ΩΩΩ – Self/Swarm Signature + Introspective Diff Logger
# ============================================================

import hashlib
from datetime import datetime
from pathlib import Path

AWARENESS_LOG_PATH = Path("agentic_ai/tex_operator_sync.txt")

class TexAwarenessSync:
    def __init__(self, operator_name="Unknown"):
        self.operator = operator_name
        self.log_file = AWARENESS_LOG_PATH
        self._ensure_log_file()

    def register_node(self, label: str, value):
        timestamp = self._now()
        line = f"[AWARENESS NET] 🧠 Node registered → {label}: {value} @ {timestamp}"
        print(line)
        self._write(line)

    def live_summary(self, data: dict):
        timestamp = self._now()
        summary = f"[AWARENESS NET] 🔎 Live Summary: {data} @ {timestamp}"
        print(summary)
        self._write(summary)

    def broadcast_state_packet(self, packet: dict, source: str = "unknown"):
        """
        Emit a full awareness packet with origin and timestamp.
        """
        timestamp = self._now()
        summary = f"[AWARENESS] 🛰️ Packet from {source} @ {timestamp}:\n{packet}"
        print(summary)
        self._write(summary)

    def _write(self, line: str):
        try:
            with self.log_file.open("a") as f:
                f.write(line + "\n")
        except Exception as e:
            print(f"[AwarenessSync ERROR] Could not write to log: {e}")

    def _now(self) -> str:
        return datetime.utcnow().isoformat()

    def _ensure_log_file(self):
        if not self.log_file.exists():
            self.log_file.parent.mkdir(parents=True, exist_ok=True)
            self.log_file.touch()

# === 🧠 Utility: Reflex Signature ===
def get_reflex_signature(reflex_packet: dict) -> str:
    """
    Generates a hash-based signature string from reflex packet contents.
    """
    reflex_type = reflex_packet.get("type", "UNKNOWN")
    payload = reflex_packet.get("payload", {})
    entropy = reflex_packet.get("entropy", 0.0)
    intensity = payload.get("intensity", 0.0)
    composite = f"{reflex_type}|E:{entropy:.3f}|I:{intensity:.3f}"
    hash_digest = hashlib.sha256(composite.encode()).hexdigest()[:12]
    return f"{composite}|HASH:{hash_digest}"

# === Optional: Future Scoring Heuristic ===
def awareness_score(reflexes: list) -> float:
    """
    Stub: computes an aggregated awareness score from a list of reflexes.
    Could combine entropy, alignment, and consensus cohesion.
    """
    if not reflexes:
        return 0.0
    return sum([r.get("entropy", 0) for r in reflexes]) / len(reflexes)