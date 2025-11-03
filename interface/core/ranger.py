import os
import shutil
from pathlib import Path
from core.config import EXTENSIONS
from core.doublons import demander_action_doublon

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

def organiser_fichiers(repertoire, log_callback=None):
    stats = {
        "actions": {"déplacés": 0, "renommés": 0, "remplacés": 0, "ignorés": 0},
        "catégories": {}
    }
    choix_global = None
    appliquer_global = False

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

        chemin_destination = os.path.join(dossier_cible, item)

        # Gestion des doublons
        if os.path.exists(chemin_destination):
            if appliquer_global:
                action = choix_global
            else:
                action, appliquer_global = demander_action_doublon(item, dossier_cible)
                choix_global = action

            if action == "remplacer":
                os.remove(chemin_destination)
                shutil.move(chemin_complet, chemin_destination)
                stats["actions"]["remplacés"] += 1
                message = f"{item} remplacé dans {categorie}/{extension}"
            elif action == "ignorer":
                stats["actions"]["ignorés"] += 1
                message = f"{item} ignoré (déjà présent dans {categorie}/{extension})"
            else:  # renommer
                nouveau_nom = generer_nom_unique(dossier_cible, item)
                shutil.move(chemin_complet, os.path.join(dossier_cible, nouveau_nom))
                stats["actions"]["renommés"] += 1
                message = f"{item} renommé → {categorie}/{extension}/{nouveau_nom}"
        else:
            shutil.move(chemin_complet, chemin_destination)
            stats["actions"]["déplacés"] += 1
            message = f"{item} déplacé vers {categorie}/{extension}"

        stats["catégories"].setdefault(categorie, 0)
        stats["catégories"][categorie] += 1

        if log_callback:
            log_callback(message)

    return stats
