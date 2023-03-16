import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

################################# Importation des fichiers CSV #################################

file_names = ['./data/2021/usagers-2021.csv', './data/2021/vehicules-2021.csv', './data/2021/lieux-2021.csv', './data/2021/caracteristiques-2021.csv']
donnees_2021 = pd.read_csv(file_names[0])

for file in file_names[1:]:
    temp_df = pd.read_csv(file)
    donnees_2021 = pd.merge(donnees_2021, temp_df, on='id', how='inner')

donnees_2021 = donnees_2021.sort_values(by='id').reset_index(drop=True)


file_names = ['./data/2020/usagers-2020.csv', './data/2020/vehicules-2020.csv', './data/2020/lieux-2020.csv', './data/2020/caracteristiques-2020.csv']
donnees_2020 = pd.read_csv(file_names[0])

for file in file_names[1:]:
    temp_df = pd.read_csv(file)
    donnees_2020 = pd.merge(donnees_2020, temp_df, on='id', how='inner')

donnees_2020 = donnees_2020.sort_values(by='id').reset_index(drop=True)

file_names = ['./data/2019/usagers-2019.csv', './data/2019/vehicules-2019.csv', './data/2019/lieux-2019.csv', './data/2019/caracteristiques-2019.csv']
donnees_2019 = pd.read_csv(file_names[0])

for file in file_names[1:]:
    temp_df = pd.read_csv(file)
    donnees_2019 = pd.merge(donnees_2019, temp_df, on='id', how='inner')

donnees_2019 = donnees_2019.sort_values(by='id').reset_index(drop=True)


################################# Modifications des données #################################

donnees_2021 = donnees_2021.loc[donnees_2021['sexe'] != -1]

donnees_combined = pd.concat([donnees_2019, donnees_2020, donnees_2021], ignore_index=True)

# rempalce les "," par des ".", les ":" par des "."  et convertit en float
donnees_combined['lat'] = donnees_combined['lat'].str.replace(',', '.').astype(float)
donnees_combined['long'] = donnees_combined['long'].str.replace(',', '.').astype(float)
donnees_combined['hrmn'] = donnees_combined['hrmn'].str.replace(':', '.').astype(float)
donnees_combined = donnees_combined.loc[donnees_combined['vma'] != -1]
################################# Graphes #################################

# Nombre d'accidents par mois de l'année

# ===== Graphe nb accidents par mois 2019 =====
sns.countplot(x='mois', data=donnees_2019)
plt.title('Nombre d\'accidents par mois de 2019')
plt.xlabel("Mois de l'accident")
plt.ylabel("Nombre d'accidents")
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ['Janvier', 'Février', 'Mars', 'Avril', 'Mai',
                                       'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre',
                                       'Novembre', 'Décembre'], rotation=90)
plt.savefig("./public/images/image_accidents_mois_2019.png")
# plt.show()
# ===== Graphe nb accidents par mois 2020 =====
sns.countplot(x='mois', data=donnees_2020)
plt.title('Nombre d\'accidents par mois de 2020')
plt.xlabel("Mois de l'accident")
plt.ylabel("Nombre d'accidents")
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ['Janvier', 'Février', 'Mars', 'Avril', 'Mai',
                                       'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre',
                                       'Novembre', 'Décembre'], rotation=90)
plt.savefig("./public/images/image_accidents_mois_2020.png")
# plt.show()
# ===== Graphe nb accidents par mois 2021 =====
sns.countplot(x='mois', data=donnees_2021)
plt.title('Nombre d\'accidents par mois de 2021')
plt.xlabel("Mois de l'accident")
plt.ylabel("Nombre d'accidents")
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ['Janvier', 'Février', 'Mars', 'Avril', 'Mai',
                                       'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre',
                                       'Novembre', 'Décembre'], rotation=90)
plt.savefig("./public/images/image_accidents_mois_2021.png")
# plt.show()
# ===== Graphe nb accidents par mois pour 2019-2020-2021 =====
sns.countplot(x='mois', data=donnees_combined)
plt.title('Nombre d\'accidents par mois de 2019-2020-2021')
plt.xlabel("Mois de l'accident")
plt.ylabel("Nombre d'accidents")
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ['Janvier', 'Février', 'Mars', 'Avril', 'Mai',
                                       'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre',
                                       'Novembre', 'Décembre'], rotation=90)
plt.savefig("./public/images/image_accidents_mois_all.png")
# plt.show()