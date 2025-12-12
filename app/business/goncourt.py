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
    def get_book_full_details(book_id):
        book_dao: BookDao = BookDao()
        return book_dao.read_full(book_id)

    @staticmethod
    def get_all_books():
        """
        récupère la liste de tous les livres
        :return:
        """
        book_dao: BookDao = BookDao()
        return book_dao.read_all()

    @staticmethod
    def get_all_books_by_phase(phase_id: int):
        """
        récupère la liste de tous les livres par phase de sélection
        :param phase_id:
        :return:
        """
        book_dao: BookDao = BookDao()
        return book_dao.list_by_phase(phase_id)

    @staticmethod
    def get_remaining_books_from_previous_phase(previous_phase_id: int, current_phase_id: int):
        """
        Récupère les livres disponibles pour la phase de sélection en cours
        :param previous_phase_id:
        :param current_phase_id:
        :return:
        """
        book_dao: BookDao = BookDao()
        return book_dao.get_remaining_books_from_previous_phase(previous_phase_id, current_phase_id)

    @staticmethod
    def set_books_for_phase(phase_id: int, book_ids: list[int]):
        """
        Assigne des livres à une sélection donnée, utilisé pour les tests
        :param phase_id:
        :param book_ids:
        :return:
        """
        phase_dao: PhaseDao = PhaseDao()
        phase_dao.set_books_for_phase(phase_id, book_ids)

    @staticmethod
    def add_book_to_phase(phase_id: int, book_id):
        """
        Assigne un livre à une phase de sélection donnée
        :param phase_id:
        :param book_id:
        :return:
        """
        phase_dao: PhaseDao = PhaseDao()
        phase_dao.add_book_to_phase(phase_id, book_id)

    @staticmethod
    def set_vote_for_book(id_jury_member: int, id_phase: int, id_book: int):
        """
        Définit les votes pour un livre donné
        :param id_jury_member:
        :param id_phase:
        :param id_book:
        :return:
        """
        vote_dao: VoteDao = VoteDao()
        vote_dao.set_votes_for_book(id_jury_member, id_phase, id_book)

    @staticmethod
    def get_phase_by_id(phase_id: int):
        """
        Récupère une phase de sélection et ses détails
        :param phase_id:
        :return:
        """
        phase_dao: PhaseDao = PhaseDao()
        return phase_dao.read(phase_id)

    @staticmethod
    def is_selection_not_empty(phase_id: int):
        """
        Vérifie si une selection n'est pas vide (utilisé dans des tests)
        :param phase_id:
        :return:
        """
        phase_dao: PhaseDao = PhaseDao()
        return phase_dao.is_selection_not_empty(phase_id)

    @staticmethod
    def is_selection_complete(phase_id: int):
        """
        Vérifie si une sélection est complète
        :param phase_id:
        :return:
        """
        phase_dao: PhaseDao = PhaseDao()
        return phase_dao.is_selection_complete(phase_id)

    @staticmethod
    def record_final_votes(votes_by_book: dict[int, int]) -> None:
        """
           Enregistre les votes agrégés par livre pour une phase donnée.

        :param votes_by_book:
        :return:
        """

        vote_dao: VoteDao = VoteDao()
        for book_id, nb_votes in votes_by_book.items():
            vote_dao.set_votes_for_book(nb_votes, 7, 4, book_id)

    @staticmethod
    def get_award_winner():
        """
        Renvoie le gagnant du concours
        """
        vote_dao: VoteDao = VoteDao()
        result = vote_dao.get_award_winner()
        if result is None:
            return None

        book_id, total_votes = result

        book_dao: BookDao = BookDao()
        book = book_dao.read(book_id)
        return book, total_votes
