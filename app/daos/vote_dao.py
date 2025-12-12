# -*- coding: utf-8 -*-

"""
Classe Dao[Vote]
"""

from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.vote import Vote


@dataclass
class VoteDao(Dao[Vote]):

    # TODO: implémenter create/read/update/delete ou laisser VoteDao abstraite
    def create(self, vote: Vote) -> int:
        ...
        return 0

    def read(self, id_vote: int) -> Optional[Vote]:
        ...
        return None

    def update(self, vote: Vote) -> bool:
        ...
        return True

    def delete(self, vote: Vote) -> bool:
        ...

    def set_votes_for_book(self, nb_votes: int, id_jury_member: int, id_phase: int, id_book: int) -> None:
        # ici, on assigne un seul vote par défaut

        """
                Assigne un nombre de votes à un livre pour un membre et une phase.
                Si un vote existe déjà pour (membre, phase, livre), il est mis à jour.
                Sinon, il est créé.
                """

        sql = """
                    INSERT INTO vote (
                        vot_nb_votes,
                        vot_fk_mem_id,
                        vot_fk_pha_id,
                        vot_fk_boo_id
                    )
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        vot_nb_votes = VALUES(vot_nb_votes)
                """

        params = (nb_votes, id_jury_member, id_phase, id_book)

        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)

        self.connection.commit()

    def get_award_winner(self, ):
        """
                Renvoie le gagnant du concours
                """
        with self.connection.cursor() as cursor:
            sql = """
                       SELECT
                           vot_fk_boo_id   AS book_id,
                           SUM(vot_nb_votes) AS total_votes
                       FROM vote
                       WHERE vot_fk_pha_id = 4
                       GROUP BY vot_fk_boo_id
                       ORDER BY total_votes DESC
                       LIMIT 1
                   """
            cursor.execute(sql)
            record = cursor.fetchone()

        if record is None:
            return None

        book_id: int = record["book_id"]
        total_votes: int = record["total_votes"]
        return book_id, total_votes

    def delete_by_phase(self, phase_id: int) -> None:
        """
        Supprime les votes pour une phase donnée
        """
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM vote WHERE vot_fk_pha_id = %s"
            cursor.execute(sql, (phase_id,))

        self.connection.commit()
