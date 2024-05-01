from django.contrib import admin
from .models import Trait


# Register your models here.
@admin.register(Trait)
class TraitAdmin(admin.ModelAdmin):
    list_display = (
        "key",
        "name",
        "_type",
    )
