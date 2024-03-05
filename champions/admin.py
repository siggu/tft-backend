from django.contrib import admin
from .models import Champion, Skill

# Register your models here.


@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "cost",
        "skill",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "skill_type",
    )
