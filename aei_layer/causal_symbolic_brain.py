# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/causal_symbolic_brain.py (v2)
# Purpose: Upgraded Causal Graph Engine with Inference, Feedback Loop Detection,
#          and Temporal Reasoning for AGI-Level Symbolic Causality
# Status: 🔒 GODMIND TIER 4.5+ — FINALIZED UPGRADE v2.0
# ============================================================

import networkx as nx
import json
from datetime import datetime
from core_layer.memory_engine import recall_values, store_to_memory
from tex_backend.tex_core_event_bus import emit_event

CAUSAL_SOURCE = "neuro_symbolic_fusion"
OUTPUT_LOG = "memory_archive/causal_symbolic_graph.jsonl"
VISUAL_EXPORT = "memory_archive/causal_symbolic_graph.gexf"

class CausalSymbolicBrain:
    def __init__(self):
        self.graph = nx.DiGraph()

    def extract_causal_edges(self, fused_logic: str):
        """Extracts cause-effect pairs using a basic heuristic."""
        clauses = fused_logic.split(" and ")
        edges = []
        for clause in clauses:
            if " causes " in clause:
                parts = clause.split(" causes ")
                if len(parts) == 2:
                    cause, effect = parts[0].strip(), parts[1].strip()
                    edges.append((cause, effect))
        return edges

    def construct_graph(self, records):
        for record in records:
            logic = record.get("fused_logic", "")
            edges = self.extract_causal_edges(logic)
            ts = record.get("timestamp", datetime.utcnow().isoformat())
            for src, tgt in edges:
                if self.graph.has_edge(src, tgt):
                    self.graph[src][tgt]["weight"] += 1
                else:
                    self.graph.add_edge(src, tgt, weight=1, timestamps=[ts])

    def detect_feedback_loops(self):
        cycles = list(nx.simple_cycles(self.graph))
        return cycles

    def score_influence(self):
        return nx.pagerank(self.graph, weight="weight")

    def persist_graph(self):
        data = {
            "timestamp": datetime.utcnow().isoformat(),
            "nodes": list(self.graph.nodes),
            "edges": [(u, v, self.graph[u][v]) for u, v in self.graph.edges],
            "feedback_loops": self.detect_feedback_loops(),
            "influence_scores": self.score_influence()
        }
        store_to_memory("causal_graph", data)
        emit_event("causal_symbolic_graph_updated", data)

        with open(OUTPUT_LOG, "a") as f:
            f.write(json.dumps(data) + "\n")

        nx.write_gexf(self.graph, VISUAL_EXPORT)

    def trace_inference_chain(self, source, depth=3):
        paths = []
        for target in nx.descendants(self.graph, source):
            for path in nx.all_simple_paths(self.graph, source=source, target=target, cutoff=depth):
                paths.append(path)
        return paths

    def run(self):
        print("[CAUSAL SYMBOLIC BRAIN v2] ⚖️ Upgraded causal reasoning engine running...")
        fused_records = recall_values(CAUSAL_SOURCE, limit=500)
        if not fused_records:
            print("[CAUSAL SYMBOLIC BRAIN] ⚠️ No fusion records found.")
            return

        self.construct_graph(fused_records)
        self.persist_graph()

        print(f"[CAUSAL SYMBOLIC BRAIN] ✔️ Graph built: {len(self.graph.nodes)} nodes, {len(self.graph.edges)} edges")
        loops = self.detect_feedback_loops()
        if loops:
            print(f"⛔️ Detected feedback loops: {len(loops)}")
        else:
            print("✅ No feedback loops detected.")

if __name__ == "__main__":
    CausalSymbolicBrain().run()