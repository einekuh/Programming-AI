import kagglehub
path = kagglehub.dataset_download("lainguyn123/student-performance-factors")

filename = path + "/StudentPerformanceFactors.csv"
print("Dataset file: ", filename)

import pandas as pandas

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

print(df["Hours_Studied"].value_counts( ))