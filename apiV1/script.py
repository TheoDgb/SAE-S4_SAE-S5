import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
# 3D graphe
from mpl_toolkits.mplot3d import Axes3D
# Heatmap
import folium
from folium.plugins import HeatMap

################################# Importation des fichiers CSV #################################

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
accidents['lat'] = accidents['lat'].str.replace(',', '.').astype(float)
accidents['long'] = accidents['long'].str.replace(',', '.').astype(float)
accidents['hrmn'] = accidents['hrmn'].str.replace(':', '.').astype(float)
accidents = accidents.loc[accidents['vma'] != -1]

################################# Graphes #################################

# ===== répartition des usagers par sexe =====
fig = plt.figure(figsize=(6.5, 5))
sns.countplot(x='sexe', data=usagers)
plt.title('Répartition des usagers par sexe en 2019-2020-2021')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1], ['Homme', 'Femme'])
plt.savefig("./public/images/image_sexe_all.png")
# plt.show()

fig = plt.figure(figsize=(6.5, 5))
sns.countplot(x='sexe', data=usagers2021)
plt.title('Répartition des usagers par sexe en 2021')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1], ['Homme', 'Femme'])
plt.savefig("./public/images/image_sexe2021.png")
# plt.show()

fig = plt.figure(figsize=(6.5, 5))
sns.countplot(x='sexe', data=usagers2020)
plt.title('Répartition des usagers par sexe en 2020')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1], ['Homme', 'Femme'])
plt.savefig("./public/images/image_sexe2020.png")
# plt.show()

fig = plt.figure(figsize=(6.5, 5))
sns.countplot(x='sexe', data=usagers2019)
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
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Créer un histogramme en 2D des heures et des mois
hist, xedges, yedges = np.histogram2d(accidents['hrmn'], accidents['mois'], bins=(24, 12))
# Obtenir les coordonnées x, y et z des bords de l'histogramme
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0
# Obtenir les dimensions des bords de chaque rectangle d'histogramme
dx = dy = 1
dz = hist.ravel()
# Créer l'histogramme en 3D
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

ax.set_xlabel('Heures')
ax.set_ylabel('Mois')
ax.set_zlabel('Nombre d\'accidents')
ax.set_title('Histogramme 3D du nombre d\'accidents par heures et mois')
plt.savefig("./public/images/image_3d_accidents_heures_mois.png")
# plt.show()



# ===== Heatmap nombre d'accidents =====
map = folium.Map(location=[46.2276, 2.2137], zoom_start=6)

# Ajouter une couche de chaleur (heatmap) en utilisant les coordonnées des accidents
heatmap = HeatMap(data=accidents[['lat', 'long']], radius=15)
heatmap.add_to(map)

# Ajouter une couche de contrôle avec une légende pour la heatmap
folium.LayerControl().add_to(map)
map.add_child(heatmap)

# trèèès long à charger => heatmap créée sur Jupyter puis sauvegardée dans le projet
# map.save("./public/view/heatmapshow.html")
# afficher la carte
# map

# faire un await dans le javascript pour attendre le dl des csv