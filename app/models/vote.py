# -*- coding: utf-8 -*-

"""
Classe Vote
"""

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Vote:
    """Détail d'un Vote."""
    id_vote: Optional[int] = field(default=None, init=False)
    id_jury_member:int
    id_phase: str
    id_book: int

