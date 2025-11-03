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
fenetre.geometry("700x500")

# Icône personnalisée
try:
    fenetre.iconbitmap("assets/logo.ico")
except Exception:
    pass  # Ignore si l'icône n'est pas compatible ou absente

# Sélection du dossier
cadre_choix = tk.Frame(fenetre)
cadre_choix.pack(pady=10)

label_dossier = tk.Label(cadre_choix, text="Dossier à organiser :")
label_dossier.pack(side=tk.LEFT)

entree_dossier = tk.Entry(cadre_choix, width=60)
entree_dossier.pack(side=tk.LEFT, padx=5)

btn_parcourir = tk.Button(cadre_choix, text="Parcourir", command=choisir_dossier)
btn_parcourir.pack(side=tk.LEFT)

# Bouton d'action
btn_lancer = tk.Button(fenetre, text="Lancer l'organisation", command=lancer_organisation, bg="#4CAF50", fg="white")
btn_lancer.pack(pady=10)

# Zone de log
log_zone = scrolledtext.ScrolledText(fenetre, width=85, height=20)
log_zone.pack(padx=10, pady=10)

fenetre.mainloop()
