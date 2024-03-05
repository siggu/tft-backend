from django.contrib import admin
from .models import Augment


# Register your models here.
@admin.register(Augment)
class AugmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "tier",
    )
