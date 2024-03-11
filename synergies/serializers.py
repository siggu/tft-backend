from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Origin, Job
from medias.serializers import PhotoSerializer


class OriginSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Origin
        fields = "__all__"
        depth=1


class JobSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Job
        fields = "__all__"
        depth=1
