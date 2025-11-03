# 📄 README — Organiseur de fichiers (Tkinter)

## 🧩 Description

Organiseur de fichiers est une application Python avec interface Tkinter permettant de trier automatiquement les fichiers d’un dossier selon leur extension. Elle gère les doublons intelligemment (remplacement, renommage, ou ignorance) et affiche un journal des actions en temps réel.

---

## 🚀 Fonctionnalités

- Tri automatique des fichiers par catégorie et extension
- Détection et gestion des doublons avec boîte de dialogue
- Interface graphique responsive et intuitive
- Journal d’activité en console intégrée
- Résumé final des actions effectuées
- Icône personnalisée pour l’application et l’exécutable

---

## 🛠️ Installation

### 1. Cloner le projet

```bash
git clone https://github.com/jo19lune/organiseur-fichiers.git
cd organiseur-fichiers
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

> Si `requirements.txt` n’existe pas, installe simplement Tkinter (souvent préinstallé) :
    ```bash
    pip install pillow
    ```

---

## ▶️ Exécution

```bash
python interface/main.py
```

---

## 📦 Compilation en `.exe` (Windows)

### 1. Installer PyInstaller

```bash
pip install pyinstaller
```

### 2. Lancer le script de build

```bash
python build.py
```

> L’exécutable sera généré dans le dossier `dist/` sous le nom `OrganiseurFichiers.exe`.

---

### 📁 Structure du projet

```texte
OrganiseurFichiers/
├── build.py
├── interface/
│   ├── main.py
│   ├── assets/
│   │   ├── logo.ico
│   │   ├── logo.png
│   │   └── alert.ico
│   ├── core/
│   │   ├── ranger.py
│   │   ├── doublons.py
│   │   └── config.py
│   └── README.md
```

---

## 📌 À venir

- Export des statistiques en `.json`
- Version mobile avec Kivy
- Mode automatique en ligne de commande

---
