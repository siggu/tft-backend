from rest_framework.serializers import ModelSerializer
from .models import Augment
from medias.serializers import PhotoSerializer


class AugmentSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Augment
        fields = "__all__"
