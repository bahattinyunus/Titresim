import unittest
from titresim.core.tuning import TuningSystem


class TestTuningSystem(unittest.TestCase):
    def test_convert_a4(self):
        # 440 Hz -> 432 Hz
        conv = TuningSystem.convert_a4(440.0, 440.0, 432.0)
        self.assertAlmostEqual(conv, 432.0, places=2)

    def test_note_to_frequency(self):
        # A4 at 432 Hz
        freq = TuningSystem.note_to_frequency("A", 4, a4_ref=432.0)
        self.assertEqual(freq, 432.0)

        # C4 at 440 Hz (~261.63 Hz)
        freq_c4 = TuningSystem.note_to_frequency("C", 4, a4_ref=440.0)
        self.assertAlmostEqual(freq_c4, 261.63, places=1)

    def test_pythagorean_scale(self):
        scale = TuningSystem.pythagorean_scale(216.0)
        self.assertEqual(len(scale), 8)
        # 8th note should be 432.0 Hz
        self.assertEqual(scale[-1][1], 432.0)

    def test_makam_53tet(self):
        # Rast: [0, 9, 17, 22, 31, 40, 48, 53]
        steps = [0, 9, 17, 22, 31, 40, 48, 53]
        freqs = TuningSystem.calculate_makam_53tet(220.0, steps)
        self.assertEqual(len(freqs), 8)
        self.assertEqual(freqs[0], 220.0)
        self.assertGreater(freqs[-1], 430.0)


if __name__ == "__main__":
    unittest.main()
