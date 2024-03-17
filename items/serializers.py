from rest_framework.serializers import ModelSerializer
from .models import Item
from medias.serializers import PhotoSerializer


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"
