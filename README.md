# Plateforme intelligente d'analyse et de prédiction des risques en assurance automobile

## Présentation

Ce projet consiste en la conception et le développement d'une plateforme intelligente dédiée à l'analyse et à la prédiction des risques en assurance automobile.

Réalisé dans le cadre d'un stage chez **WAFA Assurance**, le projet combine une démarche de **Data Science et de Machine Learning** avec le développement d'une **application web Django**.

L'objectif principal est de permettre à un Agent Assurance d'analyser les caractéristiques des contrats automobiles, d'étudier les facteurs associés aux sinistres et d'obtenir une estimation de la probabilité qu'un contrat soit associé à un sinistre.

Le projet s'appuie sur le dataset **freMTPL2 - French Motor Third Party Liability Insurance Claims Data**, contenant 678 013 contrats d'assurance automobile et 26 639 sinistres.

---

## Problématique

L'assurance automobile génère un volume important de données relatives aux conducteurs, aux véhicules et aux contrats.

La problématique étudiée dans ce projet est la suivante :

> **Comment prédire, à partir des caractéristiques historiques d'un contrat d'assurance automobile, la probabilité qu'il soit associé à un sinistre et intégrer cette prédiction dans un outil utilisable par un Agent Assurance ?**

Pour répondre à cette problématique, une démarche complète de Data Science a été mise en place, depuis l'audit et le nettoyage des données jusqu'à l'intégration du modèle de Machine Learning dans une plateforme web.

---

## Objectifs

Les principaux objectifs du projet sont :

- auditer et explorer les données d'assurance automobile ;
- nettoyer et préparer les données ;
- analyser les facteurs associés à la fréquence des sinistres ;
- réaliser le Feature Engineering nécessaire à la modélisation ;
- entraîner et comparer plusieurs modèles de Machine Learning ;
- gérer le déséquilibre entre les classes `Claim` et `No Claim` ;
- optimiser le modèle retenu à l'aide d'une recherche d'hyperparamètres ;
- intégrer le modèle final dans une application Django ;
- fournir à l'Agent Assurance une interface permettant d'analyser les données et d'effectuer des prédictions ;
- conserver l'historique des prédictions réalisées.

---

## Données utilisées

Le projet utilise le dataset :

**freMTPL2 - French Motor Third Party Liability Insurance Claims Data**

Deux sources principales sont utilisées :

```text
freMTPL2freq.csv
freMTPL2sev.csv
```

## Méthodologie Data Science et Machine Learning

Le projet suit une démarche complète de Data Science, depuis l'exploration des données jusqu'à l'intégration du modèle de Machine Learning dans la plateforme web.

### 1. Audit et exploration des données

Une première analyse des données a été réalisée afin de :

- vérifier la structure et les dimensions des datasets ;
- identifier les valeurs manquantes et les doublons ;
- analyser les variables disponibles ;
- étudier la distribution des sinistres ;
- identifier les principales caractéristiques des contrats d'assurance.

### 2. Nettoyage et préparation des données

Les données ont ensuite été nettoyées et préparées pour la modélisation :

- traitement des valeurs aberrantes ;
- vérification des doublons ;
- préparation des variables numériques et catégorielles ;
- fusion des données de fréquence et de sévérité ;
- création de la variable cible `HasClaim`.

La variable `HasClaim` permet de distinguer les contrats associés à un sinistre (`Claim`) des contrats sans sinistre (`No Claim`).

### 3. Feature Engineering

Une étape de Feature Engineering a été réalisée afin de transformer et préparer les variables nécessaires à la modélisation.

Cette étape comprend notamment la préparation des caractéristiques liées au conducteur, au véhicule et au contrat d'assurance.

### 4. Modélisation

Plusieurs algorithmes de Machine Learning ont été étudiés et comparés :

- Régression Logistique ;
- Decision Tree ;
- Random Forest.

Une attention particulière a été portée au déséquilibre entre les classes `Claim` et `No Claim`.

### 5. Optimisation du modèle

Le modèle Random Forest a ensuite été optimisé à l'aide d'une recherche d'hyperparamètres avec `RandomizedSearchCV` et une validation croisée.

Le modèle final retenu est ensuite sauvegardé afin de pouvoir être utilisé directement par la plateforme Django.

### 6. Intégration dans la plateforme web

Le modèle optimisé est intégré à l'application Django.

L'Agent Assurance peut ainsi :

- saisir les caractéristiques d'un contrat ;
- obtenir une prédiction `Claim` ou `No Claim` ;
- consulter la probabilité de sinistre ;
- analyser différents facteurs de risque ;
- consulter l'historique des prédictions.




## Technologies utilisées

### Data Science et Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

### Développement web

- Django
- HTML
- CSS
- JavaScript
- Chart.js
- Bootstrap / Bootstrap Icons

### Base de données

- SQLite

### Gestion du projet

- Git
- GitHub
- Visual Studio Code


## Aperçu de la plateforme

### Page de connexion

![Page de connexion](screenshots/login.png)

### Tableau de bord

![Tableau de bord - Vue 1](screenshots/dashboard1.png)

![Tableau de bord - Vue 2](screenshots/dashboard2.png)

### Prédiction du risque

![Prédiction - Vue 1](screenshots/prediction1.png)

![Prédiction - Vue 2](screenshots/prediction2.png)

### Analyse statistique

![Analyse - Vue 1](screenshots/analysis1.png)

![Analyse - Vue 2](screenshots/analysis2.png)

### Historique des prédictions

![Historique des prédictions](screenshots/history.png)