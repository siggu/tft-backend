from django.contrib import admin
from .models import Item


# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "key",
        "name",
        "description",
        "shortDesc",
        "composition1",
        "composition2",
        "tag1",
        "tag2",
        "tag3",
    )
