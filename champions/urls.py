from django.urls import path
from . import views

urlpatterns = [
    path("set11", views.Set11Champions.as_view()),
    path("set11/<str:key>", views.Set11ChampionDetail.as_view()),
    path("set12", views.Set12Champions.as_view()),
    path("set12/<str:key>", views.Set12ChampionDetail.as_view())
]
