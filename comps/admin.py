from django.contrib import admin
from .models import Comp


@admin.register(Comp)
class CompAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "get_champions",
    )

    def get_champions(self, obj):
        return ",".join([champion.name for champion in obj.champions.all()])
