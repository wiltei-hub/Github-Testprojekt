# utils.py
# Prüfung EMail
def ist_gueltige_email(email):
    return "@" in email and "." in email
