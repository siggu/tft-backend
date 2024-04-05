from django.urls import path
from .views import (
    SummonerProfileAPIView,
    SummonerProfileDetailAPIView,
    SummonerMathcesByPuuidAPIView,
)

urlpatterns = [
    path("fetch-puuid/", SummonerProfileAPIView.as_view()),
    path("fetch-puuid/<str:summonerName>", SummonerProfileDetailAPIView.as_view()),
    path(
        "matches-by-puuid/<str:summonerPuuid>", SummonerMathcesByPuuidAPIView.as_view()
    ),
]
