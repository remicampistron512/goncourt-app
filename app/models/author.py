# -*- coding: utf-8 -*-

"""
Classe Author.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Author:
    """
    Détails d'un auteur
    """
    id_author: Optional[int] = field(default=None, init=False)
    last_name: str
    first_name: str
    biography: Optional[str] = None

    def __str__(self) -> str:
        id_author = self.id_author if self.id_author is not None else "?"
        return f"[Auteur #{id_author}] {self.first_name} {self.last_name}"