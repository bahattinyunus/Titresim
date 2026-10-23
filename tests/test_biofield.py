"""
tests/test_biofield.py
Biyoalan, Fiziksel Diyapazon Modellemesi ve Tesla 3-6-9 Vorteks Testleri.
"""

import unittest
from titresim.core.biofield import BiofieldAcoustics, TuningFork, TeslaTriad


class TestBiofieldAcoustics(unittest.TestCase):

    def test_list_forks(self):
        forks = BiofieldAcoustics.list_forks()
        self.assertGreaterEqual(len(forks), 8)
        self.assertTrue(all(isinstance(f, TuningFork) for f in forks))

    def test_get_fork(self):
        fork_otto = BiofieldAcoustics.get_fork("otto128")
        self.assertIsNotNone(fork_otto)
        self.assertEqual(fork_otto.frequency, 128.0)
        self.assertEqual(fork_otto.category, "osteophonic")

        fork_mi = BiofieldAcoustics.get_fork("mi528")
        self.assertIsNotNone(fork_mi)
        self.assertEqual(fork_mi.frequency, 528.0)

    def test_strike_fork_signal(self):
        duration = 1.0
        sample_rate = 22050
        samples = BiofieldAcoustics.strike_fork("otto128", duration=duration, sample_rate=sample_rate)
        expected_samples = int(duration * sample_rate)
        self.assertEqual(len(samples), expected_samples)
        # Sinyal boş olmamalı ve genlik sınırları içinde olmalı
        max_amp = max(abs(s) for s in samples)
        self.assertGreater(max_amp, 0.1)
        self.assertLessEqual(max_amp, 1.0)

    def test_digital_root(self):
        self.assertEqual(BiofieldAcoustics.digital_root(174), 3)  # 1+7+4 = 12 -> 3
        self.assertEqual(BiofieldAcoustics.digital_root(528), 6)  # 5+2+8 = 15 -> 6
        self.assertEqual(BiofieldAcoustics.digital_root(963), 9)  # 9+6+3 = 18 -> 9
        self.assertEqual(BiofieldAcoustics.digital_root(432), 9)  # 4+3+2 = 9 -> 9

    def test_tesla_triads(self):
        triads = BiofieldAcoustics.list_tesla_triads()
        self.assertEqual(len(triads), 3)
        roots = [tr.root for tr in triads]
        self.assertEqual(roots, [3, 6, 9])

        tr9 = BiofieldAcoustics.get_tesla_triad(9)
        self.assertIsNotNone(tr9)
        self.assertIn(963.0, tr9.frequencies)

    def test_synthesize_tesla_vortex(self):
        samples = BiofieldAcoustics.synthesize_tesla_vortex(triad_root=9, duration=1.0, sample_rate=16000)
        self.assertEqual(len(samples), 16000)
        max_amp = max(abs(s) for s in samples)
        self.assertGreater(max_amp, 0.05)
        self.assertLessEqual(max_amp, 1.0)

    def test_fibonacci_sequence(self):
        samples = BiofieldAcoustics.generate_fibonacci_sequence(base_freq=432.0, duration=1.0, sample_rate=16000)
        self.assertEqual(len(samples), 16000)
        max_amp = max(abs(s) for s in samples)
        self.assertGreater(max_amp, 0.1)


if __name__ == "__main__":
    unittest.main()
