from rest_framework.serializers import ModelSerializer
from .models import Portal, PortalType
from medias.serializers import PhotoSerializer


class PortalTypeSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = PortalType
        fields = "__all__"


class PortalSerializer(ModelSerializer):
    portal_type = PortalTypeSerializer(read_only=True)

    class Meta:
        model = Portal
        fields = "__all__"
