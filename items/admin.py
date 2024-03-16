from django.contrib import admin
from .models import Item, ItemRecipe


# Register your models here.
@admin.register(Item)
class AugmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "effect",
        "generableItem",
    )


@admin.register(ItemRecipe)
class ItemRecipiesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "element_item1",
        "element_item2",
        "result_item",
    )
