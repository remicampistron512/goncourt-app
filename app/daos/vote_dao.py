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

    def set_votes_for_book(self, id_jury_member: int, id_phase: int,id_book: int ) -> None:
        # ici, on assigne un seul vote par défaut
        nb_votes = 1
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
