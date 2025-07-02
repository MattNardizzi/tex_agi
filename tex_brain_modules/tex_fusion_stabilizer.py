# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/tex_fusion_stabilizer.py
# Purpose: Controls fork validation, fusion entropy thresholds, and spam prevention
# ============================================================

from datetime import datetime
from core_layer.memory_engine import store_to_memory


class TexFusionStabilizer:
    def __init__(self, fork_budget=10, entropy_threshold=0.75):
        self.fork_budget = fork_budget
        self.entropy_threshold = entropy_threshold
        self.fusion_counter = 0

    def validate_fusion(self, fused_from_list):
        """
        Validates whether a proposed fusion should proceed, based on:
        - Corruption flags
        - Fork budget limits
        - Entropy diversity threshold
        """
        unique_ids = set(fused_from_list)
        corrupted = [aeon for aeon in unique_ids if aeon in {"AEON_000", "UNKNOWN"}]

        if corrupted:
            print("[FUSION STABILIZER] ❌ Corrupted AEONs detected — fusion rejected.")
            for aeon in corrupted:
                print(f"[FUSION STABILIZER] ⚠️ Rejection reason → {aeon}: invalid identity")
            self.log_blocked_fusion(fused_from_list, reason="corrupted_aeons_detected")
            return False

        if len(unique_ids) > self.fork_budget:
            print(f"[FUSION STABILIZER] ⚠️ Fork budget exceeded ({len(unique_ids)}/{self.fork_budget}) — delaying fusion.")
            self.log_blocked_fusion(fused_from_list, reason="fork_budget_exceeded")
            return False

        entropy = self._calculate_entropy(fused_from_list)
        if entropy > self.entropy_threshold:
            print(f"[FUSION STABILIZER] ⚠️ Entropy too high: {entropy:.2f} — fusion deferred.")
            self.log_blocked_fusion(fused_from_list, reason=f"entropy_too_high:{entropy:.2f}")
            return False

        print(f"[FUSION STABILIZER] ✅ Fusion approved. Entropy: {entropy:.2f}")
        return True

    def _calculate_entropy(self, fused_from_list):
        """
        Calculates diversity entropy as ratio of unique identities to total inputs.
        """
        unique = set(fused_from_list)
        return round(len(unique) / max(1, len(fused_from_list)), 4)

    def log_blocked_fusion(self, fused_from_list, reason="unspecified"):
        """
        Logs blocked fusion attempts to memory for later audit or analysis.
        """
        MAX_LOG = 10
        clean_ids = [aid for aid in fused_from_list if aid not in {"UNKNOWN", "AEON_000"}]

        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "sampled_rejected": clean_ids[-MAX_LOG:],  # Limit to last 10
            "rejected_count": len(clean_ids),
            "reason": reason
        }

        try:
            store_to_memory("blocked_fusion_attempts", log_entry)
        except Exception as e:
            print(f"[FUSION STABILIZER] ❌ Failed to log blocked fusion: {e}")