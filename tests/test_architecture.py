"""
tests/test_architecture.py
Kutsal Mimari Akustiği, Mimar Sinan Helmholtz Rezonatörleri ve Schroeder Yankılanma Testleri.
"""

import unittest
from titresim.core.architecture import AcousticArchitecture, SacredSpace


class TestAcousticArchitecture(unittest.TestCase):

    def test_list_spaces(self):
        spaces = AcousticArchitecture.list_spaces()
        self.assertGreaterEqual(len(spaces), 5)
        self.assertTrue(all(isinstance(s, SacredSpace) for s in spaces))

    def test_get_space(self):
        suleymaniye = AcousticArchitecture.get_space("suleymaniye")
        self.assertIsNotNone(suleymaniye)
        self.assertEqual(suleymaniye.resonators_count, 64)
        self.assertEqual(suleymaniye.rt60_sec, 4.2)

        hypogeum = AcousticArchitecture.get_space("hypogeum")
        self.assertIsNotNone(hypogeum)
        self.assertEqual(hypogeum.resonator_frequency_hz, 110.0)

    def test_helmholtz_calculation(self):
        # 5 litrelik bir küp, 4 cm yarıçaplı boğaz, 10 cm uzunluk
        f = AcousticArchitecture.calculate_helmholtz_frequency(
            cavity_volume_liters=5.0,
            neck_radius_cm=4.0,
            neck_length_cm=10.0,
            speed_of_sound_ms=343.0
        )
        self.assertGreater(f, 50.0)
        self.assertLess(f, 500.0)

    def test_apply_reverberation(self):
        # 0.5 saniyelik test tonu
        sample_rate = 16000
        input_signal = [0.5 * (1 if i % 100 < 50 else -1) for i in range(int(0.5 * sample_rate))]
        reverbed = AcousticArchitecture.apply_reverberation(
            input_signal,
            space_id="suleymaniye",
            sample_rate=sample_rate,
            wet_mix=0.5
        )
        # Reverb kuyruğu nedeniyle çıktı girdi boyutundan daha uzun olmalı
        self.assertGreater(len(reverbed), len(input_signal))
        max_amp = max(abs(s) for s in reverbed)
        self.assertGreater(max_amp, 0.05)
        self.assertLessEqual(max_amp, 1.0)

    def test_generate_impulse_response(self):
        ir = AcousticArchitecture.generate_impulse_response("hypogeum", duration=1.0, sample_rate=16000)
        self.assertGreaterEqual(len(ir), 16000)
        max_amp = max(abs(s) for s in ir)
        self.assertGreater(max_amp, 0.1)


if __name__ == "__main__":
    unittest.main()
