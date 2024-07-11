from django.contrib import admin

from comps.views import MetaDecks
from .models import Comp, CompElement, ItemUsage,MetaDeck


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
    
@admin.register(MetaDeck)
class MetaDeckAdmin(admin.ModelAdmin):
    list_display = [
        "name","decks",
    ]
@admin.register(ItemUsage)
class ItemUsageAdmin(admin.ModelAdmin):
    list_display = [
        "name","usages",
    ]