# -*- coding: utf-8 -*-

"""
Classe Dao[Editor]
"""

from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.editor import Editor


@dataclass
class EditorDao(Dao[Editor]):


    def create(self, editor: Editor) -> int:
        ...
        return 0

    def read(self, id_editor: int) -> Optional[Editor]:
        """
        Récupère un auteur par son id.

        """
        with self.connection.cursor() as cursor:
            sql = """
                SELECT editr_id,
                       editr_name
                FROM editor
                WHERE editr_id = %s
            """
            cursor.execute(sql, (id_editor,))
            record = cursor.fetchone()

        if record is None:
            return None

        editor = Editor(
            name=record["editr_name"],
        )
        editor.id = record["editr_id"]
        return editor

    def update(self, editor: Editor) -> bool:
        ...
        return True


    def delete(self, editor: Editor) -> bool:
        ...
        return True

