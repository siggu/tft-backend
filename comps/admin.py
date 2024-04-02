from django.contrib import admin
from .models import Comp, CompElement


@admin.register(Comp)
class CompAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(CompElement)
class CompElementsAdmin(admin.ModelAdmin):
    list_display = (
        "champion",
        "recommendedItem1",
        "recommendedItem2",
        "recommendedItem3",
        "championLevelChoice",
    )
    autocomplete_fields = [
        "recommendedItem1",
        "recommendedItem2",
        "recommendedItem3",
    ]

    def get_items(self, obj):
        return ",".join([item.name for item in obj.items.all()])
