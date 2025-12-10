# -*- coding: utf-8 -*-

"""
Classe Dao[Phase]
"""

from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.phase import Phase


@dataclass
class PhaseDao(Dao[Phase]):

    # TODO: implémenter create/read/update/delete ou laisser PhaseDao abstraite
    def create(self, phase: Phase) -> int:
        ...
        return 0

    def read(self, id_phase: int) -> Optional[Phase]:
        """Renvoie le livre correspondant à l'entité id
                  (ou None s'il n'a pu être trouvé)"""
        phase: Optional[Phase]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM phase WHERE pha_id=%s"
            cursor.execute(sql, id_phase)
            record = cursor.fetchone()
        if record is not None:
            phase = Phase(record['pha_id'],record["pha_type"],record["pha_date"],record["awa_id"])

        else:
            phase = None

        return phase


    def update(self, phase: Phase) -> bool:
        ...
        return True

    def delete(self, phase: Phase) -> bool:
        ...

    def set_books_for_phase(self, phase_id: int, book_ids: list[int]) -> None:
        """
        Remplace tous les livres associés à une phase par la liste book_ids.
        """
        with self.connection.cursor() as cursor:
            # 1) supprimer les livres actuellement associés à cette phase
            cursor.execute(
                "DELETE FROM contains WHERE cont_fk_pha_id = %s",
                (phase_id,),
            )

            # 2) insérer les nouvelles associations
            sql = """
                INSERT INTO contains (cont_fk_pha_id, cont_fk_boo_id)
                VALUES (%s, %s)
            """
            for book_id in book_ids:
                cursor.execute(sql, (phase_id, book_id))

        # valider les modifications
        self.connection.commit()
