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
        id_book = self.id_book if self.id_book is not None else "?"
        return (
            f"[Livre #{id_book}] "
            f"'{self.book_title}' "
            f"({self.publishing_date:%Y-%m-%d}) - "
            f"{self.nb_pages} pages - "
            f"ISBN {self.isbn} - "
            f"{self.editor_price} €"
        )

    def to_detailed_string(self) -> str:
        """
        Représentation détaillée du livre, incluant le résumé.
        À utiliser lorsqu'on affiche la fiche complète du livre.
        """
        id_book = self.id_book if self.id_book is not None else "?"
        header = (
            f"[Livre #{id_book}] '{self.book_title}'\n"
            f"Date de parution : {self.publishing_date:%Y-%m-%d}\n"
            f"Nombre de pages : {self.nb_pages}\n"
            f"ISBN : {self.isbn}\n"
            f"Prix éditeur : {self.editor_price} €\n"
        )
        body = f"\nRésumé :\n{self.summary}"
        return header + body