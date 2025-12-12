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
    id: Optional[int] = field(default=None, init=False)
    last_name: str
    first_name: str
    biography: Optional[str] = None

    def __str__(self) -> str:
        author_id = self.id if self.id is not None else "?"
        return f"[Auteur #{author_id}] {self.first_name} {self.last_name}"