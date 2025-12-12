from business.goncourt import Goncourt


def main(dev: bool = False) -> None:
    """Fonction principale qui sert d'entrée pour le reste du programme. Elle contient la logique de saisi
    utilisateur
    @todo Réduire la complexité cognitive de cette fonction
    """
    print("""\
    --------------------------
    Bienvenue dans l'application Goncourt
    --------------------------""")
    # On instancie l'application
    goncourt: Goncourt = Goncourt()

    while True:
        # On vérifie si la selection d'une phase est complète pour adaptée l'affichage
        second_selection_completed = goncourt.is_selection_complete(2)
        third_selection_completed = goncourt.is_selection_complete(3)
        # Affiche le lauréat, vide s'il n'a pas été encore désigné
        show_award_winner(goncourt)
        # affiche le menu principal
        print_menu(second_selection_completed, third_selection_completed)
        # mode développeur, pour notamment réinitialiser la bdd facilement
        if dev:
            print_dev_menu()

        choice = input("Votre choix: ").strip()
        # principal flux logique permettant l'affichage des menus

        # on affiche la première sélection
        if choice == "1":
            show_phase(goncourt, 1)
            ask_to_view_book_details(goncourt)
        # la deuxième selection est complète, on l'affiche
        elif choice == "2" and second_selection_completed:
            show_phase(goncourt, 2)
        # la deuxième selection est incomplète, on propose de la définir
        elif choice == "2" and not second_selection_completed:
            define_selection(goncourt, 2)
        # la troisième selection est complète, on l'affiche
        elif choice == "3" and third_selection_completed:
            show_phase(goncourt, 3)
        # la troisième selection est incomplète, on propose de la définir
        elif choice == "3" and not third_selection_completed:
            define_selection(goncourt, 3)
        # permet d'attribuer les votes pour la phase finale
        elif choice == "4":
            cast_votes(goncourt)
        # mode développeur, permet de vider certaines tables
        elif choice == "D":
            confirm = input(
                "ATTENTION: cette action va effacer les sélections 2 & 3 et tous les votes. "
                "Confirmer ? (o/N) : "
            ).strip().lower()
            if confirm == "o":
                goncourt.reset_selections_and_votes()
                print("Réinitialisation effectuée.")
            else:
                print("Réinitialisation annulée.")
        # on quitte l'application
        elif choice == "0":
            print("Au revoir.")
            break
        else:
            print("Choix invalide.")


def ask_to_view_book_details(goncourt):
    """Permet l'affichage complet des détails d'un livre"""
    while True:
        print("")
        choice_str = input("Entrez l'id du livre pour voir les détails (ou ENTER pour arrêter) : ").strip()
        if choice_str == "":
            # l'utilisateur veut arrêter avant que la sélection soit pleine
            break

        try:
            choice_id = int(choice_str)
        except ValueError:
            print("Id invalide, veuillez saisir un nombre.")
            continue

        book_details_full = goncourt.get_book_full_details(choice_id)

        if book_details_full is not None:
            book, author, editor, characters = book_details_full
            print(book.to_detailed_string())
            print(author)
            print(editor)
            for c in characters:
                print(" -", c)


def show_award_winner(goncourt: Goncourt) -> None:
    """Affiche le lauréat du concours"""
    result = goncourt.get_award_winner()
    if result is None:
        print("Aucun vote enregistré désignant le lauréat.")
        return

    book, total_votes = result
    print("\n=== Lauréat ===")
    print(f"{book.book_title} ({book.isbn}) – {total_votes} voix")


def print_dev_menu() -> None:
    print("D. Réinitialiser l'application (vide les 2ème et 3ème selections, et les votes)")


def print_menu(second_selection_completed: bool, third_selection_completed: bool) -> None:
    """
    Affiche le menu principal en fonction de l'état des sélections.
    :param second_selection_completed:
    :param third_selection_completed:
    :return:
    """
    print("1. Montrer la première selection et consulter les détails d'un livre")

    # Option 2 : deuxième sélection
    if not second_selection_completed:
        print("2. Définir la seconde sélection")
    else:
        print("2. Montrer la deuxième selection")

    # Option 3 : troisième sélection
    if not third_selection_completed and second_selection_completed:
        print("3. Définir la troisième sélection")
    elif third_selection_completed:
        print("3. Montrer la troisième selection")

    # Option 4 : votes finaux
    if third_selection_completed:
        print("4. Attribuer les votes pour désigner le lauréat")
    print("0. Quitter")


def is_in_available_books(choice_id, available_books):
    """
     Vérifie si un id de livre est présent dans la liste des livres disponibles.
     """
    for book in available_books:
        if choice_id == book.id_book:
            return True
    return False


def define_selection(goncourt: Goncourt, phase_id: int) -> None:
    """
    Définit une sélection de livres pour une phase donnée
    :param goncourt:
    :param phase_id: id de la phase de sélection de livres
    :return:
    """

    # Récupère les informations de la phase de sélection
    phase = goncourt.get_phase_by_id(phase_id)

    while True:
        # combien de livres sont déjà dans cette phase ?
        current_books = goncourt.get_all_books_by_phase(phase_id)
        # nombre de livres restants à ajouter
        remaining_slots = phase.nb_books - len(current_books)
        # il ne reste plus places pour ajouter un livre, la sélection est complète
        if remaining_slots <= 0:
            print("\nLa sélection est complète.")
            break

        # quels livres restent disponibles à ajouter ?
        available_books = goncourt.get_remaining_books_from_previous_phase(phase_id - 1, phase_id)
        if not available_books:
            print("\nIl n'y a plus de livres disponibles à ajouter.")
            break

        print(f"\n----- Sélectionnez un livre à ajouter à la sélection "
              f"({remaining_slots} place(s) restante(s)) -----")

        for book in available_books:
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

        # ajout du livre à la phase de sélection
        if not goncourt.is_book_in_selection(phase_id, choice_id) and is_in_available_books(choice_id, available_books):
            goncourt.add_book_to_phase(phase_id, choice_id)
        else:
            print("Ce livre a déjà été ajouté à la sélection ou n'est pas disponible pour cette phase"
                  " veuillez en choisir un autre")


def show_phase(goncourt: Goncourt, phase_id) -> None:
    """
    Affiche les livres d'une phase de sélection de donnée
    :param goncourt:
    :param phase_id: id de la phase de sélection de livres
    :return:
    """
    phase = goncourt.get_phase_by_id(phase_id)
    books = goncourt.get_all_books_by_phase(phase_id)
    print(f"\n--- {phase.type} ---")
    for b in books:
        print(f"{b.id_book}: {b.book_title} ({b.isbn})")


def show_all(goncourt: Goncourt) -> None:
    """
    Affiche tous les livres (utilisé pour les tests)
    :param goncourt:
    :return:
    """
    print("\n--- Voici tous les livres ---")
    books = goncourt.get_all_books()
    for book in books:
        print(book)
    print("")


def cast_votes(goncourt) -> None:
    """
    Attribue des votes à chaque livre, livre après livre
    :param goncourt:
    :return:
    """
    books = goncourt.get_all_books_by_phase(3)

    print("\n=== Saisie des votes ===")

    votes_by_book: dict[int, int] = {}

    for book in books:
        while True:
            print(f"Livre #{book.id_book} : {book.book_title}")
            entry = input("Nombre de voix (entier >= 0, ENTER pour 0) : ").strip()

            if entry == "":
                nb_votes = 0
                break

            try:
                nb_votes = int(entry)
                if nb_votes < 0:
                    print("Le nombre de voix doit être >= 0.")
                    continue
                break
            except ValueError:
                print("Valeur invalide, veuillez saisir un entier.")
                continue

        votes_by_book[book.id_book] = nb_votes
        print("")

    goncourt.record_final_votes(votes_by_book)

    print("Les votes ont été enregistrés.")


if __name__ == '__main__':
    main(True)
