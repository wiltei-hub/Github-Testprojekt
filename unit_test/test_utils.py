# test_utils.py
import unittest
from utils import ist_gueltige_email

class TestUtils(unittest.TestCase):
    def test_gueltige_email(self):
        self.assertTrue(ist_gueltige_email("test@example.com"))

    def test_ungueltige_email_kein_at(self):
        self.assertFalse(ist_gueltige_email("testexample.com"))

    def test_ungueltige_email_kein_punkt(self):
        self.assertFalse(ist_gueltige_email("test@examplecom"))

if __name__ == "__main__":
    unittest.main()
