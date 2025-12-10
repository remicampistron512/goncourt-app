from dataclasses import dataclass

from daos.book_dao import BookDao
from daos.phase_dao import PhaseDao
from daos.vote_dao import VoteDao


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
        phase_dao.set_books_for_phase(phase_id, book_ids)

    @staticmethod
    def set_vote_for_book(id_jury_member: int, id_phase: int, id_book: int):
        vote_dao: VoteDao = VoteDao()
        vote_dao.set_votes_for_book(id_jury_member, id_phase, id_book)

    @staticmethod
    def get_phase_by_id(phase_id: int):
        phase_dao: PhaseDao = PhaseDao()
        return phase_dao.read(phase_id)