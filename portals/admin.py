from django.contrib import admin
from .models import Set11Portal, Set12Portal


# Register your models here.
@admin.register(Set11Portal, Set12Portal)
class PortalAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = (
        "_key",
        "title",
        "desc",
    )
