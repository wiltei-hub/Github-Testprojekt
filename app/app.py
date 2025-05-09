from integrations_test.user import kann_benutzer_registriert_werden

def registrierung_starten():
    email = input("Bitte E-Mail eingeben: ")
    passwort = input("Bitte Passwort eingeben: ")

    if kann_benutzer_registriert_werden(email, passwort):
        print("Registrierung erfolgreich!")
    else:
        print("Registrierung fehlgeschlagen – ungültige Daten.")
