import unittest
from titresim.core.isochronic import IsochronicToneGenerator


class TestIsochronicToneGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = IsochronicToneGenerator(sample_rate=22050)

    def test_generate(self):
        samples = self.gen.generate(carrier_freq=432.0, pulse_rate_hz=10.0, duration=0.5, volume=0.5)
        self.assertEqual(len(samples), 11025)
        self.assertTrue(all(-1.0 <= s <= 1.0 for s in samples))

    def test_duty_cycle(self):
        # 0.2 duty cycle
        samples = self.gen.generate(carrier_freq=200.0, pulse_rate_hz=5.0, duration=0.4, duty_cycle=0.2)
        self.assertEqual(len(samples), int(22050 * 0.4))


if __name__ == "__main__":
    unittest.main()
