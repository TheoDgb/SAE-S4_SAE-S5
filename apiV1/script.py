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

# afficher un graphe de la répartition des usagers par sexe
sns.countplot(x='sexe', data=donnees_combined)
plt.title('Répartition des usagers par sexe en 2019-2020-2021')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1], ['Homme', 'Femme'])
plt.savefig("./public/images/image_sexe_all.png")
# plt.show()

sns.countplot(x='sexe', data=donnees_2021)
plt.title('Répartition des usagers par sexe en 2021')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1], ['Homme', 'Femme'])
plt.savefig("./public/images/image_sexe2021.png")
# plt.show()

sns.countplot(x='sexe', data=donnees_2020)
plt.title('Répartition des usagers par sexe en 2020')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1], ['Homme', 'Femme'])
plt.savefig("./public/images/image_sexe2020.png")
# plt.show()

sns.countplot(x='sexe', data=donnees_2019)
plt.title('Répartition des usagers par sexe en 2019')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1], ['Homme', 'Femme'])
plt.savefig("./public/images/image_sexe2019.png")
# plt.show()

sns.countplot(x='sexe', data=donnees_combined)
plt.title('Répartition des usagers par sexe 2019-2020-2021')
plt.xlabel('Sexe')
plt.ylabel('Nombre d\'usagers')
plt.xticks([0, 1], ['Homme', 'Femme'])
plt.savefig("./public/images/image_sexe_combined.png")
# plt.show()

#Affiche un graphe avec le type de collisions
sns.countplot(x='col', data=donnees_combined)
plt.title('Type de collisions')
plt.xlabel('Type de collisions')
plt.ylabel('Nombre de collisions')
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7], ['Non renseigné', 'Deux véhicules - frontale', 'Deux véhicules – par l’arrière',
                                       'Deux véhicules – par le coté', 'Trois véhicules et plus – en chaîne',
                                       'Trois véhicules et plus - collisions multiples', 'Autre collision',
                                       'Sans collision'], rotation=90)
plt.savefig("./public/images/image_accidents_type_collisions.png")
# plt.show()


# ===== Heatmap nombre d'accidents =====
map = folium.Map(location=[46.2276, 2.2137], zoom_start=6)

# Ajouter une couche de chaleur (heatmap) en utilisant les coordonnées des accidents
heatmap = HeatMap(data=donnees_combined[['lat', 'long']], radius=15)
heatmap.add_to(map)

# Ajouter une couche de contrôle avec une légende pour la heatmap
folium.LayerControl().add_to(map)
map.add_child(heatmap)

# map.save("./public/view/heatmapshow.html")
# Afficher la carte
# map




# ===== 3D Histogramme nombre d'accidents par heures et mois =====
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Créer un histogramme en 2D des heures et des mois
hist, xedges, yedges = np.histogram2d(donnees_combined['hrmn'], donnees_combined['mois'], bins=(24, 12))
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