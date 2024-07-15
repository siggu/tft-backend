from django.contrib import admin
from .models import Set11Champion, Set12Champion

# Register your models here.


@admin.register(Set11Champion, Set12Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = (
        "key",
        "name",
    )
