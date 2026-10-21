"""
tests/test_seyir.py
Makam Seyir Sentezleyici test paketi.
"""

import unittest
from titresim.core.seyir import MakamSeyirGenerator


class TestMakamSeyirGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = MakamSeyirGenerator(sample_rate=22050)

    def test_generate_rast_seyir(self):
        samples = self.generator.generate_seyir_melody(
            makam_id="rast",
            base_freq=220.0,
            unit_note_duration=0.1
        )
        self.assertGreater(len(samples), 0)
        self.assertGreater(max(abs(s) for s in samples), 0.0)

    def test_generate_nihavend_seyir(self):
        samples = self.generator.generate_seyir_melody(
            makam_id="nihavend",
            base_freq=261.63,
            unit_note_duration=0.1
        )
        self.assertGreater(len(samples), 0)
        self.assertGreater(max(abs(s) for s in samples), 0.0)

    def test_generate_hicaz_seyir(self):
        samples = self.generator.generate_seyir_melody(
            makam_id="hicaz",
            unit_note_duration=0.1
        )
        self.assertGreater(len(samples), 0)
        self.assertGreater(max(abs(s) for s in samples), 0.0)

    def test_generate_ussak_seyir(self):
        samples = self.generator.generate_seyir_melody(
            makam_id="ussak",
            unit_note_duration=0.1
        )
        self.assertGreater(len(samples), 0)
        self.assertGreater(max(abs(s) for s in samples), 0.0)

    def test_fallback_for_unknown_makam(self):
        # Bilinmeyen makam rast şablonuna döner ve hata patlatmadan sentezler
        samples = self.generator.generate_seyir_melody(
            makam_id="bilinmeyen",
            unit_note_duration=0.05
        )
        self.assertGreater(len(samples), 0)


if __name__ == "__main__":
    unittest.main()
