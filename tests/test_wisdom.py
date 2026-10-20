import unittest
from titresim.core.wisdom import WisdomArchive, WisdomQuote


class TestWisdomArchive(unittest.TestCase):
    def test_get_all(self):
        quotes = WisdomArchive.get_all()
        self.assertGreaterEqual(len(quotes), 25)
        for q in quotes:
            self.assertIsInstance(q, WisdomQuote)
            self.assertTrue(q.author)
            self.assertTrue(q.quote_tr)
            self.assertGreater(q.recommended_freq, 0)

    def test_find_by_id(self):
        q = WisdomArchive.find_by_id("tesla_energy_vibration")
        self.assertIsNotNone(q)
        self.assertEqual(q.author, "Nikola Tesla")
        self.assertIn("titreşim", q.quote_tr.lower())

    def test_get_by_category(self):
        tasavvuf_quotes = WisdomArchive.get_by_category("tasavvuf")
        self.assertGreaterEqual(len(tasavvuf_quotes), 4)

        fizik_quotes = WisdomArchive.get_by_category("bilim_ve_fizik")
        self.assertGreaterEqual(len(fizik_quotes), 4)

    def test_get_by_author(self):
        # Case and diacritics insensitive (mevlana -> Mevlânâ)
        rumi = WisdomArchive.get_by_author("mevlana")
        self.assertGreaterEqual(len(rumi), 1)

        ibn_sina = WisdomArchive.get_by_author("ibn-i sina")
        self.assertGreaterEqual(len(ibn_sina), 1)

    def test_search(self):
        results = WisdomArchive.search("frekans")
        self.assertGreaterEqual(len(results), 2)

    def test_get_random(self):
        q = WisdomArchive.get_random()
        self.assertIsNotNone(q)
        self.assertIsInstance(q, WisdomQuote)

        q_cat = WisdomArchive.get_random(category="tasavvuf")
        self.assertIsNotNone(q_cat)
        self.assertEqual(q_cat.category, "tasavvuf")

    def test_format_quote_card(self):
        q = WisdomArchive.find_by_id("tesla_energy_vibration")
        card = WisdomArchive.format_quote_card(q)
        self.assertIn("Nikola Tesla", card)
        self.assertIn("432.0 Hz", card)
        self.assertIn("┌", card)


if __name__ == "__main__":
    unittest.main()
