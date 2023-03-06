import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

file_names = ['./data/usagers-2021.csv', './data/vehicules-2021.csv', './data/lieux-2021.csv', './data/caracteristiques-2021.csv']


donnees = pd.read_csv(file_names[0])

for file in file_names[1:]:
    temp_df = pd.read_csv(file)
    donnees = pd.merge(donnees, temp_df, on='id', how='inner')

donnees = donnees.sort_values(by='id').reset_index(drop=True)

# afficher un graphe de la répartition des usagers par sexe
sns.countplot(x='sexe', data=donnees)
plt.title('Répartition des usagers par sexe')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1, 2], ['Non renseigné','Homme', 'Femme'])
plt.savefig("./public/images/image.png")
plt.show()

#Affiche un graphe avec le type de collisions
sns.countplot(x='col', data=donnees_2021)
plt.title('Type de collisions')
plt.xlabel('Type de collisions')
plt.ylabel('Nombre de collisions')
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7], ['Non renseigné', 'Deux véhicules - frontale', 'Deux véhicules – par l’arrière',
                                       'Deux véhicules – par le coté', 'Trois véhicules et plus – en chaîne', 
                                       'Trois véhicules et plus - collisions multiples', 'Autre collision',
                                       'Sans collision'], rotation=90)
plt.show()
