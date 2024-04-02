from django.urls import path
from .views import (
    SummonerProfileAPIView,
    SummonerProfileDetailAPIView,
    SummonerMathcesByPuuidAPIView,
)

urlpatterns = [
    path("fetch-puuid/", SummonerProfileAPIView.as_view()),
    path("fetch-puuid/<str:name>", SummonerProfileDetailAPIView.as_view()),
    path("matches-by-puuid/", SummonerMathcesByPuuidAPIView.as_view()),
]
