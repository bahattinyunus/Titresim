import unittest
from titresim.core.cymatics import CircularChladniPlate, bessel_j


class TestCircularCymatics(unittest.TestCase):
    def test_bessel_j(self):
        # J_0(0) = 1.0, J_1(0) = 0.0
        self.assertAlmostEqual(bessel_j(0, 0.0), 1.0, places=4)
        self.assertAlmostEqual(bessel_j(1, 0.0), 0.0, places=4)

    def test_circular_plate(self):
        plate = CircularChladniPlate(n=2, m=3)
        self.assertEqual(plate.n, 2)
        self.assertEqual(plate.m, 3)

        grid = plate.compute_grid(resolution=21)
        self.assertEqual(len(grid), 21)
        self.assertEqual(len(grid[0]), 21)

    def test_ascii_render(self):
        plate = CircularChladniPlate.from_frequency(432.0)
        ascii_art = plate.render_ascii(resolution=15)
        self.assertIn("#", ascii_art)


if __name__ == "__main__":
    unittest.main()
