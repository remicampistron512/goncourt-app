from dataclasses import dataclass


@dataclass
class Goncourt:
    """
    Couche métier de l'application Goncourt, permettant
    – pour les utilisateurs
        – afficher la liste des livres d’une sélection
        – consulter le détail d’un livre

    – pour le président du jury
        – définir la 2e sélection
        – définir la 3e sélection (finalistes)
        – Gestion du dernier tour de scrutin

    """

