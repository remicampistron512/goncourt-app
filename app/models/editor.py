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
    id: Optional[int] = field(default=None, init=False)
    name: str

    def __str__(self) -> str:
        editor_id = self.id if self.id is not None else "?"
        return f"[Editeur #{editor_id}] {self.name}"
