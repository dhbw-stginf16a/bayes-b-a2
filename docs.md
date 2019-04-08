# Forderung
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

# Actual Content
## Dokumentation
- Netzwerkvisualisierung
  - Eigener Netzwerkentwurf
  - Netzwerkentwurf mit OpenMarkov
- Clustering und Diagramm von continuous data
- Auswahl von Knoten (filtern und vielleicht neue)
- Diagnostische, Kausale, Interkausale, Gemischte Inferenz

## Features

### Jupyter Notebook
- Plot für (continuous) data
- Performance Vergleich von verschiedenen Ansätzen
  - Eigenes Netzwerk vs OpenMarkov Netzwerk
    - Eigen(Komplex)
    - Eigen(Simpel)
    - Alles direkt auf T
    - Mit weniger nodes
    - Mit mehr zwischen nodes
    - OpenMarkov
  - Clustering mit Boxplots vs anderes Clustering
  - Test/Trainingsverteilung
    - 0.25
    - 0.5
    - 0.75
- Cluster data
- Train network
- Predict outcome
- Detiails von ausgewählten Trainings
  - CPT Anzeige
  - (Maybe show independencies)
  - (Maybe show output probability `predict_probability`)
  - (Maybe k-fold cross validation)

### Standalone Programm
- Export / Import CPT
- Input CSV -> Output Classification
- (Maybe CSV Export)
