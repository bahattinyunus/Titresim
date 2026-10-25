"""
tests/test_water.py
Suyun Hafızası, EZ Suyu Hekzagonal Yapılanma ve Kavitasyon Testleri.
"""

import unittest
from titresim.core.water import WaterAcoustics, WaterFrequency, WaterMemoryTheory, EmotoCrystal


class TestWaterAcoustics(unittest.TestCase):

    def test_list_frequencies(self):
        freqs = WaterAcoustics.list_frequencies()
        self.assertGreaterEqual(len(freqs), 5)
        self.assertTrue(all(isinstance(f, WaterFrequency) for f in freqs))

    def test_get_frequency(self):
        f528 = WaterAcoustics.get_frequency("dna_hexagonal_528")
        self.assertIsNotNone(f528)
        self.assertEqual(f528.frequency_hz, 528.0)
        self.assertGreater(f528.coherence_rating, 0.9)

    def test_list_theories_and_crystals(self):
        theories = WaterAcoustics.list_theories()
        self.assertGreaterEqual(len(theories), 3)
        self.assertTrue(all(isinstance(t, WaterMemoryTheory) for t in theories))

        crystals = WaterAcoustics.list_crystals()
        self.assertGreaterEqual(len(crystals), 4)
        self.assertTrue(all(isinstance(c, EmotoCrystal) for c in crystals))

    def test_calculate_coherence_index(self):
        c528 = WaterAcoustics.calculate_coherence_index(528.0)
        c432 = WaterAcoustics.calculate_coherence_index(432.0)
        c_random = WaterAcoustics.calculate_coherence_index(311.7)
        self.assertGreater(c528, 0.8)
        self.assertGreater(c432, 0.8)
        self.assertGreaterEqual(c_random, 0.1)

    def test_synthesize_water_tone(self):
        duration = 1.0
        sample_rate = 22050
        samples = WaterAcoustics.synthesize_water_structuring_tone(
            target="dna_hexagonal_528",
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
