# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: utils/conflict_utils.py
# Purpose: Lightweight global fallback for conflict heat scoring
# Tier: Utility – No dependency recursion
# ============================================================

def score_conflict_heatmap(entry=None) -> float:
    """
    Lightweight contradiction scoring function that avoids circular imports.
    Evaluates symbolic conflict based on high-risk keywords in summaries.
    """
    try:
        if not entry: return 0.0
        summary = entry.get("summary", "").lower()

        risk_words = [
            "contradiction", "regret", "drift", "unstable",
            "collapse", "uncertain", "conflict", "divergent"
        ]
        matches = sum(1 for w in risk_words if w in summary)
        return round(min(matches * 0.25, 1.0), 3)
    except Exception:
        return 0.5