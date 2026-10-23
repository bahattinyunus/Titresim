"""
tests/test_phonetics.py
Kutsal Kelâm ve Fonetik Formant Sentezleyici test paketi.
"""

import unittest
from titresim.core.phonetics import SacredPhonetics, SacredChant


class TestSacredPhonetics(unittest.TestCase):
    def test_get_all(self):
        chants = SacredPhonetics.get_all()
        self.assertGreaterEqual(len(chants), 8)
        for c in chants:
            self.assertIsInstance(c, SacredChant)
            self.assertTrue(c.id)
            self.assertTrue(c.name)
            self.assertGreaterEqual(len(c.formants), 2)

    def test_find_by_id_and_name(self):
        hu = SacredPhonetics.find_by_id("hu")
        self.assertIsNotNone(hu)
        self.assertEqual(hu.base_pitch_hz, 136.1)

        allah = SacredPhonetics.find_by_id("allah")
        self.assertIsNotNone(allah)

        gunne = SacredPhonetics.find_by_id("gunne")
        self.assertIsNotNone(gunne)
        self.assertIn("Nitrik Oksit", gunne.nitric_oxide_effect)

        aum = SacredPhonetics.find_by_id("aum")
        self.assertIsNotNone(aum)

    def test_synthesize_chant(self):
        samples = SacredPhonetics.synthesize_chant("hu", duration=0.5, sample_rate=22050)
        expected_len = int(0.5 * 22050)
        self.assertEqual(len(samples), expected_len)
        self.assertGreater(max(abs(s) for s in samples), 0.0)

    def test_synthesize_chant_custom_pitch(self):
        samples = SacredPhonetics.synthesize_chant("allah", duration=0.4, base_pitch=432.0, sample_rate=22050)
        self.assertEqual(len(samples), int(0.4 * 22050))
        self.assertGreater(max(abs(s) for s in samples), 0.0)

    def test_invalid_chant_raises(self):
        with self.assertRaises(ValueError):
            SacredPhonetics.synthesize_chant("gecersiz_kelam_xyz")


if __name__ == "__main__":
    unittest.main()
