from django.contrib import admin
from .models import (
    LeagueEntryDTO,
    SummonerPuuid,
    SummonerMatchesByPuuid,
    SummonerMatchByMatchId,
    MatchDetailsByMatchId,
)


# Register your models here.
@admin.register(SummonerPuuid)
class SummonerPuuidAdmin(admin.ModelAdmin):
    search_fields = ["gameName"]
    list_display = (
        "gameName",
        "tagLine",
        "puuid",
    )


@admin.register(SummonerMatchesByPuuid)
class SummonerMatchesByPuuidAdmin(admin.ModelAdmin):
    list_display = (
        "summoner_puuid",
        "match_id",
    )
    list_filter = ("summoner_puuid",)


@admin.register(SummonerMatchByMatchId)
class SummonerMatchByMatchIdAdmin(admin.ModelAdmin):
    list_display = (
        "metadata",
        "info",
    )


@admin.register(MatchDetailsByMatchId)
class MatchDetailsByMatchIdAdmin(admin.ModelAdmin):
    list_display = (
        "match_id",
        "match_detail",
    )


@admin.register(LeagueEntryDTO)
class LeagueEntryDTOAdmin(admin.ModelAdmin):
    list_display = (
        "summonerId",
        "puuid",
        "queueType",
        "tier",
        "rank",
        "leaguePoints",
        "wins",
        "losses",
    )
