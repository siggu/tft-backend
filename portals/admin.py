from django.contrib import admin
from .models import Portal


# Register your models here.
@admin.register(Portal)
class PortalAdmin(admin.ModelAdmin):
    list_display = (
        "_key",
        "title",
        "desc",
    )
