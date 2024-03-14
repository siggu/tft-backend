from django.contrib import admin
from .models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "file",
        "description",
        "augment",
        "champion",
        "skill",
        "portal",
        "origin",
        "job",
        "encounter",
    )
