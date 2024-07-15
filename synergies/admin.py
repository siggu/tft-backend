from django.contrib import admin
from .models import Set11Trait, Set12Trait


# Register your models here.
@admin.register(Set11Trait, Set12Trait)
class TraitAdmin(admin.ModelAdmin):
    list_display = (
        "key",
        "name",
        "_type",
    )
