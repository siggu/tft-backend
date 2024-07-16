from django.contrib import admin
from .models import Encounter


# Register your models here.
@admin.register(Encounter)
class EncounterAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "name",
        "ingameKey",
        "encounterDesc",
    )
