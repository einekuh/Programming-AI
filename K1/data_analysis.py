import kagglehub
import pandas as pandas
import matplotlib.pyplot as plt

path = kagglehub.dataset_download("lainguyn123/student-performance-factors")

filename = path + "/StudentPerformanceFactors.csv"
print("Dataset file: ", filename)



df = pandas.read_csv(filename)

# Grundlegende Infos zum Datensatz auslesen
#print(df.info())

# Die ersten 5 und die letzen 5 Datensätze ausgeben lassen
#print(df.head())
#print(df.tail()) 

# Statistische Angaben zum Datensatz ausgeben lassen
#print(df.describe())

# Anzahl der Werte in einer Spalte
#print(df.count())


# Ausgabe der Häufigkeiten der einzelen Merkamlsausprägungen
#print(df["Hours_Studied"].value_counts())


# Daten in einem Streudiagramm plotten

# Daten für den Plot vorbereiten
x = df['Hours_Studied']
y = df['Exam_Score']

# Plot erstellen
plt.scatter(x, y)
plt.xlabel('Stunden gelernt')
plt.ylabel('Ergebnis')
plt.title('Stunden gelernt vs. Ergebnis')
plt.show()