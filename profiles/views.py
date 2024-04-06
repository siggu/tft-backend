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
    # def get_object(self, summonerPuuid):
    #     try:
    #         return SummonerMatchesByPuuid.objects.get(summoner_puuid=summonerPuuid)
    #     except SummonerMatchesByPuuid.DoesNotExist:
    #         raise NotFound

    def get_object(self, summonerPuuid):
        try:
            return SummonerPuuid.objects.get(puuid=summonerPuuid)
        except SummonerPuuid.DoesNotExist:
            return NotFound

    def get(self, request, summonerPuuid):
        summonerMatches = self.get_object(summonerPuuid)
        serializer = serializers.SummonerMatchesByPuuidSerializer(
            summonerMatches,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, summonerPuuid):
        summoner_instance = self.get_object(summonerPuuid)

        if not summoner_instance:
            return Response(
                {"error": "SummonerPuuid not found"}, status=status.HTTP_404_NOT_FOUND
            )

        api_key = os.getenv("RIOT_API_KEY")
        url = f"https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{summonerPuuid}/ids?start=0&count=3&api_key={api_key}"

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
