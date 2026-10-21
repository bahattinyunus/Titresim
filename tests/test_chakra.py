"""
tests/test_chakra.py
Çakra Akustiği ve Rezonansı test paketi.
"""

import unittest
from titresim.core.chakra import ChakraResonance, ChakraAcoustics


class TestChakraResonance(unittest.TestCase):
    def test_chakras_loaded(self):
        chakras = ChakraResonance.get_all()
        self.assertEqual(len(chakras), 7)
        self.assertEqual(chakras[0].id, "muladhara")
        self.assertEqual(chakras[0].bija_mantra, "LAM")
        self.assertEqual(chakras[6].id, "sahasrara")
        self.assertEqual(chakras[6].bija_mantra, "AUM")

    def test_find_by_id_and_name(self):
        root = ChakraResonance.find_by_id("muladhara")
        self.assertIsNotNone(root)
        self.assertEqual(root.solfeggio_freq, 396.0)

        # Türkçe isimle arama
        root_tr = ChakraResonance.find_by_id("kök")
        self.assertIsNotNone(root_tr)
        self.assertEqual(root_tr.id, "muladhara")

        heart = ChakraResonance.find_by_id("kalp")
        self.assertIsNotNone(heart)
        self.assertEqual(heart.id, "anahata")
        self.assertEqual(heart.solfeggio_freq, 639.0)
        self.assertEqual(heart.bija_mantra, "YAM")

        third_eye = ChakraResonance.find_by_id("ajna")
        self.assertIsNotNone(third_eye)
        self.assertEqual(third_eye.solfeggio_freq, 852.0)

    def test_generate_chakra_tone_solfeggio(self):
        samples = ChakraResonance.generate_chakra_tone(
            chakra_id="muladhara",
            mode="solfeggio",
            duration=0.5,
            sample_rate=22050
        )
        self.assertEqual(len(samples), int(0.5 * 22050))
        self.assertGreater(max(abs(s) for s in samples), 0.0)

    def test_generate_chakra_tone_planetary(self):
        samples = ChakraResonance.generate_chakra_tone(
            chakra_id="anahata",
            mode="planetary",
            duration=0.5,
            sample_rate=22050
        )
        self.assertEqual(len(samples), int(0.5 * 22050))
        self.assertGreater(max(abs(s) for s in samples), 0.0)

    def test_generate_rainbow_alignment(self):
        samples = ChakraResonance.generate_rainbow_alignment(
            duration_per_chakra=0.2,
            sample_rate=22050
        )
        expected_samples = int(7 * 0.2 * 22050)
        self.assertEqual(len(samples), expected_samples)
        self.assertGreater(max(abs(s) for s in samples), 0.0)

    def test_invalid_chakra_raises(self):
        with self.assertRaises(ValueError):
            ChakraResonance.generate_chakra_tone("bilinmeyen_cakra_xyz")


if __name__ == "__main__":
    unittest.main()
