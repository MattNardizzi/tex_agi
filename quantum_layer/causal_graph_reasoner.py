# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC – All rights reserved.
# File: symbolic_layer/causal_graph_reasoner.py
# License: Private IP – Ω-tier cognition
# Purpose: Deductive engine for symbolic-causal reasoning + QAOA feedback + contradiction-driven spawning
# ============================================================

import time
import networkx as nx
from tex_engine.cognitive_event_router import CognitiveEvent, dispatch_event
from quantum_layer.quantum_randomness import quantum_entropy_sample
from quantum_layer.tex_quantum_spawn import QuantumTexSpawn
from utils.logging_utils import log

class CausalGraphReasoner:
    def __init__(self, q_optimizer, quantum_spawner: QuantumTexSpawn = None):
        """
        Accepts a shared QAOAOptimizer and optional QuantumTexSpawn instance.
        """
        self.graph = nx.DiGraph()
        self.q_optimizer = q_optimizer
        self.quantum_spawner = quantum_spawner
        self.last_analysis = None

    def add_causal_link(self, cause: str, effect: str, weight: float = 1.0):
        """
        Adds a directed edge representing cause ➝ effect with a weighted strength.
        """
        self.graph.add_edge(cause, effect, weight=weight)
        log.info(f"➕ [CausalGraph] Linked '{cause}' ➝ '{effect}' (w={weight})")

    def inject_event_chain(self, chain: list):
        """
        Accepts a list of symbolic predicates and builds a QAOA-weighted causal graph.
        """
        if not chain or len(chain) < 2:
            log.warning("[CausalGraph] ❌ Chain too short to build causal path.")
            return

        weights = self.q_optimizer.optimize(chain)
        for i in range(len(chain) - 1):
            src, tgt = chain[i], chain[i + 1]
            w = weights.get(tgt, quantum_entropy_sample())
            self.add_causal_link(src, tgt, weight=w)

        log.info("[CausalGraph] 🧠 Injected symbolic event chain.")

    def analyze_causality(self, focus_node: str = None):
        """
        Analyzes the causal graph for loops, entropy spikes, and triggers cognitive alerts.
        Emits CAUSAL_ANALYSIS event.
        """
        G = self.graph if not focus_node else nx.ego_graph(self.graph, focus_node, radius=2)
        cycles = list(nx.simple_cycles(G))
        entropy = quantum_entropy_sample()

        report = {
            "cycles_detected": len(cycles),
            "entropy": entropy,
            "focus_node": focus_node,
            "timestamp": time.time()
        }

        if cycles:
            log.warning(f"🔁 [CausalGraph] Loop(s) detected → {cycles}")
        else:
            log.info(f"✅ [CausalGraph] Acyclic. Entropy={entropy:.4f}")

        self.last_analysis = report

        dispatch_event(CognitiveEvent("CAUSAL_ANALYSIS", {
            "graph_report": report,
            "graph_size": len(self.graph.nodes),
            "graph_edges": len(self.graph.edges)
        }))

        return report

    def reason_path(self, source: str, target: str):
        """
        Attempts to resolve a probable causal path using shortest QAOA-weighted logic.
        """
        try:
            path = nx.shortest_path(self.graph, source=source, target=target, weight='weight')
            log.info(f"🧭 [CausalGraph] Reasoned path: {path}")
            return path
        except nx.NetworkXNoPath:
            log.warning(f"🚫 [CausalGraph] No causal path found: '{source}' ➝ '{target}'")
            return []

    def collapse_if_contradiction(self):
        """
        Emits CONTRADICTION_COLLAPSE if entropy and cycles exceed thresholds.
        Also spawns variants if QuantumTexSpawn is enabled.
        """
        if not self.last_analysis:
            return

        entropy = self.last_analysis["entropy"]
        cycles = self.last_analysis["cycles_detected"]

        if entropy > 0.8 and cycles > 0:
            log.warning("💥 [CausalGraph] Contradiction collapse triggered.")

            dispatch_event(CognitiveEvent("CONTRADICTION_COLLAPSE", {
                "details": self.last_analysis
            }))

            if self.quantum_spawner:
                log.info("🧬 [CausalGraph] Triggering quantum spawn due to contradiction overload.")
                self.quantum_spawner.spawn_variants(
                    emotion="doubt",
                    urgency=0.9,
                    coherence=0.4
                )