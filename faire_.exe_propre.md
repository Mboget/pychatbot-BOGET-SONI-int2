# 📝 Récap : Créer un `.exe` avec PyInstaller (Projet Python multi-fichiers)

## ✅ 1. Organisation du projet

Exemple :

```
mon_projet/
│ main.py        ← fichier principal (point d’entrée)
│ classes.py     ← tes classes
│ utils.py       ← autres fonctions
│
└── assets/
      image.png
      config.json
```

**Important :**
👉 Le `.exe` se crée *toujours* à partir du fichier qui contient :

```python
if __name__ == "__main__":
    pass
```

---

## ✅ 2. Créer et activer un environnement virtuel (recommandé)

```bash
python -m venv venv
venv\Scripts\activate
```

---

## ✅ 3. Installer PyInstaller

```bash
pip install pyinstaller
```

---

## ✅ 4. PyInstaller inclut automatiquement tes autres `.py`

Tant que tu importes tes modules dans `main.py`, par exemple :

```python
from classes import MaClasse
import utils
```

➡️ Aucun paramètre spécial à ajouter
➡️ Tous les fichiers `.py` nécessaires seront inclus.

Idem si tes fichiers sont dans un sous-dossier :

```python
from core.classes import MaClasse
```

---

## ✅ 5. Commande recommandée pour un `.exe` propre

```bash
pyinstaller --onefile --noconsole --icon=logo.ico --add-data "assets;assets" main.py
```

### Options :

* `--onefile` → un seul `.exe`
* `--noconsole` → pas de fenêtre console (pour Pygame, Tkinter…)
* `--icon=logo.ico` → icône personnalisée
* `--add-data "source;destination"` → assets, images, sons…

---

## ✅ 6. Charger les assets correctement (`resource_path`)

À mettre dans ton code si tu utilises des fichiers externes (images, JSON…) :

```python
import os, sys

def resource_path(rel_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.abspath("."), rel_path)

# Exemple d'utilisation :
image_path = resource_path("assets/image.png")
```

---

## ✅ 7. Où trouver ton `.exe` ?

Après la commande PyInstaller :

```
dist/
   main.exe
build/
main.spec
```

👉 Le fichier utilisable est dans **dist/**.

---

## 🎉 En résumé

* ✔️ PyInstaller prend automatiquement tes fichiers Python **si tu les importes**
* ✔️ Une seule commande suffit pour générer un `.exe` propre
* ✔️ Les assets doivent être ajoutés avec `--add-data`
* ✔️ Utilise `resource_path()` pour les retrouver dans l’exécutable

---