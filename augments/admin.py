from django.contrib import admin
from .models import Set11Augment, Set12Augment


# Register your models here.
@admin.register(Set11Augment, Set12Augment)
class AugmentAdmin(admin.ModelAdmin):
    list_display = (
        "key",
        "tier",
        "name",
        "desc",
        "tier",
    )
