## Virtual environnement
```bash
python -m venv .venv
```
> .venv est le nom de l'environnement virtuel.

## Connect to the venv
- **mac/linux**: `source .venv/bin/activate.fish`
- **windows**: `.venv/Scripts/activate` ou `.venv/Scripts/activate.ps1`

## Créer requirements.txt à partir de pip
```bash
pip freeze > requirements.txt
```

## Installer les librairies dans un nouvel environnement
```bash
pip install -r requirements.txt
```

## Quitter l'environnement virtuel
```bash
deactivate
```

## Contribuer
Si vous souhaitez contribuer à ce projet, n'hésitez pas à soumettre une demande de tirage ou à ouvrir un problème.

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.