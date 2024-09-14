from django.contrib import admin
from .models import Set12Charm

# Register your models here.
@admin.register(Set12Charm)
class CharmAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = (
        "name",
        "cost",
        "tier",
    )