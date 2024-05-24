# Dans votre fichier urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('generer-lignes-aleatoires/', views.generer_lignes_aleatoires, name='generer_lignes_aleatoires'),
    path('supprimer-toutes-lignes/', views.supprimer_toutes_lignes, name='supprimer_toutes_lignes'),
]
