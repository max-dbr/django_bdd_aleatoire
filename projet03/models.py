# models.py dans votre application projet03

from django.db import models

class Product(models.Model):
    reference = models.TextField(primary_key=True)
    vetement = models.TextField()
    couleur = models.TextField()
    taille = models.TextField()
    quantite = models.IntegerField()
    prix_unitaire = models.FloatField()
    prix_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False  # Indique à Django de ne pas gérer cette table
        db_table = 'stock_magasin'  # Nom de la table dans la base de données
