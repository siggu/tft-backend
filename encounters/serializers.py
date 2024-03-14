from rest_framework import serializers
from .models import Encounter
from medias.serializers import PhotoSerializer


class EncounterSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Encounter
        fields = (
            "name",
            "description_1",
            "description_2",
            "description_3",
            "description_4",
            "photos",
        )
