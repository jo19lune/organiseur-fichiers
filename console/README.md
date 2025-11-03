# 🗂️ Organiseur de fichiers par extension

---

Ce script Python permet de trier automatiquement les fichiers d’un dossier en les classant par type (images, vidéos, documents, audios, etc.) et par sous-type (ex. `pdf`, `mp4`, `png`, etc.). Il gère les fichiers sans extension, les doublons et ignore les dossiers déjà présents.

---

## 🚀 Fonctionnalités

- 🔍 Identification des fichiers par extension
- 🗂️ Classement dans des dossiers par catégorie et sous-extension
- 📁 Création automatique des dossiers si nécessaire
- 🧩 Gestion des fichiers sans extension (`autres/sans_extension`)
- 🧠 Renommage automatique en cas de doublon (`fichier_1.txt`, `fichier_2.txt`, ...)
- 🧱 Ignoration des dossiers et des fichiers déjà triés

---

## 📦 Catégories prises en charge

| Catégorie   | Extensions supportées |
|-------------|------------------------|
| images      | jpg, jpeg, png, gif, bmp, svg, webp |
| vidéos      | mp4, mkv, mov, avi, flv, wmv, 3gp |
| audios      | mp3, wav, aac, flac, ogg, m4a |
| documents   | pdf, doc, docx, txt, xls, xlsx, ppt, pptx, odt |
| archives    | zip, rar, tar, gz, 7z |
| scripts     | py, js, html, css, php, java, c, cpp, sh |
| autres      | tout ce qui ne correspond à aucune catégorie |

---

## 🛠️ Installation

1. Assurez-vous d’avoir Python 3 installé.
2. Clonez ou téléchargez le dépôt :

```bash
git clone https://github.com/jo19lune/organiseur-fichiers.git
cd organiseur-fichiers/console
```

---

## ▶️ Utilisation

```bash
python ranger.py
```

Puis saisissez le chemin du dossier à organiser lorsqu’il est demandé :

``` .
📁 Entrez le chemin du dossier à organiser : C:\Users\Loïck\Documents\À_trier
```

---

## 📁 Exemple de structure générée

``` .
À_trier/
├── images/
│   └── png/
│       └── image_1.png
├── documents/
│   ├── pdf/
│   │   └── rapport.pdf
│   └── txt/
│       └── notes.txt
├── vidéos/
│   └── mp4/
│       └── video_1.mp4
├── autres/
│   └── sans_extension/
│       └── README
```

---

## 🧩 Personnalisation

Vous pouvez modifier le dictionnaire `EXTENSIONS` dans le script pour ajouter ou retirer des types selon vos besoins.

---

## 📜 Licence

Ce projet est open-source et libre d’utilisation. Vous pouvez l’adapter, l’améliorer et le redistribuer selon vos besoins.

---
