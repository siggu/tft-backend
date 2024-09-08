from django.urls import path
from .views import (
    EntryBySummonerDetailAPIView,
    SummonerProfileAPIView,
    SummonerProfileDetailAPIView,
    SummonerMathcesByPuuidAPIView,
    SummonerBadMatchesByPuuidAPIView,
    SummonerMatchByMatchIdAPIView,
    EntryBySummonerAPIView,
)

urlpatterns = [
    path("fetch-puuid/", SummonerProfileAPIView.as_view()),
    path(
        "fetch-puuid/<str:gameName>/<str:tagLine>",
        SummonerProfileDetailAPIView.as_view(),
    ),
    path("entry/", EntryBySummonerAPIView.as_view()),
    path("entry/<str:summonerId>", EntryBySummonerDetailAPIView.as_view()),
    path("matches-by-puuid/<str:puuid>", SummonerMathcesByPuuidAPIView.as_view()),
    path(
        "matchDetails/<str:matchId>",
        SummonerMatchByMatchIdAPIView.as_view(),
    ),
    path("bad-matches-by-puuid/<str:puuid>", SummonerBadMatchesByPuuidAPIView.as_view()),
]

