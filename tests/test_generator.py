"""
Ton sentezleyici ve WAV yazıcı testleri.
"""
import unittest
import os
import wave
import tempfile
from titresim.core.generator import ToneGenerator, ADSR


class TestToneGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = ToneGenerator(sample_rate=22050)

    def test_generate_sine_length(self):
        duration = 0.5
        samples = self.gen.generate_sine(frequency=440.0, duration=duration)
        expected_samples = int(self.gen.sample_rate * duration)
        self.assertEqual(len(samples), expected_samples)

    def test_save_wav(self):
        samples = self.gen.generate_sine(frequency=528.0, duration=0.2)
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            self.gen.save_wav(tmp_path, samples)
            self.assertTrue(os.path.exists(tmp_path))
            with wave.open(tmp_path, "r") as wf:
                self.assertEqual(wf.getnchannels(), 1)
                self.assertEqual(wf.getsampwidth(), 2)
                self.assertEqual(wf.getframerate(), 22050)
                self.assertEqual(wf.getnframes(), len(samples))
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_adsr(self):
        adsr = ADSR(attack=0.1, decay=0.1, sustain_level=0.5, release=0.2)
        self.assertEqual(adsr.get_amplitude(0.0, 1.0), 0.0)
        self.assertAlmostEqual(adsr.get_amplitude(0.1, 1.0), 1.0, places=2)
        self.assertAlmostEqual(adsr.get_amplitude(0.5, 1.0), 0.5, places=2)
        self.assertAlmostEqual(adsr.get_amplitude(1.0, 1.0), 0.0, places=5)


if __name__ == "__main__":
    unittest.main()
