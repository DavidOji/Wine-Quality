# Importieren der notwendigen Bibliotheken
import pandas as pd  # Für die Datenanalyse und -manipulation
import matplotlib.pyplot as plt  # Zum Erstellen von Diagrammen und Grafiken
import numpy as np  # Für numerische Operationen

# Aufgabe 1: Laden der Weindaten aus einer CSV-Datei
path = "winequality-red.csv"  # Dateipfad für die CSV-Datei
df = pd.read_csv(path, delimiter=";")  # Lesen der CSV-Datei mit Semikolon als Trennzeichen

# Zeigen der ersten Zeilen der Daten, um die Struktur zu überprüfen
print(df.head())  # Zeigt die ersten 5 Zeilen des DataFrame
# print(df.tail())  # (optional) Zeigt die letzten 5 Zeilen
# print(df.info())  # (optional) Zeigt Informationen zum DataFrame, einschließlich Datentypen

# Überprüfen auf fehlende Werte (Nullwerte)
print(df.isnull().any())  # Gibt ein Boolesches Ergebnis zurück, das angibt, ob es Nullwerte in irgendeiner Spalte gibt

# Entfernen von Duplikaten, um sicherzustellen, dass jeder Datensatz eindeutig ist
df = df.drop_duplicates()  # Entfernt doppelte Zeilen im DataFrame

# Berechnen von deskriptiven Statistiken für die numerischen Spalten
descriptiv_statistic = df.describe()  # Liefert Statistiken wie Mittelwert, Standardabweichung, Minimum, Maximum, Quartile
print(descriptiv_statistic)  # Gibt die deskriptiven Statistiken aus

# Berechnen der Korrelationsmatrix, um Beziehungen zwischen den Spalten zu analysieren
correlation = df.corr()  # Liefert die Korrelationsmatrix, die Beziehungen zwischen den Spalten darstellt
# Zeigen der Korrelationen zur Qualitäts-Spalte in aufsteigender Reihenfolge
print(correlation["quality"].sort_values())  # Sortiert die Korrelationen nach ihrer Beziehung zur Qualität

# Erstellen eines Histogramms, um die Verteilung der Alkoholwerte zu visualisieren
histogramm_varibal = df["alcohol"]  # Wählt die Spalte "alcohol" für die Histogramm-Visualisierung
plt.hist(histogramm_varibal)  # Erstellt ein Histogramm für die Alkoholverteilung
plt.title("Verteilung des Alkoholgehalts")  # Setzt den Titel des Histogramms
plt.show()  # Zeigt das Histogramm an

# Erstellen eines Scatter-Plots, um die Beziehung zwischen Alkoholgehalt und Weinqualität darzustellen
plt.scatter(df['alcohol'], df['quality'])  # Erstellt einen Scatter-Plot
plt.title('Alkoholgehalt vs. Qualität des Weins')  # Setzt den Titel für den Scatter-Plot
plt.show()  # Zeigt den Scatter-Plot an

# Erstellen eines Boxplots, um die Verteilung des Alkoholgehalts nach Weinqualität anzuzeigen
df.boxplot(column='alcohol', by='quality')  # Erstellt einen Boxplot, der Alkoholgehalt nach Qualität gruppiert
plt.title('Alkoholgehalt nach Weinqualität')  # Setzt den Titel des Boxplots
plt.show()  # Zeigt den Boxplot an
