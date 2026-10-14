"""
Sematik (Cymatics) Chladni plaka testleri.
"""
import unittest
import os
import tempfile
from titresim.core.cymatics import ChladniPlate


class TestCymatics(unittest.TestCase):
    def test_plate_modes(self):
        plate = ChladniPlate(n=3, m=5)
        self.assertEqual(plate.n, 3)
        self.assertEqual(plate.m, 5)

    def test_from_frequency(self):
        p1 = ChladniPlate.from_frequency(50)
        p2 = ChladniPlate.from_frequency(528)
        self.assertLess(p1.n, p2.n)

    def test_compute_grid(self):
        plate = ChladniPlate(n=2, m=3)
        grid = plate.compute_grid(resolution=11)
        self.assertEqual(len(grid), 11)
        self.assertEqual(len(grid[0]), 11)

    def test_render_ascii(self):
        plate = ChladniPlate(n=2, m=4)
        ascii_art = plate.render_ascii(resolution=15)
        self.assertIn("+", ascii_art)
        self.assertIn("#", ascii_art)

    def test_export_svg(self):
        plate = ChladniPlate(n=3, m=4)
        with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            plate.export_svg(tmp_path, size=200, resolution=20)
            self.assertTrue(os.path.exists(tmp_path))
            with open(tmp_path, "r", encoding="utf-8") as f:
                content = f.read()
                self.assertIn("<svg", content)
                self.assertIn("Chladni Modes", content)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)


if __name__ == "__main__":
    unittest.main()
