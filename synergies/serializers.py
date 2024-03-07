from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Origin, Job
from medias.serializers import PhotoSerializer


class OriginSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Origin
        fields = (
            "pk",
            "name",
            "description",
            "photos",
        )
        depth = 1


class JobSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Job
        fields = (
            "pk",
            "name",
            "description",
            "photos",
        )
        depth = 1
