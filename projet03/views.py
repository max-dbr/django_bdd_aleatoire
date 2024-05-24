from django.shortcuts import render, redirect
from .models import Product
import random
from django.db import IntegrityError

# Liste de vrais vêtements
VETEMENTS = ['T-shirt', 'Veste', 'Chemise', 'Pantalon', 'Robe', 'Pull', 'Jupe', 'Short', 'Manteau']

def product_list(request):
    products = Product.objects.all()
    return render(request, 'projet03/index.html', {'products': products})

def index(request):
    return render(request, "projet03/index.html")

def generer_lignes_aleatoires(request):
    for _ in range(10):  # Générer 10 lignes aléatoires, ajustez le nombre selon vos besoins
        reference = 'REF' + str(random.randint(100, 999))

        # Vérifier si la référence existe déjà dans la base de données
        while Product.objects.filter(reference=reference).exists():
            reference = 'REF' + str(random.randint(100, 999))

        vetement = random.choice(['T-shirt', 'Veste', 'Pantalon', 'Chemise', 'Jupe', 'Short', 'Manteau', 'Pull', 'Robe' ])
        couleur = random.choice(['Rouge', 'Bleu', 'Vert', 'Jaune', 'Rouge', 'Blanc', 'Noir', 'Marron', 'Rose'])
        taille = random.choice(['T.XS', 'T.S', 'T.M', 'T.L', 'T.XL'])
        quantite = random.randint(1, 100)
        prix_unitaire = round(random.uniform(5.0, 50.0), 2)
        prix_total = round(quantite * prix_unitaire, 2)

        try:
            Product.objects.create(
                reference=reference,
                vetement=vetement,
                couleur=couleur,
                taille=taille,
                quantite=quantite,
                prix_unitaire=prix_unitaire,
                prix_total=prix_total
            )
        except IntegrityError:
            # Si une erreur d'intégrité se produit, essayez de générer une nouvelle référence
            continue

    return redirect('product_list')  # Redirection vers la page affichant la liste des produits


def supprimer_toutes_lignes(request):
    Product.objects.all().delete()
    return redirect('product_list')