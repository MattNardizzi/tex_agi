# ============================================================
# 🧠 Tier 12 — Tex Reflex Consensus Cortex
# File: finance/strategy/alpha_consensus_voter.py
# Purpose: Determines alpha strategy consensus using cognitive drift, foresight, and variant analysis.
# Compliant with loopless, sovereign, and chrono-fusion reflex architecture.
# ============================================================

import hashlib
from datetime import datetime
from agentic_ai.sovereign_memory import sovereign_memory
from core_layer.tex_manifest import TEXPULSE
from utils.logging_utils import log_event


class AlphaConsensusVoter:
    def vote(self, top_variant, alpha=None, foresight=None):
        """
        Loopless reflex consensus voter for alpha strategy confirmation.

        Inputs:
            - top_variant: Selected strategy variant (dict)
            - alpha: Optional original alpha signal
            - foresight: Optional foresight projection used in synthesis

        Outputs:
            - dict containing consensus status and rationale
        """
        timestamp = datetime.utcnow().isoformat()
        emotion = TEXPULSE.get("emotional_state", "neutral")
        urgency = float(TEXPULSE.get("urgency", 0.72))
        entropy = float(TEXPULSE.get("entropy", 0.41))
        coherence = float(TEXPULSE.get("coherence", 0.77))

        confidence = top_variant.get("confidence", 0.5)
        regret = top_variant.get("regret", 0.4)
        coherence_score = top_variant.get("coherence", 0.6)

        score = (confidence * 0.5 + coherence_score * 0.4 - regret * 0.3)
        consensus = "approved" if score > 0.55 else "rejected"

        rationale = (
            f"Confidence={confidence:.2f}, Coherence={coherence_score:.2f}, "
            f"Regret={regret:.2f}, Score={score:.3f}"
        )

        fingerprint_base = f"{top_variant['id']}|{timestamp}|{score}"
        consensus_id = hashlib.sha256(fingerprint_base.encode()).hexdigest()[:12]

        # Store memory trace
        try:
            sovereign_memory.store(
                text=f"[CONSENSUS] {consensus.upper()} for {top_variant['id']}",
                metadata={
                    "tags": ["consensus_vote", consensus],
                    "timestamp": timestamp,
                    "urgency": urgency,
                    "entropy": entropy,
                    "coherence": coherence,
                    "confidence": confidence,
                    "regret": regret,
                    "meta_layer": "consensus_voter",
                    "strategy_id": top_variant.get("id", "unknown"),
                    "alpha_reference": alpha.get("strategy_id") if alpha else None,
                    "foresight_projection": foresight.get("projected_future") if foresight else None,
                    "consensus_score": round(score, 3),
                    "rationale": rationale,
                    "consensus_id": consensus_id
                }
            )
        except Exception as e:
            log_event(f"[CONSENSUS ERROR] Memory store failed: {e}", level="error")

        return {
            "consensus": consensus,
            "rationale": rationale,
            "consensus_id": consensus_id,
            "score": round(score, 3),
            "timestamp": timestamp
        }


# === Manual Test ===
if __name__ == "__main__":
    voter = AlphaConsensusVoter()
    result = voter.vote(
        top_variant={"id": "variant_3", "confidence": 0.68, "coherence": 0.72, "regret": 0.29}
    )
    print("\n[CONSENSUS RESULT]")
    print(result)