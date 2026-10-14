"""
Osmanlı Makam Terapisi testleri.
"""
import unittest
from titresim.core.makam import MakamTherapy


class TestMakam(unittest.TestCase):
    def test_makam_load(self):
        makamlar = MakamTherapy.get_all()
        self.assertGreaterEqual(len(makamlar), 10)
        ids = [m.id for m in makamlar]
        self.assertIn("rast", ids)
        self.assertIn("nihavend", ids)
        self.assertIn("hicaz", ids)

    def test_find_by_id(self):
        rast = MakamTherapy.find_by_id("rast")
        self.assertIsNotNone(rast)
        self.assertEqual(rast.name, "Rast Makamı")
        self.assertIn("Baş", rast.organ)

    def test_search_by_organ(self):
        kalp_makamlar = MakamTherapy.search_by_organ("kalp")
        self.assertTrue(len(kalp_makamlar) > 0)

    def test_frequency_calculation(self):
        rast = MakamTherapy.find_by_id("rast")
        freqs = rast.get_frequencies(base_freq=220.0)
        self.assertEqual(len(freqs), len(rast.scale_ratios))
        self.assertEqual(freqs[0], 220.0)
        self.assertEqual(freqs[-1], 440.0)


if __name__ == "__main__":
    unittest.main()
