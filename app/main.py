from business.goncourt import Goncourt

def main() -> None:
    """Programme principal."""
    print("""\
    --------------------------
    Bienvenue dans l'application Goncourt
    --------------------------""")

    goncourt : Goncourt = Goncourt()
    print("----- AFFICHAGE DE TOUS LES LIVRES-----")
    books = goncourt.get_all_books()
    for book in books:
        print(book)
    print("")

if __name__ == '__main__':
    main()
