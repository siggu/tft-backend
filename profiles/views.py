from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import serializers
from .models import SummonerPuuid, SummonerMatchesByPuuid
import requests
import os


class SummonerProfileAPIView(APIView):
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
                        "data": summoner_puuid.puuid,
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


class SummonerProfileDetailAPIView(APIView):
    def get_object(self, name):
        try:
            return SummonerPuuid(name=name)
        except SummonerPuuid.DoesNotExist:
            return NotFound

    def get(self, request, name):
        summonerpuuid = self.get_object(name)
        serializer = serializers.SummonerPuuidSerializer(summonerpuuid)
        return Response(serializer.data)


class SummonerMathcesByPuuidAPIView(APIView):
    def get_object(self, pk):
        try:
            return SummonerPuuid.objects(pk=pk)
        except SummonerPuuid.DoesNotExist:
            return NotFound

    def get(self, request, pk):
        matches = SummonerMatchesByPuuid.objects.all()
        serializer = serializers.SummonerMatchesByPuuidSerializer(
            matches,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        try:
            summonerpuuids = self.get_object(pk)
            if not summonerpuuids:
                return Response(
                    {"error": "summonerpuuids is required in the request data"},
                    status=400,
                )

            api_key = os.getenv("RIOT_API_KEY")
            url = f"https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{summonerpuuids}?api_key={api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                matches_data = response.json()

                for match_data in matches_data:
                    match = SummonerMatchesByPuuid.objects.create()
                return Response({"message": "Match data saved successfully!"})
            else:
                return Response(
                    {
                        "error": "Failed to fetch match data",
                        "status_code": response.status_code,
                    },
                    status=response.status_code,
                )
        except Exception as e:
            return Response({"error": str(e)}, status=500)
