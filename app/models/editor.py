# -*- coding: utf-8 -*-

"""
Classe Editor.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Editor:
    """
    représente un éditeur
    """
    id_editor: Optional[int] = field(default=None, init=False)
    name: str

    def __str__(self) -> str:
        id_editor = self.id_editor if self.id_editor is not None else "?"
        return f"[Editeur #{id_editor}] {self.name}"
