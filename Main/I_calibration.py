import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Spécifiez le chemin vers le dossier contenant les fichiers
#folder_path = os.path.join('Users', 'Downloads', 'Master', 'Ma2', 'Master_thesis', 'Code_thesis', 'TR_data_pscad')
folder_path = os.getcwd()

# Liste des noms de fichiers
I_calibration = ['I_0_sensor2.txt', 'I_6_test4.txt', 'I_9_test4.txt']

# Initialiser des listes pour stocker toutes les données
all_Ii_values = []
all_Io_values = []

# Boucler sur chaque fichier
for file_name in I_calibration:
    # Construire le chemin complet du fichier
    file_path = os.path.join(folder_path, file_name)
    
    # Charger les données depuis le fichier texte correspondant
    Ii_values = np.loadtxt(file_path)  # Assurez-vous que vos données sont bien organisées dans une seule colonne
    
    # Extraire la valeur de Io à partir du nom du fichier
    Io = int(file_name.split('_')[1].split('_')[0])  # Supposant que le format du nom du fichier est I_X_test.txt
    
    # Ajouter les données aux listes globales
    all_Ii_values.extend(Ii_values)
    all_Io_values.extend(np.repeat(Io, len(Ii_values)))

# Convertir les listes en tableaux NumPy
all_Ii_values = np.array(all_Ii_values)
all_Io_values = np.array(all_Io_values)

# Calculer l'interpolation linéaire globale
coefficients = np.polyfit(all_Ii_values, all_Io_values, 1)

# Récupérer les valeurs des paramètres θ1 et θ2
theta1 = coefficients[0]
theta2 = coefficients[1]

# Affichage des résultats
print(f"θ1 (pente) : {theta1}")
print(f"θ2 (ordonnée à l'origine) : {theta2}")

# Tracer le graphique
plt.scatter(all_Ii_values, all_Io_values, label='Données brutes')
plt.plot(all_Ii_values, theta1 * all_Ii_values + theta2, color='red', label='Interpolation linéaire')
plt.xlabel('Ii (Données brutes du capteur)')
plt.ylabel('Io (Courant de référence)')
plt.legend()
plt.show()