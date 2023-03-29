# SAE-S4
Développement d'une API de visualisation de multiples données
Basquin Nicolas, Bolmont Hugo, Dal Gobbo Théo

## Suivi du projet

### 19-20/01
    => Découverte / compréhension du sujet

### 26/01
    => Recherche de différentes données intéressantes à exploiter suivant le cahier des charges

### 2-3/02
    => Validation des données choisies
    Nicolas : Création de l'API javascript et lier un script python à l'API
    Hugo : Analyse des données / pré-traitement de celles-ci
    Théo : Création du projet sur GitHub et de l'API javascript / test téléchargement des données automatique

### 23-24/02
    Nicolas : Créer une image (graphe) de données de test
    Hugo : Fusioner les données
    Théo : Création de la partie front / refonte du server.js

### 2/03
    Nicolas : Correction - Affichage des images créées par le script Python
    Hugo : Fusion des données / Réalisation des premiers graphes barplot avec les données fusionnées
    Théo : Creation de routes / affichage des images créées par le script Python / correction de crashs de l'API par le script Python sur le serveur.js

### 9/03
    => Recherche de nouveaux graphes à réaliser / Découverte de Jupyter
    Théo : Ajout et utilisation de Bootstrap

### 14/03
    => Recherche pour réaliser une IA capable de prédire le nombre d'accidents
    Nicolas : Nettoyage des données encore trop grosses
    Hugo : Modifications / création de graphes
    Théo : Implémentation de différents graphes dans l'API et ajout d'un filtre pour choisir l'année du countplot accidents par mois

### 16/04
    Nicolas : Clean les données
    Hugo : Début de l'IA
    Théo : Ajout d'une section (card) sommaire qui permet de sélectionner un graphe (auto scroll) / ajout graphe répartition des usagers par sexe dans le filtre / modification de la fonction pour afficher les images du filtre car ca n'en affichait qu'une seule / ajout de commentaire sur les graphes

### 20/04
    Nicolas : Refonte de la modélisation / fusion des données qui étaient mal faites
    Hugo : Test IA prédire le nombre d'accidents par rapport a une date et un département donné
    Théo : Téléchargement automatique des données csv depuis le site data.gouv et modification des graphes avec les nouveaux datasets

### 21/04
    Nicolas : Correction du problème du mauvais enregistrement des images des graphes
    Hugo : IA
    Théo : Correction du problème du mauvais enregistrement des images des graphes + refonte TOTALE du téléchargement automatique des données qui se téléchargeaient mal (téléchargements arrêtés en plein milieu à cause des scripts python)

### 23/04
    Nicolas : Implémentation des nouvelles données dans l'api
    Théo : Création d'un graphe bokeh vbar_stack avec une table pivot et un HoverTool représentant le nombre d'usagers pour chaque type de blessure et catégorie d'usager + ajout sur l'API

### 24/04
    Théo : Nouveau 3D graphe fait avec plotly représentant le nombre d'accidents par heure et mois

### 28/04
    Théo : Ajout d'un nouveau script pour de nouveaux graphes

### 29/04
    Théo : Allégement du code