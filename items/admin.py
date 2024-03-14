from django.contrib import admin
from .models import Item


# Register your models here.
@admin.register(Item)
class AugmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "effect",
        "generableItem",

    )
