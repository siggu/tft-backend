from django.contrib import admin
from .models import SummonerPuuid, SummonerMatchesByPuuid, SummonerMatchByMatchId


# Register your models here.
@admin.register(SummonerPuuid)
class SummonerPuuidAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "puuid",
    )


@admin.register(SummonerMatchesByPuuid)
class SummonerMatchesByPuuidAdmin(admin.ModelAdmin):
    list_display = (
        "summoner_puuid",
        "match_id",
    )


@admin.register(SummonerMatchByMatchId)
class SummonerMatchByMatchIdAdmin(admin.ModelAdmin):
    list_display = (
        "metadata",
        "info",
    )
