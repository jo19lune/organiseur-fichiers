import tkinter as tk

def demander_action_doublon(nom_fichier, dossier_cible):
    """Affiche une boîte de dialogue moderne pour décider quoi faire avec un doublon."""
    fenetre_doublon = tk.Toplevel()
    fenetre_doublon.title("Conflit de fichier")
    fenetre_doublon.geometry("460x260")
    fenetre_doublon.resizable(False, False)
    fenetre_doublon.grab_set()

    try:
        fenetre_doublon.iconbitmap("interface/assets/alert.ico")
    except Exception:
        pass

    # Variables de choix
    choix = tk.StringVar(value="renommer")
    appliquer_tous = tk.BooleanVar(value=False)

    # Titre explicatif
    label_info = tk.Label(
        fenetre_doublon,
        text=f"Le fichier « {nom_fichier} » existe déjà dans :\n{dossier_cible}",
        font=("Segoe UI", 10),
        wraplength=440,
        justify="left"
    )
    label_info.grid(row=0, column=0, columnspan=2, padx=20, pady=(15, 5), sticky="w")

    # Options radio
    tk.Radiobutton(
        fenetre_doublon, text="Remplacer le fichier existant", variable=choix, value="remplacer",
        font=("Segoe UI", 10)
    ).grid(row=1, column=0, columnspan=2, sticky="w", padx=30, pady=2)

    tk.Radiobutton(
        fenetre_doublon, text="Renommer automatiquement", variable=choix, value="renommer",
        font=("Segoe UI", 10)
    ).grid(row=2, column=0, columnspan=2, sticky="w", padx=30, pady=2)

    tk.Radiobutton(
        fenetre_doublon, text="Ignorer ce fichier", variable=choix, value="ignorer",
        font=("Segoe UI", 10)
    ).grid(row=3, column=0, columnspan=2, sticky="w", padx=30, pady=2)

    # Case à cocher
    tk.Checkbutton(
        fenetre_doublon,
        text="Appliquer ce choix à tous les doublons",
        variable=appliquer_tous,
        font=("Segoe UI", 10)
    ).grid(row=4, column=0, columnspan=2, padx=30, pady=(10, 10), sticky="w")

    # Bouton de validation
    def valider():
        fenetre_doublon.destroy()

    tk.Button(
        fenetre_doublon,
        text="Valider",
        command=valider,
        font=("Segoe UI", 10),
        width=15,
        bg="#4CAF50",
        fg="white"
    ).grid(row=5, column=0, columnspan=2, pady=(0, 15))

    fenetre_doublon.wait_window()

    return choix.get(), appliquer_tous.get()


# Test local
if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    print(demander_action_doublon("client.txt", "D:/donne"))
