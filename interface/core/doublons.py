import tkinter as tk

def demander_action_doublon(nom_fichier, dossier_cible):
    fenetre_doublon = tk.Toplevel()
    fenetre_doublon.title("Fichier en doublon")
    fenetre_doublon.geometry("400x200")
    fenetre_doublon.grab_set()

    tk.Label(fenetre_doublon, text=f"Le fichier '{nom_fichier}' existe déjà dans :\n{dossier_cible}", wraplength=380).pack(pady=10)

    choix = tk.StringVar(value="renommer")
    appliquer_tous = tk.BooleanVar(value=False)

    tk.Radiobutton(fenetre_doublon, text="Remplacer", variable=choix, value="remplacer").pack(anchor="w", padx=20)
    tk.Radiobutton(fenetre_doublon, text="Renommer", variable=choix, value="renommer").pack(anchor="w", padx=20)

    tk.Checkbutton(fenetre_doublon, text="Appliquer ce choix à tous les doublons", variable=appliquer_tous).pack(pady=10)

    def valider():
        fenetre_doublon.destroy()

    tk.Button(fenetre_doublon, text="Valider", command=valider).pack(pady=5)
    fenetre_doublon.wait_window()

    return choix.get(), appliquer_tous.get()


if __name__ == '__main__':
    demander_action_doublon("client.txt", "D:/donne")