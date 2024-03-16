from django.urls import path
from . import views

urlpatterns = [
    path("", views.Items.as_view()),
    path("recipies/", views.ItemRecipies.as_view()),
]
