from django.contrib import admin

# from comps.views import MetaDecks
from .models import Set11Comp, Set11CompElement, Set11ItemUsage, Set11MetaDeck, Set12Comp, Set12CompElement, Set12ItemUsage, Set12MetaDeck


@admin.register(Set11Comp, Set12Comp)
class CompAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ("name",)


@admin.register(Set11CompElement, Set12CompElement)
class CompElementsAdmin(admin.ModelAdmin):
    search_fields = ["name"]
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
    
@admin.register(Set11MetaDeck, Set12MetaDeck)
class MetaDeckAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = [
        "name","decks",
    ]
@admin.register(Set11ItemUsage, Set12ItemUsage)
class ItemUsageAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = [
        "name","usages",
    ]