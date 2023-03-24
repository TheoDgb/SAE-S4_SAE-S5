import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_file, save, show

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
# données par usager
usagersdata = pd.merge(accidents,usagers)
# données par véhicule
vehiculesdata = pd.merge(accidents,vehicules)

# enlever les -1 dans la colonne sexe
usagersdata = usagersdata.loc[usagersdata['sexe'] != -1]

################################# Graphes #################################

# Créer une table pivot des données d'usagers

# => Chaque ligne représente une catégorie d'usager,
# chaque colonne représente un type de blessure,
# avec le nombre d'usagers correspondant dans chaque cellule

# => la colonne'Num_Acc' est utilisé pour compter les usagers dans la table pivot car c'est un numéro unique pour chaque accident
pivot_table = pd.pivot_table(usagers, values='Num_Acc', index='catu', columns='grav', aggfunc='count')

# Créer la source de données ColumnDataSource
source = ColumnDataSource(data=dict(
    catu=['Conducteur', 'Passager', 'Piéton'],
    indemne=list(pivot_table[1]),
    tue=list(pivot_table[2]),
    hospitalise=list(pivot_table[3]),
    leger=list(pivot_table[4])
))

# Créer la figure avec les barres empilées => vbar_stack
fig = figure(x_range=['Conducteur', 'Passager', 'Piéton'],
             x_axis_label="Catégorie d'usager", y_axis_label="Nombre d'usagers",
             title="Nombre d'usagers pour chaque type de blessure par catégorie d'usager \nen 2019-2020-2021",
             # Afficher les infos en passant la souris
             tools=[HoverTool(tooltips=[
                 ('Catégorie', '@catu'),
                 ('Tué', '@tue'),
                 ('Blessé hospitalisé', '@hospitalise'),
                 ('Blessé léger', '@leger'),
                 ('Indemne', '@indemne')
             ])])
fig.vbar_stack(['tue', 'hospitalise', 'leger', 'indemne'], x='catu', width=0.8, color=['red', 'orange', 'blue', 'green'],
               source=source,
               legend_label=['Tué', 'Blessé hospitalisé', 'Blessé léger', 'Indemne'])

fig.legend.location = 'top_right'

output_file(filename="./views/nb_usagers_par_blessure_et_categorie.html")
# show(fig)
save(fig)