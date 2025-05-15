# utils.py
# Prüfung EMail: gültig, wenn @ und . enthalten sind
def ist_gueltige_email(email):
    return "@" in email and "." in email
