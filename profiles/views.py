from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from . import serializers
from .models import (
    LeagueEntryDTO,
    SummonerPuuid,
    SummonerMatchesByPuuid,
    SummonerMatchByMatchId,
    MatchDetailsByMatchId,
)
import requests
import os

# 유저 이름+태그로 puuid 찾아내기 AccountDTO
# URL + /{username}/{tagLine}?api_key={API_KEY}
ACCOUNT_URL = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"

# summoner puuid로 summoner 프로필 정보 찾아내기 SummonerDTO
# URL + /{puuid}?api_key={API_KEY}
SUMMONER_URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"

# summonerId로 랭크 게임 기본 정보 찾아내기 LeagueEntryDTO
# URL+{summonerId}?api_key={API_KEY}
ENTRY_BY_SUMMONER_URL = (
    "https://kr.api.riotgames.com/tft/league/v1/entries/by-summoner/"
)
API_KEY = os.getenv("RIOT_API_KEY")


# 유저 정보 GET, POST
class SummonerProfileAPIView(APIView):
    def get(self, request):
        allUsers = SummonerPuuid.objects.all()
        serializer = serializers.SummonerPuuidSerializer(allUsers, many=True)
        return Response(serializer.data)

    def post(self, request):
        gameName = request.data.get("gameName")
        tagLine = request.data.get("tagLine")
        print(gameName, tagLine)
        accountApiUrl = f"{ACCOUNT_URL}{gameName}/{tagLine}?api_key={API_KEY}"

        try:
            response = requests.get(accountApiUrl)

            if response.status_code == 200:
                AccountApidata = response.json()
                puuid = AccountApidata["puuid"]
                summonerApiUrl = f"{SUMMONER_URL}{puuid}?api_key={API_KEY}"

                try:
                    response = requests.get(summonerApiUrl)
                    print("summonerApiUrl response:", response)

                    if response.status_code == 200:
                        SummonerApidata = response.json()

                        # SummonerPuuid가 이미 존재하는지 확인
                        if SummonerPuuid.objects.filter(
                            puuid=SummonerApidata["puuid"]
                        ).exists():
                            return Response(
                                {
                                    "error": "SummonerPuuid가 이미 존재합니다.",
                                    "puuid": SummonerApidata["puuid"],
                                },
                                status=status.HTTP_409_CONFLICT,
                            )

                        summoner_data = {
                            "puuid": SummonerApidata["puuid"],
                            "gameName": gameName,
                            "tagLine": tagLine,
                            "accountId": SummonerApidata["accountId"],
                            "profileIconId": SummonerApidata["profileIconId"],
                            "summonerId": SummonerApidata["id"],
                            "summonerLevel": SummonerApidata["summonerLevel"],
                        }

                        serializer = serializers.SummonerPuuidSerializer(
                            data=summoner_data
                        )

                        if serializer.is_valid():
                            serializer.save()
                            return Response(
                                {
                                    "message": "SummonerPuuid Data success",
                                    "data": serializer.data,
                                }
                            )
                        else:
                            return Response(
                                serializer.errors, status=status.HTTP_400_BAD_REQUEST
                            )
                    else:
                        return Response(
                            {
                                "error": "puuid 찾기 성공 / SummonerDTO 찾기 실패 : (라이엇 Summoner API 실패)",
                                "status_code": response.status_code,
                            },
                            status=response.status_code,
                        )
                except Exception as e:
                    return Response(
                        {"Summoner Api error :": str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )
            else:
                return Response(
                    {
                        "error": "puuid 찾기 실패 : (라이엇 Account API 실패)",
                        "status_code": response.status_code,
                    },
                    status=response.status_code,
                )
        except Exception as e:
            return Response(
                {"Account api error :": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# 특정 유저 정보 GET
class SummonerProfileDetailAPIView(APIView):
    def get_object(self, gameName, tagLine):
        try:
            return SummonerPuuid.objects.get(gameName=gameName, tagLine=tagLine)
        except SummonerPuuid.DoesNotExist:
            return NotFound

    def get(self, request, gameName, tagLine):
        user = self.get_object(gameName, tagLine)
        serializer = serializers.SummonerPuuidSerializer(
            user,
        )
        return Response(serializer.data)


# 특정 유저 puuid로 매치 ids GET, POST
class SummonerMathcesByPuuidAPIView(APIView):
    def get_object(self, puuid):
        try:
            return SummonerMatchesByPuuid.objects.get(summoner_puuid=puuid)
        except SummonerMatchesByPuuid.DoesNotExist:
            raise NotFound("SummonerPuuid not found")

    def get(self, request, puuid):
        matchesByPuuid = SummonerMatchesByPuuid.objects.filter(summoner_puuid=puuid)
        if not matchesByPuuid.exists():
            raise NotFound("No matches found for the provided SummonerPuuid")
        match_details = []
        for match in matchesByPuuid:
            try:
                match_detail = MatchDetailsByMatchId.objects.get(
                    match_id=match.match_id
                )
                match_details.append(match_detail)
            except MatchDetailsByMatchId.DoesNotExist:
                continue

        if not match_details:
            raise NotFound("No match details found for the provided SummonerPuuid")

        serializer = serializers.MatchDetailsByMatchIdSerializer(
            match_details, many=True
        )
        return Response(serializer.data)

    def post(self, request, puuid):
        summoner_instance = self.get_object(puuid)

        if not summoner_instance:
            return Response(
                {"error": "SummonerPuuid not found"}, status=status.HTTP_404_NOT_FOUND
            )

        url = f"https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{summoner_instance.puuid}/ids?start=0&count=3&api_key={API_KEY}"

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

    def get(self, request, summonerMatch):
        summonerMatch = self.get_object(summonerMatch)
        try:
            serializer = serializers.MatchDetailsByMatchIdSerializer(
                summonerMatch,
            )
            return Response(serializer.data)
        except summonerMatch.DoesNotExist:
            raise NotFound

    def post(self, request, gameName, matchId):
        gameName = request.data["gameName"]
        matchId = request.data["matchId"]
        if not matchId:
            return Response(
                {"error": "matchId is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        url = f"https://asia.api.riotgames.com/tft/match/v1/matches/{matchId}?api_key={API_KEY}"
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


class EntryBySummonerAPIView(APIView):

    def get(self, request):
        entryData = LeagueEntryDTO.objects.all()
        try:
            serializer = serializers.LeagueEntryDTOSerializer(entryData, many=True)
            return Response(serializer.data)
        except entryData.DoesNotExist:
            raise NotFound

    def post(self, request):
        summonerId = request.data.get("summonerId")
        entryBySummonerAPIURL = f"{ENTRY_BY_SUMMONER_URL}{summonerId}?api_key={API_KEY}"
        try:
            response = requests.get(entryBySummonerAPIURL)
            print("response", response)
            responseJson = response.json()
            for summonerEntryData in responseJson:

                if summonerEntryData["queueType"] == "RANKED_TFT":
                    if response.status_code == 200:
                        serializer = serializers.LeagueEntryDTOSerializer(
                            data=summonerEntryData
                        )

                        if serializer.is_valid():
                            serializer.save()
                            return Response(
                                {
                                    "message": "Entry data success",
                                    "data": serializer.data,
                                }
                            )
                        else:
                            return Response(
                                serializer.errors, status=status.HTTP_400_BAD_REQUEST
                            )
                    else:
                        return Response(
                            {
                                "message": "라이엇 EntryBySummoner api 응답 실패 ",
                                "status_code": response.status_code,
                            }
                        )
        except Exception as e:
            return Response(
                {
                    "Exception": str(e),
                }
            )


class EntryBySummonerDetailAPIView(APIView):
    def get_object(self, summonerId):
        try:
            return LeagueEntryDTO.objects.get(summonerId=summonerId)
        except LeagueEntryDTO.DoesNotExist:
            raise NotFound

    def get(self, request, summonerId):
        entryData = self.get_object(summonerId)
        try:
            serializer = serializers.LeagueEntryDTOSerializer(entryData)
            return Response(serializer.data)
        except entryData.DoesNotExist:
            raise NotFound
