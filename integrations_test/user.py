# user.py
from unit_test.auth import ist_starkes_passwort
from unit_test.utils import ist_gueltige_email
def kann_benutzer_registriert_werden(email, passwort):
    return ist_gueltige_email(email) and ist_starkes_passwort(passwort)
