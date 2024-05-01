from django.urls import path
from . import views

urlpatterns = [
    path("", views.Champions.as_view()),
    path("<str:key>", views.ChampionDetail.as_view()),
]
