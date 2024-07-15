from rest_framework.serializers import ModelSerializer
from .models import Set11Item, Set12Item
from medias.serializers import PhotoSerializer


class Set11ItemSerializer(ModelSerializer):

    class Meta:
        model = Set11Item
        fields = "__all__"

class Set12ItemSerializer(ModelSerializer):

    class Meta:
        model = Set12Item
        fields = "__all__"
