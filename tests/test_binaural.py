"""
Binaural beat üretici testleri.
"""
import unittest
import os
import wave
import tempfile
from titresim.core.binaural import BinauralBeatGenerator


class TestBinaural(unittest.TestCase):
    def setUp(self):
        self.gen = BinauralBeatGenerator(sample_rate=22050)

    def test_generate_channels(self):
        duration = 0.5
        left, right = self.gen.generate(carrier_freq=200, beat_freq=10, duration=duration)
        expected_samples = int(self.gen.sample_rate * duration)
        self.assertEqual(len(left), expected_samples)
        self.assertEqual(len(right), expected_samples)

    def test_save_stereo_wav(self):
        left, right = self.gen.generate(carrier_freq=216, beat_freq=7.83, duration=0.2)
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            self.gen.save_stereo_wav(tmp_path, left, right)
            self.assertTrue(os.path.exists(tmp_path))
            with wave.open(tmp_path, "r") as wf:
                self.assertEqual(wf.getnchannels(), 2)  # Stereo
                self.assertEqual(wf.getsampwidth(), 2)
                self.assertEqual(wf.getframerate(), 22050)
                self.assertEqual(wf.getnframes(), len(left))
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)


if __name__ == "__main__":
    unittest.main()
