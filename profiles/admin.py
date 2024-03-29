from django.contrib import admin
from .models import SummonerPuuid


# Register your models here.
@admin.register(SummonerPuuid)
class SummonerPuuidAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "puuid",
    )
