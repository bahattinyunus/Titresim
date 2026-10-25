"""
tests/test_bowls.py
Tibet Ses Çanakları ve Himalaya Gong Modal Akustik Testleri.
"""

import unittest
from titresim.core.bowls import SingingBowlAcoustics, SingingBowl


class TestSingingBowlAcoustics(unittest.TestCase):

    def test_list_bowls(self):
        bowls = SingingBowlAcoustics.list_bowls()
        self.assertGreaterEqual(len(bowls), 8)
        self.assertTrue(all(isinstance(b, SingingBowl) for b in bowls))

    def test_get_bowl(self):
        bowl_om = SingingBowlAcoustics.get_bowl("full_moon_om")
        self.assertIsNotNone(bowl_om)
        self.assertEqual(bowl_om.fundamental_hz, 136.1)
        self.assertIn("Kalp", bowl_om.name)

        gong = SingingBowlAcoustics.get_bowl("himalayan_wind_gong")
        self.assertIsNotNone(gong)
        self.assertEqual(gong.fundamental_hz, 64.0)

    def test_synthesize_struck_bowl(self):
        duration = 1.0
        sample_rate = 22050
        samples = SingingBowlAcoustics.synthesize_struck_bowl(
            bowl_id="full_moon_om",
            duration=duration,
            sample_rate=sample_rate
        )
        expected_len = int(duration * sample_rate)
        self.assertEqual(len(samples), expected_len)
        max_amp = max(abs(s) for s in samples)
        self.assertGreater(max_amp, 0.1)
        self.assertLessEqual(max_amp, 1.0)

    def test_synthesize_singing_rim(self):
        duration = 1.5
        sample_rate = 22050
        samples = SingingBowlAcoustics.synthesize_singing_rim(
            bowl_id="tibetan_root",
            duration=duration,
            sample_rate=sample_rate
        )
        expected_len = int(duration * sample_rate)
        self.assertEqual(len(samples), expected_len)
        max_amp = max(abs(s) for s in samples)
        self.assertGreater(max_amp, 0.1)
        self.assertLessEqual(max_amp, 1.0)


if __name__ == "__main__":
    unittest.main()
