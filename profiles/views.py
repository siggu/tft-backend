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
from rest_framework.request import Request


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
        print(gameName, tagLine)
        try:
            user = self.get_object(gameName, tagLine)
            
            serializer = serializers.SummonerPuuidSerializer(
                user,
            )
            return Response(serializer.data)
        except Exception as e:
            print("exception !!!",e)
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

                                # SummonerMathcesByPuuidAPIView의 post 메소드 호출
                                request_data = {
                                    "puuid": SummonerApidata["puuid"]
                                }
                                request_obj = Request(request=request, data=request_data)
                                matches_update_view = SummonerMathcesByPuuidAPIView()
                                update_response = matches_update_view.post(request_obj, SummonerApidata["puuid"])

                                if update_response.status_code == status.HTTP_200_OK:
                                    return Response(
                                        {
                                            "message": "SummonerPuuid Data and Matches Updated successfully",
                                            "data": serializer.data,
                                        }
                                    )
                                else:
                                    return update_response
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



# 특정 유저 puuid로 매치 ids GET, POST
class SummonerMathcesByPuuidAPIView(APIView):

    def get(self, request, puuid):
        try:
            SummonerPuuid.objects.get(puuid=puuid)
        except SummonerPuuid.DoesNotExist:
            return Response({"error": "SummonerPuuid not found"}, status=status.HTTP_404_NOT_FOUND)
        matchesByPuuid = SummonerMatchesByPuuid.objects.filter(summoner_puuid=puuid)

        if len(matchesByPuuid) == 0:
            # 데이터가 없으면 POST 요청을 내부적으로 호출
            post_response = self.post(request, puuid)
            if post_response.status_code != status.HTTP_200_OK:
                return post_response
            matchesByPuuid = SummonerMatchesByPuuid.objects.filter(summoner_puuid=puuid).order_by('-id')[:20]
            if len(matchesByPuuid) == 0:
                raise NotFound("match데이터가 없어서 puuid의 매치 데이터를 DB에 저장할 수 없음.")
        match_details = []
        for match in matchesByPuuid:
            try:
                match_detail = MatchDetailsByMatchId.objects.get(
                    match_id=match.match_id
                )
                match_details.append(match_detail)
            except MatchDetailsByMatchId.DoesNotExist:
                raise NotFound("matchId는 있지만 해당 매치의 matchDetails는 없음")

        serializer = serializers.MatchDetailsByMatchIdSerializer(
            match_details, many=True
        )
        return Response(serializer.data)

    def post(self, request, puuid):
        try:
            summoner_instance = SummonerPuuid.objects.get(puuid=puuid)
        except SummonerPuuid.DoesNotExist:
            return Response({"error": "SummonerPuuid not found"}, status=status.HTTP_404_NOT_FOUND)

        url = f"https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{summoner_instance.puuid}/ids?start=0&count=20&api_key={API_KEY}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                matches_data = response.json()

                if isinstance(matches_data, list) and matches_data:
                    match_instances = []
                    for match_id in matches_data:
                        match_instance, created = SummonerMatchesByPuuid.objects.update_or_create(
                            summoner_puuid=summoner_instance, 
                            match_id=match_id
                        )
                        match_instances.append(match_instance)

                    # 각 match_id에 대해 SummonerMatchByMatchIdAPIView의 post 요청을 수행
                    for match_id in matches_data:
                        match_id_post_response = SummonerMatchByMatchIdAPIView().post(request, match_id)
                        if match_id_post_response.status_code not in [status.HTTP_200_OK, status.HTTP_201_CREATED]:
                            return Response(
                                {"error": f"Failed to save match details for match_id {match_id}"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )

                    return Response(
                        {
                            "message": f"{len(match_instances)} match data saved successfully!"
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
                        "error": f"riot api 실패(https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{summoner_instance.puuid}/ids?start=0&count=20&api_key=)",
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

    def get(self, request, matchId):
        match_detail  = self.get_object(matchId)
        try:
            serializer = serializers.MatchDetailsByMatchIdSerializer(
                match_detail,
            )
            return Response(serializer.data)
        except match_detail.DoesNotExist:
            raise NotFound

    def post(self, request, matchId):
        print("matchId", matchId)
        if not matchId:
            return Response(
                {"error": "matchId is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        matchDetailUrl = f"https://asia.api.riotgames.com/tft/match/v1/matches/{matchId}?api_key={API_KEY}"
        print("matchDetailUrl", matchDetailUrl)
        try:
            api_response = requests.get(matchDetailUrl)

            if api_response.status_code == 200:
                data = api_response.json()

                match_instance, created = MatchDetailsByMatchId.objects.update_or_create(
                    match_id=matchId,
                    defaults={'match_detail': data},
                )

                serializer = serializers.MatchDetailsByMatchIdSerializer(match_instance)
                return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
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
                                {serializer.data}
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
        try:
            entryData = self.get_object(summonerId)
            serializer = serializers.LeagueEntryDTOSerializer(entryData)
            return Response(serializer.data)
        except Exception as e:
            print("exception !!!",e)
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
                                return Response(serializer.data)
                            else:
                                return Response(
                                    {
                                        "message" : "serializer 가 유효하지 않음",
                                        "status_code": response.status_code,
                                    }
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
                    {"message" : "라이엇에 없는 내용입니다 entry dto",
                    "Exception": str(e),
                    }
                )
