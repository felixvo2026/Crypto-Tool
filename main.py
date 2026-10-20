import sys

def verschluesseln(text, passwort):
    endergebnis = ""
    for i in range(len(text)):
        zahl = ord(text[i])
        
        pass_index = i % len(passwort)
        verschiebung = ord(passwort[pass_index])
        
        neue_zahl = zahl + verschiebung
        neuer_buchstabe = chr(neue_zahl)
        endergebnis += neuer_buchstabe

    return endergebnis


def entschluesseln(text, passwort):
    endergebnis = ""
    for i in range(len(text)):
        zahl = ord(text[i])
        pass_index = i % len(passwort)
        verschiebung = ord(passwort[pass_index])
        neue_zahl = zahl - verschiebung
        neuer_buchstabe = chr(neue_zahl)
        endergebnis += neuer_buchstabe

    return endergebnis


def main():
    eingabe = input("Willst du entschluesseln(e) oder verschluessenln(v)s? : ")
    zahl = input("Text/Geheimtext: ")
    passswort = input("Passwort: ")
    f = verschluesseln if eingabe == "v" else entschluesseln
    print(f(zahl, passswort))

try:
    while True:
        main()
except KeyboardInterrupt:
    print("\nProgramm beendet.")
    sys.exit()
