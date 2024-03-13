from rest_framework.serializers import ModelSerializer
from .models import Item
from medias.serializers import PhotoSerializer


class ItemSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Item
        fields = "__all__"
