
import pandas as pd

# Dateipfad zur Excel-Datei angeben
excel_datei = "C:\Users\Acer\BettingOddsCalculator\DataFootballData"

# Excel-Datei einlesen
daten = pd.read_excel(excel_datei)

# Jetzt kannst du mit den Daten arbeiten, z.B. sie anzeigen
print(daten)