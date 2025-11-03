import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from core.ranger import organiser_fichiers
import os

def choisir_dossier():
    dossier = filedialog.askdirectory()
    if dossier:
        # Normalise le chemin
        dossier = os.path.normpath(dossier)
        entree_dossier.delete(0, tk.END)
        entree_dossier.insert(0, dossier)

def afficher_message(msg):
    log_zone.insert(tk.END, msg + "\n")
    log_zone.see(tk.END)

def lancer_organisation():
    dossier = entree_dossier.get().strip()
    if not dossier or not os.path.isdir(dossier):
        messagebox.showwarning("Dossier invalide", "Veuillez sélectionner un dossier existant.")
        return

    log_zone.delete(1.0, tk.END)
    try:
        stats = organiser_fichiers(dossier, log_callback=afficher_message)
        total = sum(stats.values())
        messagebox.showinfo("Organisation terminée", f"{total} fichiers déplacés.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Organiseur de fichiers")
fenetre.geometry("800x600")
fenetre.minsize(600, 400)

# Icône personnalisée
try:
    fenetre.iconbitmap("interface/assets/logo.ico")
except Exception:
    pass

# Configuration du grid principal
fenetre.columnconfigure(0, weight=1)
fenetre.rowconfigure(2, weight=1)

# Cadre de sélection
cadre_choix = tk.Frame(fenetre)
cadre_choix.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
cadre_choix.columnconfigure(1, weight=1)

label_dossier = tk.Label(cadre_choix, text="Dossier à organiser :")
label_dossier.grid(row=0, column=0, sticky="w")

entree_dossier = tk.Entry(cadre_choix)
entree_dossier.grid(row=0, column=1, padx=5, sticky="ew")

btn_parcourir = tk.Button(cadre_choix, text="Parcourir", command=choisir_dossier)
btn_parcourir.grid(row=0, column=2)

# Bouton d'action
btn_lancer = tk.Button(fenetre, text="Lancer l'organisation", command=lancer_organisation, bg="#4CAF50", fg="white")
btn_lancer.grid(row=1, column=0, pady=10)

# Zone de log
log_zone = scrolledtext.ScrolledText(fenetre)
log_zone.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

fenetre.mainloop()
