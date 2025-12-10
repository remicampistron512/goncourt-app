from business.goncourt import Goncourt


def main() -> None:
    """Programme principal."""
    print("""\
    --------------------------
    Bienvenue dans l'application Goncourt
    --------------------------""")

    goncourt: Goncourt = Goncourt()

    #show_all(goncourt)
    """print("----- AJOUT DE LIVRES A LA PHASE 2 -----")
    book_id_list = [1,2,3,4,5,6,7,8]
    goncourt.set_books_for_phase(2,book_id_list)

    print("----- AJOUT DE LIVRES A LA PHASE 3 -----")
    book_id_list2 = [1,2,3,4]
    goncourt.set_books_for_phase(3,book_id_list2)"""

    goncourt.set_vote_for_book(2, 4, 2)
    show_phase(goncourt,1)


def show_phase(goncourt: Goncourt, phase_id) -> None:
    phase = goncourt.get_phase_by_id(phase_id)
    books = goncourt.get_all_books_by_phase(phase_id)
    print(f"\n--- {phase.type} ---")
    for b in books:
        print(f"{b.id_book}: {b.book_title} ({b.isbn})")


def show_all(goncourt: Goncourt) -> None:
    print("----- AFFICHAGE DE TOUS LES LIVRES-----")
    books = goncourt.get_all_books()
    for book in books:
        print(book)
    print("")

    print("----- AFFICHAGE DES LIVRES DE LA PHASE 1 -----")
    books = goncourt.get_all_books_by_phase(1)
    for book in books:
        print(book)
    print("")

    print("----- AFFICHAGE DES LIVRES DE LA PHASE 2 -----")
    books2 = goncourt.get_all_books_by_phase(2)
    for book in books2:
        print(book)
    print("")

    print("----- AFFICHAGE DES LIVRES DE LA PHASE 3 -----")
    books3 = goncourt.get_all_books_by_phase(3)
    for book in books3:
        print(book)
    print("")


if __name__ == '__main__':
    main()
