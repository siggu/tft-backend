from django.urls import path
from . import views

urlpatterns = [
    path("", views.Encounters.as_view()),
]
