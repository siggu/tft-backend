from django.urls import path
from . import views

urlpatterns = [
    path("", views.Traits.as_view()),
]
