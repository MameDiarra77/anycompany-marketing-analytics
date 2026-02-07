#  AnyCompany – Marketing Analytics & Decision Dashboards

##  Objectif du projet

Ce projet vise à construire un **Data Product marketing** permettant :

* d’analyser le comportement des clients,
* de segmenter la clientèle,
* d’estimer la propension à l’achat,
* et de fournir un **dashboard décisionnel** pour orienter les actions marketing.

Le projet combine :

* **Python** pour l’analyse et le Machine Learning,
* **pandas / scikit-learn** pour la modélisation,
* **Streamlit** pour la visualisation et l’aide à la décision.

---

##  Stack technique

* **Langage** : Python
* **Analyse de données** : pandas, numpy
* **Machine Learning** : scikit-learn
* **Visualisation & Data App** : Streamlit
* **Versioning** : Git / GitHub

---

##  Structure du projet

```
anycompany-marketing-analytics/
│
├── app.py                         # Point d’entrée Streamlit
│
├── pages/                         # Pages Streamlit
│   ├── 00_home.py                 # Page d’accueil
│   ├── 01_customer_segmentation_kmeans.py
│   ├── 01_sales_dashboard.py
│   ├── 03_reviews_dashboard.py
│   ├── 06_decision_dashboard.py   # Dashboard décisionnel final
│
├── ml/                            # Scripts ML & données générées
│   ├── create_ml_data.py
│   ├── sales_regression.py
│   ├── test_clustering.py
│   ├── cluster_profiles.csv
│   ├── customers_segmented.csv
│   ├── customers_propensity_scores.csv
│
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
├── README.md
├── business_insights.md
└── .gitignore
```

---

##  Données utilisées

Les données clients sont construites à partir d’indicateurs comportementaux :

* nombre de transactions
* chiffre d’affaires total
* panier moyen
* récence
* exposition aux promotions

Les datasets finaux utilisés par l’application :

* `customers_segmented.csv`
* `customers_propensity_scores.csv`
* `cluster_profiles.csv`

---

##  Analyses réalisées

### 1️ Segmentation clients – KMeans

Un algorithme **K-Means** est utilisé pour identifier des groupes de clients homogènes.

**Features utilisées** :

* fréquence d’achat
* panier moyen
* récence
* achats promotionnels

**Résultat** :

* 4 segments clients distincts
* profils interprétables métier

---

### 2️ Propension à l’achat

Un score de propension est calculé afin de classer les clients selon leur probabilité d’achat :

* Forte
* Moyenne
* Faible

Ces segments sont utilisés pour prioriser les actions marketing.

---

### 3️ Analyse ventes & performance

* Analyse descriptive des ventes
* Visualisation des tendances
* Comparaison des comportements par segment

---

##  Application Streamlit

L’application Streamlit est organisée en **pages thématiques** :

### Pages disponibles

* **Home** : présentation du projet
* **Customer Segmentation (KMeans)** : analyse des clusters
* **Sales Dashboard** : indicateurs commerciaux
* **Reviews Dashboard** : analyse client
* **Decision Dashboard** : synthèse décisionnelle finale

---

##  Decision Dashboard (Livrable clé)

La page **Decision Dashboard** fournit :

### KPI principaux

* Nombre total de clients
* Nombre de segments
* % de clients à forte propension

### Insights métier

* Identification des segments à forte valeur
* Analyse du potentiel marketing par segment

### Recommandations marketing

* ciblage premium
* campagnes promotionnelles ciblées
* stratégies de fidélisation

 Cette page constitue la **valeur business du projet**.

---

##  Lancement de l’application

###  Installation des dépendances

```bash
pip install -r requirements.txt
```

###  Lancer Streamlit

```bash
streamlit run app.py
```


---

##  Documentation métier

* **README.md** : documentation technique et projet
* **business_insights.md** : interprétations métier & recommandations marketing

---

##  Auteurs

Projet réalisé par :

* **Mame Diarra NDIAYE**
* **Seynabou SENE**
* **Pla Dorgelès AYEBIE**
* **Emeric GNANVI**

Dans le cadre d’un projet d’**Analytics Marketing & Data Product**.

---

##  Statut du projet

✔ Analyse complétée
✔ Segmentation validée
✔ Dashboard décisionnel fonctionnel
✔ Livrables prêts

---

