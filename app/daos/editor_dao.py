# -*- coding: utf-8 -*-

"""
Classe Dao[Editor]
"""

from dataclasses import dataclass
from typing import Optional

import pymysql  # type: ignore
from daos.dao import Dao
from models.editor import Editor


@dataclass
class EditorDao(Dao[Editor]):

    def create(self, editor: Editor) -> int:
        """
        Creation d'un éditeur
        :param editor:
        :return:
        """
        ...
        return 0

    def read(self, id_editor: int) -> Optional[Editor]:
        """
        Récupère un auteur par son id.

        """
        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
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
        editor.id_editor = record["editr_id"]
        return editor

    def update(self, editor: Editor) -> bool:
        """
        Mis à jour d'un éditeur
        :param editor:
        :return:
        """
        ...
        return True

    def delete(self, editor: Editor) -> bool:
        """
        Suppression d'un éditeur
        :param editor:
        :return:
        """
        ...
        return True
