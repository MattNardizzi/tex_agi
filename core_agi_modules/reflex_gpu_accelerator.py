# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: core_agi_modules/reflex_gpu_accelerator.py
# Tier: Ω∞ — Reflex Acceleration via GPU (PyTorch)
# Purpose: Accelerates reflex signal processing using GPU tensors
# ============================================================

import torch
from datetime import datetime

class ReflexGPUAccelerator:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.last_eval_time = None
        print(f"[GPU_ACCELERATOR] Initialized on device: {self.device}")

    def evaluate_reflex_signals(self, signal_batch: list[dict]) -> list[tuple[str, float]]:
        """
        Accepts a list of reflex signals with keys:
        - 'reflex': name of the reflex
        - 'urgency': float
        - 'valence': float
        - 'memory_pressure': float
        - 'coherence': float

        Returns ranked list of reflexes by composite weighted score.
        """
        if not signal_batch:
            return []

        names = [s['reflex'] for s in signal_batch]

        data = torch.tensor([
            [s.get('urgency', 0.0),
             s.get('valence', 0.0),
             s.get('memory_pressure', 0.0),
             s.get('coherence', 1.0)]
            for s in signal_batch
        ], dtype=torch.float32, device=self.device)

        # === Weight Vector: [urgency, valence, memory, inverse coherence]
        weights = torch.tensor([0.35, 0.25, 0.25, 0.15], device=self.device)
        inv_coherence = 1.0 - data[:, 3]
        data[:, 3] = inv_coherence

        scores = torch.matmul(data, weights)
        scored = list(zip(names, scores.tolist()))
        ranked = sorted(scored, key=lambda x: -x[1])
        self.last_eval_time = datetime.utcnow().isoformat()

        return ranked

    def get_device(self):
        return self.device

    def get_last_eval_time(self):
        return self.last_eval_time

# === Singleton instance ===
gpu_accelerator = ReflexGPUAccelerator()