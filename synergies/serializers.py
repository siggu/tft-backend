from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Origin, Job, SynergyTier, SynergyStack
from medias.serializers import PhotoSerializer


class OriginSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Origin
        fields = "__all__"
        depth = 1


class JobSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Job
        fields = "__all__"
        depth = 1


class SynergyTierSerializer(ModelSerializer):
    class Meta:
        model = SynergyTier
        fields = "__all__"


class SynergyStackSerializer(ModelSerializer):
    class Meta:
        model = SynergyStack
        fields = "__all__"
