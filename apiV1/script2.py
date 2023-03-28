import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

################################# Import des fichiers CSV #################################

# lectures des fichiers de 2021
caracteristiques2021 = pd.read_csv('./data/2021/caracteristiques-2021.csv',sep=';')
lieux2021 = pd.read_csv('./data/2021/lieux-2021.csv',sep=';')
usagers2021 = pd.read_csv('./data/2021/usagers-2021.csv',sep=';')
vehicules2021 = pd.read_csv('./data/2021/vehicules-2021.csv',sep=';')

# lectures des fichiers de 2020
caracteristiques2020 = pd.read_csv('./data/2020/caracteristiques-2020.csv',sep=';')
lieux2020 = pd.read_csv('./data/2020/lieux-2020.csv',sep=';')
usagers2020 = pd.read_csv('./data/2020/usagers-2020.csv',sep=';')
vehicules2020 = pd.read_csv('./data/2020/vehicules-2020.csv',sep=';')

# lectures des fichiers de 2019
caracteristiques2019 = pd.read_csv('./data/2019/caracteristiques-2019.csv',sep=';')
lieux2019 = pd.read_csv('./data/2019/lieux-2019.csv',sep=';')
usagers2019 = pd.read_csv('./data/2019/usagers-2019.csv',sep=';')
vehicules2019 = pd.read_csv('./data/2019/vehicules-2019.csv',sep=';')

################################# Modifications des données #################################

# concaténation des années
caracteristiques = pd.concat([caracteristiques2021,caracteristiques2020,caracteristiques2019])
lieux = pd.concat([lieux2021,lieux2020,lieux2019])
usagers = pd.concat([usagers2021,usagers2020,usagers2019])
vehicules = pd.concat([vehicules2021,vehicules2020,vehicules2019])

# remplace les "," par des ".", les ":" par des "."  et convertit en float pour les latitudes et longitudes
caracteristiques['lat'] = caracteristiques['lat'].str.replace(',', '.').astype(float)
caracteristiques['long'] = caracteristiques['long'].str.replace(',', '.').astype(float)
caracteristiques['hrmn'] = caracteristiques['hrmn'].str.replace(':', '.').astype(float)

# données par accident
accidents = pd.merge(caracteristiques,lieux)
# drop des colonnes inutiles
accidents = accidents.drop(columns=['com', 'adr', 'int', 'voie', 'v1', 'v2', 'circ', 'nbv', 'vosp', 'prof', 'pr', 'pr1', 'plan', 'lartpc'])

# données par usager
usagersdata = pd.merge(accidents,usagers)

# données par véhicule
vehiculesdata = pd.merge(accidents,vehicules)
# drop des colonnes inutiles
vehiculesdata = vehiculesdata.drop(columns=['senc'])

# enlever les -1 dans la colonne sexe
usagersdata = usagersdata.loc[usagersdata['sexe'] != -1]

# ajouter une colonne nombre d'usagers impliqués dans l'accident
merged_df = pd.merge(accidents, usagers, on='Num_Acc')
# Calculer le nombre d'usagers par accident
usagers_par_accident = merged_df.groupby('Num_Acc')['Num_Acc'].count().reset_index(name='Nombre_Usagers')
# Fusionner le nombre d'usagers par accident avec le dataframe accidents
accidents = pd.merge(accidents, usagers_par_accident, on='Num_Acc')
accidents = accidents.rename(columns={'Num_Acc_x': 'Num_Acc', 'Num_Acc_y': 'Nombre_Usagers'})

# ajouter une colonne nombre de véhicules impliqués dans l'accident
merged_df = pd.merge(accidents, vehicules, on='Num_Acc')
# Calculer le nombre de vehicules par accident
vehicules_par_accident = merged_df.groupby('Num_Acc')['Num_Acc'].count().reset_index(name='Nombre_Vehicules')
# Fusionner le nombre de vehicules par accident avec le dataframe accidents
accidents = pd.merge(accidents, vehicules_par_accident, on='Num_Acc')
accidents = accidents.rename(columns={'Num_Acc_x': 'Num_Acc', 'Num_Acc_y': 'Nombre_Vehicules'})

################################# Graphes #################################

# Compter le nombre d'accidents par nombre de véhicules impliqués
fig = plt.figure(figsize=(6.5, 5))
fig.subplots_adjust(right=0.6)

u_count = accidents['Nombre_Usagers'].value_counts()

# Regrouper les catégories 6 et plus en une catégorie
last_index_to_combine = 5
new_label = "6+"
new_size = sum(u_count[last_index_to_combine:])

labels = u_count.index.tolist()[:last_index_to_combine] + [new_label]
sizes = u_count.values.tolist()[:last_index_to_combine] + [new_size]

# Créer le diagramme circulaire
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=180)
plt.axis('equal')
plt.legend(title='Nombre d usagers impliqués', loc='center left', bbox_to_anchor=(1, 0.5))

# Afficher le diagramme
plt.title('Répartition du nombre d usagers par accident')
plt.savefig("./public/images/image_nb_accidents_par_usager.png")
# plt.show()



# Compter le nombre d'accidents par nombre de véhicules impliqués
fig = plt.figure(figsize=(6.5, 5))
fig.subplots_adjust(right=0.6)

v_count = accidents['Nombre_Vehicules'].value_counts()

# Regrouper les catégories 4 et plus en une catégorie
last_index_to_combine = 4
new_label = "5+"
new_size = sum(u_count[last_index_to_combine:])

labels = v_count.index.tolist()[:last_index_to_combine] + [new_label]
sizes = v_count.values.tolist()[:last_index_to_combine] + [new_size]

# Créer le diagramme circulaire
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=180)
plt.axis('equal')
plt.legend(title='Nombre de vehicules impliqués', loc='center left', bbox_to_anchor=(1, 0.5))

# Afficher le diagramme
plt.title('Répartition du nombre de véhicules par accident')
plt.savefig("./public/images/image_nb_vehicules_par_accident.png")
# plt.show()



# Mapper les numéros à des textes dans un dictionnaire
fig = plt.figure()

etat_texte = {1: 'Indemne', 2: 'Tué', 3: 'Blessé hospitalisé', 4: 'Blessé léger'}

df = usagersdata

# Remplacer les numéros par les textes dans la colonne "état"
df['grav'] = df['grav'].replace(etat_texte)

# Compter le nombre d'occurrences de chaque état pour chaque place
counts = df.groupby(['place', 'grav'])['grav'].count()

# Diviser par le nombre total d'occurrences pour chaque place pour obtenir les proportions
proportions = counts.groupby('place', group_keys=False).apply(lambda x: x / float(x.sum()))

# Afficher le graphique à barres des proportions pour chaque place
ax = proportions.unstack().plot(kind='bar', stacked=True)
ax.set_ylabel('Proportion')
ax.set_title('Proportion de chaque état après accidents pour chaque place')

# Déplacer la légende en dehors du graphique
ax.legend(title='État', loc='center right', bbox_to_anchor=(1, 0.5))
plt.savefig("./public/images/image_proportion_etat_apres_accident_par_place.png")
# plt.show()