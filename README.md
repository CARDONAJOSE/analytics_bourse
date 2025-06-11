# Tableau de Bord Financier

Ce projet est une application Streamlit pour analyser les données financières en utilisant la bibliothèque `yfinance`. L'application permet aux utilisateurs de rechercher des informations sur les actions, de visualiser des statistiques de prix et de volumes, et de générer des graphiques interactifs.

## Caractéristiques

- **Recherche de Tickers** : Permet de rechercher des informations détaillées sur les actions en utilisant leur symbole de ticker.
- **Statistiques de Prix et de Volumes** : Affiche des statistiques telles que le prix d'ouverture, de clôture, le maximum, le minimum et le volume moyen des transactions.
- **Graphiques Interactifs** : Génère des graphiques de lignes et de volumes en utilisant `plotly` et `calplot`.
- **Informations Supplémentaires** : Affiche des informations supplémentaires telles que le beta, le secteur et l'industrie de l'entreprise.


# structure du projet
``` bash
financial-dashboard/
│
├── app.py                  # Fichier principal de l'application Streamlit
├── requirements.txt        # Liste des dépendances du projet
├── README.md               # Documentation du projet
└── modules/                # Répertoire pour les modules supplémentaires
    ├── __init__.py         # Fichier pour convertir le répertoire en paquet
    ├── graphique.py        # Module pour les fonctions de graphiques
    └── utils.py            # Module pour les fonctions utilitaires
```

## Virtual environnement
```bash
python -m venv .venv
```
> .venv est le nom de l'environnement virtuel.

## Connect to the venv
- **mac/linux**: `source .venv/bin/activate.fish`
- **windows**: `.venv/Scripts/activate` ou `.venv/Scripts/activate.ps1`


## Installer les librairies dans un nouvel environnement
```bash
pip install -r requirements.txt
```

## Quitter l'environnement virtuel
```bash
deactivate
```
### Installation

1. **Cloner le dépôt**:
   ```bash
   git clone https://github.com/CARDONAJOSE/analytics_bourse.git
   cd pdf-summary-app
2. **Lancement de l’application web sans docker** :  
   - Démarrez l’application :  
     ```bash
     streamlit run app.py
     ```
   - Rendez-vous sur `http://localhost:5000` (par défaut) pour interagir avec l’interface.

3. **Lancement de l’application web avec docker** :  
   - Démarrez l’application :  
     ```bash
     docker compose up --build -d
     ```
   - Rendez-vous sur `http://localhost:8501` (par défaut) pour interagir avec l’interface.

- arrete docker
    ```bash
    docker compose down
    ```

## Contribuer
Si vous souhaitez contribuer à ce projet, n'hésitez pas à soumettre une demande de tirage ou à ouvrir un problème.

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.