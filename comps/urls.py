from django.urls import path
from . import views

urlpatterns = [
    path("", views.Comps.as_view()),
]
