# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex/aei_layer/regret_interface.py
# Purpose: Stable interface for regret scoring to break circular dependency
# Status: 🔒 AEI-SAFE INTERFACE
# ============================================================

from aei_layer.fork_regret_engine import RegretScorer

# Exposed scoring function for forks
def score_regret_likelihood(fork_signal):
    """
    Calculates the regret-likelihood of a given decision fork.

    Args:
        fork_signal (dict): Snapshot of the forked belief/action trace
    Returns:
        float: Likelihood score between 0 and 1
    """
    return RegretScorer().compute_likelihood(fork_signal)