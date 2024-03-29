from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import serializers
from .models import SummonerPuuid
import requests
import os


class SummonerPuuidAPIView(APIView):
    def get(self, request):
        summonerpuuids = SummonerPuuid.objects.all()
        serializer = serializers.SummonerPuuidSerializer(
            summonerpuuids,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        profile_name = request.data.get("summonerName")
        api_key = os.getenv("RIOT_API_KEY")
        url = f"https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{profile_name}?api_key={api_key}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                summoner_puuid = SummonerPuuid.objects.create(
                    id=data["id"],
                    accountId=data["accountId"],
                    puuid=data["puuid"],
                    name=data["name"],
                    profileIconId=data["profileIconId"],
                    revisionDate=data["revisionDate"],
                    summonerLevel=data["summonerLevel"],
                )
                return Response(
                    {
                        "message": "Summoner puuid fetched and saved successfully!",
                        "data": summoner_puuid.id,
                    }
                )
            else:
                return Response(
                    {
                        "error": "Failed to fetch summoner puuid",
                        "status_code": response.status_code,
                    },
                    status=response.status_code,
                )
        except Exception as e:
            return Response({"error": str(e)}, status=500)
