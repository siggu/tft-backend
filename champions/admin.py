from django.contrib import admin
from .models import Champion

# Register your models here.


@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "cost",
        "display_synergies",
    )

    def display_synergies(self, obj):
        return ", ".join([synergy.name for synergy in obj.synergies.all()])

    display_synergies.short_description = "Synergies"
