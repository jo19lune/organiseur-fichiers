import tkinter as tk

def demander_action_doublon(nom_fichier, dossier_cible):
    """Affiche une boîte de dialogue pour décider quoi faire avec un doublon."""
    fenetre_doublon = tk.Toplevel()
    fenetre_doublon.title("Fichier en doublon")
    fenetre_doublon.geometry("420x240")
    fenetre_doublon.grab_set()

    tk.Label(
        fenetre_doublon,
        text=f"Le fichier '{nom_fichier}' existe déjà dans :\n{dossier_cible}",
        wraplength=400,
        justify="left"
    ).pack(pady=10)

    choix = tk.StringVar(value="renommer")
    appliquer_tous = tk.BooleanVar(value=False)

    # Options de gestion
    cadre_options = tk.Frame(fenetre_doublon)
    cadre_options.pack(pady=5)

    tk.Radiobutton(cadre_options, text="Remplacer", variable=choix, value="remplacer").pack(anchor="w")
    tk.Radiobutton(cadre_options, text="Renommer", variable=choix, value="renommer").pack(anchor="w")
    tk.Radiobutton(cadre_options, text="Ignorer", variable=choix, value="ignorer").pack(anchor="w")

    # Case à cocher
    tk.Checkbutton(
        fenetre_doublon,
        text="Appliquer ce choix à tous les doublons",
        variable=appliquer_tous
    ).pack(pady=10)

    # Bouton de validation
    def valider():
        fenetre_doublon.destroy()

    tk.Button(fenetre_doublon, text="Valider", command=valider).pack(pady=5)
    fenetre_doublon.wait_window()

    return choix.get(), appliquer_tous.get()


if __name__ == '__main__':
    demander_action_doublon("client.txt", "D:/donne")