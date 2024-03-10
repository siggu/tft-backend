from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Origin, Job
from medias.serializers import PhotoSerializer


class OriginSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Origin
        depth = 1
        fields = "__all__"


class JobSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Job
        fields = "__all__"
        depth = 1
