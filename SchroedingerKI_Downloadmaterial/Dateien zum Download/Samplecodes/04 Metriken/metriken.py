from collections import Counter

# Beispieldatensatz: Medizinischer Test für seltene Krankheit
# 1 = krank, 0 = gesund
# Format: (tatsächlicher_zustand, test_vorhersage)
testdaten = [
    # 5 kranke Patienten (selten)
    (1, 1),  # Korrekt als krank erkannt
    (1, 0),  # Fälschlich als gesund eingestuft
    (1, 0),  # Fälschlich als gesund eingestuft
    (1, 1),  # Korrekt als krank erkannt
    (1, 1),  # Korrekt als krank erkannt
    
    # 95 gesunde Patienten (häufig)
    *[(0, 0)] * 90,  # 90 korrekt als gesund erkannt
    *[(0, 1)] * 5    # 5 fälschlich als krank eingestuft
]

# Berechne die Metriken
true_positives = sum(1 for actual, pred in testdaten if actual == 1 and pred == 1)
true_negatives = sum(1 for actual, pred in testdaten if actual == 0 and pred == 0)
false_positives = sum(1 for actual, pred in testdaten if actual == 0 and pred == 1)
false_negatives = sum(1 for actual, pred in testdaten if actual == 1 and pred == 0)

# Berechne verschiedene Metriken
accuracy = (true_positives + true_negatives) / len(testdaten)
precision = true_positives / (true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)

print("Medizinischer Screening-Test Auswertung")
print("-" * 40)
print(f"Gesamtzahl Patienten: {len(testdaten)}")
print(f"Davon tatsächlich krank: {sum(1 for actual, _ in testdaten if actual == 1)}")
print(f"Davon tatsächlich gesund: {sum(1 for actual, _ in testdaten if actual == 0)}")
print("\nErgebnisse:")
print(f"True Positives (korrekt als krank erkannt): {true_positives}")
print(f"False Positives (fälschlich als krank eingestuft): {false_positives}")
print(f"True Negatives (korrekt als gesund erkannt): {true_negatives}")
print(f"False Negatives (fälschlich als gesund eingestuft): {false_negatives}")
print("\nMetriken:")
print(f"Accuracy: {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")