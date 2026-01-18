# Entscheidungsbäume.
# Zählen mithilfe der Counter-Klasse
from collections import Counter

wochenplan = ['Schnitzel', 'Burger', 'Salat', 'Schnitzel', 'Salat', 'Pommes', 'Salat']
gezaehlt = Counter(wochenplan)
print(gezaehlt)
print(gezaehlt.most_common())
print(gezaehlt.most_common(1))
print(gezaehlt.values())
Counter({'Schnitzel': 2, 'Salat': 2, 'Burger': 1, 'Pommes': 1})
# Zugriff auf die Häufigkeit einzelner Elemente
print("Schnitzel:", gezaehlt['Schnitzel'])  # Ausgabe: 2
print("Burger:", gezaehlt['Burger'])        # Ausgabe: 1
print("Salat:", gezaehlt['Salat'])          # Ausgabe: 3
print("Pommes:", gezaehlt['Pommes'])        # Ausgabe: 1
for item, count in gezaehlt.items():
    print(f"{item}: {count}")



# SET Informationen
wochenplan = ['Schnitzel', 'Burger', 'Salat', 'Schnitzel', 'Salat', 'Pommes', 'Salat']
print(set(wochenplan))