import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
db_path = os.path.join(BASE_DIR, 'db.sqlite3')

# Connexion à la base de données
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Affiche toutes les tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

# Vérifie si la table 'stock_magasin' existe
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stock_magasin';")
exists = cursor.fetchone()
if exists:
    print("Table 'stock_magasin' exists.")
else:
    print("Table 'stock_magasin' does not exist.")
    # Crée la table si elle n'existe pas
    cursor.execute('''
        CREATE TABLE stock_magasin (
            Reference TEXT,
            Vetement TEXT,
            Couleur TEXT,
            Taille TEXT,
            Quantite INTEGER,
            Prix_unitaire FLOAT,
            Prix_total DECIMAL
        );
    ''')
    print("Table 'stock_magasin' created.")

# Insérer des données de test
cursor.execute('''
    INSERT INTO stock_magasin (Reference, Vetement, Couleur, Taille, Quantite, Prix_unitaire, Prix_total)
    VALUES ('REF123', 'T-Shirt', 'Rouge', 'M', 10, 19.99, 199.90);
''')
conn.commit()

# Affiche les données de la table 'stock_magasin'
cursor.execute("SELECT * FROM stock_magasin;")
rows = cursor.fetchall()

print("Data in 'stock_magasin':")
for row in rows:
    print(row)

# Ferme la connexion
conn.close()
