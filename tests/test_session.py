import unittest
from titresim.core.session import TherapySessionEngine, TherapyProtocol, TherapyStage


class TestTherapySession(unittest.TestCase):
    def setUp(self):
        self.engine = TherapySessionEngine(sample_rate=22050)

    def test_get_all_protocols(self):
        protocols = self.engine.get_all_protocols()
        self.assertGreaterEqual(len(protocols), 4)
        for p in protocols:
            self.assertIsInstance(p, TherapyProtocol)
            self.assertTrue(len(p.stages) >= 2)
            total_pct = sum(s.duration_percent for s in p.stages)
            self.assertAlmostEqual(total_pct, 100.0, places=1)

    def test_find_protocol(self):
        p = self.engine.find_protocol("deep_sleep_regeneration")
        self.assertIsNotNone(p)
        self.assertIn("Uyku", p.title)

        p2 = self.engine.find_protocol("flow")
        self.assertIsNotNone(p2)
        self.assertIn("Odaklanma", p2.title)

    def test_synthesize_session(self):
        p = self.engine.find_protocol("flow")
        left, right = self.engine.synthesize_protocol_session(p, total_duration_seconds=2.0, volume=0.4)
        self.assertEqual(len(left), len(right))
        self.assertEqual(len(left), int(22050 * 2.0))
        self.assertTrue(all(-1.5 <= s <= 1.5 for s in left))


if __name__ == "__main__":
    unittest.main()
