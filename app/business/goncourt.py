from dataclasses import dataclass

from daos.book_dao import BookDao
from daos.phase_dao import PhaseDao


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

    @staticmethod
    def get_all_books():
        book_dao: BookDao = BookDao()
        return book_dao.read_all()

    @staticmethod
    def get_all_books_by_phase(phase_id: int):
        book_dao: BookDao = BookDao()
        return book_dao.list_by_phase(phase_id)

    @staticmethod
    def set_books_for_phase(phase_id: int, book_ids: list[int]):
        phase_dao: PhaseDao = PhaseDao()
        phase_dao.set_books_for_phase(phase_id,book_ids)

