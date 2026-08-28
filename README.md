# Assurance Risque

Plateforme intelligente d'analyse et de prédiction des risques en assurance automobile développée dans le cadre d'un projet de stage.

## Présentation

Ce projet a pour objectif d'aider un **Agent Assurance** à analyser les données des assurés, comprendre les facteurs influençant les sinistres, prédire la probabilité qu'un client déclare un sinistre et estimer le coût attendu du risque grâce au Machine Learning.

Le projet est réalisé à partir du dataset **freMTPL2 – French Motor TPL Insurance Claims Data**.

## Objectifs

* Analyser statistiquement les contrats d'assurance automobile.
* Étudier les facteurs liés au risque de sinistre.
* Prédire la probabilité de sinistre.
* Expliquer les facteurs qui influencent les prédictions.
* Estimer le coût attendu du risque.
* Développer une plateforme web avec Django.

## Technologies utilisées

### Data Science

* Python
* Pandas
* NumPy

### Visualisation

* Matplotlib

### Machine Learning

* Scikit-learn

### Développement Web

* Django
* HTML/CSS
* JavaScript

### Base de données

* PostgreSQL (prévu)

## Structure du projet

```text
assurance_risque/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_audit.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── ...
│
├── django_project/
├── models/
├── reports/
├── src/
├── README.md
└── .gitignore
```

## Progression du projet

| Étape               | Statut     |
| ------------------- | ---------- |
| Data Audit          | ✅ Terminé  |
| Data Cleaning       | ✅ Terminé  |
| Feature Engineering | 🔄 À venir |
| Machine Learning    | ⏳ À venir  |
| Dashboard Django    | ⏳ À venir  |

## Résultats obtenus jusqu'à présent

* Analyse exploratoire de plus de **678 000 contrats**.
* Étude des facteurs tels que l'âge du conducteur, le Bonus-Malus, l'âge du véhicule, la puissance, la marque, le carburant et la région.
* Nettoyage des données et suppression des doublons.
* Agrégation des montants de sinistres par contrat.
* Création d'un dataset propre (`insurance_clean.csv`) prêt pour les prochaines étapes du Machine Learning.

## Prochaines étapes

* Feature Engineering.
* Encodage des variables catégorielles.
* Entraînement des modèles de prédiction.
* Explication des prédictions.
* Développement du tableau de bord Django.
