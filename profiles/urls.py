from django.urls import path
from .views import SummonerPuuidAPIView

urlpatterns = [
    path("fetch-puuid/", SummonerPuuidAPIView.as_view()),
]
