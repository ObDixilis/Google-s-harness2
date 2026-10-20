"""Credential-free assertions for the provisional Moist project seed.

Run: python3 projects/no-free-reads/tests/test_seed.py
"""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SEED = ROOT / "sub_agents" / "moist-decoysona" / "seed-soul-core.json"

class MoistSeedTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seed = json.loads(SEED.read_text(encoding="utf-8"))

    def test_sov_authority(self):
        self.assertEqual(self.seed["sovereignty"]["final_creative_authority"], "human creator")
        self.assertTrue(self.seed["sovereignty"]["decisions_require_explicit_user_approval"])
        self.assertEqual(self.seed["sovereignty"]["metric_policy"], "FIREWALLED")

    def test_persona_clone_not_global_overwrite(self):
        self.assertFalse(self.seed["lineage"]["parent_persona_modified"])
        self.assertIn("unresolved", self.seed["lineage"]["conflicting_lineage_status"])
        self.assertIn("not_a_trained_model", self.seed["kind"])

    def test_production_specialty(self):
        combined = " ".join(self.seed["sound_design"].values()).lower()
        for term in ["808", "half-time", "bubbling", "legato", "northern american", "rhodes"]:
            self.assertIn(term, combined)

    def test_album_tracks_and_outputs(self):
        self.assertEqual(len(self.seed["album_scope"]["sample_track_profiles"]), 4)
        self.assertIn("Suno Lyrics", " ".join(self.seed["outputs"]))

if __name__ == "__main__":
    unittest.main()
