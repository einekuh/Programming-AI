import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from matplotlib.patches import FancyArrowPatch

# Zufällige Daten erzeugen mit Korrelation zwischen zwei Variablen
np.random.seed(42)  # Für Reproduzierbarkeit
n_samples = 150

# Korrelierte Daten erstellen (positive Korrelation)
x = np.random.normal(size=n_samples)
noise = np.random.normal(0, 0.5, n_samples)
y = x + noise  # Variable 2 hängt von Variable 1 ab plus etwas Rauschen

# Daten in Matrix umwandeln
X = np.vstack((x, y)).T

# PCA durchführen
pca = PCA(n_components=2)
pca.fit(X)

# Eigenvektoren (Hauptkomponenten) extrahieren
components = pca.components_
explained_variance = pca.explained_variance_

# Skalierungsfaktor für die Pfeile (zur besseren Sichtbarkeit)
arrow_scale = 3.5

# Plot erstellen
plt.figure(figsize=(10, 8))

# Daten plotten
plt.scatter(X[:, 0], X[:, 1], color='red', alpha=0.7)

# Mittelwert berechnen (PCA Zentrum)
mean = np.mean(X, axis=0)

# Hauptkomponenten als Pfeile darstellen
for i, (comp, var) in enumerate(zip(components, explained_variance)):
    comp = comp * np.sqrt(var) * arrow_scale  # Skalieren mit Varianz für bessere Visualisierung
    
    # Farbe und Stil je nach Komponente
    if i == 0:
        color = 'darkred'
        width = 3
    else:
        color = 'blue'
        width = 2
    
    # Pfeil zeichnen
    arrow = FancyArrowPatch(
        mean, mean + comp,
        arrowstyle='-|>',
        linewidth=width,
        color=color,
        mutation_scale=15
    )
    plt.gca().add_patch(arrow)
    
    # Text für Hauptkomponente
    text_pos = mean + comp * 1.1
    plt.annotate(
        f'Hauptkomponente {i+1}',
        xy=text_pos,
        xytext=text_pos + np.array([0.5, 0.5]) if i == 0 else text_pos + np.array([0.5, -1.5]),
        fontsize=12,
        color=color,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color, lw=1),
        arrowprops=dict(arrowstyle="->", color=color)
    )

# Achsenbeschriftungen
plt.xlabel('Variable 1', fontsize=12)
plt.ylabel('Variable 2', fontsize=12)
plt.title('PCA Visualisierung: Hauptkomponenten in 2D', fontsize=14)

# Achseneinstellungen für bessere Sichtbarkeit
x_range = np.max(X[:, 0]) - np.min(X[:, 0])
y_range = np.max(X[:, 1]) - np.min(X[:, 1])
plt.xlim([np.min(X[:, 0]) - x_range*0.1, np.max(X[:, 0]) + x_range*0.1])
plt.ylim([np.min(X[:, 1]) - y_range*0.1, np.max(X[:, 1]) + y_range*0.1])

# Grid anzeigen
plt.grid(True, linestyle='--', alpha=0.7)

# Gleichmäßige Skalierung für beide Achsen
plt.axis('equal')

plt.tight_layout()
plt.savefig('pca_visualization.png', dpi=300, bbox_inches='tight')
plt.show()