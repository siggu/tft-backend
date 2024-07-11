from django.urls import path
from . import views

urlpatterns = [
    path("", views.Comps.as_view()),
    path("meta/decks",views.MetaDecks.as_view()),
    path("meta/items",views.MetaItems.as_view()),
]
