# -*- coding: utf-8 -*-

"""
Classe Dao[Author].
"""

import pymysql  # type: ignore
from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.author import Author


@dataclass
class AuthorDao(Dao[Author]):
    """
    Classe Dao pour un auteur.

    """

    def create(self, author: Author) -> int:
        ...
        return 0

    def read(self, id_author: int) -> Optional[Author]:
        """
        Récupère un auteur par son id.


        """
        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT aut_id,
                       aut_last_name,
                       aut_first_name,
                       aut_biography
                FROM author
                WHERE aut_id = %s
            """
            cursor.execute(sql, (id_author,))
            record = cursor.fetchone()

        if record is None:
            return None

        author = Author(
            last_name=record["aut_last_name"],
            first_name=record["aut_first_name"],
            biography=record["aut_biography"],
        )
        author.id_author = record["aut_id"]
        return author

    def update(self, author: Author) -> bool:
        ...
        return True

    def delete(self, author: Author) -> bool:
        ...
        return True
