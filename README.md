# goncourt-app

Application console simulant le déroulement de la sélection des livres pour le **Prix Goncourt 2025**.

L'application utilise une base de données MySQL et une architecture en couches (modèle, DAO, métier, interface console).

## Fonctionnalités

L’application permet de :

- **Afficher les livres pour chaque sélection** (phases 1, 2, 3) lorsqu’elles sont définies.
- **Afficher le détail d’un livre** :
  - titre, résumé, auteur, éditeur, personnages principaux,
  - date de parution, nombre de pages, ISBN, prix éditeur.
- **Définir les sélections de livres** pour :
  - la **2ᵉ phase**, à partir des livres de la 1ʳᵉ sélection ;
  - la **3ᵉ phase**, à partir des livres de la 2ᵉ sélection.
- **Attribuer des votes** pour la **phase finale (4ᵉ)** :
  - saisie du nombre de voix par livre finaliste,
  - calcul du lauréat (livre ayant obtenu le plus de voix).
- (Mode développeur) **Réinitialiser** les sélections 2 et 3 ainsi que les votes de la phase finale.

## Architecture

Le projet est organisé de la façon suivante :

- `models/` : classes métier (Book, Author, Editor, Phase, Vote, Character, …).
- `daos/`   : accès à la base MySQL (`BookDao`, `PhaseDao`, `VoteDao`, etc.).
- `business/` : logique métier (classe `Goncourt`) :
  - gestion des sélections,
  - contrôle du nombre de livres par phase,
  - calcul du lauréat à partir des votes.
- `main.py` : interface console (menus, saisies utilisateur).
.

## Prérequis

- Python 3.x
- MySQL (base `goncourt_app` avec les tables et données du script SQL fourni)
- Bibliothèque Python :
  - `pymysql`

## Installation

1. Créer un environnement virtuel et l’activer :

   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # Linux / macOS
   source .venv/bin/activate
``

2. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Créer la base de données MySQL `goncourt_app` et importer le script SQL du projet.

4. Vérifier la configuration de connexion dans `daos/dao.py`
   (hôte, base, utilisateur, mot de passe).

## Utilisation

Depuis la racine du projet :

```bash
python main.py
```

L’application affiche un menu console permettant :

* d’afficher les différentes sélections,
* de définir les sélections 2 et 3,
* d’entrer les votes de la phase finale,
* d’afficher le lauréat calculé,
* (en mode développeur) de réinitialiser les sélections et les votes.

