# Beispielhafte Confusion Matrix
cm = [[150, 2],  # [TN, FP]
      [4, 6]]    # [FN, TP]
cm = [[142, 21], [11, 134]]
# Berechne Precision, Recall, F1-Score und Support für jede Klasse
def calculate_metrics(cm):
    # True Positives, False Positives, False Negatives, True Negatives
    tp = cm[1][1]
    fp = cm[0][1]
    fn = cm[1][0]
    tn = cm[0][0]

    # Precision
    precision_true = tp / (tp + fp) if (tp + fp) != 0 else 0
    precision_false = tn / (tn + fn) if (tn + fn) != 0 else 0

    # Recall
    recall_true = tp / (tp + fn) if (tp + fn) != 0 else 0
    recall_false = tn / (tn + fp) if (tn + fp) != 0 else 0

    # F1-Score
    f1_true = 2 * (precision_true * recall_true) / (precision_true + recall_true) if (precision_true + recall_true) != 0 else 0
    f1_false = 2 * (precision_false * recall_false) / (precision_false + recall_false) if (precision_false + recall_false) != 0 else 0

    # Support
    support_true = tp + fn
    support_false = tn + fp

    # Macro Average
    macro_avg_precision = (precision_true + precision_false) / 2
    macro_avg_recall = (recall_true + recall_false) / 2
    macro_avg_f1 = (f1_true + f1_false) / 2

    # Weighted Average
    total_support = support_true + support_false
    weighted_avg_precision = ((precision_true * support_true) + (precision_false * support_false)) / total_support
    weighted_avg_recall = ((recall_true * support_true) + (recall_false * support_false)) / total_support
    weighted_avg_f1 = ((f1_true * support_true) + (f1_false * support_false)) / total_support

    return {
        "precision": {"True": precision_true, "False": precision_false},
        "recall": {"True": recall_true, "False": recall_false},
        "f1-score": {"True": f1_true, "False": f1_false},
        "support": {"True": support_true, "False": support_false},
        "macro avg": {"precision": macro_avg_precision, "recall": macro_avg_recall, "f1-score": macro_avg_f1},
        "weighted avg": {"precision": weighted_avg_precision, "recall": weighted_avg_recall, "f1-score": weighted_avg_f1}
    }

# Berechne die Metriken basierend auf der Confusion Matrix
metrics = calculate_metrics(cm)

# Drucke den Klassifikationsbericht basierend auf der Confusion Matrix
print("Klassifikationsbericht:")
print(f"              precision    recall  f1-score   support")
print(f"       False       {metrics['precision']['False']:.2f}      {metrics['recall']['False']:.2f}      {metrics['f1-score']['False']:.2f}       {metrics['support']['False']}")
print(f"        True       {metrics['precision']['True']:.2f}      {metrics['recall']['True']:.2f}      {metrics['f1-score']['True']:.2f}       {metrics['support']['True']}")
print(f"   macro avg       {metrics['macro avg']['precision']:.2f}      {metrics['macro avg']['recall']:.2f}      {metrics['macro avg']['f1-score']:.2f}")
print(f"weighted avg       {metrics['weighted avg']['precision']:.2f}      {metrics['weighted avg']['recall']:.2f}      {metrics['weighted avg']['f1-score']:.2f}")