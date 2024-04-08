from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import serializers
from .models import SummonerPuuid, SummonerMatchesByPuuid, SummonerMatchByMatchId
import requests
import os


# 유저 정보 GET, POST
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


# 특정 유저 정보 GET
class SummonerProfileDetailAPIView(APIView):
    def get_object(self, summonerName):
        try:
            return SummonerPuuid.objects.get(name=summonerName)
        except SummonerPuuid.DoesNotExist:
            return NotFound

    def get(self, request, summonerName):
        summonerpuuid = self.get_object(summonerName)
        serializer = serializers.SummonerPuuidSerializer(summonerpuuid)
        return Response(serializer.data)


# 특정 유저 puuid로 매치 ids GET, POST
class SummonerMathcesByPuuidAPIView(APIView):
    def get_object(self, summonerName):
        try:
            return SummonerPuuid.objects.get(name=summonerName)
        except SummonerPuuid.DoesNotExist:
            raise NotFound("SummonerPuuid not found")

    def get(self, request, summonerName):
        summonerMatches = self.get_object(summonerName)
        serializer = serializers.SummonerMatchesByPuuidSerializer(
            summonerMatches.matches.all(), many=True
        )
        return Response(serializer.data)

    def post(self, request, summonerName):
        summoner_instance = self.get_object(summonerName)

        if not summoner_instance:
            return Response(
                {"error": "SummonerPuuid not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # api_key = os.getenv("RIOT_API_KEY")
        url = f"https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{summonerName}/ids?start=0&count=3&api_key={api_key}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                matches_data = response.json()

                if isinstance(matches_data, list) and matches_data:
                    match_instances = []
                    for match_id in matches_data:
                        match_instances.append(
                            SummonerMatchesByPuuid(
                                summoner_puuid=summoner_instance, match_id=match_id
                            )
                        )

                    # 한 번에 매치들을 생성하고 저장
                    SummonerMatchesByPuuid.objects.bulk_create(match_instances)

                    return Response(
                        {
                            "message": f"{len(matches_data)} match data saved successfully!"
                        }
                    )
                else:
                    return Response(
                        {"error": "No match_id found in the response"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
            else:
                return Response(
                    {
                        "error": "Failed to fetch match data",
                        "status_code": response.status_code,
                    },
                    status=response.status_code,
                )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# 특정 유저의 매치 id로 매치 정보 GET, POST
class SummonerMatchByMatchIdAPIView(APIView):
    def get_object(self, matchId):
        try:
            return SummonerMatchByMatchId.objects.get(match_id=matchId)
        except SummonerMatchByMatchId.DoesNotExist:
            raise NotFound

    def get(self, request, summonerName, matchId):
        summonerMatch = self.get_object(matchId)
        serializer = serializers.SummonerMatchByMatchIdSerializer(
            summonerMatch,
        )
        return Response(serializer.data)

    def post(self, request, summonerName, matchId):
        if not matchId:
            return Response(
                {"error": "matchId is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        api_key = os.getenv("RIOT_API_KEY")
        url = f"https://asia.api.riotgames.com/tft/match/v1/matches/{matchId}?api_key={api_key}"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        "error": "Failed to fetch match data",
                        "status_code": response.status_code,
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        except requests.RequestException as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
