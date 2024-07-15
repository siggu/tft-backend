from django.urls import path
from . import views

urlpatterns = [
    path("set11", views.Set11Items.as_view()),
    path("set12", views.Set12Items.as_view())
]
