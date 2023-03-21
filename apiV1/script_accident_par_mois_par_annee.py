import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

caracteristiques2021 = pd.read_csv('./data/2021/caracteristiques-2021.csv',sep=';')
lieux2021 = pd.read_csv('./data/2021/lieux-2021.csv',sep=';')
usagers2021 = pd.read_csv('./data/2021/usagers-2021.csv',sep=';')
vehicules2021 = pd.read_csv('./data/2021/vehicules-2021.csv',sep=';')

caracteristiques2020 = pd.read_csv('./data/2020/caracteristiques-2020.csv',sep=';')
lieux2020 = pd.read_csv('./data/2020/lieux-2020.csv',sep=';')
usagers2020 = pd.read_csv('./data/2020/usagers-2020.csv',sep=';')
vehicules2020 = pd.read_csv('./data/2020/vehicules-2020.csv',sep=';')

caracteristiques2019 = pd.read_csv('./data/2019/caracteristiques-2019.csv',sep=';')
lieux2019 = pd.read_csv('./data/2019/lieux-2019.csv',sep=';')
usagers2019 = pd.read_csv('./data/2019/usagers-2019.csv',sep=';')
vehicules2019 = pd.read_csv('./data/2019/vehicules-2019.csv',sep=';')

################################# Modifications des données #################################

# supprimer les lignes qui ont pour valeur de sexe -1
usagers2021 = usagers2021.loc[usagers2021['sexe'] != -1]

accidents2021 = pd.merge(caracteristiques2021,lieux2021)
accidents2020 = pd.merge(caracteristiques2020,lieux2020)
accidents2019 = pd.merge(caracteristiques2019,lieux2019)

accidents = pd.concat([accidents2021,accidents2020,accidents2019])
usagers = pd.concat([usagers2021,usagers2020,usagers2019])
vehicules = pd.concat([vehicules2021,vehicules2020,vehicules2019])

# remplace les "," par des ".", les ":" par des "."  et convertit en float
# accidents['lat'] = accidents['lat'].str.replace(',', '.').astype(float)
# accidents['long'] = accidents['long'].str.replace(',', '.').astype(float)
# accidents['hrmn'] = accidents['hrmn'].str.replace(':', '.').astype(float)
# accidents = accidents.loc[accidents['vma'] != -1]

################################# Graphes #################################

# Nombre d'accidents par mois de l'année

# ===== Graphe nb accidents par mois pour 2019-2020-2021 =====
fig = plt.figure(figsize=(6.5, 6))
ax = fig.add_subplot(1, 1, 1)
fig.subplots_adjust(bottom=0.2)

sns.countplot(x='mois', data=accidents)
plt.title('Nombre d\'accidents par mois de 2019-2020-2021')
plt.xlabel("Mois de l'accident")
plt.ylabel("Nombre d'accidents")
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ['Janvier', 'Février', 'Mars', 'Avril', 'Mai',
                                       'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre',
                                       'Novembre', 'Décembre'], rotation=90)
plt.savefig("./public/images/image_accidents_mois_all.png")
# plt.show()

# ===== Graphe nb accidents par mois 2021 =====
fig = plt.figure(figsize=(6.5, 6))
ax = fig.add_subplot(1, 1, 1)
fig.subplots_adjust(bottom=0.2)

sns.countplot(x='mois', data=accidents2021)
plt.title('Nombre d\'accidents par mois de 2021')
plt.xlabel("Mois de l'accident")
plt.ylabel("Nombre d'accidents")
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ['Janvier', 'Février', 'Mars', 'Avril', 'Mai',
                                       'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre',
                                       'Novembre', 'Décembre'], rotation=90)
plt.savefig("./public/images/image_accidents_mois_2021.png")
# plt.show()

# ===== Graphe nb accidents par mois 2020 =====
fig = plt.figure(figsize=(6.5, 6))
ax = fig.add_subplot(1, 1, 1)
fig.subplots_adjust(bottom=0.2)

sns.countplot(x='mois', data=accidents2020)
plt.title('Nombre d\'accidents par mois de 2020')
plt.xlabel("Mois de l'accident")
plt.ylabel("Nombre d'accidents")
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ['Janvier', 'Février', 'Mars', 'Avril', 'Mai',
                                       'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre',
                                       'Novembre', 'Décembre'], rotation=90)
plt.savefig("./public/images/image_accidents_mois_2020.png")
# plt.show()

# ===== Graphe nb accidents par mois 2019 =====
fig = plt.figure(figsize=(6.5, 6))
ax = fig.add_subplot(1, 1, 1)
fig.subplots_adjust(bottom=0.2)

sns.countplot(x='mois', data=accidents2019)
plt.title('Nombre d\'accidents par mois de 2019')
plt.xlabel("Mois de l'accident")
plt.ylabel("Nombre d'accidents")
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ['Janvier', 'Février', 'Mars', 'Avril', 'Mai',
                                       'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre',
                                       'Novembre', 'Décembre'], rotation=90)
plt.savefig("./public/images/image_accidents_mois_2019.png")
# plt.show()