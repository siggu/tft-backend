from django.urls import path
from .views import (
    SummonerProfileAPIView,
    SummonerProfileDetailAPIView,
    SummonerMathcesByPuuidAPIView,
    SummonerMatchByMatchIdAPIView,
)

urlpatterns = [
    path("fetch-puuid/", SummonerProfileAPIView.as_view()),
    path(
        "fetch-puuid/<str:gameName>/<str:tagLine>",
        SummonerProfileDetailAPIView.as_view(),
    ),
    # path("fetch-puuid/<str:gameName>", SummonerProfileDetailAPIView.as_view()),
    path("matches-by-puuid/<str:puuid>", SummonerMathcesByPuuidAPIView.as_view()),
    path(
        "matches-by-puuid/<str:gameName>/<str:matchId>",
        SummonerMatchByMatchIdAPIView.as_view(),
    ),
]
