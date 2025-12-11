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
    second_selection_exists = goncourt.is_selection_not_empty(2)
    third_selection_exists = goncourt.is_selection_not_empty(3)

    while True:

        print("\n=== Goncourt App ===")
        print("1. Montrer la première selection")
        if not second_selection_exists:
            print("2. Définir la seconde sélection")
        else:
            print("2. Montrer la deuxième selection")

        if not third_selection_exists:
            print("3. Définir la troisième sélection (president)")
        else:
            print("3. Montrer la troisième selection")

        print("0. Quit")

        choice = input("Your choice: ").strip()
        # @todo implementer selection exists et define selection
        if choice == "1":
            show_phase(goncourt,1)
        elif choice == "2" and second_selection_exists:
            show_phase(goncourt, 2)
        elif choice == "2" and not second_selection_exists:
            pass
             #define_selection(goncourt,2)
        elif choice == "3" and third_selection_exists:
            show_phase(goncourt, 3)
        elif choice == "3" and not third_selection_exists:
            pass
            # define_selection(goncourt,3)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")





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
