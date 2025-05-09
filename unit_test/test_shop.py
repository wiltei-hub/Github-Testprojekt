# test_shop.py
import unittest
from shop import berechne_rabatt

class TestShop(unittest.TestCase):
    def test_normaler_rabatt(self):
        self.assertEqual(berechne_rabatt(preis=100, prozent=10), 90)

    def test_null_rabatt(self):
        self.assertEqual(berechne_rabatt(preis=50, prozent=0), 50)

    def test_ungueltiger_rabatt(self):
        with self.assertRaises(ValueError):
            berechne_rabatt(preis=100, prozent=150)

if __name__ == "__main__":
    unittest.main()
