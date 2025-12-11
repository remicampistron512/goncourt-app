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
    #show_phase(goncourt, 1)

    # @todo implémenter la gestion du 4eme tour avec les votes
    while True:
        second_selection_completed = goncourt.is_selection_complete(2)
        third_selection_completed = goncourt.is_selection_complete(3)

        print("\n=== Goncourt App ===")
        print("1. Montrer la première selection")
        if not second_selection_completed:
            print("2. Définir la seconde sélection")
        else:
            print("2. Montrer la deuxième selection")

        if not third_selection_completed and second_selection_completed:
            print("3. Définir la troisième sélection")
        elif third_selection_completed:
            print("3. Montrer la troisième selection")

        if third_selection_completed:
            print("4. Attribuer les votes pour désigner le lauréat")
        print("0. Quit")

        choice = input("Votre choix: ").strip()
        if choice == "1":
            show_phase(goncourt, 1)
        elif choice == "2" and second_selection_completed:
            show_phase(goncourt, 2)
        elif choice == "2" and not second_selection_completed:
            define_selection(goncourt, 2)
        elif choice == "3" and third_selection_completed:
            show_phase(goncourt, 3)
        elif choice == "3" and not third_selection_completed:
            define_selection(goncourt, 3)
        elif choice == "4":
            cast_votes(goncourt)
        elif choice == "0":
            print("Au revoir.")
            break
        else:
            print("Choix invalide.")


def define_selection(goncourt: Goncourt, phase_id: int) -> None:
    phase = goncourt.get_phase_by_id(phase_id)

    while True:
        # 1) combien de livres sont déjà dans cette phase ?
        current_books = goncourt.get_all_books_by_phase(phase_id)
        remaining_slots = phase.nb_books - len(current_books)

        if remaining_slots <= 0:
            print("\nLa sélection est complète.")
            break

        # 2) quels livres restent disponibles à ajouter ?
        available_books = goncourt.get_remaining_books_from_previous_phase(phase_id-1,phase_id)
        if not available_books:
            print("\nIl n'y a plus de livres disponibles à ajouter.")
            break

        print(f"\n----- Sélectionnez un livre à ajouter à la sélection "
              f"({remaining_slots} place(s) restante(s)) -----")

        for book in available_books:
            # suppose que Book.__str__ est déjà bien défini
            print(book)

        print("")
        choice_str = input("Entrez l'id du livre (ou ENTER pour arrêter) : ").strip()
        if choice_str == "":
            # l'utilisateur veut arrêter avant que la sélection soit pleine
            break

        try:
            choice_id = int(choice_str)
        except ValueError:
            print("Id invalide, veuillez saisir un nombre.")
            continue

        # 3) ajout du livre à la phase via le service métier
        goncourt.add_book_to_phase(phase_id, choice_id)


def show_phase(goncourt: Goncourt, phase_id) -> None:
    phase = goncourt.get_phase_by_id(phase_id)
    books = goncourt.get_all_books_by_phase(phase_id)
    print(f"\n--- {phase.type} ---")
    for b in books:
        print(f"{b.id_book}: {b.book_title} ({b.isbn})")


def show_all(goncourt: Goncourt) -> None:
    print("\n--- Première sélection ---")
    books = goncourt.get_all_books()
    for book in books:
        print(book)
    print("")



if __name__ == '__main__':
    main()
