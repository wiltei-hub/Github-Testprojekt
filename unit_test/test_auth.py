# test_auth.py
import unittest
from auth import ist_starkes_passwort

class TestAuth(unittest.TestCase):
    def test_starkes_passwort(self):
        self.assertTrue(ist_starkes_passwort("Passwort123"))

    def test_zu_kurz(self):
        self.assertFalse(ist_starkes_passwort("Pw1"))

    def test_ohne_zahlen(self):
        self.assertFalse(ist_starkes_passwort("NurBuchstaben"))

if __name__ == "__main__":
    unittest.main()
