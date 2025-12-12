# -*- coding: utf-8 -*-

"""
Classe character.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Character:
    """
    Représente les personnages principaux d'un livre

    """
    id: Optional[int] = field(default=None, init=False)
    nickname: str
    last_name: str
    first_name: str
    book_id: int

    def __str__(self) -> str:
        char_id = self.id if self.id is not None else "?"

        full_name_parts: list[str] = []
        if self.first_name:
            full_name_parts.append(self.first_name)
        if self.last_name:
            full_name_parts.append(self.last_name)

        full_name = " ".join(full_name_parts)
        label = full_name or self.nickname or "(unknown)"
        return f"[Personnage #{char_id}] {label}"
