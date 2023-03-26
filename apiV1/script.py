import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_file, save, show

# 3D graphe
import plotly.graph_objs as go
# Heatmap
import folium
from folium.plugins import HeatMap

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

# ===== répartition des usagers par sexe =====
fig = plt.figure(figsize=(6.5, 5))
sns.countplot(x='sexe', data=usagersdata)
plt.title('Répartition des usagers par sexe en 2019-2020-2021')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1], ['Homme', 'Femme'])
plt.savefig("./public/images/image_sexe_all.png")
# plt.show()

fig = plt.figure(figsize=(6.5, 5))
sns.countplot(x='sexe', data=usagersdata[usagersdata['an'] == 2021])
plt.title('Répartition des usagers par sexe en 2021')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1], ['Homme', 'Femme'])
plt.savefig("./public/images/image_sexe2021.png")
# plt.show()

fig = plt.figure(figsize=(6.5, 5))
sns.countplot(x='sexe', data=usagersdata[usagersdata['an'] == 2020])
plt.title('Répartition des usagers par sexe en 2020')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1], ['Homme', 'Femme'])
plt.savefig("./public/images/image_sexe2020.png")
# plt.show()

fig = plt.figure(figsize=(6.5, 5))
sns.countplot(x='sexe', data=usagersdata[usagersdata['an'] == 2019])
plt.title('Répartition des usagers par sexe en 2019')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1], ['Homme', 'Femme'])
plt.savefig("./public/images/image_sexe2019.png")
# plt.show()



# ===== type de collisions =====
fig = plt.figure(figsize=(6.5, 8))
ax = fig.add_subplot(1, 1, 1)
fig.subplots_adjust(bottom=0.45)

sns.countplot(x='col', data=accidents)
plt.title('Type de collisions')
plt.xlabel('Type de collisions')
plt.ylabel('Nombre de collisions')
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7], ['Non renseigné', 'Deux véhicules - frontale', 'Deux véhicules – par l’arrière',
                                       'Deux véhicules – par le coté', 'Trois véhicules et plus – en chaîne',
                                       'Trois véhicules et plus - collisions multiples', 'Autre collision',
                                       'Sans collision'], rotation=90)
plt.savefig("./public/images/image_accidents_type_collisions.png")
# plt.show()



# ===== 3D Histogramme nombre d'accidents par heures et mois =====

# Créer un histogramme en 2D des heures et des mois
# compte le nombre d'accidents pour chaque combinaison de mois et d'heure
hist, xedges, yedges = np.histogram2d(accidents['mois'], accidents['hrmn'], bins=(12, 24))

# Créer l'histogramme en 3D
fig = go.Figure(data=[go.Surface(x=np.flip(xedges[:-1]), y=yedges[:-1], z=hist.T)]) #.T pour inverser les axes, on peut mettre colorscale='jet' pour changer la couleur
# np.flip pour inverser l'axe des mois "du 12 au 1" au lieu de "du 1 au 12"

fig.update_layout(title='Histogramme 3D du nombre d\'accidents par heure et mois',
                  scene=dict(xaxis_title='Mois', yaxis_title='Heures', zaxis_title='Nombre d\'accidents'),
                  scene_xaxis_ticktext=np.flip(['Décembre', 'Novembre', 'Octobre', 'Septembre', 'Août', 'Juillet', 'Juin', 'Mai', 'Avril', 'Mars', 'Février', 'Janvier']),
                  scene_xaxis_tickvals=np.flip(xedges[:-1]))
                  # inverse l'affichage dans la légende des mois et donne le nom des mois
fig.write_html('./views/3d_nb_accidents_heures_mois.html')
# fig.show()



# ===== Heatmap nombre d'accidents =====
map = folium.Map(location=[46.2276, 2.2137], zoom_start=6)

# Ajouter une couche de chaleur (heatmap) en utilisant les coordonnées des accidents
heatmap = HeatMap(data=accidents[['lat', 'long']], radius=15)
heatmap.add_to(map)

# Ajouter une couche de contrôle avec une légende pour la heatmap
folium.LayerControl().add_to(map)
map.add_child(heatmap)

map.save("./views/heatmapshow.html")