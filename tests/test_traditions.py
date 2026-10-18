import unittest
from titresim.core.traditions import SacredTraditions


class TestSacredTraditions(unittest.TestCase):
    def test_get_all(self):
        items = SacredTraditions.get_all()
        self.assertGreaterEqual(len(items), 5)

    def test_find_by_id(self):
        tr = SacredTraditions.find_by_id("islam_qiraat")
        self.assertIsNotNone(tr)
        self.assertIn("Kıraat", tr.practice)

    def test_search(self):
        results = SacredTraditions.search("vagus")
        self.assertGreaterEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
