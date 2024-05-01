from django.urls import path
from . import views

urlpatterns = [
    path("", views.Augments.as_view()),
]
