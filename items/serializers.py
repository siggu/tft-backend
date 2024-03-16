from rest_framework.serializers import ModelSerializer
from .models import Item, ItemRecipe
from medias.serializers import PhotoSerializer


class ItemSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Item
        fields = "__all__"


class ItemRecipiesSerializer(ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = ItemRecipe
        fields = "__all__"
        depth = 1
