"""
tests/test_organs.py
Organ Rezonansı ve Biyofiziksel Frekans Terapisi test paketi.
"""

import unittest
from titresim.core.organs import OrganResonance, OrganInfo


class TestOrganResonance(unittest.TestCase):
    def test_get_all(self):
        organs = OrganResonance.get_all()
        self.assertGreaterEqual(len(organs), 10)
        for org in organs:
            self.assertIsInstance(org, OrganInfo)
            self.assertTrue(org.id)
            self.assertTrue(org.name)
            self.assertGreater(org.frequency, 0.0)

    def test_find_by_id_and_name(self):
        heart = OrganResonance.find_by_id("heart")
        self.assertIsNotNone(heart)
        self.assertEqual(heart.frequency, 136.10)

        # Türkçe isimle arama
        kalp = OrganResonance.find_by_id("kalp")
        self.assertIsNotNone(kalp)
        self.assertEqual(kalp.id, "heart")

        brain = OrganResonance.find_by_id("beyin")
        self.assertIsNotNone(brain)
        self.assertEqual(brain.frequency, 727.0)

        liver = OrganResonance.find_by_id("karaciğer")
        self.assertIsNotNone(liver)
        self.assertEqual(liver.frequency, 317.83)

    def test_generate_organ_tone(self):
        samples = OrganResonance.generate_organ_tone("heart", duration=0.5, sample_rate=22050)
        expected_len = int(0.5 * 22050)
        self.assertEqual(len(samples), expected_len)
        self.assertGreater(max(abs(s) for s in samples), 0.0)

    def test_generate_full_body_scan(self):
        samples = OrganResonance.generate_full_body_scan(duration_per_organ=0.1, sample_rate=22050)
        num_organs = len(OrganResonance.get_all())
        expected_len = int(num_organs * 0.1 * 22050)
        self.assertEqual(len(samples), expected_len)
        self.assertGreater(max(abs(s) for s in samples), 0.0)

    def test_invalid_organ_raises(self):
        with self.assertRaises(ValueError):
            OrganResonance.generate_organ_tone("bilinmeyen_organ_xyz")


if __name__ == "__main__":
    unittest.main()
