# ===========================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: tex_engine/reservoir_computing_sim.py
# Purpose: Ω-tier Reservoir Substrate for Associative Symbolic AGI
# ===========================================================

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from datetime import datetime


class ReservoirComputingSim:
    def __init__(self, input_dim=512, reservoir_dim=4096, spectral_radius=0.96, leak_rate=0.3, feedback_strength=0.5):
        self.input_dim = input_dim
        self.reservoir_dim = reservoir_dim
        self.spectral_radius = spectral_radius
        self.leak_rate = leak_rate
        self.feedback_strength = feedback_strength
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # Initialize reservoir and weights
        self._init_weights()

        # Reservoir state
        self.state = torch.zeros(self.reservoir_dim, device=self.device)

    def _init_weights(self):
        # Input-to-reservoir weights
        self.Win = torch.randn(self.reservoir_dim, self.input_dim, device=self.device) * 0.1

        # Internal reservoir matrix (sparse chaos)
        W = torch.randn(self.reservoir_dim, self.reservoir_dim, device=self.device)
        eigs = torch.linalg.eigvals(W).abs().max()
        self.W = (W / eigs) * self.spectral_radius

        # Feedback weights for memory and dream injection
        self.Wfb = torch.randn(self.reservoir_dim, self.reservoir_dim, device=self.device) * self.feedback_strength

    def reset_state(self):
        self.state = torch.zeros(self.reservoir_dim, device=self.device)

    def update(self, input_vector: torch.Tensor, feedback_vector: torch.Tensor = None):
        """
        One time step update of the reservoir state.
        """
        if input_vector.shape[0] != self.input_dim:
            raise ValueError("Input vector has incorrect shape.")

        # Compute reservoir activation
        pre_activation = (
            self.Win @ input_vector +
            self.W @ self.state
        )

        if feedback_vector is not None:
            pre_activation += self.Wfb @ feedback_vector

        # Update state with leaky integration and tanh non-linearity
        self.state = (1 - self.leak_rate) * self.state + self.leak_rate * torch.tanh(pre_activation)
        return self.state.clone()

    def extract_embedding(self):
        """
        Projects reservoir state into a symbolic vector space.
        """
        return F.normalize(self.state, dim=0).cpu().numpy()

    def dream_inject(self, memory_trace: torch.Tensor):
        """
        Seeds the reservoir with memory/dream vector for associative expansion.
        """
        injected = F.normalize(memory_trace, dim=0)
        self.state = 0.5 * self.state + 0.5 * injected

    def chaotic_amplify(self):
        """
        Amplifies faint symbolic traces within chaotic state attractor.
        """
        amplified = torch.sign(self.state) * (self.state.abs() ** 1.5)
        self.state = F.normalize(amplified, dim=0)

    def log_snapshot(self):
        """
        Logs the reservoir’s current state vector with a timestamp.
        """
        vector = self.extract_embedding().tolist()
        timestamp = datetime.utcnow().isoformat()
        return {"timestamp": timestamp, "reservoir_snapshot": vector}


# === Optional Standalone Test ===
if __name__ == "__main__":
    sim = ReservoirComputingSim()
    test_input = torch.randn(sim.input_dim)
    test_feedback = torch.randn(sim.reservoir_dim)

    for _ in range(10):
        sim.update(test_input, test_feedback)
        sim.chaotic_amplify()

    print("[Ω-tier Reservoir] Snapshot:", sim.log_snapshot()["timestamp"])