# -*- coding: utf-8 -*-

"""
DAO pour les personnages (Character).
"""

from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.character import Character


@dataclass
class CharacterDao(Dao[Character]):
    """
    Classe Dao character
    """

    def create(self, character: Character) -> int:
        """Créé l'entité Character"""
        ...
        return True

    def read(self, id_character: int) -> Optional[Character]:
        """Renvoie le personnage correspondant à l'entité id
                  (ou None s'il n'a pu être trouvé)"""
        with self.connection.cursor() as cursor:
            sql = """
                SELECT cha_id,
                       char_nickname,
                       cha_last_name,
                       cha_first_name,
                       boo_id
                FROM character_
                WHERE cha_id = %s
            """
            cursor.execute(sql, (id_character,))
            record = cursor.fetchone()

        if record is None:
            return None

        character = Character(
            nickname=record["char_nickname"],
            last_name=record["cha_last_name"],
            first_name=record["cha_first_name"],
            book_id=record["boo_id"],
        )
        character.id_character = record["cha_id"]
        return character

    def update(self, character: Character) -> bool:
        """
            Met à jour en BD l'entité Character
        """
        ...
        return True

    def delete(self, character: Character) -> bool:
        ...
        return True

