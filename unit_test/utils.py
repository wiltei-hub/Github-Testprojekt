# utils.py
# Prüfung EMail: gültig, wenn @ und . enthalten sind
def ist_gueltige_email(email):
    """
    Diese Funktion prüft auf gültige EMail-Adresse 
    Eine EMail-Adresse wird als gültig betrachtet, wenn sie das ET-Zeichen @ und einen Punkt . enthält
    :param email:
    :return:
    """
    return "@" in email and "." in email
