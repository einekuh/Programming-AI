import pandas as pd

# Datensatz als Dictionary definieren
#data = {
    #"Feature1": [1.10, 1.20, 2.10, 3.10, 1.20],
   # "Feature2": [3.20, 2.10, 5.30, 2.10, 6.40],
    #"Feature3": [0.81, 0.89, 1.80, 2.81, 0.90],
    #"Feature4": [1.60, 1.05, 2.65, 1.05, 3.20],
    #"Feature5": [4.32, 2.84, 7.16, 2.84, 8.64],
    #"Feature6": [0.31, 0.48, 0.19, 0.48, 0.16],
    #"Label": ["A", "B", "A", "C", "D"]
#}

data = {
    "A": [1.10, 1.20, 2.10, 3.10, 1.20],
    "B": [2.40, 2.10, 1.30, 3.10, 6.40],
    "C": [0.80, 1.05, 1.30, 1.05, 3.20],
    "D": [4.32, 2.84, 7.16, 2.84, 8.64]
}

# DataFrame erstellen
df = pd.DataFrame(data)

# Korrelation berechnen (Label-Spalte entfernen)
#correlation_matrix = df.drop(columns=["Label"]).corr()


correlation_matrix = df.corr()

# Formatierung: Rundung auf 2 Dezimalstellen

correlation_matrix = correlation_matrix.round(2)

def print_matrix():
    print(correlation_matrix)
