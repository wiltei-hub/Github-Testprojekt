# utils.py
# Prüfung EMail: gültig, wenn @ und . enthalten sind
def ist_gueltige_email(email):
    """
    
    :param email:
    :return:
    """
    return "@" in email and "." in email
