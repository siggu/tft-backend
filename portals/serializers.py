from rest_framework.serializers import ModelSerializer
from .models import Portal
from medias.serializers import PhotoSerializer


class PortalSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Portal
        fields = "__all__"
