# test_user.py
import unittest
from user import kann_benutzer_registriert_werden

class TestUserIntegration(unittest.TestCase):

    def test_gueltige_registrierung(self):
        result = kann_benutzer_registriert_werden("test@example.com", "S123")
        self.assertTrue(result)

    def test_ungueltige_email(self):
        result = kann_benutzer_registriert_werden("testexample.com", "Sicher123")
        self.assertFalse(result)

    def test_schwaches_passwort(self):
        result = kann_benutzer_registriert_werden("test@example.com", "abc")
        self.assertFalse(result)

    def test_beides_ungueltig(self):
        result = kann_benutzer_registriert_werden("test", "123")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
