Ihre Aufgabe in diesem Themenfeld: `Bayes_B`
Ihr Datensatz: A2

Es soll ein Versicherungstarif ausgewählt werden. Zur Wahl steht nur eine
begrenzte Zahl an Tarifen. Als mögliche Informationen können die Angaben zu
Altersgruppe,  Geschlecht,  Familienstand,  Kinderzahl,  Alter  des  ältesten
und jüngsten Kindes, Hausbesitzer oder Mieter, Urbanes oder ländliches Umfeld,
Bundesland, Aktienbesitz, Einkommen, Bildungsstand und Beruf vorliegen. Es ist
eine beliebige Eingabe von Messungen einzelner ggf. nicht aller Attribute zu
ermöglichen. Erstellen Sie ein Bayes Netz, welches die Zusammenhänge
modelliert und plausibel auf Basis der Beispieldaten gefüllte CPTs nutzt. Legen
Sie diesem Bayes Netz Beispieleingaben vor und geben Sie das
Klassifikationsergebnis geeignet aus.

- Legen Sie diesem Bayes Netz Beispieleingaben vor und geben Sie das Klassifikationsergebnis geeignet aus.
- Formatvorschlag: CSV Datei in welcher nicht beobachtete Merkmale ausgelassen wurden

Entwickeln  Sie eine  Software, welche bei  Eingabe einer Testdatei, welche
Angaben zu oben genannten Referenzdaten (z.B. alte Fallakten incl. Tarif)
enthält  (ggf. unvollständig), entscheidet, welcher Tarif für den jeweiligen
Fall empfohlen werden soll. 

## Fachliche Bearbeitung (25 Punkte)
- Lösungsqualität
- Umfang der Funktionalität
- Konzept
- Korrekte Verwendung von Kernfunktionen
- Anpassung an die Aufgabenstellung
- Nutzung der erworbenen Kenntnisse aus der Vorlesung

## Dokumentation (15 Punkte)
- Begründung von Entwurf und Umsetzung
- Test und Ergebnisbewertung
- Dokumentation des Programms und Codestruktur/Codequalität

# Running
Build and run docker container with:

```
docker build -t jupyter-bayes .
docker run -p 8888:8888 -v (pwd):/home/jovyan/work bayes
```

# Programmentwurf - Standalone
In order to run the programmentwurf.py, install all requirements with;

```
pip install -r requirements.txt
```
or run though jupyter notebook docker container;

```
!pyhton programmentwurf.py
```

Make sure the programmentwurf.py and bayesan network model file bayesian_model.p are in the same directory.
Modify and/or overwrite the existing versicherung_validation.csv and run the programm to get predictions.
All columns have to exsist, although do not have to be filled with values.
