# Bayes Network
Ihre Aufgabe in diesem Themenfeld: `Bayes_B`
Ihr Datensatz: A2

Daniel Schaefer und David Marchi

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

## Documentation

See `docs.md`

## Running Jupyter Notebook
Build and run docker container with:

```
docker build -t jupyter-bayes .
docker run -p 8888:8888 -v (pwd):/home/jovyan/work bayes
```

## Programmentwurf - Standalone
Everything is in the `standalone/` directory.
In order to run the `programmentwurf.py,` install all requirements with;

```
pip install -r requirements.txt
```
or run though Jupyter notebook docker container:

```
!python programmentwurf.py
```

Make sure the `programmentwurf`.py and bayesian network model file `bayesian_model`.p are in the same directory.
Modify and/or overwrite the existing `versicherung_validation`.csv and run the programm to get predictions.
