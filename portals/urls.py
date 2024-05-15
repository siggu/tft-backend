from django.urls import path
from . import views

urlpatterns = [
    path("", views.Portals.as_view()),
]
