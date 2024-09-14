from django.contrib import admin
from .models import Set11Item, Set12Item


# Register your models here.
@admin.register(Set11Item, Set12Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "key",
        "name",
    )
