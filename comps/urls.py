from django.urls import path
from . import views

urlpatterns = [
    path("set11", views.Set11Comps.as_view()),
    path("set11/meta/decks", views.Set11MetaDecks.as_view()),
    path("set11/meta/items", views.Set11MetaItems.as_view()),
    path("set12", views.Set12Comps.as_view()),
    path("set12/meta/decks", views.Set12MetaDecks.as_view()),
    path("set12/meta/items", views.Set12MetaItems.as_view())
]
