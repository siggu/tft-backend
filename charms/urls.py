from django.urls import path
from . import views

urlpatterns = [
    path("set12", views.Set12Charms.as_view()),
]
