from django.urls import path
from . import views

urlpatterns = [
    path("set11", views.Encounters.as_view()),
]
