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
    def get_object(self, summonerName):
        try:
            return SummonerPuuid.objects.get(name=summonerName)
        except SummonerPuuid.DoesNotExist:
            raise NotFound

    def get(self, request, summonerName):
        summonerpuuid = self.get_object(summonerName)
        serializer = serializers.SummonerPuuidSerializer(summonerpuuid)
        return Response(serializer.data)


class SummonerMathcesByPuuidAPIView(APIView):
    def get_object(self, summonerPuuid):
        try:
            return SummonerMatchesByPuuid.objects.get(summoner_puuid=summonerPuuid)
        except SummonerMatchesByPuuid.DoesNotExist:
            raise NotFound

    def get(self, request, summonerPuuid):
        summonerMatches = self.get_object(summonerPuuid)
        serializer = serializers.SummonerMatchesByPuuidSerializer(
            summonerMatches,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, summonerPuuid):
        summonerpuuid = summonerPuuid
        api_key = os.getenv("RIOT_API_KEY")
        url = f"https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{summonerpuuid}/ids?start=0&count=1&api_key={api_key}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                matches_data = response.json()

                for match_data in matches_data:
                    match = SummonerMatchesByPuuid.objects.create(
                        summoner_puuid=summonerpuuid,
                        match_id=match_data["match_id"],
                    )
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
