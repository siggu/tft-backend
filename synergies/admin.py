from django.contrib import admin
from .models import Synergy


# Register your models here.
@admin.register(Synergy)
class SynergyAdmin(admin.ModelAdmin):
    pass
