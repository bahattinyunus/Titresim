"""
tests/test_breath.py
Biyogeribildirim & Solunum Rehberi test paketi.
"""

import unittest
from titresim.core.breath import CoherenceBreathGuide, BreathPattern


class TestCoherenceBreathGuide(unittest.TestCase):
    def test_patterns_defined(self):
        patterns = CoherenceBreathGuide.PATTERNS
        self.assertGreaterEqual(len(patterns), 4)
        self.assertIn("coherence", patterns)
        self.assertIn("box", patterns)
        self.assertIn("4-7-8", patterns)
        self.assertIn("relax", patterns)

    def test_get_pattern(self):
        box = CoherenceBreathGuide.get_pattern("box")
        self.assertIsNotNone(box)
        self.assertEqual(box.inhale_sec, 4.0)
        self.assertEqual(box.hold_in_sec, 4.0)

        weil = CoherenceBreathGuide.get_pattern("4-7-8")
        self.assertIsNotNone(weil)
        self.assertEqual(weil.exhale_sec, 8.0)

        fallback = CoherenceBreathGuide.get_pattern("bilinmeyen_pattern")
        self.assertEqual(fallback.id, "coherence")

    def test_generate_guided_session(self):
        samples = CoherenceBreathGuide.generate_guided_session(
            pattern_id="box",
            total_duration_sec=2.0,
            sample_rate=22050
        )
        expected_len = int(2.0 * 22050)
        self.assertEqual(len(samples), expected_len)
        self.assertGreater(max(abs(s) for s in samples), 0.0)

    def test_generate_coherence_session(self):
        samples = CoherenceBreathGuide.generate_guided_session(
            pattern_id="coherence",
            total_duration_sec=3.0,
            base_freq=216.0,
            sample_rate=22050
        )
        self.assertEqual(len(samples), int(3.0 * 22050))
        self.assertGreater(max(abs(s) for s in samples), 0.0)


if __name__ == "__main__":
    unittest.main()
