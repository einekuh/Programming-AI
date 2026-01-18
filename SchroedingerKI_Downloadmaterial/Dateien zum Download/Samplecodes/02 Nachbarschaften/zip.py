list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Verwende zip, um die beiden Listen zu kombinieren
zipped = zip(list1, list2)

# Konvertiere den zip-Iterator in eine Liste und drucke sie aus
print(list(zipped))