# auth.py
def ist_starkes_passwort(passwort):
    return len(passwort) >= 8 and any(c.isdigit() for c in passwort)
