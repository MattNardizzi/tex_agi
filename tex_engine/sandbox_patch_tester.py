# ============================================================
# © 2025 Sovereign Cognition / VortexBlack LLC. All rights reserved.
# File: tex_engine/sandbox_patch_tester.py
# Purpose: Validates and scores AGI-generated code patches before integration
# Tier: Ω – Patch firewall + mutation integrity gateway
# ============================================================

import tempfile
import subprocess
import os
import json
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory
from tex_brain_modules.tex_patcher_engine import TexPatcherEngine

class SandboxPatchTester:
    def __init__(self):
        self.codename = "Ω-SandboxGatekeeper"
        self.test_log = "memory_archive/patch_test_results.jsonl"
        self.identity = TEXPULSE["identity"]
        self.patcher = TexPatcherEngine()

    def validate_patch(self, proposed_code: str):
        """
        Executes code in a temporary environment and returns result and diagnostics.
        """
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as tmp:
            tmp.write(proposed_code)
            tmp_path = tmp.name

        try:
            result = subprocess.run(
                ["python", tmp_path],
                capture_output=True,
                timeout=5
            )
            success = result.returncode == 0
            diagnostics = result.stderr.decode() if not success else result.stdout.decode()
        except Exception as e:
            success = False
            diagnostics = str(e)
        finally:
            os.remove(tmp_path)

        return success, diagnostics.strip()

    def score_patch(self, success: bool, diagnostics: str):
        """
        Evaluates the safety and coherence of a patch execution result.
        """
        if success:
            return 1.0, "accept"
        elif "SyntaxError" in diagnostics:
            return 0.0, "reject"
        else:
            return 0.5, "manual_review"

    def log_result(self, patch_meta: dict, success: bool, diagnostics: str, score: float, decision: str):
        """
        Logs sandbox outcome and routes result to long-term memory.
        """
        result = {
            "timestamp": datetime.utcnow().isoformat(),
            "proposed_by": patch_meta.get("proposed_by", "unknown"),
            "target_file": patch_meta["module_name"],
            "description": patch_meta["description"],
            "intent_alignment": patch_meta.get("intent_alignment"),
            "test_success": success,
            "score": score,
            "decision": decision,
            "diagnostics": diagnostics,
        }

        with open(self.test_log, "a") as f:
            f.write(json.dumps(result) + "\n")

        store_to_memory("patch_test_results", result)
        return result

    def run_sandbox_test(self, patch_meta: dict):
        """
        Orchestrates validation → scoring → logging → verification.
        """
        code = patch_meta["proposed_code"]
        success, diagnostics = self.validate_patch(code)
        score, decision = self.score_patch(success, diagnostics)
        result = self.log_result(patch_meta, success, diagnostics, score, decision)

        # Send result to TexPatcher for memory archival
        self.patcher.accept_verified_patch(result)

        return result


# === Ω Test Hook ===
if __name__ == "__main__":
    dummy_patch = {
        "module_name": "emotion_meta_reflector.py",
        "description": "Handles paralyzing emotion logic drift",
        "proposed_code": "def run():\n    print('Emotion stabilized.')",
        "timestamp": datetime.utcnow().isoformat(),
        "proposed_by": "Ω-SeedProposer",
        "intent_alignment": "Reflexive stabilization of internal state",
    }

    tester = SandboxPatchTester()
    result = tester.run_sandbox_test(dummy_patch)

    print(f"[Ω-SANDBOX] Patch Decision: {result['decision']} — Score: {result['score']}")
    if result['diagnostics']:
        print("Diagnostics:\n", result['diagnostics'])