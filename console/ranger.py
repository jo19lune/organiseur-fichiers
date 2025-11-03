import os
import shutil
from pathlib import Path

# Dictionnaire des extensions par catégorie
EXTENSIONS = {
    "images": ["jpg", "jpeg", "png", "gif", "bmp", "svg", "webp"],
    "videos": ["mp4", "mkv", "mov", "avi", "flv", "wmv", "3gp"],
    "audios": ["mp3", "wav", "aac", "flac", "ogg", "m4a"],
    "documents": ["pdf", "doc", "docx", "txt", "xls", "xlsx", "ppt", "pptx", "odt"],
    "archives": ["zip", "rar", "tar", "gz", "7z"],
    "scripts": ["py", "js", "html", "css", "php", "java", "c", "cpp", "sh"]
}

def get_category(extension):
    for category, exts in EXTENSIONS.items():
        if extension.lower() in exts:
            return category
    return "autres"

def generer_nom_unique(dossier, nom_fichier):
    base = Path(nom_fichier).stem
    ext = Path(nom_fichier).suffix
    compteur = 1
    nouveau_nom = nom_fichier

    while os.path.exists(os.path.join(dossier, nouveau_nom)):
        nouveau_nom = f"{base}_{compteur}{ext}"
        compteur += 1

    return nouveau_nom

def organiser_fichiers(repertoire):
    for item in os.listdir(repertoire):
        chemin_complet = os.path.join(repertoire, item)

        # Ignore les dossiers
        if not os.path.isfile(chemin_complet):
            continue

        # Ignore les fichiers déjà déplacés dans un sous-dossier
        if os.path.dirname(chemin_complet) != os.path.abspath(repertoire):
            continue

        # Récupère l'extension ou "sans_extension"
        extension = Path(item).suffix.lstrip(".").lower() or "sans_extension"
        categorie = get_category(extension)

        # Dossier cible : catégorie/sous-extension
        dossier_cible = os.path.join(repertoire, categorie, extension)
        os.makedirs(dossier_cible, exist_ok=True)

        # Gère les doublons
        nom_final = generer_nom_unique(dossier_cible, item)

        # Déplace le fichier
        shutil.move(chemin_complet, os.path.join(dossier_cible, nom_final))
        print(f"{item} → {categorie}/{extension} (→ {nom_final})")

if __name__ == "__main__":
    dossier_source = input("Entrez le chemin du dossier à organiser : ").strip()
    if os.path.isdir(dossier_source):
        organiser_fichiers(dossier_source)
        print("Organisation terminée.")
    else:
        print("Dossier invalide.")
