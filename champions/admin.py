from django.contrib import admin
from .models import Champion

# Register your models here.


@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = (
        "key",
        "name",
    )
