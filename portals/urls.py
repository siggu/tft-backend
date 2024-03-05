from django.urls import path
from . import views

urlpatterns = [
    path("", views.Portals.as_view()),
    path("champ/", views.ChampPortals.as_view()),
    path("combat/", views.CombatPortals.as_view()),
    path("spatula/", views.SpatulaPortals.as_view()),
    path("coin/", views.CoinPortals.as_view()),
    path("card/", views.CardPortals.as_view()),
    path("item/", views.ItemPortals.as_view()),
]
