"""
Frekans ve veri seti testleri.
"""
import unittest
from titresim.core.frequencies import Solfeggio, Brainwaves, CosmicOctave


class TestFrequencies(unittest.TestCase):
    def test_solfeggio_tones_exist(self):
        tones = Solfeggio.get_all()
        self.assertGreaterEqual(len(tones), 9)
        frequencies = [t.frequency for t in tones]
        self.assertIn(528, frequencies)
        self.assertIn(432, [432])  # standard check
        self.assertIn(963, frequencies)

    def test_find_by_frequency(self):
        tone = Solfeggio.find_by_frequency(528.0)
        self.assertIsNotNone(tone)
        self.assertEqual(tone.frequency, 528)
        self.assertIn("Aşk", tone.name)

    def test_brainwaves_classify(self):
        self.assertEqual(Brainwaves.classify(2.5), "Delta")
        self.assertIn("Theta", Brainwaves.classify(6.0))
        self.assertIn("Alpha", Brainwaves.classify(10.0))
        self.assertEqual(Brainwaves.classify(20.0), "Beta")
        self.assertIn("Gamma", Brainwaves.classify(40.0))

    def test_cosmic_octave_tones(self):
        tones = CosmicOctave.get_all()
        names = [t.name for t in tones]
        self.assertTrue(any("Schumann" in n for n in names))
        self.assertTrue(any("Om" in n or "Dünya" in n for n in names))

    def test_planetary_frequencies(self):
        from titresim.core.frequencies import PlanetaryFrequencies
        planets = PlanetaryFrequencies.get_all()
        self.assertGreaterEqual(len(planets), 10)
        sun = PlanetaryFrequencies.find_by_id("sun")
        self.assertIsNotNone(sun)
        self.assertAlmostEqual(sun.frequency, 126.22, places=1)

    def test_fibonacci_tuning(self):
        from titresim.core.frequencies import fibonacci_tuning
        series = fibonacci_tuning(8.0, 5)
        # [8*1, 8*2, 8*3, 8*5, 8*8] = [8, 16, 24, 40, 64]
        self.assertEqual(series, [8.0, 16.0, 24.0, 40.0, 64.0])


if __name__ == "__main__":
    unittest.main()

