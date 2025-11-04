from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.filemanager import MDFileManager
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window
from ui.home import MainScreen
from core.ranger import organiser_fichiers
import os

class OrganiseurApp(MDApp):
    logs = StringProperty("")
    dossier_selectionne = ""

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
        Builder.load_file("ui/home.kv")
        return MainScreen()

    def ouvrir_filemanager(self):
        self.file_manager = MDFileManager(
            exit_manager=self.fermer_filemanager,
            select_path=self.selectionner_dossier,
            preview=False
        )
        self.file_manager.show(os.path.expanduser("~"))

    def fermer_filemanager(self, *args):
        self.file_manager.close()

    def selectionner_dossier(self, path):
        self.dossier_selectionne = path
        Snackbar(text=f"Dossier sélectionné : {path}", duration=2).open()
        self.fermer_filemanager()

    def log(self, message):
        self.logs += message + "\n"

    def lancer_organisation(self):
        if not self.dossier_selectionne or not os.path.isdir(self.dossier_selectionne):
            Snackbar(text="Dossier invalide ou non sélectionné", duration=2).open()
            return

        self.logs = ""
        try:
            stats = organiser_fichiers(self.dossier_selectionne, log_callback=self.log)
            actions = stats["actions"]
            categories = stats["catégories"]
            total = sum(actions.values())

            resume = f"\nFichiers traités : {total}\n"
            resume += f"- Déplacés : {actions['déplacés']}\n"
            resume += f"- Renommés : {actions['renommés']}\n"
            resume += f"- Remplacés : {actions['remplacés']}\n"
            resume += f"- Ignorés : {actions['ignorés']}\n\n"
            resume += "Par catégorie :\n"
            for cat, count in categories.items():
                resume += f"- {cat} : {count}\n"

            self.log(resume)
        except Exception as e:
            self.log(f"[ERREUR] {str(e)}")

    def effacer_logs(self):
        self.logs = ""
        Snackbar(text="Rapport effacé", duration=2).open()

if __name__ == "__main__":
    OrganiseurApp().run()
