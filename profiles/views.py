from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import serializers
from .models import (
    SummonerPuuid,
    SummonerMatchesByPuuid,
    SummonerMatchByMatchId,
    MatchDetailsByMatchId,
)
import requests
import os


# 유저 정보 GET, POST
class SummonerProfileAPIView(APIView):
    def get(self, request, gameName, tagLine):
        summonerpuuids = SummonerPuuid.objects.all()
        serializer = serializers.SummonerPuuidSerializer(
            summonerpuuids,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, gameName, tagLine):
        gameName = request.data.get("gameName")
        tagLine = request.data.get("tagLine")
        print(gameName, tagLine)
        api_key = os.getenv("RIOT_API_KEY")
        # url = f"https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{profile_name}?api_key={api_key}"
        url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={api_key}"
        try:
            response = requests.get(url)
            print("response", response)
            if response.status_code == 200:
                data = response.json()
                summoner_puuid = SummonerPuuid.objects.create(
                    puuid=data["puuid"],
                    gameName=data["gameName"],
                    tagLine=data["tagLine"],
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
    def get_object(self, gameName):
        try:
            return SummonerPuuid.objects.get(name=gameName)
        except SummonerPuuid.DoesNotExist:
            return NotFound

    def get(self, request, gameName):
        summonerpuuid = self.get_object(gameName)
        serializer = serializers.SummonerPuuidSerializer(summonerpuuid)
        return Response(serializer.data)


# 특정 유저 puuid로 매치 ids GET, POST
class SummonerMathcesByPuuidAPIView(APIView):
    def get_object(self, gameName):
        try:
            return SummonerPuuid.objects.get(name=gameName)
        except SummonerPuuid.DoesNotExist:
            raise NotFound("SummonerPuuid not found")

    def get(self, request, gameName):
        summonerMatches = self.get_object(gameName)
        serializer = serializers.SummonerMatchesByPuuidSerializer(
            summonerMatches.matches.all(), many=True
        )
        return Response(serializer.data)

    def post(self, request, gameName):
        summoner_instance = self.get_object(gameName)

        if not summoner_instance:
            return Response(
                {"error": "SummonerPuuid not found"}, status=status.HTTP_404_NOT_FOUND
            )

        api_key = os.getenv("RIOT_API_KEY")
        url = f"https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{summoner_instance.puuid}/ids?start=0&count=3&api_key={api_key}"

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
            return MatchDetailsByMatchId.objects.get(match_id=matchId)
        except MatchDetailsByMatchId.DoesNotExist:
            raise NotFound

    def get(self, request, gameName, matchId):

        summonerMatch = self.get_object(matchId)
        try:
            serializer = serializers.MatchDetailsByMatchIdSerializer(
                summonerMatch,
            )
            return Response(serializer.data)
        except summonerMatch.DoesNotExist:
            raise NotFound

    def post(self, request, gameName, matchId):
        print("matchId", matchId)
        print("request", request.data)
        gameName = request.data["gameName"]
        matchId = request.data["matchId"]
        if not matchId:
            return Response(
                {"error": "matchId is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        api_key = os.getenv("RIOT_API_KEY")
        url = f"https://asia.api.riotgames.com/tft/match/v1/matches/{matchId}?api_key={api_key}"
        print("url", url)
        try:
            api_response = requests.get(url)

            if api_response.status_code == 200:
                data = api_response.json()

                push_data = MatchDetailsByMatchId.objects.create(
                    match_id=matchId,
                    match_detail=data,
                )

                return Response(push_data)
            else:
                return Response(
                    {
                        "error": "Failed to fetch match data",
                        "status_code": api_response.status_code,
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        except requests.RequestException as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
