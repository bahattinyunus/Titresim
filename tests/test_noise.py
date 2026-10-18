import unittest
from titresim.core.noise import NoiseGenerator


class TestNoiseGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = NoiseGenerator(sample_rate=22050, seed=123)

    def test_white_noise(self):
        samples = self.gen.generate_white_noise(duration=0.5, volume=0.5)
        self.assertEqual(len(samples), 11025)
        self.assertTrue(all(-0.5 <= s <= 0.5 for s in samples))

    def test_pink_noise(self):
        samples = self.gen.generate_pink_noise(duration=0.5, volume=0.4)
        self.assertEqual(len(samples), 11025)
        self.assertTrue(all(-1.0 <= s <= 1.0 for s in samples))

    def test_brown_noise(self):
        samples = self.gen.generate_brown_noise(duration=0.5, volume=0.4)
        self.assertEqual(len(samples), 11025)
        self.assertTrue(all(-1.0 <= s <= 1.0 for s in samples))


if __name__ == "__main__":
    unittest.main()
