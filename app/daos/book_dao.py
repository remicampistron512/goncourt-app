# -*- coding: utf-8 -*-

"""
Classe Dao[Book]
"""
from decimal import Decimal

from models.book import Book
from models.author import Author
from models.editor import Editor
from models.character import Character
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

    def get_remaining_books_from_previous_phase(
            self,
            previous_phase_id: int,
            current_phase_id: int,
    ) -> list[Book]:
        """
        Retourne les livres qui étaient sélectionnés à la phase précédente,
        mais qui ne sont pas encore associés à la phase courante.
        """
        with self.connection.cursor() as cursor:
            sql = """
                   SELECT *
                   FROM book
                   JOIN contains c_prev
                     ON c_prev.cont_fk_boo_id = boo_id
                    AND c_prev.cont_fk_pha_id = %s
                   LEFT JOIN contains c_curr
                     ON c_curr.cont_fk_boo_id = boo_id
                    AND c_curr.cont_fk_pha_id = %s
                   WHERE c_curr.cont_fk_boo_id IS NULL
                   ORDER BY boo_id
               """
            cursor.execute(sql, (previous_phase_id, current_phase_id))
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


    def read_full(
        self, book_id: int
    ) -> Optional[tuple[Book, Author, Editor, list[Character]]]:
        """
        Retourne une vue complète d'un livre accompagné de son auteur, personnages et éditeur

        :param book_id: boo_id du livre
        :return: un tuple contenant (Book, Author, Editor, [Character...]) ou None.
        """

        # Livre, auteur, éditeur
        with self.connection.cursor() as cursor:
            sql = """
                SELECT
                    b.boo_id,
                    b.boo_title,
                    b.boo_summary,
                    b.boo_publishing_date,
                    b.boo_nb_pages,
                    b.boo_isbn,
                    b.boo_editor_price,
                    a.aut_id,
                    a.aut_last_name,
                    a.aut_first_name,
                    a.aut_biography,
                    e.editr_id,
                    e.editr_name
                FROM book b
                JOIN author a ON b.aut_id = a.aut_id
                JOIN editor e ON b.editr_id = e.editr_id
                WHERE b.boo_id = %s
            """
            cursor.execute(sql, (book_id,))
            record = cursor.fetchone()

        if record is None:
            return None

        # Livre
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

        # Auteur
        author = Author(
            last_name=record["aut_last_name"],
            first_name=record["aut_first_name"],
            biography=record["aut_biography"],
        )
        author.id_author = record["aut_id"]

        # Éditeur
        editor = Editor(
            name=record["editr_name"],
        )
        editor.id_editor = record["editr_id"]

        # Personnages
        with self.connection.cursor() as cursor:
            sql_chars = """
                SELECT cha_id,
                       char_nickname,
                       cha_last_name,
                       cha_first_name,
                       boo_id
                FROM character_
                WHERE boo_id = %s
                ORDER BY cha_id
            """
            cursor.execute(sql_chars, (book_id,))
            char_records = cursor.fetchall()

        characters: list[Character] = []
        for rec in char_records:
            character = Character(
                nickname=rec["char_nickname"],
                last_name=rec["cha_last_name"],
                first_name=rec["cha_first_name"],
                book_id=rec["boo_id"],
            )
            character.id_character = rec["cha_id"]
            characters.append(character)

        return book, author, editor, characters
