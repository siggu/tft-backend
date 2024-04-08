from django.urls import path
from .views import (
    SummonerProfileAPIView,
    SummonerProfileDetailAPIView,
    SummonerMathcesByPuuidAPIView,
    SummonerMatchByMatchIdAPIView,
)

urlpatterns = [
    path("fetch-puuid/", SummonerProfileAPIView.as_view()),
    path("fetch-puuid/<str:summonerName>", SummonerProfileDetailAPIView.as_view()),
    path(
        "matches-by-puuid/<str:summonerName>", SummonerMathcesByPuuidAPIView.as_view()
    ),
    path(
        "matches-by-puuid/<str:summonerName>/<str:matchId>",
        SummonerMatchByMatchIdAPIView.as_view(),
    ),
]
