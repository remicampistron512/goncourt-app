# -*- coding: utf-8 -*-

"""
Classe Dao[Book]
"""
from decimal import Decimal

from models.book import Book
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class BookDao(Dao[Book]):
    def create(self, book: Book) -> int:
        """Crée en BD l'entité Book correspondant au livre Book

        :param book: à créer sous forme d'entité Book en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué).
        """
        ...
        return 0

    def read(self, id_book: int) -> Optional[Book]:
        """Renvoie le livre correspondant à l'entité id
           (ou None s'il n'a pu être trouvé)"""
        book: Optional[Book]

        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM  book WHERE boo_id=%s"
            cursor.execute(sql, id_book)
            record = cursor.fetchone()
        if record is not None:
            book = Book(record['boo_title'], record['boo_summary'], record['boo_publishing_date'], record['boo_nb_pages'],record['boo_isbn'],record['boo_editor_price'])
            book.id_book = record['boo_id']
        else:
            book = None

        return book

    def read_all(self) -> list[Book]:
        """
        Renvoie tous les livres
        :return:
        """
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM book"
            cursor.execute(sql)
            records = cursor.fetchall()

        books: list[Book] = []

        for record in records:

            price = record["boo_editor_price"]
            if isinstance(price, str):
                price = Decimal(price)

            book = Book(
                book_title=record["boo_title"],
                summary=record["boo_summary"],
                publishing_date=record["boo_publishing_date"],
                nb_pages=record["boo_nb_pages"],
                isbn=record["boo_isbn"],
                editor_price=price,
            )
            book.id_book = record["boo_id"]
            books.append(book)

        return books

    def list_by_phase(self, phase_id: int) -> list[Book]:
        """
             Renvoie tous les livres d'une phase
             :return:
             """
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM book JOIN contains ON cont_fk_boo_id = boo_id WHERE cont_fk_pha_id = %s"

            cursor.execute(sql,phase_id)
            records = cursor.fetchall()

        books: list[Book] = []

        for record in records:

            price = record["boo_editor_price"]
            if isinstance(price, str):
                price = Decimal(price)

            book = Book(
                book_title=record["boo_title"],
                summary=record["boo_summary"],
                publishing_date=record["boo_publishing_date"],
                nb_pages=record["boo_nb_pages"],
                isbn=record["boo_isbn"],
                editor_price=price,
            )
            book.id_book = record["boo_id"]
            books.append(book)

        return books


    def update(self, book: Book) -> bool:
        """Met à jour en BD l'entité Book correspondant à Book, pour y correspondre

        :param book: livre déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, book: Book) -> bool:
        """Supprime en BD l'entité Book correspondant à Book

        :param book: livre dont l'entité Book correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True
