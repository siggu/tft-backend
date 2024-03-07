from django.contrib import admin
from .models import Origin, Job


# Register your models here.
@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "get_champions",
    )

    def get_champions(self, obj):
        return ",".join([champion.name for champion in obj.champions.all()])


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "get_champions",
    )

    def get_champions(self, obj):
        return ",".join([champion.name for champion in obj.champions.all()])
