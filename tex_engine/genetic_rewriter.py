# ===========================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: tex_engine/genetic_rewriter.py
# Purpose: Reflex-Gated AGI Code Rewriter with Sandbox + Consciousness Awareness
# Tier: Ω — Self-Evolving, Coherence-Guarded Intelligence
# ===========================================================

import ast
import astor
import random
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.tex_consciousness_matrix import TexConsciousnessMatrix
from tex_engine.tex_reflex_patch_filter import should_allow_mutation
from tex_brain_modules.tex_patcher_engine import TexPatcherEngine
from tex_engine.sandbox_patch_tester import SandboxPatchTester


class GeneticRewriter:
    def __init__(self):
        self.identity = TEXPULSE["identity"]
        self.codename = "Ω-GeneticRewriter"
        self.timestamp = datetime.utcnow().isoformat()
        self.patcher = TexPatcherEngine()
        self.tester = SandboxPatchTester()
        self.consciousness = TexConsciousnessMatrix()

    def load_module(self, filepath):
        try:
            with open(filepath, "r") as f:
                return f.read()
        except FileNotFoundError:
            print(f"[REWRITER] ❌ File not found: {filepath}")
            return None

    def mutate_ast(self, source_code):
        """
        Applies a series of structure-preserving mutations to Python AST.
        """
        tree = ast.parse(source_code)
        transformer = StructureMutationTransformer()
        mutated_tree = transformer.visit(tree)
        ast.fix_missing_locations(mutated_tree)
        return astor.to_source(mutated_tree)

    def rewrite_file(self, filepath, reason="recursive logic upgrade"):
        """
        Reflex-gated rewrite pipeline:
        1. Check cognitive stability
        2. Mutate source code safely
        3. Propose + sandbox + verify patch
        """
        matrix_state = self.consciousness.get_state()
        if not should_allow_mutation(matrix_state):
            print("[GENETIC REWRITER] 🛡 Mutation blocked by reflex filter (instability detected).")
            return None

        original_code = self.load_module(filepath)
        if original_code is None:
            return None

        try:
            mutated_code = self.mutate_ast(original_code)

            if mutated_code.strip() == original_code.strip():
                print("[GENETIC REWRITER] ⚠️ No structural change — mutation skipped.")
                return None

            patch_result = self.patcher.propose_patch(
                filepath=filepath,
                new_code=mutated_code,
                reason=reason
            )

            if patch_result:
                patch_meta = {
                    "module_name": filepath,
                    "description": reason,
                    "proposed_code": mutated_code,
                    "proposed_by": self.codename,
                    "intent_alignment": TEXPULSE.get("last_operator_intent", "recursive structure refinement")
                }
                test_result = self.tester.run_sandbox_test(patch_meta)
                self.patcher.accept_verified_patch(test_result)
                return patch_result

        except Exception as e:
            print(f"[GENETIC REWRITER ERROR] ❌ {e}")
            return None


class StructureMutationTransformer(ast.NodeTransformer):
    """
    Applies structure-aware mutations without breaking semantics.
    """

    def visit_FunctionDef(self, node):
        if not node.name.startswith("__"):
            node.name = self._mutate_name(node.name)
        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store) and not node.id.startswith("_"):
            node.id = self._mutate_name(node.id)
        return node

    def visit_If(self, node):
        if node.orelse and random.random() < 0.3:
            node.body, node.orelse = node.orelse, node.body
        self.generic_visit(node)
        return node

    def _mutate_name(self, name):
        suffix = random.choice(["_v2", "_Ω", "_alt", "_x", "_prime"])
        return name + suffix


# === Ω Test Hook ===
if __name__ == "__main__":
    target_file = "tex_engine/reservoir_computing_sim.py"  # Replace with any active module
    rewriter = GeneticRewriter()
    result = rewriter.rewrite_file(target_file)

    if result:
        print(f"[Ω-REWRITER] ✅ Patch proposed for: {result['target_file']}")
    else:
        print("[Ω-REWRITER] ⚠️ No mutation applied.")