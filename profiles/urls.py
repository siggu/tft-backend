from django.urls import path
from .views import SummonerPuuidAPIView, SummonerMathcesByPuuidAPIView

urlpatterns = [
    path("fetch-puuid/", SummonerPuuidAPIView.as_view()),
    path("matches-by-puuid/", SummonerMathcesByPuuidAPIView.as_view()),
]
