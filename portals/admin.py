from django.contrib import admin
from .models import Portal, PortalType


# Register your models here.
@admin.register(Portal)
class PortalAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(PortalType)
class PortalTypeAdmin(admin.ModelAdmin):
    list_display = ("portal_type",)
