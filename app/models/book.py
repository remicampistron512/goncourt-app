# -*- coding: utf-8 -*-

"""
Classe Book
"""
import datetime
import decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Book:
    """Détail d'un livre."""
    id_book: Optional[int] = field(default=None, init=False)
    book_title: str
    summary: str
    publishing_date: datetime.date
    nb_pages: int
    isbn: str
    editor_price: decimal.Decimal

    def __str__(self) -> str:
        book_id = self.id if self.id is not None else "?"
        return (
            f"[Book #{book_id}] "
            f"'{self.book_title}' "
            f"({self.publishing_date:%Y-%m-%d}) - "
            f"{self.nb_pages} pages - "
            f"ISBN {self.isbn} - "
            f"{self.editor_price} €"
        )
