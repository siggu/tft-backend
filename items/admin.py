from django.contrib import admin
from .models import Item


# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "name",
        "description",
        "effect",
        "generableItem",
        "composition1",
        "composition2",
        "tags",
    )
