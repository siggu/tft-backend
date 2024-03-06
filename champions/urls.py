from django.urls import path
from . import views

urlpatterns = [
    path("", views.Champions.as_view()),
    path("<int:pk>", views.ChampionDetail.as_view()),
    path("<int:pk>/skill", views.Skills.as_view()),
    path("<int:pk>/photos", views.Skills.as_view()),
]
