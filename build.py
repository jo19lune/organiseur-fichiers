import os
import sys
from PyInstaller.__main__ import run as pyi_run

def build_exe(onefile: bool = True):
    # Point d’entrée
    entry = os.path.join("interface", "main.py")
    if not os.path.exists(entry):
        print(f"[ERROR] Impossible de trouver {entry}")
        sys.exit(1)

    # Nom de l'exécutable
    exe_name = "Organiseur de Fichiers"

    # Séparateur de données selon l'OS
    sep = ";" if sys.platform.startswith("win") else ":"

    # Arguments de base
    args = [
        entry,
        "--name", exe_name,
        "--clean",
        "--windowed",
        "--noconfirm",
        "--log-level", "DEBUG",
    ]
    args += ["--onefile"] if onefile else ["--onedir"]

    # Ajout des chemins de recherche
    args += ["--paths", "interface"]
    args += ["--paths", os.path.dirname(os.path.abspath(__file__))]

    # Ressources à inclure
    datas = [
        ("interface/assets/logo.ico", "interface/assets"),
        ("interface/assets/logo.png", "interface/assets"),
        ("interface/assets/alert.png", "interface/assets"),
    ]

    for src, dst in datas:
        if os.path.exists(src):
            args += ["--add-data", f"{os.path.abspath(src)}{sep}{dst}"]
        else:
            print(f"[WARN] Ressource manquante : {src}")

    # Icône principale
    icon_path = os.path.abspath("interface/assets/logo.ico")
    if os.path.exists(icon_path):
        args += ["--icon", icon_path]
    else:
        print(f"[WARN] Icône principale manquante : {icon_path}")

    # Lancement
    print("\nLancement de PyInstaller avec les arguments :\n")
    for arg in args:
        print("  ", arg)

    try:
        pyi_run(args)
        print("\nCompilation terminée avec succès.")
    except Exception as e:
        print("\nErreur lors de la construction :", e)
        raise

if __name__ == "__main__":
    build_exe(onefile=True)
