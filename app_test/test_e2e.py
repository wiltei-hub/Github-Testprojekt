import unittest
from unittest.mock import patch
from app.app import registrierung_starten

class TestEndToEnd(unittest.TestCase):

    @patch("builtins.input", side_effect=["test@example.com", "Sicher123"])
    @patch("builtins.print")
    def test_erfolgreiche_registrierung(self, mock_print, mock_input):
        registrierung_starten()
        mock_print.assert_called_with("Registrierung erfolgreich!")

    @patch("builtins.input", side_effect=["test@", "abc"])
    @patch("builtins.print")
    def test_fehlgeschlagene_registrierung(self, mock_print, mock_input):
        registrierung_starten()
        mock_print.assert_called_with("Registrierung fehlgeschlagen – ungültige Daten.")

if __name__ == "__main__":
    unittest.main()
