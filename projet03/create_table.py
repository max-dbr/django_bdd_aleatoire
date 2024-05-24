import sqlite3
import os

from src.portfolio.settings import BASE_DIR


def create_table():
    # Connexion à la base de données
    conn = sqlite3.connect(os.path.join(BASE_DIR, 'db.sqlite3'))
    cursor = conn.cursor()

    try:
        # Création de la table si elle n'existe pas déjà
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock_magasin (
                Reference TEXT PRIMARY KEY,
                Vetement TEXT,
                Couleur TEXT,
                Taille TEXT,
                Quantite INTEGER,
                Prix_unitaire FLOAT,
                Prix_total DECIMAL
            )
        ''')
        print("La table 'stock_magasin' a été créée avec succès.")

        # Insertion d'une ligne dans la table pour tester
        cursor.execute('''
            INSERT INTO stock_magasin (Reference, Vetement, Couleur, Taille, Quantite, Prix_unitaire, Prix_total)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', ('REF123', 'T-Shirt', 'Rouge', 'M', 10, 19.99, 199.9))
        print("Une ligne a été insérée avec succès.")

        # Commit des modifications
        conn.commit()

    except sqlite3.Error as e:
        # En cas d'erreur, afficher l'erreur
        print("Une erreur s'est produite lors de la création de la table ou de l'insertion de la ligne :", e)

    finally:
        # Fermer la connexion
        conn.close()

# Appeler la fonction pour créer la table et insérer une ligne
create_table()
