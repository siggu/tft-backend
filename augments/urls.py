from django.urls import path
from . import views

urlpatterns = [
    path("set11", views.Set11Augments.as_view()),
    path("set12", views.Set12Augments.as_view())
]
