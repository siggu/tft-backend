# views.py

from django.http import JsonResponse
from .models import SummonerPuuid
import requests
import os


def fetch_and_save_puuid(request):
    profile_name = request.GET.get("profileName")  # 프로필 이름은 GET 파라미터로 받아옴
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
            return JsonResponse(
                {
                    "message": "Summoner puuid fetched and saved successfully!",
                    "data": summoner_puuid.id,
                }
            )
        else:
            return JsonResponse(
                {
                    "error": "Failed to fetch summoner puuid",
                    "status_code": response.status_code,
                },
                status=response.status_code,
            )
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
