import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

################################# Importation des fichiers CSV #################################

file_names = ['2021/usagers-2021.csv', '2021/vehicules-2021.csv', '2021/lieux-2021.csv', '2021/caracteristiques-2021.csv']
donnees_2021 = pd.read_csv(file_names[0])

for file in file_names[1:]:
    temp_df = pd.read_csv(file)
    donnees_2021 = pd.merge(donnees_2021, temp_df, on='id', how='inner')

donnees_2021 = donnees_2021.sort_values(by='id').reset_index(drop=True)


file_names = ['2020/usagers-2020.csv', '2020/vehicules-2020.csv', '2020/lieux-2020.csv', '2020/caracteristiques-2020.csv']
donnees_2020 = pd.read_csv(file_names[0])

for file in file_names[1:]:
    temp_df = pd.read_csv(file)
    donnees_2020 = pd.merge(donnees_2020, temp_df, on='id', how='inner')

donnees_2020 = donnees_2020.sort_values(by='id').reset_index(drop=True)

file_names = ['2019/usagers-2019.csv', '2019/vehicules-2019.csv', '2019/lieux-2019.csv', '2019/caracteristiques-2019.csv']
donnees_2019 = pd.read_csv(file_names[0])

for file in file_names[1:]:
    temp_df = pd.read_csv(file)
    donnees_2019 = pd.merge(donnees_2019, temp_df, on='id', how='inner')

donnees_2019 = donnees_2019.sort_values(by='id').reset_index(drop=True)


################################# Modifications des données 2021 #################################

donnees_2021 = donnees_2021.loc[donnees_2021['sexe'] != -1]


################################# Graphes #################################

# afficher un graphe de la répartition des usagers par sexe
sns.countplot(x='sexe', data=donnees_2021)
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
