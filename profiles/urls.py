from django.urls import path
from .views import fetch_and_save_puuid

urlpatterns = [
    path("fetch-puuid/", fetch_and_save_puuid, name="fetch_and_save_puuid"),
]
